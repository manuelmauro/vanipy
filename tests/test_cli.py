from click.testing import CliRunner

from vanipy import vanipy


def test_vanipy_prefix_json_out():
    runner = CliRunner()
    result = runner.invoke(vanipy, ["prefix", "--json", "ASD"])
    assert result.exit_code == 0
    assert "ASD" in result.output


def test_vanipy_prefix_table_out():
    runner = CliRunner()
    result = runner.invoke(vanipy, ["prefix", "ASD"])
    assert result.exit_code == 0
    # TODO make this work
    # assert "ASD" in result.stdout
