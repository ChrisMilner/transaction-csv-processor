from argparse import ArgumentParser

from src.processor import Processor
from src.list_outputter import ListOutputter
from src.config import FileConfig


def parse_args():
    parser = ArgumentParser(prog='Transation CSV Processor')
    parser.add_argument('-f', '--file', required=True)
    parser.add_argument('-t', '--type', required=True,  choices=FileConfig.FILE_TYPES)
    parser.add_argument('-o', '--out',  required=False, choices=ListOutputter.OUTPUT_OPTIONS, default='file')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    processor = Processor(args.type) 
    result = processor.process_csv(args.file)

    outputter = ListOutputter(result)
    outputter.output(args.out)
