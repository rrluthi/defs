import typer
from typing import Optional

app = typer.Typer()


@app.command()
def enc(string: str, algo: str):
    typer.echo("Encode")


@app.command()
def dec(string: str, algo: Optional[str] = typer.Argument(None)):
    typer.echo("Decode")


@app.command()
def hsh():
    typer.echo("Hash")


@app.command()
def file(algo: str, input_file: str, output_file: str) -> None:
    typer.echo("File")


if __name__ == "__main__":
    app()

