print("Creating Tree")

import argparse
import pathlib
from pathlib import Path

arg_parser = argparse.ArgumentParser(
        prog = 'VHDLBlockTree',
        description = 'This program assembles a hierarchy tree based on the current valid VHDL',
        epilog = 'As of now the \"generate\" VHDL functionality is NOT supported.')

arg_parser.add_argument('path_to_top', type = pathlib.Path)

args = arg_parser.parse_args()
print(args.path_to_top.exists())
