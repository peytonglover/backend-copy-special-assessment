#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "peyton glover got help from coaches"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    path_list = []
    for path in os.listdir(dirname):
        pattern = re.search(r'__(\w+)__', path)
        if pattern:
            path_list.append(os.path.abspath(os.path.join(dirname, path)))
    return path_list


def copy_to(path_list, dest_dir):
    """Copies files in path_list to new destination"""
    # your code here
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for paths in path_list:
        filename = os.path.basename(paths)
        shutil.copy(paths, os.path.join(dest_dir, filename))


def zip_to(path_list, dest_zip):
    """Creates a zip file of files in path_list"""
    # your code here
    cmd = ['zip', '-j', dest_zip]
    cmd.extend(path_list)
    try:
        subprocess.check_output(cmd)
    except subprocess.CalledProcessError as e:
        print(e.output)
        raise


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='name of dir to search')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).
    if not ns:
        parser.print_usage()
        return
    # Your code here: Invoke (call) your functions
    if not ns.from_dir:
        parser.print_usage()
        return

    to_dir = ns.todir
    to_zip = ns.tozip
    from_dir = ns.from_dir
    path_list = get_special_paths(from_dir)

    if to_dir:
        copy_to(path_list, to_dir)
    elif to_zip:
        zip_to(path_list, to_zip)
    else:
        print('\n'.join(get_special_paths(from_dir)))


if __name__ == "__main__":
    main(sys.argv[1:])
