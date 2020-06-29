#program to read a file line by line a store them in a variable

f= open("gitam.txt","w")
f.write("hello let's learn python programing")

f= open("gitam.txt","r")
k= f.read()

print(k)
f.close()

