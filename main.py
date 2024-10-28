"""
ETL-Query script
"""
from mylib.extract import extract
from mylib.query import create_query, read_query, update_query, delete_query
import argparse
import sys

def handle_arguments(args):
    """Add action based on initial calls"""
    parser = argparse.ArgumentParser(
        description="CRUD Script", formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "Functions",
        choices=["extract", "crud"],
        help="Specify one of the functions to execute: extract or crud."
    )

    # Parse arguments
    return parser.parse_args(args)

def main():
    # Handle command-line arguments
    args = handle_arguments(sys.argv[1:])

    # Execute based on the chosen function
    if args.Functions == "extract":
        print("Extracting data....")
        print(extract())
    elif args.Functions == "crud":
        print("Creating data...")
        create_query()
        print("Reading data...")
        print(read_query())
        print("Updating data...")
        update_query(80, 63, "Boston Red Sox")
        print("Deleting data...")
        print(delete_query())

if __name__ == "__main__":
    main()