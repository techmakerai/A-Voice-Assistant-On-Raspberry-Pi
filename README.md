# A Voice Assistant (Chatbot) on Raspberry Pi

A voice assistant (chatbot) built with Raspberry Pi, Python, and OpenAI ChatGPT API. This repository includes a Python program that can call OpenAI's ChatGPT API to obtain a response for any questions a user may ask and then convert the text response to a voice response. This version has been tested on Raspberry Pi 4. 

Following the YouTube video here to learn more about this code:    
[https://youtu.be/nHpJaE559r4](https://youtu.be/nHpJaE559r4)

## Materials 

* Raspberry Pi
* Speaker
* Microphone (https://www.microcenter.com/product/613575/adafruit-industries-mini-usb-microphone-black)

## Set System Environment Variables 

OPENAI_API_KEY=(API key from OpenAI website)   
PYGAME_HIDE_SUPPORT_PROMPT=hide

## Install Python and Packages 
You will need to install the following packages to run this code: 

```console
$ pip install speechrecognition openai pyttsx3 pyaudio pygame
```


