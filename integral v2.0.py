#this program calculates the area under the function
x1 = float (input ('Enter X1\n'))
x2 = float (input ('Enter X2\n'))
iterations = int (input ('Enter the amount of iterations\n '))
dx = (x2 - x1)/iterations

# IF ONLY I COULD MAKE THE FUCTION TO BE LOCATED ONLY HERE


#smaller iteration
x=x1
area = 0
counter = 0
totalarea = 0
while counter != iterations:
	counter = counter + 1
	## print ('the count is', counter)
	y = x**2 #define the function # IF ONLY I COULD MAKE IT APPEAR ONCE IN THE BEGINNING
	area = y * dx
	totalarea = totalarea + area
	## print ('x is', x, '\nand y is', y, '\nand smaller area is', area)
	x = x + dx

#larger iteration
x=x1+dx
area = 0
counter = 0
totalarea2 = 0
while counter != iterations:
	counter = counter + 1
	## print ('the count is', counter)
	y = x**2 #define the function # IF ONLY I COULD MAKE IT APPEAR ONCE IN THE BEGINNING
	area = y * dx
	totalarea2 = totalarea2 + area
	## print ('x is', x, '\nand y is', y, '\nand larger area is', area)
	x = x + dx

print ("An average between", round (totalarea, 2), 'and', round (totalarea2, 2), "IS", round((totalarea+totalarea2)/2, 4))