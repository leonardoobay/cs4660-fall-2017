List practice

Lists are one of the programming features that Python supports
particularly well. Python makes it very easy to create lists and do all kinds
of things with them. If you use lists in other programming languages, you
don’t have quite the flexibility that you do in Python.

In Python, we write lists as a series of values separated by commas and
enclosed in brackets.

For example, below is a list of daily_high_temps:

daily_high_temps = [83, 80, 73, 75, 79, 83, 86]

Each element (or value) in the list is going to have some index. If we want
to get the value in one of those boxes—basically, get an element out—
we need a way to refer to it. We can refer to an element of a list by putting
the index in brackets right after the variable name.

variable_name[index]


In the temperature list, printing out the fifth value, “daily_high_temps [4],”
would print out 79.

(index_numbers---->[0,  1,  2,  3,  4,  5,  6  ]

daily_high_temps = [83, 80, 73, 75, 79, 83, 86]

print(daily_high_temps[4])

OUTPUT:
79

The index doesn’t have to be a number; it can be a variable, as long as
that variable has an integer value. So, we can assign the value of 1 to i
and then print “daily_high_temps[i]” and get 80.

daily_high_temps = [83, 80, 73, 75, 79, 83, 86]

i = 1


print (daily_high_temps[i])


OUTPUT:
80

Source: https://guidebookstgc.snagfilms.com/9151_ComputerScience.pdf

