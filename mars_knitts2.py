import requests
from bs4 import BeautifulSoup
import re

# base url for the MARS reports
base_url = 'http://lms01.harvard.edu/mars-reports/'

# list of months to retrieve urls for
months = ['jan-15-data/', 'feb-15-data/', 'mar-15-data/', 'apr-15-data/']

# list of reports to retrieve urls for
reports = ['R07_Unmatched_Primary_Headings_LC_Subjects']


# function to retrieve URLs for specified reports from specified months
def getURLs():

    # create an empty list to hold the URLs
    urlList = []

    for month in months:

        url = base_url + month

        data = (requests.get(url)).content

        soup = BeautifulSoup(data)

        for link in soup.find_all('a'):

            for report in reports:

                regex = report + '[_\d{3}]*' + '.htm'

                # returns a list of what it finds, and an empty list if nothing is found
                filename = re.findall(regex, link.get('href'))

                # specifies that we only want the results of re.findall if there's data
                if filename:

                    # specifies we want the contents of the list, not the list itself
                    reportUrl = url + filename[0]

                    urlList.append(reportUrl)

    parseReports(urlList)


def parseReports(urlList):

    # gets the bib numbers from a report
    # right now, just parses R06 & R07 reports - probably works on R13, R14, R25 too

    bibsList = []

    for url in urlList:

        report = (requests.get(url)).content

        newSoup = BeautifulSoup(report)

        bibs = newSoup.find_all("td", class_='ctl_no')

        for bib in bibs:

            if str(bib.get_text()):

                bibsList.append(str(bib.get_text()))

    print bibsList


getURLs()