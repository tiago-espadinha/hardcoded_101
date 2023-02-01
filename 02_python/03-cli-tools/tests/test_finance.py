import pytest
from click.testing import CliRunner
from devkit.cli import main

def test_finance_help():
    runner = CliRunner()
    result = runner.invoke(main, ["finance", "--help"])
    assert result.exit_code == 0
    assert "Track personal finances" in result.output