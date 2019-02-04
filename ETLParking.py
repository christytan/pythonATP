# // extract data from realtime api to database

# // 1/extract data from api
# // 2/call the same api every 5 min(match the update frequency) - do them have api call limitation?
# // 3/load data into oracle db



#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata
from io import StringIO
from tabulate import tabulate

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
#client = Socrata("data.smgov.net", None)

# Example authenticated client (needed for non-public datasets):
client = Socrata("data.smgov.net",
                 "cTSRNtRpIobl1Bp9avgIa76D0",
                 username="gchristytan@gmail.com",
                 password="Tanchen062900")

# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("tce2-7ir6", limit=10)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     print(results_df)

# print(tabulate(results_df, headers='keys', tablefmt='psql'))
print(results_df.to_string())