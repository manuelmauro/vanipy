from click.testing import CliRunner

from vanipy import vanipy


def test_vanipy_cli():
    runner = CliRunner()
    result = runner.invoke(vanipy, ["ASD"])
    assert result.exit_code == 0
    assert "ASD" in result.output
