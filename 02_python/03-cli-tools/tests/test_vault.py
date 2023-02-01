import pytest
from click.testing import CliRunner
from devkit.cli import main

def test_vault_help():
    runner = CliRunner()
    result = runner.invoke(main, ["vault", "--help"])
    assert result.exit_code == 0
    assert "Securely manage passwords" in result.output