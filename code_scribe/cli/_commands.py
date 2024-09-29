"""Command line interface for Jobrunner"""

# Standard libraries
import os

# Feature libraries
import click

from code_scribe.cli import code_scribe
from code_scribe import api
from code_scribe import lib


@code_scribe.command(name="index")
@click.option(
    "--root-dir", "-r", default=os.getcwd(), help="Root directory of the project"
)
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
@click.argument("fortran-files", nargs=-1, required=True)
@click.option(
    "--root-dir", "-r", default=os.getcwd(), help="Root directory of the project"
)
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


@code_scribe.command(name="translate")
@click.argument("fortran-files", nargs=-1, required=True)
@click.option(
    "--seed-prompt", "-p", required=True, help="TOML seed file for chat template"
)
@click.option(
    "--model",
    "-m",
    cls=lib.MutuallyExclusiveOption,
    help="Gen AI model name or path",
    mutually_exclusive=["save_prompts"],
)
@click.option(
    "--save-prompts",
    "-s",
    is_flag=True,
    cls=lib.MutuallyExclusiveOption,
    help="Save file specific prompts to json file",
    mutually_exclusive=["model"],
)
def translate(fortran_files, seed_prompt, model, save_prompts):
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
    if (not model) and (not save_prompts):
        raise click.UsageError(
            "Please provide either the '--model/-m' or '--save-prompts/-p' option"
        )
    api.translate(fortran_files, seed_prompt, model, save_prompts)
