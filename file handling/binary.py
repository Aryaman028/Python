import pickle
file = open("binarywb.dat","wb")
pickle.dump("yes you are right",file)
file.close()

file = open("binarywb.dat","rb")
data = pickle.load(file)
print(data)
file.close() 
