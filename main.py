import json
import os
from optparse import OptionParser
from typing import List
from models.ecrm_request import ECRMRequest
from models.purchase import Purchase
from utils.functions import read_csv_file
import requests
from dotenv import load_dotenv
import jsonpickle

load_dotenv()

# Declare the required options

parser = OptionParser()

parser.add_option("-c", "--cFile", dest="customer_file_path", 
                  action="store", type="string",
                    help="The path of the customer csv file")

parser.add_option("-p", "--pFile", dest="purchase_file_path",
                  action="store", type="string",
                    help="The path of the purchase csv file")

parser.set_usage(parser.get_prog_name() + " -c customer_file_path -p purchase_file_path")

options, args = parser.parse_args()

if not (options.customer_file_path and options.purchase_file_path):
    parser.error("Customer file path (-c) and purchase file path (-p) are required.")

# Read purchases & Customers files from the path 

customers_data = read_csv_file(options.customer_file_path)
purchases_data = read_csv_file(options.purchase_file_path)

# Group purchases by customer_id

grouped = purchases_data.groupby('customer_id')
ecrm_request: List[ECRMRequest]=[]
for name, group in grouped:
    #  get purchases 
    purchases:List[Purchase] = []
    for idx,item in group.iterrows():
      purchases.append(
        Purchase(
          currency=item['currency'],
          price=int(item['price']),
          product_id=item['product_id'],
          quantity=int(item['quantity']),
          purchased_at=item['date'],
          ),
        )
    # get Customer      
    customer= customers_data.loc[customers_data['customer_id'].values == int(group.iloc[0]['customer_id'])]

    ecrm_request.append(
      ECRMRequest(
        salutation='', # value not provided !
        last_name=customer['lastname'].values[0],
        first_name=customer['firstname'].values[0],
        email=customer['email'].values[0],
        purchases=purchases
      )
    )

#  Generate the JSON file 

put_data = jsonpickle.encode(ecrm_request,unpicklable=False)

#  execute PUT REST request
# To increase the security the best way is to add a bear token in header

try:
  response =  requests.put(
    url=os.getenv('ECRM_API_URL'),        # TODO Adapt by envirenment 
    headers={                             # [IGNORE THE 'headers' IF YOU DONT USE BEARER TOKENS]
      'Content-Type': 'application/json',
      'Authorization': 'Bearer BEARER'
      },
    json=put_data
    ) 
  if (response.status_code == 200):
    print("Updated succefully")
  else:
    raise Exception('ERROR : '+response.text)
except Exception as e:
  raise e