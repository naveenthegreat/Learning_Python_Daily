#File I/O

'''
Python file handling involves performing operations such as creating,
opening, reading, writing, and closing files

File handling allows you to:
    
    -Save progress or logs (like JSON)
    -Read config files
    -Track history (like expenses, habits)

    
'''
# open("filename", "mode of opening(read mode by default)")

'''
MODES OF OPENING A FILE:

 r   - open for reading
 w   - open for writing
 a   - open for appending
 +   - open for updating.
'rb'  will open for read in binary mode.
'rt'   open for read in text mode.'''

f = open("Learning_Python_Daily/Learning_Python_Daily/nav.txt", "r")
data = f.read()
print(data)
f.close()

# write

na="Naveen is the great"
f = open("na.txt","w")
f.write(na)
f.close()

# #We can also use f.readline() function to read one full line at a time.

f=open("Learning_Python_Daily/Learning_Python_Daily/nav.txt")
data=f.readline() # Read one line from the file.
print(data,type(data))
f.close()
#or
f=open("Learning_Python_Daily/Learning_Python_Daily/nav.txt")
data=f.readlines() # Read lines from the file.
print(data,type(data))
f.close()
#or
f=open("Learning_Python_Daily/Learning_Python_Daily/nav.txt")
data1=f.readline() # Read one line from the file.
print(data,type(data))

data2=f.readline() # Read one line from the file.
print(data2,type(data2))

data3=f.readline() # Read one line from the file.
print(data3,type(data3))
f.close()
#or
data=f.readline()
while(data != ""):
    print(data)
    data=f.readline()

f.close()

# Open the file in read mode using 'with', which automatically closes thefile
with open("Learning_Python_Daily/Learning_Python_Daily/nav.txt", "r") as f:
    print(f.read())# Read the contents of the file
