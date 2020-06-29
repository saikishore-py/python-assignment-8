#program to append text to a file and display the text

#append a file
f= open("gitam_file.txt","a")
string= ''' Let's start coding'''
f.write(string)
f.close()