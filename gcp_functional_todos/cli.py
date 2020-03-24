"""Console script for gcp_functional_todos."""
# flake8: noqa
# pylint: skip-file
import argparse
import sys


def main():
    """Console script for gcp_functional_todos."""
    parser = argparse.ArgumentParser()
    parser.add_argument("_", nargs="*")
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print(
        "Replace this message by putting your code into "
        "gcp_functional_todos.cli.main"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
