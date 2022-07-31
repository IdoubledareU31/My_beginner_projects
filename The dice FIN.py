print ("""
Two pieces of six-dice are being thrown. Number of throws is specified by the user.
The program will calculate which resulting sums are encountered the most often.
""")

import random


throws = int(input ('Number of throws: '))
listsums=[]
listtimes=[]
listnumbers=[]
counter=0
result=0
listcounter=[]
for throw in range (0, throws):
	a, b = random.randint (1,6), random.randint (1,6)
	sum = a+b
	listsums.append(sum)

print ("Here is the list of the resulting sums:", listsums, "\n")
#print ("Here are all the numbers present in the results:", set(listsums))

for number1 in set(listsums):
	times=0
	for number2 in listsums:
		if number2 == number1:
			times +=1
	print ("number {} was encountered {} times".format(number1, times))
	listtimes.append(times)
	listnumbers.append(number1)
totallist=list(zip(listnumbers,listtimes))
for item in listtimes:
	if listtimes[counter]==max(listtimes):
		listcounter.append(counter)
	counter +=1
print ('\n')
for count in listcounter:
	print ("Number {} was encountered the most and {} times in total".format(listnumbers[count],listtimes[count]))
#print (listcounter)

    