#!/usr/bin/env python3
import collections
import json
import os

import click
from git import Repo, GitCommandError

root_dir = os.path.dirname(os.path.abspath(__file__))

with open('repos.json') as fobj:
    notebook_repos = json.load(fobj)

if os.path.isfile('repos.private.json'):
    with open('repos.private.json') as fobj:
        notebook_repos.update(json.load(fobj))

notebook_repos = collections.OrderedDict(sorted(notebook_repos.items()))


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

        try:
            untracked_files_count = sum(1 for f in repo.untracked_files)

            commits_behind = repo.iter_commits('master..origin/master')
            commits_behind_count = sum(1 for c in commits_behind)

            commits_ahead = repo.iter_commits('origin/master..master')
            commits_ahead_count = sum(1 for c in commits_ahead)

            repo_error = False
        except GitCommandError:
            repo_error = True

        if commits_behind_count:
            click.secho('{0} is {1} commits behind.'.format(
                local, commits_behind_count), fg='blue')

        elif commits_ahead_count:
            click.secho('{0} is {1} commits ahead.'.format(
                local, commits_ahead_count), fg='blue')

        elif untracked_files_count:
            click.secho('{0} has {1} untracked files.'.format(
                local, untracked_files_count), fg='blue')

        elif repo_error:
            click.secho('{0} repo has an error.'.format(local), fg='red')

        else:
            click.secho('{0} everything is awesome.'.format(local), fg='green')


if __name__ == '__main__':
    cli.add_command(init)
    cli.add_command(status)
    cli()
