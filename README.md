# Transaction CSV Processor

> Formats CSV transaction lists from various bank accounts into a standardised format

## Usage
```sh
python3 .\process.py -f <FILE> -t <TYPE> -o <OUTPUT_METHOD>
```

* `FILE` - The CSV transaction file you want to process
* `TYPE` - The type of transaction list, currently supported options are:
  * `DETECT` - Will attempt to detect one of the following types from the filename
  * `NW_DEBIT` - Natwest Debit card
  * `NW_CREDIT` - Natwest Credit card
  * `STARLING` - Starling account
* `OUTPUT_METHOD` - How you want the data outputted, defaults to `file`. Options are:
  * `file` - Outputs the formatted data into a file called `output.csv`
  * `clipboard` - Copies the formatted data into your clipboard ready to be pasted into a spreadsheet
