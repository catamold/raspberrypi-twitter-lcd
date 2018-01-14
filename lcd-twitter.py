import twitter
import CharLCD
from RPLCD import CharLCD
import time
import HTMLParser
import RPi.GPIO as GPIO

lcd = CharLCD(numbering_mode=GPIO.BOARD, pin_rs=26, pin_e=24, pins_data=[22, 18, 16, 12])

api = twitter.Api(consumer_key='5Eok4J7w2UvOzzjxoIoQrmw3R',
	consumer_secret='jCQT2tKt44LjNbYqBuZkNdXUbEKum4aFTJ9PBrWos8nC68PeRu',
	access_token_key='2458501699-4rnvybDyCndQjLS38sw5wlBNdIfiEettqvhvZOv',
	access_token_secret='p9LVT4LWQYqkuqbsNUiJjV4wpdUMY53s1cnEUIbyVQmpB')

htmlParser = HTMLParser.HTMLParser()
lcd.clear()
lcd.write_string("Pornire program")
time.sleep(5)
lcd.clear()

try:
    while True:
        print "Cautare twitter..."
        try:
            homeTimeline=api.GetHomeTimeline(count=1)
        except:
            lcd.clear()
            lcd.write_string("Eroare se reincearca conexiunea...")
            continue
        print "Tweet gasit..."
		
        tweetUser = homeTimeline[0].user.screen_name
        tweetText = homeTimeline[0].text
        tweetText = htmlParser.unescape(tweetText)
        tweetText = tweetText.replace('\n',' ')
        
        count = (len(tweetUser) + len(tweetText) + 2) / 32
        print count
        allText = tweetUser+": "+tweetText
        print allText

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
                 time.sleep(5)
                 lcd.clear()
                 lcd.write_string(textToWrite)	 
        time.sleep(10)
		
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()
    lcd.write_string("Termianre program")
