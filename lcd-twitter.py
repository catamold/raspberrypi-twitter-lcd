#################################################
#            Raspberry Pi - Twitter             #
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

GPIO.setwarnings(False)

lcd = CharLCD(numbering_mode=GPIO.BOARD, pin_rs=26, pin_e=24, pins_data=[22, 18, 16, 12])

api = twitter.Api(consumer_key='oVXAYUbej3bI11JJ7SUJzbU8H',
	consumer_secret='z5W098nv50E819lpZjTssJX4ldapQFZUSZDFQr4JHhzJvwxnKx',
	access_token_key='953957604451024897-Qmc5yDPXXx3QEFpmW02kuXSOPhmi61S',
	access_token_secret='QqdkH9bGyiZEEsAb9ko4ez3cJck9VjKDQgJdsMrLLW5lP')

htmlParser = HTMLParser.HTMLParser()
lcd.clear()
lcd.write_string("Pornire program")
time.sleep(5)
lcd.clear()

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
        #count = (len(tweetUser) + len(tweetText) + 2) / 32
        count = len(allText) / 32
        count += 1
        print count
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
