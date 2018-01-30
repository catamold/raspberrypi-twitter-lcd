import os

allText = "The music video exclusive on iPhone #BeStrongRO directed by @shmandeluca is out on @AppleMusic. We love  making videos with you. https://t.co/8l0aMazpJr"
tweetUser = "catalinmold"

splittext = allText.split(" ")
textcount = len(splittext)


file = open('Categories.txt','r')
line = file.readline()

categoriesno = 0
while line:
    line = file.readline()
    categoriesno += 1
file.close()

file = open('Categories.txt','r')
line = file.readline()

i = 0
lineRead = [None]*(categoriesno)
categories = [None]*(categoriesno)

while line:
    lineRead [i] = line
    line = file.readline()
    i += 1
file.close()



for i in range(0,categoriesno):
    for j in range(len(lineRead [i])):
        if lineRead[i][j] == ":":
            categories [i] = lineRead [i][:j]
            subcat = j
        if lineRead[i][j] == ",":
            subcategories = lineRead [i][subcat+2:j]
            subcat = j
            for k in range(0,textcount):
                if splittext [k] == subcategories:
                    fileTweet = open(categories [i] + '.txt', 'w')
                    fileTweet.write (tweetUser + ": " + allText + "\n\n")  
            print (subcategories)
print (categories)
fileTweet.close()


    
