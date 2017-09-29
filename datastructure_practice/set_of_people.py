"""
In the following, we’ve created a set of people, and we initialize it with
three people’s names. Notice that we have the elements of the set inside
the curly braces, separated by commas. This code also shows that we
can use the “in” statement to check whether or not a particular item is in
the set or not. In this case, we check for the string “John.” Because that
string was part of the set, this code will print out “Yes!”
"""

people = {'John', 'Sue', 'Bill'}
        if 'John' in people:
          print("Yes!")
        else:
          print("No!")


OUTPUT:
Yes!



########################### Other method of writign sets

people = set(['John', 'Sue', 'Bill'])
          if 'John' in people:
              print("Yes!")
          else:
              print("No!")


OUTPUT:
Yes!
