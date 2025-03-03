import csv

from decimal import Decimal
from src.config import FileConfig


class Processor:
    def __init__(self, type):
        self.config = FileConfig.from_type(type) if type != 'DETECT' else None

    def process_csv(self, filename):
        if not self.config:
            self.config = FileConfig.detect_from_filename(filename)

        with open(filename) as file:
            return self._process_transactions(csv.DictReader(file))

    def _process_transactions(self, transaction_reader):
        multiplier = (-1 if self.config.flip_values else 1)

        formatted = [
            [t[self.config.date_col], t[self.config.desc_col], str(multiplier * Decimal(t[self.config.value_col]))]
            for t in transaction_reader
            if t[self.config.value_col]
        ]

        return formatted
