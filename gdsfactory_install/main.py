import subprocess
import typer
import uv
from pathlib import Path

app = typer.Typer()


def run_command(cmd: list[str]) -> None:
    """Helper function to run commands with error handling."""
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error: {e}")
        raise typer.Exit(code=1)


@app.command()
def install():
    """Install gdsfactory in the current environment."""
    uv_bin = uv.find_uv_bin()
    run_command(
        [
            uv_bin,
            "tool",
            "install",
            "--force",
            "--python",
            "python3.12",
            "gdsfactory@latest",
        ]
    )
    run_command([uv_bin, "tool", "update-shell"])
    typer.echo("✅ Successfully installed gdsfactory")


@app.command()
def create_env(env_name: str = typer.Argument(..., help="Name of the virtual environment")):
    """Create a new virtual environment in the current directory."""
    uv_bin = uv.find_uv_bin()
    env_path = Path.cwd() / env_name
    
    if env_path.exists():
        typer.echo(f"Error: Environment '{env_name}' already exists")
        raise typer.Exit(code=1)
    
    run_command([uv_bin, "venv", "create", str(env_path)])
    typer.echo(f"✅ Successfully created virtual environment at {env_path}")


if __name__ == "__main__":
    app()
