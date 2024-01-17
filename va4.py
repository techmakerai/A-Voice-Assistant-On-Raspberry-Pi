# A Voice Chatbot built with Python and OpenAI's ChatGPT API
# By TechMakerAI on YouTube 
# 
from openai import OpenAI
import speech_recognition as sr
import pyttsx3
import os
import pyaudio
from datetime import date
import time
 
#os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame

pygame.mixer.init()

client = OpenAI()

today = str(date.today())

engine = pyttsx3.init()

engine.setProperty('rate', 190) # speaking rate 

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id) # o for male; 1 for female

# function to interact with OpenAI's ChatGPT API

def chatfun(talk): 
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages= talk,
        max_tokens=124
    )

    talk.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})

    return talk

# select to use OpenAI's text to speech API
openaitts = True

def speak_text(text):
    global openaitts    

    if openaitts:

        response = client.audio.speech.create(
            model="tts-1",
            # alloy: man; nova: woman
            voice="nova",
            input= text )
    
        fname = 'output.mp3'
    
        mp3file =open(fname, 'w+') 
    
        #if os.path.exists(fname):
        #    os.remove(fname)    
                      
        response.stream_to_file(fname)

        showtext = True  

        try:        
            pygame.mixer.music.load(mp3file)
            pygame.mixer.music.play()
        
            while pygame.mixer.music.get_busy():
                #  
                if showtext:
                    print("AI: " + text)
                    showtext = False 
                time.sleep(0.25)
            
            pygame.mixer.music.stop()    
            mp3file.close()
        
        except KeyboardInterrupt:
            pygame.mixer.music.stop()
            mp3file.close()
            #print("\nAudio playback stopped.")
    else:
        engine.say(text)
        print("AI: " + text)
        engine.runAndWait()
        

talk = []

# save conversation to a log file 
def append2log(text):
    global today
    fname = 'chatlog-' + today + '.txt'
    with open(fname, "a") as f:
        f.write(text + "\n")

# Main loop for conversation
def main():
    global talk, today  
    
    rec = sr.Recognizer()
    mic = sr.Microphone()
    rec.dynamic_energy_threshold=False
    rec.energy_threshold = 400
    
    
    
    sleeping = True 
    
    while True:     
        
        with mic as source1:            
            rec.adjust_for_ambient_noise(source1, duration= 1)

            print("Listening ...")
            
            try: 
                audio = rec.listen(source1, timeout = 10, phrase_time_limit = 15)
               
                text = rec.recognize_google(audio)
                
                if sleeping == True:
                    # User must start the conversation with the wake-up word "Jack"
                    # This word can be chagned. 
                    if "jack" in text.lower():
                        request = text.lower().split("jack")[1]
                        sleeping = False
                        # AI is awake now, start a new conversation 
                        talk = []                        
                        today = str(date.today())                        

                    else:
                        continue
                      
                        
                else: 
                    
                    request = text.lower()

                    if "that's all" in request:
                                               
                        append2log(f"You: {request}\n")
                        
                        speak_text("Bye now")
                        #print('Bye now')
                        
                        sleeping = True
                        # AI goes back to speeling mode
                        continue
                        
                append2log(f"You: {request}\n")

                print(f"You: {request}\n")

                talk.append({'role': 'user', 'content': request})

                talk = chatfun(talk)

                append2log(f"AI: {talk[-1]['content'].strip()}\n")
                # 
                speak_text(talk[-1]['content'].strip())
 
            except Exception as e:
                continue 
 
if __name__ == "__main__":
    main()

    

