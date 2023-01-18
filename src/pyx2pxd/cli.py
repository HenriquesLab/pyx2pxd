"""Console script for pyx2pxd."""
import argparse
import sys

from . import pyx2pxd


def main():
    """Console script for pyx2pxd.
    Pass path to dir where pyx2pxd should look for .pyx files as argument.
    >>> pyx2pxd example_dir"""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()
    
    pyx2pxd.main()

    # print("Arguments: " + str(args._))
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
