import argparse
from unittest import mock
from geci_cli import geci_cli


@mock.patch(
    "argparse.ArgumentParser.parse_args",
    return_value=argparse.Namespace(kwarg1="Isla", kwarg2="Temporada"),
)
def test_command(mock_args):
    obtained_paths = geci_cli()
    expected_paths_kwarg1 = "Isla"
    assert obtained_paths.kwarg1 == expected_paths_kwarg1
