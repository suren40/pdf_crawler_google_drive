# PDF downloads
The intension of the script was to download the all the pdf files
related to my subject which which provide by the [Engineering Reference](https://www.engineerrefe.com/search/label/english%20electrical?&max-results=9)
.


The steps I followed,modules I used are given below in the points
* I used requests,xpath for crawling the links of the each containing the download button.
	* I had the problem while clicking next page after google selenium was an option but I found one extension using that extension I crawled every web pages because pagination was very hard for.
	* The app was Dataminer(google it)!
	* The sample code for the link_crawler.py which contains extraction of first page

* Next, I wanted to the url of google drive and the name of the file so that I can download and name file at the same time.I coded script to output the file in .csv which contains the google drive link of every file. It is on csv_ready.py

* The download part of the file is in download.py. I used the module called [google drive downloader](https://github.com/ndrplz/google-drive-downloader/).
	* I put the name of the file and changed the .zip file to .pdf. 

