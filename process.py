import csv

from decimal import Decimal
from argparse import ArgumentParser

from src.clipboard import copy_to_clipboard
from src.config import FileConfig


def process_transactions(transaction_reader, config):
    multiplier = (-1 if config.flip_values else 1)

    formatted = [
        [t[config.date_col], t[config.desc_col], str(multiplier * Decimal(t[config.value_col]))]
        for t in transaction_reader
        if t[config.value_col]
    ]

    return formatted

def process_csv(in_file, type):
    config = FileConfig.from_type(type)

    with open(in_file) as in_csv:
        processed = process_transactions(csv.DictReader(in_csv), config)

        return "\n".join(["\t".join(p) for p in processed])

def parse_args():
    parser = ArgumentParser(prog='Transation CSV Processor')
    parser.add_argument('-i', '--in-file', required=True)
    parser.add_argument('-t', '--type', required=True, choices=FileConfig.FILE_TYPES)

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    processed = process_csv(args.in_file, args.type)

    copy_to_clipboard(processed)
    print('Result copied to clipboard')
