#Step 1 How to get the data from https://inspirehep.net/
import requests
from pprint import pprint


record_type = input("What Section would you like to search?")
query_string = input("query bullshit")

#create a function to search through the website
def lookup(record_type, query_string):
    #Types in Search area
    
    #require record_type to equal one of the words from list
    list = ['literature', 'authors', 'conferences', 'seminars', 'journals', 'jobs', 'experiments', 'data']
    if not record_type in list:
        print("Error, this is an incorrect search parameter. ")
        #stop action if search parameter is wrong

    url = f"https://inspirehep.net/api/{record_type}?q={query_string}"
    r = requests.get(url)
    return r.content
#set lookup = to a variable
api_results = lookup(record_type,query_string)
pprint(lookup(record_type,query_string))
