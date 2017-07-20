# imports the argv module
from sys import argv

# assigns argvs to vars
script, filename = argv

# makes a file object
# used a built in method to open that file
txt = open(filename)

# prints filename
print "Here's your file %r:" % filename

# since the file was assigned to txt var then can read it
print txt.read()
txt.close()

#asks for user prompt
print 'Type the filename again:'
file_again = raw_input('> ');

txt_again = open(file_again)

print txt_again.read()
txt.close()
