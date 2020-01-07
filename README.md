# Free Electrical Engineering Books downloader of Engineering Reference Sites
 
The intension of the script was to download the all the pdf files
related to my Electrical subject which provided by the [Engineering Reference](https://www.engineerrefe.com/search/label/english%20electrical?&max-results=9)
.
----
For those who want to just download the pdf file using python :
the steps to follow is :
1. Clone my repo 
	git clone git@github.com:suren40/pdf_crawler_google_drive.git
2. Install google drive downloader module
	pip install googledrivedownloader -t .

3. Download the file just by typing put the number if the error comes to start from the ls remaining.
	python downdload.py 1

The steps I followed,modules and methods.  I used  are given below in my own words.

### Python Modules I used are :
* Requests
* google-drive-downloader
### Methods I follow to crawl
* I used requests,xpath for crawling the links of the each page for downloading.
* I used the scraping tool first crawl all the pages link and save it into the csv.
* Once I had the url link of google drive I used the google_drive-downloader.


* The download part of the file is in download.py. I used the module called [google drive downloader](https://github.com/ndrplz/google-drive-downloader/).
	* I put the name of the file and changed the .zip file to .pdf. 

