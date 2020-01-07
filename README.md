# Free Electrical Engineering Books downloader of Engineering Reference Sites
 
The intension of the script was to download the all the pdf files
related to my Electrical subject which provided by the [Engineering Reference](https://www.engineerrefe.com/search/label/english%20electrical?&max-results=9)
.


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

