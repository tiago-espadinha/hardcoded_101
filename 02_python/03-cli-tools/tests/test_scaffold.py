import pytest
from click.testing import CliRunner
from devkit.cli import main

def test_scaffold_help():
    runner = CliRunner()
    result = runner.invoke(main, ["scaffold", "--help"])
    assert result.exit_code == 0
    assert "Scaffold a new project" in result.output