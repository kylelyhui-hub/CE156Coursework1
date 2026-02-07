Exercise 1 (30%)
Write a function that returns a list of all non-prime numbers between two positive integers 
supplied as arguments. Use this in a program that asks the user to supply two positive 
integers, checks that the input is valid, then calls the function and outputs the numbers in 
the returned list, with 10 numbers per output line. The output should be displayed in the 
format
8 9 10 12 11 14 15 16 18 20
21 22 24 25 26 28
If the user enters negative numbers the program should output an appropriate error 
message; the two numbers should be accepted in either order. The range should be 
inclusive; if the user inputs 312 and 351 (or 351 and 312) these two numbers (which are 
both non-prime) should be included in the output.

Exercise 2 (20%)
Write a function that takes as an argument a list of strings and generates and returns a 
dict object mapping lengths to lists of strings of that length. For example if the list is 
[”The”, ”cat”, ”sat”, ”on”, ”a”, ”carpet”]; the dict that is produced 
should be { 1:[”a”], 2:[”on”], 3:[”The” ,”cat” ,”sat”], 6:[”carpet”]}.
Write code that asks the user to input a line of text, splits the text into a list of words, 
supplies the list as an argument to the above function and finally outputs the dict object 
returned by the function. (The format of the output does not matter.)

Exercise 3 (50%)
The three functions for this exercise should be written in a single .py file. You should not 
submit any code that calls the functions, although it is strongly recommended that you do 
produce such code in order to test your functions. The functions must have the names 
specified here and take a single argument since they will be tested using code that I will 
produce; they should not perform any input or output.

a) Write a function called fun1 that takes a string as a parameter and returns True if 
and only if the string is a palindrome. The function should be not case sensitive, so 
“Dad” should be regarded as a a palindrome. Spaces are significant so “red er”
should not be regarded as a palindrome.

b) Write a function called fun2 that takes a string as a parameter, converts the string 
to lower-case and returns the most frequent letter. (If there are equally frequent 
letters you may return any one of them.) Characters that are not letters should be 
ignored. The function should return None if there are no letters in the string.

c) Write a function called fun3 that takes a string as a parameter, counts the number 
of letters, digits and spaces in the string and returns a tuple containing the three counts
