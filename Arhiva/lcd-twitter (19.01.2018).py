#################################################
#           Raspberry Pi - #Twitter             #
#    Universitatea Tehnica din Cluj-Napoca      #
#   Facultatea de Automatica si Calculatoare    #
#        Departamentul de Calculatoare          #
#               Moldovan Catalin                #
#                 Grupa: 30225                  #
# Cadru didactic: prof. dr. ing. Radu Munteanu  #
#               Data: 18.01.2018                #
#################################################
import twitter
from RPLCD import CharLCD
import time
import HTMLParser
import RPi.GPIO as GPIO
import sys

GPIO.setwarnings(False)

lcd = CharLCD(numbering_mode=GPIO.BOARD, pin_rs=26, pin_e=24, pins_data=[22, 18, 16, 12])

api = twitter.Api(consumer_key='BEAwnAZfPNRRhYY0Q033mexo0',
	consumer_secret='PmSPXvtMA55kksFWNHjpMOpe8hOLXyqgQsEVPuR75oq9rz1VuZ',
	access_token_key='2458501699-tdl901yBFOVKhUBwDMrsCEMN6pODSR0OWu3oaxw',
	access_token_secret='D8cvt3hVTtm3CjcXxKwH1BOrdy9yM8XtpJOa5oTAQYqXp')

htmlParser = HTMLParser.HTMLParser()
lcd.clear()
lcd.write_string("Pornire program")
time.sleep(5)
lcd.clear()

hashtag = "#BeStrongRO"
countHashtag = 0
twitterName = [None]*10
words = 280
        
try:
    while True:
        print "Cautare twitter..."
        lcd.clear()
        lcd.write_string("Finding tweets")
        try:
            homeTimeline=api.GetHomeTimeline(count=1)
        except:
            lcd.clear()
            lcd.write_string("Eroare conexiune")
            continue
        print "Tweet gasit..."
		
        tweetUser = homeTimeline[0].user.screen_name
        tweetText = homeTimeline[0].text
        tweetText = htmlParser.unescape(tweetText)
        tweetText = tweetText.replace('\n',' ')

        allText = tweetUser+": "+tweetText
        if "https://" in allText: 
            for i in range(len(allText)-8):
                if allText[i:i+8] == "https://":
                    allText = allText[:i] + "<link>"
        count = len(allText) / 32
        count += 1
        print count
        print allText

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
                    twitterName[countHashtag] = "@" + tweetUser
                    countHashtag += 1
        print "%s: %d" % (hashtag,countHashtag)
        for i in range (countHashtag):
            sys.stdout.write ("%s " % (twitterName[i]))            

        file = open('rudewords.txt','r')
        line = file.readline()
        rudewcount = 0
        while line:
            line = file.readline()
            rudewcount += 1
        file.close()

        file = open('rudewords.txt','r')
        line = file.readline()
        rudew = [None]*(rudewcount)
        i = 0
        while line:
            rudew [i] = line
            line = file.readline()
            i += 1
        file.close()

        allow = 1
        splittext = tweetText.split(" ")
        textcount = len(splittext)

        for i in range(0,rudewcount):
            if rudew [i][len(rudew [i])-1] == "\n":
                rudew [i] = rudew [i][:len(rudew [i])-1]

        for i in range(0,textcount):
                for j in range (0,rudewcount):
                        if splittext [i] == rudew [j]:
                                allow = 0
                                break
                        else:
                                continue
                                
        if allow == 1:
             for i in range(count):
                 textToWrite = allText[32*i : 32*(i+1)]
                 print textToWrite
                 firstText = textToWrite[:16]
                 lastText = textToWrite[16:32]
                 textToWrite = firstText + "    " + lastText
                 time.sleep(3)
                 lcd.clear()
                 lcd.write_string(textToWrite)	 
        time.sleep(3)
		
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()
    lcd.write_string("END Connection")

    fileTweet = open('TweetPost.txt', 'w')
    tweetPost = "Our " + hashtag + " campain has " + str(countHashtag) + " tweets. THANKS TO: "
    others = 0
    for i in range (countHashtag):
        if len(tweetPost) + len(twitterName[i]) + 1 < words - 15:
            tweetPost = tweetPost + twitterName[i] + " "
        else:
            others = 1
    if others == 1:
        tweetPost = tweetPost + "and many others"
    fileTweet.write (tweetPost)
    api.PostUpdate (tweetPost)
    fileTweet.close()
    
