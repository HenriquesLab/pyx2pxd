"""Console script for pyx2pxd."""
import sys

from . import pyx2pxd


def main():
    """
    Console script for pyx2pxd.
    Pass path to dir where pyx2pxd should look for .pyx files as argument.

    
    """

    pyx2pxd.main()


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
