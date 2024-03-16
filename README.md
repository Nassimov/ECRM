# Setup
```pip install -r requirements.txt```
# Run

```
Usage: main.py -c customer_file_path -p purchase_file_path

Options:
  -h, --help            show this help message and exit
  -c CUSTOMER_FILE_PATH, --cFile=CUSTOMER_FILE_PATH
                        The path of the customer csv file
  -p PURCHASE_FILE_PATH, --pFile=PURCHASE_FILE_PATH
                        The path of the purchase csv file
```
## Current exemple
``` python3 main.py -c customers.csv -p purchases.csv ```