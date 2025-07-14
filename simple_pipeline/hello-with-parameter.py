"""Say hello to a person given as argument."""

import argparse


def parse_args():
    """Define and parse command line arguments."""
    parser = argparse.ArgumentParser(description="Say hello to a person.")
    parser.add_argument("--name", type=str, help="Name of the person to greet")
    return parser.parse_args()


def main():
    args = parse_args()
    print(f"Hello, {args.name}!")


if __name__ == "__main__":
    main()
