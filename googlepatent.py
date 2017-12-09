"""

        ******************** GOOGLE PATENT DATA EXTRACTION ***********************
        ** SUMMARY 
        GOOGLE PATENT API HAS BEEN DEPRECIATED AND NO LONGER PROVIDES API SUPPORT 
        I HAVE BUILT A WORK AROUND THE LIST OBFUSCATION BY SCRIPTING A DOWNLOAD STEP TO EXTRACT EACH 
        PATENT LIST FROM THE RELATED CSV AND THEN PARSING THE URL. THIS URL CAN THE BE CRAWLED.
        
        1. AUTOMATED WEB SEARCH
        2. AUTOMATED CSV PULL
        3. CSV URL PARSING
        4. WEB CRAWLING

        AUTHOR: ADAM MCMURCHIE
        DISCLAIMER: THIS CODE IS FOR PROOF OF CONCEPT ONLY, USE ONLY AND SHOULD NOT BE DISTRIBUTED AS AN OFFICIAL TOOL.

"""



import csv
import urllib2

# Import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup


# Basic search phrase we will use to get a list - best to be as short as possible
patent_search_phrase = 'typewriter'

# This is the exact patent phrase - and is required in order to get an exact match
patent_exact_phrase = "Electronic typewriter with display device "

# initializing field
Extracted_row = 'empty'

# URL will be modified for each patent key
url = 'https://patents.google.com/xhr/query?url=q%3D' + patent_search_phrase + '&exp=&download=true'

# Saving contents of URl to var
response = urllib2.urlopen(url)
cr = csv.reader(response)

# Fishing for the relevant row
for row in cr:
    if patent_exact_phrase in row:
        Extracted_row = row
        continue
#     print row


# Verification
print 'the value saved is '
print Extracted_row

# Get the last element

URL_ELEMENT = Extracted_row[-1]


print 'The URL Element is'
print URL_ELEMENT

# Just in case we need to convert to string with later soup version
patentURL = URL_ELEMENT

#pulling URL contents to var
page = urllib2.urlopen(patentURL)

# Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page, "html5lib")


# view format
print soup.prettify()