import sys

allText = "The music video for #BeStrongRO directed by @shmandeluca is out on @AppleMusic. We love  making videos with you. https://t.co/8l0aMazpJr"
tweetUser = "@catalinmold"

hashtag = "#BeStrongRO"
countHashtag = 1
twitterName = [None]*10
twitterName[0] = "@johny"
fileTweet = open('TweetPost.txt', 'w')
words = 280

if "https://" in allText: 
    for i in range(len(allText)-8):
        if allText[i:i+8] == "https://":
            allText = allText[:i] + "<link>"   
print (allText)


if hashtag in allText:
    if countHashtag == 0:
        twitterName[countHashtag] = tweetUser
        countHashtag += 1
    else:
        aux = 1
        for i in range(countHashtag):
            if tweetUser in twitterName[i]:
                aux = 0
                break
        if aux == 1:
            twitterName[countHashtag] = tweetUser
            countHashtag += 1


    
count = 5     
for i in range(count):
    textToWrite = allText[32*i : 32*(i+1)]
    firstText = textToWrite[:16]
    lastText = textToWrite[16:32]
    textToWrite = firstText + "    " + lastText
    print (textToWrite)

    
print ("%s: %d" % (hashtag,countHashtag))
tweetPost = "Our " + hashtag + " campain has " + str(countHashtag) + " tweets. THANKS TO: "
others = 0
for i in range (countHashtag):
    sys.stdout.write ("%s " % (twitterName[i]))
    if len(tweetPost) + len(twitterName[i]) + 1 < words - 15:
        tweetPost = tweetPost + twitterName[i] + " "
    else:
        others = 1
if others == 1:
    tweetPost = tweetPost + "and many others"
fileTweet.write (tweetPost)
fileTweet.close()
