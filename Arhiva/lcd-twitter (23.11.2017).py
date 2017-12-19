>>> import twitter
import CharLCD
from RPLCD import CharLCD

lcd = CharLCD(pin_rs=26, pin_e=24, pins_data=[22, 18, 16, 12]) #configurare LCD

api=twitter.Api(consumer_key='5Eok4J7w2UvOzzjxoIoQrmw3R',
	consumer_secret='jCQT2tKt44LjNbYqBuZkNdXUbEKum4aFTJ9PBrWos8nC68PeRu',
	access_token_key='2458501699-4rnvybDyCndQjLS38sw5wlBNdIfiEettqvhvZOv',
	access_token_secret='p9LVT4LWQYqkuqbsNUiJjV4wpdUMY53s1cnEUIbyVQmpB')

lcd.clear()
lcd.write_string('Pornire program')
time.sleep(5)