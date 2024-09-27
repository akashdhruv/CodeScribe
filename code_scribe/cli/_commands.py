"""Command line interface for Jobrunner"""

# Standard libraries
import os

# Feature libraries
import click

from code_scribe.cli import code_scribe
from code_scribe import api


@code_scribe.command(name="index")
@click.option("--root-dir", "-r", default=os.getcwd())
def index(root_dir):
    """
    \b
    Index files along a project directory tree
    \b

    \b
    This command walks along the directory directory tree and
    parses files to creating mapping for modules, subroutines,
    and functions
    \b
    """
    message = api.index(root_dir)
    click.echo(message)


@code_scribe.command(name="draft")
@click.argument("fortran-files", nargs=-1)
@click.option("--root-dir", "-r", default=os.getcwd())
def draft(fortran_files, root_dir):
    """
    \b
    Perform a draft conversion from Fortran to C++
    \b

    \b
    This command performs a line-by-line conversion to
    prepare a list of files for generative AI use
    \b
    """
    for sfile in fortran_files:
        message = api.draft(sfile, root_dir)
        click.echo(message)


@code_scribe.command(name="neural-translate")
@click.argument("fortran-files", nargs=-1)
@click.option("--model", "-m", default=None)
@click.option("--prompt", "-p", required=True)
@click.option("--save-prompt", is_flag=True)
def neural_translate(fortran_files, model, prompt, save_prompt):
    """
    \b
    Perform a generative AI conversion
    \b

    \b
    This command applies generative AI to convert code from
    Fortran to C++, and create a corresponding Fortran/C
    interface
    \b
    """
    api.neural_translate(fortran_files, model, prompt, save_prompt)
