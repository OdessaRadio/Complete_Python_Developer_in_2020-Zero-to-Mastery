# file I/O

my_file = open('test.txt')
#print(my_file.read()) # the idea of read function is cursor functionality. read only once after open
my_file.seek(0) # moves cursor
#print(my_file.read())
my_file.seek(0)

print(my_file.readline())
my_file.seek(0)
print(my_file.readline())
my_file.seek(0)
print(my_file.readlines())

# we have to close manually if we open with open command

my_file.close()


