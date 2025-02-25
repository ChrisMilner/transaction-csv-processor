import csv

from src.clipboard import copy_to_clipboard


class ListOutputter:
    OUTPUT_OPTIONS = ['clipboard', 'file']

    def __init__(self, data):
        self.data = data
    
    def output(self, method):
        if method == 'file':
            self.output_to_file(f"output.csv")
        elif method == 'clipboard':
            self.output_to_clipboard()

    def output_to_file(self, filename):
        with open(filename, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(self.data)
        
        print(f"Result written to {filename}")

    def output_to_clipboard(self):
        copy_to_clipboard(self._format_data_for_clipboard())

        print("Result copied to clipboard")
    
    def _format_data_for_clipboard(self):
        return "\n".join(["\t".join(p) for p in self.data])
