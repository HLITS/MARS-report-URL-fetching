import requests
from bs4 import BeautifulSoup
import re

base_url = 'http://lms01.harvard.edu/mars-reports/'

months = ['jan-15-data/', 'feb-15-data/', 'mar-15-data/', 'apr-15-data/']

reports = ['R00_Near_Match', 'R03_Authority_Change_Report_AUTHS', 'R04_Authority_Delete_Report_AUTHS']

for month in months:

    url = base_url + month

    data = (requests.get(url)).content

    soup = BeautifulSoup(data)

    for link in soup.find_all('a'):

        for report in reports:

            regex = report + '[_\d{3}]*' + '.htm'
            
            filename = re.findall(regex, link.get('href'))

            if filename:
               
			   reportUrl = url + filename[0]
			   
               print reportUrl