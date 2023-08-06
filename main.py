import webbrowser #pip install python3 
# sudo apt-get install git 
# sudo apt install python3-pyaudio   
import speech_recognition as sr #pip install SpeechRecognition
import pyttsx3 # pip install pyttsx3
import pywhatkit #pip install pywhatkit
import RPi.GPIO as GPIO # pip install RPi.GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)# TO GO CLASS 1  (TO 16 IN MEGA) {GPIO 5}
GPIO.setup(17, GPIO.OUT)# TO COME BACK FROM CLASS 1 (TO 17 IN MEGA)  {GPIO 6}
GPIO.setup(18, GPIO.OUT)# TO GO CLASS 2 (TO 18 IN MEGA) {GPIO 3})# TO COME BACK FROM CLASS (TO 19 IN MEGA) {GPIO 4}
GPIO.setup(19, GPIO.IN)# WHEN REACHED CLASS 1 (TO 15 IN MEGA) {GPIO 1}

GPIO.setwarnings(False)
GPIO.output(16,False)
GPIO.output(17,False)
GPIO.output(18,False)

engine = pyttsx3.init("espeak")
voices = engine.getProperty('voices')
engine.setProperty('voice','english_rp+f4')
engine.setProperty('rate',80)

def speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def takeMessage():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(": Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:

        print(": Recognizing...")
        Tmsg = r.recognize_google(audio,language='en-in')
        print(f": Your Command : {query}\n")

    except:
        return ""
    return Tmsg.lower()

def TakeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(": Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:

        print(": Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f": Your Command : {query}\n")

    except:
        return ""
    return query.lower()
    
# def wish():
#     import datetime
#     hour = int(datetime.datetime.now().hour)
#     if hour >=0 and hour<12:
#         speak("Good Morning Sir, I Am Your AI Assistent JARVIS")
#     elif hour>=12 and hour<18:
#         speak("Good Afternoon Sir, I Am Your AI Assistent JARVIS")
#     else:
#         speak("Good Night Sir, I Am Your AI Assistent JARVIS")



def TaskExe():

    speak("Jarvis at your service Sir ")
    speak("How Can I Help You")

    while True:
        query = TakeCommand()
#         print(query)
        if 'open google' in query:
            webbrowser.open("www.google.com")
        elif 'youtube search' in query:
            webbrowser.open("www.youtube.com")
        elif 'open facebook' in query:
            webbrowser.open('www.facebook.com')
        elif 'hi Jarvis' in query:
            speak("Hi sir")
        elif 'hello' in query:
            speak("Hello Sir") 
        elif 'thanks' in query:
            speak("Welcome Sir") 
        elif 'what is your name' in query:
            speak("I am Jarvis")
        elif ' who are you' in query:
            speak("I am your A I Assistant")
        elif 'what is a i' in query:
            speak("Artificial intelligence is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by animals including humans")
        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("google search","")
            speak("This I Found for your search Sir")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,2)
                speak(result)

            except:
                speak("No Speakable Data")

        elif 'search' in query:
            import wikipedia as googleScrap
            query = query.replace("search","")
            speak("This I Found for your search Sir")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,2)
                speak(result)

            except:
                speak("No Speakable Data")


        elif 'deliver to class 1' in  query:
            print("delivering to class 1")
            GPIO.output(16,False)
            sleep(3)
            speak("Going to class 1 to deliver your message")
            speak("Please tell me what is your message")
            msg = TakeCommand()
            print(msg)
            print("Recordedd")    
            GPIO.output(17,True)
            GPIO.output(18,False)
            sleep(1)
            GPIO.output(16,True)
            sleep(3)
            while GPIO.input(19)==0:
                sleep(0.2)
            print("delevered")
            
            GPIO.output(16,False)
            sleep(2);
            speak(msg)
            GPIO.output(16,False)
            sleep(2);
            GPIO.output(17,False)
            GPIO.output(18,False)
            sleep(0.2)
            GPIO.output(16,True)
            sleep(3)
            print("going back")
            while GPIO.input(19)==0:
                sleep(0.2)
            print("Reached Home")
            GPIO.output(16,False)
            
        elif 'deliver to class 2' in  query:
            print("delivering to class 2")
            GPIO.output(16,False)
            sleep(3)
            speak("Going to class 2 to deliver your message")
            speak("Please tell me what is your message")
            msg = TakeCommand()
            GPIO.output(17,False)
            GPIO.output(18,True)
            sleep(1)
            GPIO.output(16,True)
            sleep(3)
            while GPIO.input(19)==0:
                sleep(0.2)
            print("delevered")
            GPIO.output(16,False)
            sleep(3);
            speak(msg)
            GPIO.output(16,False)
            sleep(3)
            GPIO.output(17,False)
            GPIO.output(18,False)
            sleep(0.2)
            GPIO.output(16,True)
            sleep(3)
            print("going back")
            while GPIO.input(19)==0:
                sleep(0.2)
            print("Reached Home")
            GPIO.output(16,False)
            
        elif 'explain yourself' in query:
            import datetime
            hour = int(datetime.datetime.now().hour)
            if hour >=0 and hour<12:
                speak("Good Morning Sir, I am an A I Assistent Jarvis")
            elif hour>=12 and hour<18:
                speak("Good Afternoon Sir, I am an A I Assistent Jarvis")
            else:
                speak("Good Evening Sir, I am an A I Assistent Jarvis")
            speak("I am a project developed by SAGES Basna")
            sleep(1)
            speak("My developers are Shubh Rajput and Mohnish Thakur")
            sleep(1)
            speak("They have used a Raspberry Pi 3 B plus and Arduino Mega as my processing units")
            sleep(1)
            speak("Other components which they used are speakers and mic for my communication")
            sleep(1)
            speak("IR and Ultrasonic sensors for my obstacle avoidance")
            sleep(1)
            speak("I can do the following tasks as Information gathering ,Obstacle Avoidance , Students Info which is feeded in my program And deliver teachers message to any class")
            sleep(1)
            speak("And This all task can be done by just your voice command")

            speak("i am a voice controled assistant robot which can be used for Information gathering , Students info , message delivery , delivery of any object ")
        
        # data of student 1 shubh
        
        elif 'who is shubh' in query:
            speak("Shubh is a student of class 11th of SAGES Basna ")

        elif 'tell me about shubh' in query:
            speak("Shubh is a student of class 11th of SAGES Basna ")
            
        elif 'parents of shubh' in query:
            speak("His Father's name is Vijay Singh Rajput ")
            speak("His Mother's name is Kalpana Singh Rajput ")

        elif 'd o b of shubh' in query:
            speak("Shubh was born on 26 March 2008")

        elif 'when was shubh born' in query:
            speak("Shubh was born on 26 March 2008")
            
        elif 'contact of shubh' in query:
            speak("His Mobile Number is  9 9 9 3 2 8 3 7 0 0")
            
        elif 'home address of shubh' in query:
            speak("His Home is in Arekel Deepa ")
            sleep(0.5)
            speak("Basna District Mahasamund Chattisgadh")
            
            
        # data of student 2 mohnish
        elif 'who is mohnish' in query:
            speak("Mohnish is a student of class 12th of SAGES Basna ")

        elif 'tell me about mohnish' in query:
            speak("Mohinsh is a student of class 12th of SAGES Basna ")
            
        elif 'parents of mohnish' in query:
            speak("His Father's name is Satya Narayan Thakur ")
            speak("His Mother's name is Usha Thakur ")

        elif 'd o b of mohnish' in query:
            speak("Mohnish was born on 14 November 2006")

        elif 'when was mohnish born' in query:
            speak("Mohnish was born on 14 November 2006")
            
        elif 'contact of mohnish' in query:
            speak("His Mobile Number is  6 2 6 5 6 7 3 9 0 8")
            
        elif 'home address of mohnish' in query:
            speak("His Home is in Bansula Deepa ")
            sleep(0.5)
            speak("Basna District Mahasamund Chattisgadh")
            
         # data of student 3 harsh
        elif 'who is harsh' in query:
            speak("Harsh is a student of class 10th of SAGES Basna ")

        elif 'tell me about harsh' in query:
            speak("Harsh is a student of class 10th of SAGES Basna ")
            
        elif 'parents of harsh' in query:
            speak("His Father's name is Nand Kumar Dhruw ")
            speak("His Mother's name is Yogeshwari Dhruw ")

        elif 'd o b of harsh' in query:
            speak("Harsh was born on 17 March 2008")

        elif 'when was harsh born' in query:
            speak("Harsh was born on 17 March 2008")
            
        elif 'contact of harsh' in query:
            speak("His Mobile Number is  8 8 8 9 3 6 5 7 8 7")
            
        elif 'home address of harsh' in query:
            speak("His Home is in Arekel Depa ")
            sleep(0.5)
            speak("Basna District Mahasamund Chattisgadh")
            
         # data of student 4 Varsha
        elif 'who is varsha' in query:
            speak("Varsha is a student of class 12th of SAGES Basna ")

        elif 'tell me about varsha' in query:
            speak("Varsha is a student of class 12th of SAGES Basna ")
            
        elif 'parents of varsha' in query:
            speak("Her Father's name is Hemant Barik ")
            speak("Her Mother's name is Praphasini Barik ")

        elif 'd o b of varsha' in query:
            speak("Varsha was born on 29 July 2006")

        elif 'when was varsha born' in query:
            speak("Varsha was born on 29 July 2006")
            
        elif 'contact of varsha' in query:
            speak("Her Mobile Number is  9 3 4 0 8 2 0 2 8 8")
            
        elif 'home address of varsha' in query:
            speak("Her Home is near  Raipur Road ")
            sleep(0.5)
            speak("Basna District Mahasamund Chattisgadh")
            
         # data of student 2 mohonish
        elif 'who is moh' in query:
            speak("Shubh is a student of class 12th of SAGES Basna ")

        elif 'tell me about shubh' in query:
            speak("Shubh is a student of class 12th of SAGES Basna ")
            
        elif 'parents of shubh' in query:
            speak("His Father's name is Vijay Singh Rajput ")
            speak("His Mother's name is Kalpana Singh Rajput ")

        elif 'd o b of shubh' in query:
            speak("Shubh was born on 26 march 2008")
            
        elif 'contact of shubh' in query:
            speak("His Mobile Number is  9 9 9 3 2 8 3 7 0 0")

        elif 'when was shubh born' in query:
            speak("Shubh was born on 26 march 2008")
            
        elif 'home address of shubh' in query:
            speak("His Home Address is Arekel Depa ")
            sleep(0.5)
            speak("Basna District Mahasamund Chattisgadh")





TaskExe()



