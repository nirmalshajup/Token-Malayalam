from gtts import gTTS
from playsound import playsound
token = input("Enter a Token Number:")
txt = "ടോക്കൺ നമ്പർ" +token
ob = gTTS(txt,lang = 'ml')
ob.save("token.mp3")
playsound("token.mp3")