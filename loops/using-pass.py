# ------------------------------------------------------------------------------------
# Tutorial: How to use pass statement within loops.
# ------------------------------------------------------------------------------------


# Nothing actually happens when pass is executed in python. It just passes control to next line that automatically happens but 
# sometimes it comes handy, especially in production codes. As we can't leave the body of if, else, for, while, etc undefined or 
# it'll throw error so sometimes we use pass with these statements to not get any error.

# So, it's used sometimes where we need to define a syntactically empty block.
# It is much like a comment but python interpreter executes it while comments get ignored completely. 


for i in [1, 2, 3]:
    pass
i=0
my_list=[1, 2, 3]
while i < len(my_list):
    print(my_list[i])
    i+=1

# In above example we won't get any error as we are using pass but if we don't use pass and just use
# for loop without body then we'll get error. 



# ------------------------------------------------------------------------------------
# Challenge: Create a function that asks user whether he/she uses github or not, if no then print the steps to make github account 
# and if yes then just pass it and print "that's good" outside the body of else block but inside the function.
# Then call that function exactly 3 times using a for loop. 
# ------------------------------------------------------------------------------------
