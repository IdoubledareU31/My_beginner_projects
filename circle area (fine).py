### this program calculates the area under the function
radius = float (input('enter radius here\n'))
x1 = 0
x2 = radius
aiterations = int (input ('enter the amount of area iterations\n '))
viterations = int (input ('enter the amount of volume iterations\n '))


dz = radius/viterations

x=x1
discarea = 0
counter1 = 0
totalarea = 0
totalvolume = 0
counter2 = 0
while counter2 != viterations:
	dx = radius/aiterations
	x = 0 
	while counter1 != aiterations:
		counter1 = counter1 + 1
		y = (radius**2 - x**2)**0.5 #define the function
		discarea = y * dx
		totalarea = totalarea + discarea
		x = x + dx
	print ("Disc area #", counter2, 'is', totalarea*4)
	radius = radius - dz
	totalvolume = totalvolume + totalarea*4*dz
	counter2 += 1
print ('Volume of a sphere is', totalvolume*2)