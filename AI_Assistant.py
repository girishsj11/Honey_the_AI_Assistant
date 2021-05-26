# -*- coding: utf-8 -*-

'''!pip install pyttsx3
#!sudo apt-get update && sudo apt-get install espeak # for linux sys
!pip install SpeechRecognition
!pip install wikipedia
!pip install pyautogui
!pip install psutil
!pip install pyjokes'''

try:
    import time as ton
    import datetime
    import smtplib
    import os
    import pyautogui
    import webbrowser as web
    import wikipedia
    import psutil
    import pyjokes
    import speech_recognition as sr
    import pyttsx3
except Exception as e:
    print("Error in importing Modules")
    print(e)
finally:
    print('libraries imported')

def speak(audio):

  engine = pyttsx3.init() # object creation

  """ RATE
  rate = engine.getProperty('rate')   # getting details of current speaking rate, #printing current voice rate
  engine.setProperty('rate', 150)     # setting up new voice rate


  VOLUME
  volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
  engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

  VOICE
  voices = engine.getProperty('voices')       #getting details of current voice
  #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male"""
  voices = engine.getProperty('voices')       #getting details of current voice
  engine.setProperty('voice',voices[1].id)   #changing index, changes voices. 1 for female 

  engine.say(audio)
  #engine.say(audio + str(rate))
  engine.runAndWait()
  #engine.stop()

  """Saving Voice to a file
  # On linux make sure that 'espeak' and 'ffmpeg' are installed
  engine.save_to_file(audio, 'test.mp3')
  engine.runAndWait()"""
  
# Date and Time Function
def time():
    try:
        t=datetime.datetime.now().strftime('%H:%M:%S')
        speak("the Current time is ")
        speak(t)
        #print(t)
    except Exception as e:
        print(e)

def date():
    
    try:
         year=int(datetime.datetime.now().year)
         day=int(datetime.datetime.now().day)
         month=int(datetime.datetime.now().month)
         speak("the Current date is ")
         speak(day)
         speak(month)
         speak(year)
         #print(year,day,month)
    except Exception as e:
        print(e)
        

#Greeting Function

def greet():
    try:
          h=datetime.datetime.now().hour
    
          if h>=6 and h<=12:
            speak("Good Morning")
          elif h>=12 and h<=16:
            speak("Good Afternoon")
          elif h>=17 and h<=21:
            speak("Good Evening ")
          elif h>=22 and h<=24:
            speak("Good Night")
          else:
            speak("Good Night")
        
          speak("Honey at your Service. How can I help you?")
    
    except Exception as e:
        print(e)
  
# Speech_Recognition Function
def command():
    try:
        r= sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold=2
            audio= r.listen(source)
            ton.sleep(2)
    except Exception as e:
        print(e)

        try:
            print("Recognizing....")
            query = r.recognize_google(audio,'en=US')
        except Exception as e:
            print(e)
            speak("Say that again Please...")
        return "None"
    return query

def sendmail(content='',to='',email='purushothamd709@gmail.com',password='**********'):
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(email,password)
        server.sendmail(email,to,content)
        server.close()
    except Exception as e:
        print(e) 
        
def screenshot():
    try:
        img=pyautogui.screenshot()
        img.save(r'C:\Users\Public\Pictures')
    except Exception as e:
        print(e)
  

def cpu():
    try:
        usage= str(psutil.cpu_percent())
        speak('cpu is at '+ usage)
        battery = psutil.sensors_battery
        speak('battery is at')
        speak(battery.percent)
    except Exception as e:
        print(e)


def jokes():
    try:
        speak(pyjokes.jokes.get_joke())
    except Exception as e:
        print(e)
  
def main():
    try:
        greet()
    
        while True:
            query=command().lower()
            print(query)
        
            if "time" in query:
                time()
        
            if 'date' in query:
                date()
        
            elif 'bye' in query:
                speak("Bye , see you again")
                quit()
        
            elif 'wikipedia' in query:
                speak("Searching...")
                query = query.replace('wikipedia','')
                result = wikipedia.summary(query,sentences=2)
                speak(result)
        
            elif ('send email' or 'send mail') in query:
                try:
                    speak('what should i say ?')
                    content= command()
                    speak(content)
                    to="email of person to whom we want to mail"
                    sendmail(to=to,content=content)
                except Exception as e:
                    speak(e)
                    speak("Unable to send the message")
                
            elif "Search in chrome" in query:
                speak(" What should i search?")
                #chromepath = r"C:\Users\Public\Desktop\Google Chrome.lnk"
                search = command().lower
                web.open(search+" .com")
                #web.get(chromepath).open_new_tab(Search+ ".com")
              
            elif 'logout' in query:
                os.system('shutdown - l')
        
            elif 'shutdown' in query:
                os.system('shutdown /s /t 1')
        
            elif 'restart' in query:
                os.system('shutdown /r /t 1')
        
            elif 'play songs' in query:
                song_dir_path = os.path(input('enter the directory path'))
                songs = os.listdir(song_dir_path)
                os.startfile(os.path.join(song_dir_path, songs[0]))
        
            elif 'remember that ' in query:
                speak("What should i remember?")
                data=command()
                speak("you said me to remember"+ data)
                rem= open("data.txt",'w')
                rem.write(data)
                rem.close()
        
            elif 'do you know anything' in query:
                rem = open('data.txt','r')
                speak('you said me to remember that' + rem.read())
          
            elif 'screenshot' in query:
                screenshot()
                speak('Done')
          
            elif 'cpu' in query:
                cpu()
            
            elif 'joke' or 'jokes' in query:
                jokes()

    except Exception as e:
        print(e)
        
        
main()       
        