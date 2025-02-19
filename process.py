import csv

from decimal import Decimal
from argparse import ArgumentParser
from clipboard import copy_to_clipboard


def process_transactions(transaction_reader, flip_sign):
    # TODO: Add different formatting options
    multiplier = (-1 if flip_sign else 1)

    formatted = [
        [t['Date'], t['Reference'], str(multiplier * Decimal(t['Amount (GBP)']))]
        for t in transaction_reader
        if t['Amount (GBP)']
    ]


    # TODO: Sort by date ASC
    return formatted

def process_csv(in_file):
    with open(in_file) as in_csv:
        processed = process_transactions(csv.DictReader(in_csv), flip_sign=False)

        return "\n".join(["\t".join(p) for p in processed])

def parse_args():
    parser = ArgumentParser(prog='Transation CSV Processor')
    parser.add_argument('-i', '--in-file', required=True)

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    processed = process_csv(args.in_file)

    copy_to_clipboard(processed)
    print('Result copied to clipboard')
