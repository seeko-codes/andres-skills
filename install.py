#!/usr/bin/env python3
"""Install Turn to Life inside a project without replacing user-owned files."""
import argparse
from pathlib import Path
import shutil
import sys


def install(project, dry_run=False, skills_dir='.agents/skills'):
    source = Path(__file__).resolve().parent / 'skills'
    project = Path(project).expanduser().resolve()
    relative = Path(skills_dir)
    if relative.is_absolute() or '..' in relative.parts or relative == Path('.'):
        raise ValueError('Skills directory must be a relative path inside the project.')
    if (project == Path.home().resolve() or project == Path(project.anchor)
            or any(part in ('.agents', '.claude', '.codex', '.pi') for part in project.parts)):
        raise ValueError('Choose a project root, not a global home or agent configuration directory.')
    destination = (project / relative).resolve()
    if destination == source or source in destination.parents:
        raise ValueError('Destination must be outside the source skills directory.')
    if destination == project or project not in destination.parents:
        raise ValueError('Skills path resolves outside the project; shared symlinks are not followed.')
    if not project.is_dir():
        raise ValueError('Project root must be an existing directory; create the project first.')
    if destination.exists() and not destination.is_dir():
        raise ValueError('Destination exists and is not a directory.')

    skills = sorted(path.parent for path in source.glob('*/SKILL.md'))
    if not skills or not (source / 'turn-to-life' / 'SKILL.md').is_file():
        raise ValueError('Bundle is incomplete: keep install.py next to the full skills directory.')
    # Include dangling symlinks. Never follow one and overwrite a shared source.
    conflicts = [destination / skill.name for skill in skills
                 if (destination / skill.name).exists() or (destination / skill.name).is_symlink()]
    legacy = destination / 'orchestrator'
    if legacy.exists() or legacy.is_symlink():
        conflicts.append(legacy)
    if conflicts:
        names = '\n'.join('  ' + str(path) for path in conflicts)
        raise ValueError('Refusing existing skill names (including legacy orchestrator):\n' + names
                         + '\nReview and back up existing skills before replacing them. Nothing copied.')

    for skill in skills:
        print(('Would install: ' if dry_run else 'Install: ') + str(destination / skill.name))
    if dry_run:
        return
    destination.mkdir(parents=True, exist_ok=True)
    copied = []
    try:
        for skill in skills:
            # copytree refuses an existing destination, including one created after preflight.
            shutil.copytree(skill, destination / skill.name)
            copied.append(skill.name)
    except OSError as exc:
        raise OSError('Installation incomplete; inspect the destination before retrying. '
                      'Completed: ' + (', '.join(copied) or 'none')
                      + '. A partial next directory may remain. ' + str(exc)) from exc
    print('Installed ' + str(len(skills)) + ' skills. Ask your agent to use turn-to-life.')
    print('If not discovered, reload skills/start a new session as your runner requires.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', help='Existing project root; never a global skills directory.')
    parser.add_argument('--skills-dir', default='.agents/skills',
                        help='Project-relative skills location (default: .agents/skills).')
    parser.add_argument('--dry-run', action='store_true', help='Validate and show paths without writing.')
    args = parser.parse_args()
    try:
        install(args.project, args.dry_run, args.skills_dir)
    except (OSError, ValueError) as exc:
        print('turn-to-life: ' + str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
