#!/usr/bin/env python3
"""
pdf_crawler.py : - I'm writing this script to download the pdf files
related to my electrical engineering from one of the website.

"""
import requests,csv
from lxml import html
def crawl(url):
	"""
	
	:Always try to use this one okay!
	
	"""
	page_content = requests.get(url)
	tree = html.fromstring(page_content.content)
	data= tree.xpath('//a[@class="newbutton download"]/@href')[0]
	with open('drive.txt','a') as f:
		f.write(str(data)+"\n")
		f.close()
	

if __name__ == "__main__":
	with open('data.csv','rt') as f:
		data = csv.reader(f)
		num = 1
		for row in data:
			url = row[0]
			crawl(url)
			print(num)
			num += 1
	
