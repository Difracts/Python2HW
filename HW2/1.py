import os
f1 = open("names1.txt",'r')
f2 = open("names2.txt",'w+')
lines = f1.readlines()
for i in lines:
    date = i.split()
    date[0] = date[0].capitalize()
    date[1] = date[1].capitalize()
    date[-1] = "301+" + date[-1]
    past = date[0]+" "+date[1]+" "+date[2]+" "+date[3]
    f2.write("".join(past+"\n"))
    