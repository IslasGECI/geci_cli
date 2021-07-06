from geci_cli import geci_cli
from unittest import mock

import argparse

@mock.patch('argparse.ArgumentParser.parse_args',return_value=argparse.Namespace(kwarg1="Isla", kwarg2="Temporada"))
def test_command(mock_args):
    obtained_paths = geci_cli()
    pass