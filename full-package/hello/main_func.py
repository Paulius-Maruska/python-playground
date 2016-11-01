import argparse
import sys

from .hello_func import hello


def get_parser():
    parser = argparse.ArgumentParser(
        description="Say hello.",
    )
    parser.add_argument("names", metavar="name", type=str, nargs="+",
                        help="name to say hello to")
    parser.add_argument("-e", "--stderr", dest="stream", action="store_const", const=sys.stderr, default=sys.stdout,
                        help="output all greatings in stderr, instead of stdout")
    return parser


def main(args=None):
    parser = get_parser()
    parsed = parser.parse_args(args)
    for name in parsed.names:
        hello(name, parsed.stream)
