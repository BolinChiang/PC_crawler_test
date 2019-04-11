import requests
import json
import sys
import os


class PcrawlerClass():

    def __init__(self):
        print("Welcome Pcrawler")

    def search_pchome(self, text):
        open("re_title.txt", 'w')
        url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=" + text

        res = requests.get(url)  # Request Method: GET
        data = json.loads(res.text)
        webdatas = data['prods']
        for product in webdatas:

            with open("re_title.txt", 'a') as file:
                file.write(product['name'] + "\n")
                file.close()
            #print(product['name'])