import csv,requests
from lxml import html
count = 0
page_content = requests.get('https://www.engineerrefe.com/search/label/english%20electrical?&max-results=9')
tree = html.fromstring(page_content.content)
rows = tree.xpath('//h2[@class="post-title"]/a')
path_link = './@href'
path_name = './text()'
for row in rows:
    link = row.xpath(path_link)[0]
    name = row.xpath(path_name)[0]
    with open('listing.csv','a') as f:
        thewriter = csv.writer(f)
        if count == 0: 
            header = ['link'.upper(),'name'.upper()]
            thewriter.writerow(header)
            count +=1
        thewriter.writerow([link,name])

