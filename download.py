import csv
from google_drive_downloader import GoogleDriveDownloader as gdd
with open ('drive.csv','rt') as f:
	data = csv.reader(f)
	item_list = list(data)
	print(len(item_list))
for i in range(205,len(item_list)):
	link = item_list[i][0].strip()
	print(link)
	file_name = item_list[i][1]+'.pdf'
	print(file_name)
	gdd.download_file_from_google_drive(file_id=link,dest_path='./data/'+file_name)
