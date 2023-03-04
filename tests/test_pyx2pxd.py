#!/usr/bin/env python

"""Tests for `pyx2pxd` package."""

import os
from pyx2pxd.pyx2pxd import autogenerate_pxd_files


def test_pyx2pxd():
    """
    Test the pyx2pxd function
    """
    path = os.path.dirname(os.path.realpath(__file__))
    func_name = "cdef int test_pyx2pxd():\n"
    file = open(os.path.join(path, "testpyx.pyx"), "w")
    lines_to_write = "# cython: autogen_pxd=True\n"
    lines_to_write += "\n"
    lines_to_write += func_name
    lines_to_write += "    return 1"
    file.writelines(lines_to_write)
    file.close()
    autogenerate_pxd_files(path)
    assert (
        func_name[:-2]
        in open(os.path.join(path, "testpyx.pxd"), "r").readlines()[-1]
    )
    os.remove(os.path.join(path, "testpyx.pyx"))
    os.remove(os.path.join(path, "testpyx.pxd"))
