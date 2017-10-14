    """ Two common ways of opening files.
    Both methods do the same thing.
    """
    
       """These methods are just to open files ONLY!
       Reading and writing to files comes later!
       """
    
########## OPTION 1
myfile = open("Filename", "w")
#Do something here
myfile.close()


########## OPTION 2
with open("Filename", "w") as myfile:
#Do something here
