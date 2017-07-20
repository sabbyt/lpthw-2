from sys import argv
# import = how you add features/modules to your script from the Python feature set
# instead of giving all features - can choose, making it more lightweight

# argv = argument variable
# holds the arguments you pass to your Python script when you run it

script, dog, cat = argv

mouse = raw_input('What is the name of your mouse? ')

print "The script is called:", script
print 'Your dog variable is:', dog
print 'Your car variable is:', cat
print 'Your mouse variable is:', mouse
