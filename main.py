import requests
import json
import sys
import os
from pcrawler import *


get_input = sys.argv[1]
# get_input = input("go")


pcw = PcrawlerClass()
pcw.search_pchome(get_input)
