import click
import pom_creator


@click.command(help=":To Create pom file")
@click.argument("project", required=True)
def start(project):
    pom_creator.create_pom(project)


if __name__ == "__main__":
    start()

