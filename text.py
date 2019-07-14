#!/usr/bin/env python3
'''
This is for the finding the text

'''
import requests
from lxml import html

url = "https://www.engineerrefe.com/2019/05/protection-of-industrial-power.html"
page_content = requests.get(url)
with open ("content.txt","w",encoding='utf-8') as file:
	file.write(html.fromstring(page_content.content:))
	file.close()
print("Done !!")

