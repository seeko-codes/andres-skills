"""Installation must copy the bundle without overwriting user-owned state."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name) / 'project with spaces'
        self.project.mkdir()
        self.dest = self.project / '.agents' / 'skills'

    def run_install(self, *options):
        return subprocess.run(
            [sys.executable, str(ROOT / 'install.py'), str(self.project), *options],
            text=True, capture_output=True, cwd=self.temp.name,
        )

    def test_full_bundle_is_copied_exactly_without_brand_or_repository(self):
        result = self.run_install()
        self.assertEqual(result.returncode, 0, result.stderr)
        source = ROOT / 'skills'
        names = {p.parent.name for p in source.glob('*/SKILL.md')}
        self.assertIn('turn-to-life', names)
        self.assertEqual({p.name for p in self.dest.iterdir()}, names)
        for name in names:
            for file in (source / name).rglob('*'):
                if file.is_file():
                    self.assertEqual(file.read_bytes(), (self.dest / file.relative_to(source)).read_bytes())
        self.assertFalse((self.dest / 'brand').exists())
        self.assertFalse((self.dest / '.git').exists())

    def test_dry_run_makes_no_directories(self):
        result = self.run_install('--dry-run')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('turn-to-life', result.stdout)
        self.assertFalse(self.dest.parent.exists())

    def test_existing_name_aborts_before_any_copy(self):
        existing = self.dest / 'tdd'
        existing.mkdir(parents=True)
        sentinel = existing / 'mine.txt'
        sentinel.write_text('keep me')
        result = self.run_install()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Refusing existing skill names', result.stderr)
        self.assertEqual(sentinel.read_text(), 'keep me')
        self.assertEqual([p.name for p in self.dest.iterdir()], ['tdd'])

    def test_dangling_symlink_is_preserved(self):
        self.dest.mkdir(parents=True)
        collision = self.dest / 'turn-to-life'
        collision.symlink_to(self.dest / 'missing-source', target_is_directory=True)
        result = self.run_install()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Refusing existing skill names', result.stderr)
        self.assertTrue(collision.is_symlink())
        self.assertEqual([p.name for p in self.dest.iterdir()], ['turn-to-life'])

    def test_legacy_orchestrator_is_not_silently_duplicated(self):
        (self.dest / 'orchestrator').mkdir(parents=True)
        result = self.run_install()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('orchestrator', result.stderr)
        self.assertFalse((self.dest / 'turn-to-life').exists())

    def test_repeat_install_never_overwrites_an_edit(self):
        first = self.run_install()
        self.assertEqual(first.returncode, 0, first.stderr)
        entry = self.dest / 'turn-to-life' / 'SKILL.md'
        entry.write_text('my local change')
        second = self.run_install()
        self.assertNotEqual(second.returncode, 0)
        self.assertEqual(entry.read_text(), 'my local change')

    def test_rejects_source_subdirectory(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / 'install.py'), str(ROOT / 'skills' / 'nested'), '--dry-run'],
            text=True, capture_output=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('outside the source', result.stderr)
        self.assertFalse((ROOT / 'skills' / 'nested').exists())

    def test_regular_file_destination_is_preserved(self):
        self.dest.parent.mkdir(parents=True)
        self.dest.write_text('not a directory')
        result = self.run_install()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('not a directory', result.stderr)
        self.assertEqual(self.dest.read_text(), 'not a directory')

    def test_unrelated_skills_are_preserved(self):
        existing = self.dest / 'unrelated'
        existing.mkdir(parents=True)
        (existing / 'SKILL.md').write_text('unrelated skill')
        result = self.run_install()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((existing / 'SKILL.md').read_text(), 'unrelated skill')


    def test_custom_local_skills_directory(self):
        result = self.run_install('--skills-dir', '.claude/skills')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.project / '.claude/skills/turn-to-life/SKILL.md').is_file())
        self.assertFalse(self.dest.exists())

    def test_relative_path_cannot_escape_project(self):
        result = self.run_install('--skills-dir', '../outside')
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('relative path inside', result.stderr)
        self.assertFalse((self.project.parent / 'outside').exists())

    def test_absolute_skills_directory_is_rejected(self):
        outside = Path(self.temp.name) / 'outside'
        result = self.run_install('--skills-dir', str(outside))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('relative path inside', result.stderr)
        self.assertFalse(outside.exists())

    def test_shared_root_symlink_cannot_escape_project(self):
        outside = Path(self.temp.name) / 'shared'
        outside.mkdir()
        (self.project / '.agents').symlink_to(outside, target_is_directory=True)
        result = self.run_install()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('outside the project', result.stderr)
        self.assertEqual(list(outside.iterdir()), [])
        self.assertTrue((self.project / '.agents').is_symlink())

    def test_project_instructions_and_preferences_are_untouched(self):
        for name in ('AGENTS.md', 'TURN-TO-LIFE.md'):
            (self.project / name).write_text('human owned')
        result = self.run_install()
        self.assertEqual(result.returncode, 0, result.stderr)
        for name in ('AGENTS.md', 'TURN-TO-LIFE.md'):
            self.assertEqual((self.project / name).read_text(), 'human owned')

    def test_global_home_is_not_a_project_target(self):
        # Dry-run only: never create data in the real home directory.
        result = subprocess.run(
            [sys.executable, str(ROOT / 'install.py'), str(Path.home()), '--dry-run'],
            text=True, capture_output=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('project root, not a global', result.stderr)


if __name__ == '__main__':
    unittest.main()
