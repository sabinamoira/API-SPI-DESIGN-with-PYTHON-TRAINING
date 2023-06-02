#!/usr/bin/env python3

# pprint makes dictionaries a lot more human readable
from pprint import pprint

# requests is used to send HTTP requests (get it?)
import requests
import urllib.request
import json
#URL = "https://swapi.dev/luke/force"      # Comment out this line
URL= "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=fcd11be9d2ba4d5d9db16661273ae4f9"     # Uncomment this line

# Printing responses from https://newsapi.org/ 
def main():
    """sending GET request, checking response"""

    # SWAPI response is stored in "resp" object
    resp= requests.get(URL)

    # check to see if the status is anything other than what we want, a 200 OK
    if resp.status_code == 200:
        # convert the JSON content of the response into a python dictionary
      #Prints the api response
        apiResp= resp.json()
        # pprint(apiResp)
          # call the api
        APIurl = urllib.request.urlopen(URL)

    # strip off the attachment (JSON) and read it
    # the problem here, is that it will read out as a string
        jsonToSring = APIurl.read()

        jsonTOstring = json.loads(jsonToSring.decode("utf-8"))
      


      
      # Get the first article from json string
        firstArticle = jsonTOstring["articles"]
      # print the first article json
        # pprint(firstArticle[0])




        # send HTTP GET to one of the entries within the list
        r = requests.get(URL)
        decodedjson = r.json() # decode the JSON on the response
          # gets articles from the json
        articles = decodedjson.get("articles")
       # holds the first article
        first_article = articles[0]
   
      
      # this solution uses "f-strings" (string templates) to return the data
       # prints first article title and contents
      
        print(f"The first article's title is: \n {first_article['title']} \n \n And its content is: \n  {first_article['content']}")


    else:
        print("That is not a valid URL.")

if __name__ == "__main__":
    main()

