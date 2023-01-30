# f = open("aryaman.txt","w")
# f.write("Aryaman is briliant in programing \n")
# f.write("He is outstanding \n")
# f.close()
# f = open("aryaman.txt","a")
# f.write("Bolo tarara \n")
# f.write("jai ho \n")
# f.close()
c = 0
c1 = 0
f = open("aryaman.txt","r")
t = f.readlines()
for line in t:
    words = line.split(" ")
    for i in words:
        c += 1
        for j in i:
            c1 +=1

print("countletters",c1)

print("count:",c)
f.seek(0)
t = f.read(10)
print(t)
f.close()

f = open("demofile3.txt","w")
f.write("File has been started")
l = ["Aryaman \n" ,"teri \n", "kya haal hai \n"]
f.writelines(l)
f.close()
f = open("demofile3.txt","a")
f.write("More content has been added")
f.close()
