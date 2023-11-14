# Every month, a random number of students take the driving test at Fast & Furious (F&F) Driving School. To pass the test, a student cannot accumulate more than 18 demerit points.
# At the end of the month, F&F wants to calculate the average demerit points accumulated by ONLY the students who have passed, rounded to the nearest integer.
# Write a function which would allow them to do so. If no students passed the test that month, return 'No pass scores registered.'.
# Example:
# [10,10,10,18,20,20] --> 12
def passed(lst):
    passed_students = []
    sum = 0
    for student in lst:
        if student <= 18:
            passed_students.append(student)
            sum += student
    if len(passed_students) > 0:
        return round(sum / len(passed_students))
    else:
        return "No pass scores registered."


# This is linear time and constant space it is checking with a for loop or going through a line to verify if the "if" condition is true. Constant space as it is adding values to a variable.

# Can you find the needle in the haystack?

# Write a function findNeedle() that takes an array full of junk but containing one "needle"

# After your function finds the needle it should return a message (as a string) that says:

# "found the needle at position " plus the index it found the needle, so:

# Example(Input --> Output)

# ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 
# Note: In COBOL, it should return "found the needle at position 6"
def find_needle(haystack):
    for i in haystack:
        if i == 'needle':
            return f"found the needle at position {haystack.index(i)}"
#This was my solution upon doing the question, it is linear time as it is going through the for
#loop locating the 'needle'. Once it is found the if checks returns the the statement shown. It is constant space as no variable is being added.
#The better version is done below
def find_needle(haystack):
    return f"found the needle at position {haystack.index('needle')}"


# In this kata, you will write an arithmetic list which is basically a list that contains consecutive terms in the sequence.
# You will be given three parameters :

# first the first term in the sequence
# c the constant that you are going to ADD ( since it is an arithmetic sequence...)
# l the number of terms that should be returned
# Useful link: Sequence

# Be sure to check out my Arithmetic sequence Kata first ;)
# Don't forget about the indexing pitfall ;)
def seqlist(first, c, l):
    new_list = []
    num = first
    for i in range(0, l):
        new_list.append(num)
        num += c
    return new_list
# I finished this challenge with a linear time and constant space Following through the loop I was able to add the numbers in the list limit the memory usage and going in a straight line depending on the range function.