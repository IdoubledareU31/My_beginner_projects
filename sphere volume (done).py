### This program calculates a volume of a sphere by calculating areas 
### and volumes of discs it consists of. 
### done and correct!!!
radius = float (input('enter radius here\n'))
x1 = 0
x2 = radius

#In how many rectangles do you want to split a quarter of a circle?
aiterations = int (input ('enter the amount of area iterations\n '))

#How many discs do you want a half of a sphere to be split into?
viterations = int (input ('enter the amount of volume iterations\n '))


dz = radius/viterations # thickness of one disc
dx = radius/aiterations # width of on rectangle
x=x1
counter1 = 0
qdiscarea = 0
totalvolume = 0
counter2 = 0
z=0
newradius = radius
while counter2 != viterations:
	x = 0
	counter1 = 0
	qdiscarea = 0
	while counter1 != aiterations:
		dx = newradius/aiterations
		counter1 = counter1 + 1
		y = (newradius**2 - x**2)**0.5
		area = y * dx
		qdiscarea = qdiscarea + area
		x = x + dx
	
	print ("\nDisc area #", counter2, 'is', qdiscarea*4, 'radius is', newradius)
	print ('area is', area, 'y is', y, 'x is', x)
	z += dz
	newradius = (radius**2 - z**2)**0.5
	totalvolume = totalvolume + qdiscarea*4*dz
	counter2 += 1
print ('Volume of a sphere is', totalvolume*2)