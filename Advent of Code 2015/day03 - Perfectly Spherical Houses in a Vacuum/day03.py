santax = 0
santay = 0
robox = 0
roboy = 0
isrobotactive = 0 #set to 1 to activate the santa robot
santavsroboturn = 0
houselist = [(0,0)]
uniquehouse = 1
with open('input03.txt') as f:
	while 1:
		direction = f.read(1)
		if santavsroboturn == 0:
			if direction == '^':
				santay+= 1
			elif direction == '>':
				santax += 1
			elif direction == 'v':
				santay -= 1
			elif direction == '<':
				santax -= 1
			else:
				break
			if isrobotactive == 1:
				santavsroboturn = 1
			if (santax,santay) not in houselist:
				houselist.append((santax,santay))
				uniquehouse+=1
		else:
			if direction == '^':
				roboy+= 1
			elif direction == '>':
				robox += 1
			elif direction == 'v':
				roboy -= 1
			elif direction == '<':
				robox -= 1
			else:
				break
			santavsroboturn = 0
			if (robox,roboy) not in houselist:
				houselist.append((robox,roboy))
				uniquehouse+=1
print('The total amount of unique houses is: ',uniquehouse)
