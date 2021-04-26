#! /usr/bin/env python

import sys
from packaging import version

import numpy


def prev() -> str:
    major, minor, _ = _installed().release

    if minor == 0:
        exit(1)

    minor -= 1
    print(f"{major}.{minor}.0")
    exit()


def _installed() -> version:
    return version.parse(numpy.__version__)


if __name__ == "__main__":
    globals()[sys.argv[1]]()
