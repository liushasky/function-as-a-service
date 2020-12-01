import os

import click

from faas import create_app
from faas._http import create_server


@click.command()
@click.option("--target", envvar="FUNCTION_TARGET", type=click.STRING, required=True)
@click.option("--source", envvar="FUNCTION_SOURCE", type=click.Path(), default=None)
@click.option(
    "--signature-type",
    envvar="FUNCTION_SIGNATURE_TYPE",
    type=click.Choice(["http", "event", "cloudevent"]),
    default="http",
)
@click.option("--host", envvar="HOST", type=click.STRING, default="0.0.0.0")
@click.option("--port", envvar="PORT", type=click.INT, default=8080)
@click.option("--debug", envvar="DEBUG", is_flag=True)
@click.option("--dry-run", envvar="DRY_RUN", is_flag=True)
def _cli(target, source, signature_type, host, port, debug, dry_run):
    app = create_app(target, source, signature_type)
    if dry_run:
        click.echo("Function: {}".format(target))
        click.echo("URL: http://{}:{}/".format(host, port))
        click.echo("Dry run successful, shutting down.")
    else:
        create_server(app, debug).run(host, port)
