#program to read a entire text file

f= open("gitam_file.txt", "w")
f.write("hello everyone , this is kishore from Gitam")

f= open("gitam_file.txt","r")
s= f.read()

print(s)
f.close