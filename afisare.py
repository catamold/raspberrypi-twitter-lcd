allText = "The music video for #CrisisFest directed by @shmandeluca is out on @AppleMusic. We love  making videos with you. https://t.co/8l0aMazpJr"

if "https://" in allText: 
    for i in range(len(allText)-8):
        if allText[i:i+8] == "https://":
            allText = allText[:i] + "<link>"   
print (allText)

count = 5     
for i in range(count):
    textToWrite = allText[32*i : 32*(i+1)]
    firstText = textToWrite[:16]
    lastText = textToWrite[16:32]
    textToWrite = firstText + "    " + lastText
    print (textToWrite)



