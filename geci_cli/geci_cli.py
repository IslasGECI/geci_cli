import argparse


def geci_cli():
    parser = argparse.ArgumentParser(description="GECI CLI")
    parser.add_argument("-i", "--input", action="append", nargs="+", help="Input files path")
    parser.add_argument("-o", "--output", action="append", nargs="+", help="Output files path")
    parser.add_argument("-d", "--drop", action="append", nargs="+", help="Drop values")
    parser.add_argument(
        "-n", "--iterations", action="append", nargs="+", help="Number of iterations"
    )
    return parser.parse_args()
