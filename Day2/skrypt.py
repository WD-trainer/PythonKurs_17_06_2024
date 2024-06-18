import os
import click ### https://github.com/pallets/click


@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
@click.option('--password',prompt=True, confirmation_prompt=True, hide_input=True)
def hello(count, name, password):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello, {name}!")
        click.echo(f'Moje super tajne hasło: {password}')

if __name__ == '__main__':
    hello()