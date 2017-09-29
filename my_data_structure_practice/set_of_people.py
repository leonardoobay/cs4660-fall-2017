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


##########################
"""
Sets have some additional operations defined on them that can be very
useful. First, sets have an “add” method defined. To add a new element to
a set, just call “add” as a method on that set and pass in the new element
as a parameter. In the following example, we have a set of friends from
work, and we add “Kathy” to that list. You can see from the output that
Kathy is added to the set. Likewise, there is a “remove” method defined.
In the example, we remove “Fred” from the list.
"""

work_friends = {'Sue', 'Eric', 'Fred'}
        print(work_friends)
work_friends.add('Kathy')
        print(work_friends)
work_friends.remove('Fred')
        print(work_friends)


OUTPUT:
{'Fred', 'Eric', 'Sue'}
{'Fred', 'Eric', 'Sue', 'Kathy'}
{'Eric', 'Sue', 'Kathy'}
