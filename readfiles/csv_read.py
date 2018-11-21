import csv

date = csv.reader(open('E:\\info.csv','r'))

for user in date:
    print(user)
    print(user[1])