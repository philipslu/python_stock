import csv
csvfile = ('c:/Sheet1.csv','rb')
reader=csv.reader(csvfile)
for line in reader:
    print line
    
csvfile=file('c:/Sheet1.csv','wb')    
writer = csv.writer(csvfile)
writer.writerow(['site','data','total','totalsold','memo'])
data = [reader]
writer.writerows(data)
csvfile.close()