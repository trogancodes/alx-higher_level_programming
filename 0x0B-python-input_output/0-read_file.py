#!/usr/bin/python3
"""Defines a text file-reading function."""
def read_file(filename=""):
    """Print the contents of  UTF8 into stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
