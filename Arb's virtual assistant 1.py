import openai
import pyttsx3
import speech_recognition as sr 
import webbrowser 
from googlesearch import search
from datetime import datetime, date

openai.api_key = "..." #replace with api key

def chatgpt_chat(value):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= [{"role": "user", "content": f"{value}"}],
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,)
    
    message = response.choices[0].message.content.strip()

    return message


def Speak(audio):

    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[0].id)
   

    engine.say(audio)

    engine.runAndWait()


def start_up():

    Speak("Hello my name is Sam, I am your virtual companion. How can I help you?")

def query():

    luck = 1
    start_up()

    while (True):

        value = Commands().lower()


        if "open google" in value:
            Speak("Opening Google")
            webbrowser.open("https://www.google.ca")
            continue 
                

        elif "search up" in value:
            Speak("Opening Google")
            
            if "up" in value:
                num = value.strip().split("up")
                string = num.pop(-1)
                Speak(f"Searching up: {string}...")

                my_list = []
                num = 1

                
                for i in search(string,lang="us", num_results=4):
                    print(f"""link {num}: {i} """)
                    
                    my_list.append(i)
                    num += 1 

                value1 = Commands().lower()

                if "summarize link one" or "summarize link 1" in value1:
                    request = f"Summarize this link in 10 lines or less {my_list[0]}"
                    chatgpt_response = chatgpt_chat(request)

                    
                    Speak("In 10 lines or less,")
                    Speak(chatgpt_response)


                elif "summarize link two" or "summarize link 2" in value1:
                    request = f"Summarize this link in 10 lines or less {my_list[1]}"
                    chatgpt_response = chatgpt_chat(request)

                    Speak("In 10 lines or less,") 
                    Speak(chatgpt_response)

                elif "summarize link three" or "summarize link 3" in value1:
                    request = f"Summarize this link in 10 lines or less {my_list[2]}"
                    chatgpt_response = chatgpt_chat(request)
                    
                    Speak("In 10 lines or less,") 
                    Speak(chatgpt_response)

                elif "summarize link four" or "summarize link 4" in value1:
                    request = f"Summarize this link in 10 lines or less {my_list[3]}"
                    chatgpt_response = chatgpt_chat(request)

                    Speak("In 10 lines or less,") 
                    Speak(chatgpt_response)

                else:
                    continue

            continue 

        elif "open youtube" in value:
            Speak("Opening Youtube")
            webbrowser.open("https://www.youtube.com")
            continue

        elif "your name" in value:
            Speak("Hello, my name is Sam.")
            continue
        
        elif "time" in value or "date" in value:
            time = Telltime()

            if "date" in value:
                current_date = date.today()

                Speak(f"The date today is {current_date}")

                continue 

            else:
                Speak(time) 

                continue 

        elif "bye" or "done" or "close" or "finished" in value:
            Speak("Bye, good day to you sir. shutting off")
            print("(´ 〜｀*) zzz")
            exit()


def Commands():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print('Listening')
        r._pause_threshold = 0.71

        r.adjust_for_ambient_noise(source)
        value = r.listen(source)

        try:
            print("Recognizing Data...")

            listen = r.recognize_google(value,language="en-US")

            print("The Command is:=",listen)

            
        except Exception as e:
            print(e)
            Speak("I do not Understand, Please try again.")
            print("Please try again")
            return "null"
        
        return listen

def Telltime():

    value = datetime.now()
    string = f"The time is {value.hour}:{value.minute}."

    return string
    
if __name__ == '__main__':
    query()

    









