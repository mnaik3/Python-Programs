#Problem Statement

Please create an addition and subtraction program that takes numbers in String format and returns output in
String format. The program can be written in C, C++, Java or Python.

Solution:
Created a python program to evaluate given expression.

Steps used for developement:
1.Take input from User.
2.Now modified string to convert into a evaluable expression.
3.As we are considering only + and - operators we can ignore brackets if any from string given.
4.Ignore brackets and spaces from string and put it into result_string.
5.Push data into array by group correctly as values. (Group as per operators in the string.)
6.Add conditions for invalid String.
7.Adjust operators according to mathematical rules(That is + and - is -, - and - is +, -and + is - and + and + is +)
8.Add Condition to ignore operators and numbers greater than 100,000,000 before converting to integer. and then convert everything else to integer.
9.Evaluate value of integer expression.
10.Return a String output.
