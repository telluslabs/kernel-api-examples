"""
MIT License

Copyright (c) 2018 TellusLabs

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

## download_csv.py
##
## This script will download a CSV containing the TellusLabs data specified in
## the script.  The CSV output from this script has standardized columns in a
## specified order, and this script can be ran daily to produce the expected
## output.
##
## The script below uses a date range from January 1st, 2018 through May 1st,
## 2018.  To only retrieve values for the current date, replace the hard-coded
## date values with the current_date variable
##
## You can retrieve your personal API key from your profile page in the Kernel
## Web platform.  https://kernel.telluslabs.com/#/profile
##
## To get an updated list of available metric codes in Kernel, please download
## the TellusLabs Data Dictionary from your profile page in Kernel Web.
## https://kernel.telluslabs.com/#/profile
##
## For additional assistance, please email kernel-support@telluslabs.com



import requests
import datetime

API_KEY = 'abc123'  # Replace with your API key!
assert API_KEY is not None, 'Please set API_KEY to your personal API key'

current_date = datetime.datetime.today().strftime('%Y-%m-%d')

GEO_LEVEL = 'level_2' # 'level_1' = National, 'level_2' = State, 'level_3' = County
COUNTRY_ISO = 'USA'  # 3-letter country ISO
START_DATE = '2018-01-01'
END_DATE = '2018-05-01'
TARGET_FILE_PATH = '/Users/John/Desktop/telluslabs_data.csv' # Replace with path to your target CSV file
METRIC_CODES = 'SATTELREF1,SATTELREF2,SATTELREF3,SATTELREF4,SATTELREF5,SATTELREF6,SATTELREF7'  # Replace with your desired metrics
CROP = 'corn' # Replace with your desired crop

r = requests.get('https://api.kernel.telluslabs.com/api/v1/metrics/',
                 params={
                     'geo_level': GEO_LEVEL,
                     'country_iso': COUNTRY_ISO,
                     'start_date': START_DATE,
                     'end_date': END_DATE,
                     'api_key': API_KEY,
                     'metric_code': METRIC_CODES,
                     'crop': CROP
                 },
                 headers={'Accept': 'text/csv'})
r.raise_for_status()

with open(TARGET_FILE_PATH, 'w') as f:
    f.write(r.text)

print('CSV generated at {}'.format(TARGET_FILE_PATH))
