import os
import click

@click.command()
@click.argument("filename")
def createfile(filename):
    """Creates a file with the given filename."""
    path = os.path.join(os.getcwd(), filename)
    try:
        with open(path, mode="x") as f:
            click.echo(f"File created at {path}")
    except FileExistsError:
        click.echo(f"File '{filename}' already exists.")

@click.command()
@click.option('--dirname', '-d', default="NewTouchDirectory", type=str, help="Name of the directory to create")
def creatdir(dirname):
    """Creates a directory with the given name."""
    try:
        os.makedirs(dirname, exist_ok=True)
        click.echo(f"Directory '{dirname}' created.")
    except Exception as e:
        click.echo(f"Error creating directory: {e}")

@click.command()
@click.argument('filepath')
def readfile(filepath):
    """Reads the content of a file"""
    try:
        with open(filepath, "r") as f:
            content = f.read()
            click.echo(content)
    except Exception as e:
        click.echo(f"Error reading file: {e}")

@click.group(invoke_without_command=True)
@click.pass_context
@click.argument("filename", required=False)
@click.option('--dir', '-d', default=None, type=str, help="Name of the directory to create")
@click.option('--filepath', '-rf', type=str, help="Path of the file to read content")
def cli(ctx, filename, dir, filepath):
    """Command-line interface for file and directory operations."""
    # If filename is provided, invoke createfile
    if filename:
        ctx.invoke(createfile, filename=filename)
    # If -D option is used, invoke creatdir
    elif dir:
        ctx.invoke(creatdir, dirname=dir)
    # If -rf option is used, invoke readfile
    elif filepath:
        ctx.invoke(readfile, filepath=filepath)
    # If neither is provided, show help
    else:
        click.echo(ctx.get_help())

# Add commands to the group
cli.add_command(createfile)
cli.add_command(creatdir)
cli.add_command(readfile)

if __name__ == '__main__':
    cli()
