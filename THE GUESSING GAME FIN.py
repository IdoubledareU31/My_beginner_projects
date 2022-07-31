#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
x = random.randint (1, 100)
# print (x)
counter = 1
d1=0
diff=0
guess = float(input ('Guess the number:'))

while guess != x:
    while guess < 1 or guess > 100:
        guess = float (input ('OUT OF BOUNDS! GUESS AGAIN:'))
        
    counter += 1
    d = guess - x
    d = abs(d)
    if d <= 10 and counter == 2:
            guess = float(input ('WARM! GUESS AGAIN:'))
            d1 = abs (guess - x)
            diff = d1-d
    elif counter == 2:
            guess = float(input ('COLD! GUESS AGAIN:'))
            d1 = abs (guess - x)
            diff = d1-d
    else:
        if diff<=0:
            guess = float(input('WARMER! GUESS AGAIN:'))
            d1 = abs (guess - x)
            diff = d1-d
        else:
            guess = float(input('COLDER! GUESS AGAIN:'))
            d1 = abs (guess - x)
            diff = d1-d
            
else:
    print ("THAT'S RIGHT! IT TOOK YOU {} TRIES".format (counter))
    
    


# In[ ]:





# In[ ]:





# In[ ]:




