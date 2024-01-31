# A Voice Assistant (Chatbot) on Raspberry Pi

A voice assistant (chatbot) built with Raspberry Pi, Python, and OpenAI ChatGPT API. This repository includes a Python program that can call OpenAI's ChatGPT API to obtain a response for any questions a user may ask and then convert the text response to a voice response. This version has been tested on Raspberry Pi 4. 

Following the YouTube video here to learn more about this code:    
[https://youtu.be/nHpJaE559r4](https://youtu.be/nHpJaE559r4)

## Materials    
* Raspberry Pi
* Speaker
* Microphone (https://www.microcenter.com/product/613575/adafruit-industries-mini-usb-microphone-black)

## Install Python and Packages    
You will need to install the following packages to run this code: 
```console
pip install speechrecognition openai pyttsx3 pyaudio pygame
```
If you have Python 3.12 or newer, also install the "setuptools" package,    
```console
pip install setuptools
```
## Setup System Environment Variables    
First, edit the bash profile at "~/.bashrc" with a text editor and add the following environment variables:
```console
export OPENAI_API_KEY='your-api-key-here'   
export PYGAME_HIDE_SUPPORT_PROMPT=hide
```
Note that there is no space before and after "=". Then, re-load your new bash profile to activate it,        
```console
source ~/.bashrc 
```
After this, it will be activated, and it will be activated automatically at the startup of your Raspberry Pi. So you only need to set up this once.  

If you would rather want your API key to be accessible only for a specific project, then you can follow the instructions here,  
https://platform.openai.com/docs/quickstart 





