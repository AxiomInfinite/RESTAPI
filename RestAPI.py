#Step 1 How to get the data from https://inspirehep.net/
import os, sys
import requests
from pprint import pprint

#Find a way to return this point when error hits
record_type = input("What Section would you like to search?")
query_string = input("")
#Ask user toe search through list 

#create a function to search through the website
def lookup(record_type, query_string):
    
    #require record_type to equal one of the words from list
    list = ['literature', 'authors', 'conferences', 'seminars', 'journals', 'jobs', 'experiments', 'data']
    if not record_type in list:
        print("Error, this is an incorrect search parameter, try again. ")
        #Figure out how to restart Function if this error
        quit()
        
    url = f"https://inspirehep.net/api/{record_type}?q={query_string}"
    r = requests.get(url)
    return r.content

#set lookup = to a variable for more flexibilty
api_results = lookup(record_type,query_string)
pprint(lookup(record_type,query_string))
