
import requests
import json
import sys
import os


#get_input = sys.argv[1]
get_input = input("go")

def search_pchome(text):

    url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=" + text

    res = requests.get(url)  # Request Method: GET
    data = json.loads(res.text)
    webdatas = data['prods']
    for product in webdatas:

        with open("re_title", 'a') as file:
            file.write(product['name'] + "\n")
            file.close()
        #print(product['name'])


search_pchome(get_input)
