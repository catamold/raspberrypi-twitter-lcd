import twitter
import CharLCD
from RPLCD import CharLCD
import time
import HTMLParser
import RPi.GPIO as GPIO

lcd = CharLCD(numbering_mode=GPIO.BOARD, pin_rs=26, pin_e=24, pins_data=[22, 18, 16, 12]) # configurare LCD

api=twitter.Api(consumer_key='5Eok4J7w2UvOzzjxoIoQrmw3R',
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
            lcd.write_string(u'An Error occurred! Retrying')
            continue
        print "Tweet gasit..."
		
        tweetUser = homeTimeline[0].user.screen_name
        tweetText = homeTimeline[0].text
        tweetText = htmlParser.unescape(tweetText) # Convertire simboluri HTML ex. &amp - (@)
        tweetText = tweetText.replace('\n',' ') # Liniile noi se inlocuiesc cu spatii
        
# Sectionam Tweet-ul in mai multe parti in functie de cat de lung este acesta pentru a putea incapea pe display-ul LCD
        
        count = (len(tweetUser) + len(tweetText) + 2) / 32
        print count
        allText = tweetUser+": "+tweetText
        print allText

         for i in range(count):
             textToWrite = allText[32*i : 32*(i+1)]
             print textToWrite
             time.sleep(5)
             lcd.clear()
             lcd.write_string(textToWrite)
			 
        time.sleep(10);
		
except KeyboardInterrupt:
    pass
finally:
    lcd.clear()
    lcd.write_string("Termianre program")
