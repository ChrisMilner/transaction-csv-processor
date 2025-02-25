from argparse import ArgumentParser

from src.clipboard import copy_to_clipboard
from src.config import FileConfig
from src.processor import Processor


def parse_args():
    parser = ArgumentParser(prog='Transation CSV Processor')
    parser.add_argument('-i', '--in-file', required=True)
    parser.add_argument('-t', '--type', required=True, choices=FileConfig.FILE_TYPES)

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    processor = Processor(args.type) 
    result = processor.process_csv(args.in_file)

    copy_to_clipboard(result)
    print('Result copied to clipboard')
