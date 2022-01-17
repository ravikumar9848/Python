f = open('merge.txt','r')
data = f.read()
print(data.count('the'))
#The tell() method returns the current file position in a file stream.
print(f.tell())

'''seek() function is used to change the position of the File Handle to a given specific position.
   File handle is like a cursor, which defines from where the data has to be read or written in the file.'''
print(f.seek(20))
