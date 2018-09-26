import re
from pathlib import Path

import click
from git import Repo, GitCommandError

PATH_RE = re.compile(
    r'^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})-(?P<slug>[\w|-]+)$'
)


@click.command()
def cli():
    root_path = Path(__file__).resolve().parent

    notebook_paths = [
        root_path.joinpath('Public/Random'),
        root_path.joinpath('Private/Random'),
        root_path.joinpath('Clients/Braithwaite'),
        root_path.joinpath('Clients/Fairtax'),
    ]

    for path in notebook_paths:
        for notebook_path in path.glob('*'):
            if notebook_path.is_dir() and PATH_RE.match(notebook_path.name):
                click.echo(notebook_path)


if __name__ == '__main__':
    cli()
