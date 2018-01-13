
TEST = "Look there are very big boobs right in front of you."

file = open('rudewords.txt','r')
line = file.readline()

rudewcount = 0
while line:
    line = file.readline()
    rudewcount += 1
file.close()

file = open('rudewords.txt','r')
line = file.readline()


i = 0
rudew = [None]*(rudewcount)
while line:
    rudew [i] = line
    line = file.readline()
    i += 1
file.close()

allow = 1
splittext = TEST.split(" ")
textcount = len(splittext)

for i in range(0,rudewcount):
    if rudew [i][len(rudew [i])-1] == "\n":
        rudew [i] = rudew [i][:len(rudew [i])-1]

print (rudew)
print (splittext)

for i in range(0,textcount):
	for j in range (0,rudewcount):
		if splittext [i] == rudew [j]:
			allow = 0
			break
		else:
			continue
			
if allow == 1:
    print("Text admis")
else:
    print ("Text respins")

		
			
		
	
	
