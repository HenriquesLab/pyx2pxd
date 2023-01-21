#!/usr/bin/env python

"""Tests for `pyx2pxd` package."""

import pytest
import os


from pyx2pxd.pyx2pxd import autogenerate_pxd_files


@pytest.fixture
def sanbox_path() -> str:
    """
    Get the sandbox directory for testing
    """
    path = os.path.join(os.path.dirname(__file__), "..", "sandbox")
    return path


def test_pyx2pxd(sanbox_path: str):
    """
    Test the pyx2pxd function
    """
    autogenerate_pxd_files(sanbox_path)
    assert os.system("cythonize -i " + os.path.join(sanbox_path, "*.pyx")) == 0
    

