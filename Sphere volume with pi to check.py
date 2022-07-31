#done and correct

radius = int(input('Enter RADIUS: '))
pi = 22/7
viterations = int(input('Enter the amount of ITERATIONS: '))
x=0
dx=radius/viterations
totalvolume = 0
counter = 0
while counter != viterations:
	y = (radius**2 - x**2)**0.5
	discarea = pi*(y**2)
	totalvolume = totalvolume + discarea*dx
	print ('total volume #',counter, 'IS', round (totalvolume, 2), 'and area is', discarea)
	x = x + dx
	counter += 1
print ('The volume of a sphere is', round (totalvolume*2, 4))
