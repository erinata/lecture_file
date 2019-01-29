f = open("data.txt")

#print(f.read(3))

print(f.read())


# f = open("data2.txt","w")

# print(f)

with open("data2.txt",'w',encoding = 'utf-8') as f:
   f.write("Hello data2\n")
   f.write("This is a test\n")

with open("data3.txt",'a',encoding = 'utf-8') as f:
   f.write("Hello data3\n")
   f.write("This is a test\n")
   f.write("This is a test of appending\n")


import csv

with open('dataset.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for r in csv_reader:
    	print(r)




