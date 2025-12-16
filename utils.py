import argparse
import os

INPUT_FILE_MAP = {
    'small': 'input_small.txt',
    'full': 'input.txt',
    'test': 'input_test.txt'
}

def get_input(caller_file):
    """
    Parse command line arguments and return the appropriate input file content.

    Args:
        caller_file: Pass __file__ from the calling script

    Returns:
        str: Content of the selected input file

    Usage:
        input = get_input(__file__)

    Command line options:
        --input small (default): Uses input_small.txt
        --input full: Uses input.txt
        --input test: Uses input_test.txt
    """
    parser = argparse.ArgumentParser(description='Advent of Code Solution')
    parser.add_argument('--input', '-i', choices=['small', 'full', 'test'], default='small',
                        help='Input file to use: small (input_small.txt), full (input.txt), or test (input_test.txt)')
    args = parser.parse_args()

    # Get the directory of the calling file
    caller_dir = os.path.dirname(os.path.abspath(caller_file))
    input_path = os.path.join(caller_dir, INPUT_FILE_MAP[args.input])

    with open(input_path, 'r') as input_file:
        return input_file.read()
