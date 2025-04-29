course = 'Python for Beginners'
print(len(course))

##########################################################################

print(course.upper())       # does not change the original string
print(course)

print(course.lower())

##########################################################################

print(course.find('t'))    # python is case sensitive
print(course.find('z'))
print(course.find('for'))

##########################################################################

print(course.replace('Beginners', 'Absolute Beginners'))

##########################################################################

print('Python' in course )
print('python' in course )
