"""
This is the python script which helps to crawl the pdf files from the drive url.
drive.csv has the drive url and google drive downloader will download


Crawler may stop any time so we need to give the input  manaully to start the crawler using sys.argv
"""

import csv
from sys import argv

import sys

from google_drive_downloader import GoogleDriveDownloader as gdd
def crawler(DRIVE_URL,start):
    with open (DRIVE_URL,'rt') as f:
        data = csv.reader(f)
        item_list = list(data)
        print(len(item_list))
    for i in range(start,len(item_list)):
        link = item_list[i][0].strip()
        print(link)
        file_name = item_list[i][1]+'.pdf'
        print(file_name)
        gdd.download_file_from_google_drive(file_id=link,dest_path='./data/'+file_name)


if __name__ == "__main__":
    start = argv[1]

    DRIVE_URL = "drive.csv"
    print("Main Function started")
    crawler(DRIVE_URL,int(start))
