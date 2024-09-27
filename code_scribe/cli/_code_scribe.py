"""Command line interface for Jobrunner"""

# Standard libraries
import subprocess
import pkg_resources

# Feature libraries
import click


@click.group(name="code-scribe", invoke_without_command=True)
@click.pass_context
@click.option("--version", "-v", is_flag=True)
def code_scribe(ctx, version):
    """
    \b
    Software development tool for converting code from Fortran to C++
    """
    if ctx.invoked_subcommand is None and not version:
        subprocess.run(
            "export PATH=~/.local/bin:/usr/local/bin:$PATH && code-scribe --help",
            shell=True,
            check=True,
        )

    if version:
        click.echo(pkg_resources.require("CodeScribe")[0].version)
