#!/usr/bin/env python3
import json
import os

import click
from git import Repo

root_dir = os.path.dirname(os.path.abspath(__file__))

with open('repos.json') as fobj:
    notebook_repos = json.load(fobj)


@click.group()
def cli():
    pass


@click.command()
def init():
    """Clone all the repos."""
    for local, remote in notebook_repos.items():
        full = os.path.join(root_dir, local)

        if not os.path.exists(full):
            Repo.clone_from(remote, os.path.join(full))
            click.echo(click.style('Clone {}'.format(local), fg='green'))
        else:
            click.echo(click.style('Skip {}'.format(local), fg='blue'))


@click.command()
def status():
    for local, remote in notebook_repos.items():
        full = os.path.join(root_dir, local)

        repo = Repo(full)

        untracked_files_count = sum(1 for f in repo.untracked_files)

        commits_behind = repo.iter_commits('master..origin/master')
        commits_behind_count = sum(1 for c in commits_behind)

        commits_ahead = repo.iter_commits('origin/master..master')
        commits_ahead_count = sum(1 for c in commits_ahead)

        if commits_behind_count:
            click.echo('{0} is {1} commits behind.'.format(
                local, commits_behind_count))

        if commits_ahead_count:
            click.echo('{0} is {1} commits ahead.'.format(
                local, commits_ahead_count))

        if untracked_files_count:
            click.echo('{0} has {1} untracked files.'.format(
                local, untracked_files_count))


if __name__ == '__main__':
    cli.add_command(init)
    cli.add_command(status)
    cli()
