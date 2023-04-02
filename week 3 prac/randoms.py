"""
What did you see on line 1?
The smallest  number on line 1 is 6 and the largest number is 19.

What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?
The smallest  number on line 2 is 3 and the largest number 7.
Line 2 could not have produced a 4 since the step is 2 and 4 is not a multiple of 2 within the range.

What did you see on line 3?
What was the smallest number you could have seen, what was the largest?
The smallest number that could have been generated on line 3 is 2.8 and 3.9.

Write code, not a comment, to produce a random number between 1 and 100 inclusive.

"""
import random
random_number = random.randint(1, 101)
print(random_number)
