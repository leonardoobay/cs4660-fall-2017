#####################################
"""
A few preliminaries


We have one boat in the form of an array.

The boat will move the objects from A to B.

There is one commander of the boat--that's you.

You are implied, so your space on the boat is not explicitly stated.

Reason being, boats don't operate themselves yet.

We have a simple boat that will never posses the AI to operate itself.

We need to move all three Strings from A to B.

However, we can't lose any elements in the process.

As expected, goat eats lettuce.
Wolf eats goat.
No one eats wolf.
Wolf does not eat lettuce.

As such, the wolf is our space variable.
What this means is that the wolf creates space on land.
This is useful since we can only moves objects one at a time.
We can move objects from A to B, and from B to A as needed.

Play the game here: http://jeux.lulu.pagesperso-orange.fr/html/anglais/loupChe/loupChe1.htm#

Disclaimer: I type up the solution in a few minutes, so it won't be the best looking solution.
            It is valid, however.

"""
######################################

We have three variables in the form of 


String wolf, goat, lettuce;


array[] simpleBoatArray = [3]; 


piece_of_land_A = A


piece_of_land_B = B


Land_A houses a wolf, a goat, and lettuce.
Land_B is empty and ready to house the tree elements.


First move:
  Put goat in the boat.
  Then, move goat from A to B.
  Lettuce and wolf remain in A.
  Return to A on an empty boat.
  
  
  Second move:
    While goat is in B,
    put lettuce in the boat.
    Move lettuce from A to B.
    If goat eats lettuce, AND goat and lettuce 
    are on the same landmass, put goat or lettuce in boat.
   
    However, if wof eats goat, and goat and wolf 
    are on the same landmass, put goat or wolf in boat OR
    put wolf in the same landmass as lettuce.
    
    In this situation, we put the lettuce back in the boat, and love the lettuce from B to A.
    Leave the goat in landmass B.
    Return to landmass A with the lettuce.
    
    Status:
    Wolf and lettuce occupy landmass A.
    Goat occupies landmass B.
    
    
    Third move:
    Put wolf in the boat.
    Move wolf from A to B.
    While at B, put goat in the boat, and move back to A.
    
    Status:
      Wolf occupies B
      Goat and lettuce occupy A
      
      
      Fourth move:
        While at A,
        Put lettuce in the boat, and move lettuce from A to B
        Leave goat at A.
        Return to A with an empty boat.
        
        Status:
          Wolf and lettuce occupy B
          Goat occupies A
          
          
          Fift move:
            While boat is empty, and wolf and lettuce are in B, 
            move goat from A to B.
            
            
            Status:
              Game ends
              You win!
              You move all elements from A to B without losing any of them.

