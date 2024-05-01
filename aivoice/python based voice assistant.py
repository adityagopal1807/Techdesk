import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import random
import wikipedia
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer
import random
from googletrans import Translator
import cv2



mixer.init()

password = "0000"
password_hint = "Hint: It's a four-digit number."
def speechtx(x):
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

def open_camera():
    print("Opening Camera")
    speechtx("opening camera")
    video_cap=cv2.VideoCapture(0)
    while True:
        ret , video_data= video_cap.read()
        cv2.imshow("video_live",video_data)
        if cv2.waitKey(10)==ord("q"):
            break
    video_cap.release() 
    print("Opening Camera")
    speechtx("opening camera")   
    
 
 
    
def playssmusicccc():
    mixer.music.load('effect.mp3')
    mixer.music.play()    



def get_password():
    for _ in range(5):
        speechtx("Please enter the password to start")
        password_input = input("Please enter the password to start: ")
        


        if password_input == password:
            
            print("Password correct. Starting the assistant.")
            speechtx("Password correct. Starting the assistant")
            playssmusicccc()
            break
        elif password_input == "change password":
            change_password()
            print("Password changed successfully.")
            speechtx("Password changed successfully")
        else:
            print("Incorrect password. Please try again.")
            speechtx("Incorrect password. Please try again")
            if _ < 4:
                print("You have", 4 - _ , "attempts left.")
                print(password_hint)
                speechtx(password_hint)

def change_password():
    global password
    new_password = input("Enter new password (four-digit number): ")

    if len(new_password) == 4 and new_password.isdigit():
        password = new_password
    else:
        print("Invalid password format. Password must be a four-digit number.")
        change_password()

get_password()


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speechtx("How can i assist you")

        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio,language='en-IN')
            print(data)
            return data.lower()
        except sr.UnknownValueError:
            print("Not Understood")
            return None
        

def translate_text(text, dest_language):
    translator = Translator()
    translated = translator.translate(text, dest=dest_language)
    return translated.text        


def wikipedia_search(query):
    try:
        result = wikipedia.summary(query, sentences=4)
        print(result)
        speechtx(result)
    except wikipedia.exceptions.PageError:


        print("Page not found.")
        speechtx("Page not found.")
    except wikipedia.exceptions.DisambiguationError:
        print("Multiple matches found. Please be more specific.")
        speechtx("Multiple matches found. Please be more specific.")       
    


while True:
        data1 = sptext()
    

        if not data1:
            print("You didn't say anythings.....")
            speechtx("You didn't say anythings")
            continue


        elif "your name" in data1:
            name = "My name is Jeenie."
            print(name)
            speechtx(name)

        elif "tell me about yourself" in data1 or "give me your introduction" in data1 or "jennie give me your introduction" in data1:
            intro="Hello everyone, as you all are interested to know about me, so i am here to introduce myself in front of you all. My name is Jennie. I am specially designed for the tech desk competition. I am basically a voice assistant which can give output according to the user command. And please don't ask about my gender as its all on my developer, Ha ha ha ha ......"  
            print(intro)
            speechtx(intro)

        elif "open camera" in data1:
            open_camera()    
              

        elif "hello" in data1 or "hii" in data1:
            hello="HII ,my name is jennie how can i assist you today"  
            print(hello)
            speechtx(hello) 

        elif "how are you" in data1 or "how r u" in data1:
            how="I am good whats about you"  
            print(how) 
            speechtx(how)  

        elif "old are you" in data1 or "what is your age" in data1:
            age = "I am a new-born made for the TechDesk competition."
            print(age)
            speechtx(age)
        
        

        elif 'time' in data1:
            time = datetime.datetime.now().strftime("%I:%M %p")
            speechtx(time)
        

        elif 'translate' in data1 or "translation" in data1:
            speechtx("please say the text you want to translate") 
            text_to_translate=sptext() 
            translate_text=translate_text(text_to_translate,"hi")
            print(f"Translated text :{translate_text}") 
            speechtx(f"the translated text is:{translate_text}") 

        elif "youtube" in data1:
            webbrowser.open("https://www.youtube.com/")
            youtube = "Opening YouTube."
            speechtx(youtube)

        elif "open google" in data1:
            webbrowser.open("https://www.google.com/")
            google = "Opening Google."
            speechtx(google)
        elif "open instagram" in data1:
            webbrowser.open("https://www.instagram.com/")
            insta = "Opening instagram."
            speechtx(insta)
        elif "joke" in data1:
            joke_1 = pyjokes.get_joke(language="en", category="neutral")
            print(joke_1)
            speechtx(f"{joke_1},.          Ha ha ha ha.....")

        elif "weather" in data1:
            print("weather is sunny")
            speechtx("weather is sunny. I am opening partner website for more details") 
            webbrowser.open("https://www.accuweather.com/en/in/india-weather") 


             


        elif "open whatsapp" in data1:
             webbrowser.open("https://www.whatsapp.com/")
             whatsapp="opening whatsapp"
             speechtx(whatsapp)   
    

        elif "day" in data1:
            day = datetime.datetime.now().strftime("%A")
            speechtx(f"Today is {day}.")

        elif "date" in data1:
            date = datetime.datetime.now().strftime("%B %d, %Y")
            speechtx(f"Today's date is {date}.")

        elif "google search" in data1:
            search_query = data1.replace("google search", "")
            search_url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(search_url)
            speechtx(f"Here are the search results for {search_query}.")


        
        elif "calculation" in data1 or "calculate" in data1 or "calculator" in data1:
            while True:
                print('''OPERATORS:-
1. Add(+)
2. Substrate (-)
3. Multiply(*)
4. Divide(÷)
5. Exit''')
                speechtx("Enput operator")
                c=input("Enter operator:")
                if c =="5":
                    print("Thanks for using our calculator")
                    speechtx("thanks for using our calculator")
                    break
                
                else:
                   speechtx("enter first number")
                   a=eval(input("Enter 1st number:"))
                   speechtx(a)
                   speechtx("Enter second number")
                   b=eval(input("Enter 2nd number:"))
                   speechtx(b)
                

            
                   if c=="1":
                      sum1=("The sum is ",a+b)
                      print("The sum is ",a+b)
                      speechtx(sum1)
                   elif c=="2":
                      sub="The substraction is ",a-b
                      print("The substraction is ",a-b)
                      speechtx(sub)
                   elif c=="3":
                      print("The multiplication is ",a*b) 
                      mult="the multiplication is",a*b
                      speechtx(mult)   
                   elif c=="4":
                      divi="The division is ",a/b
                      print("The division is ",a/b)
                      speechtx(divi)
                   
                   else:
                      wrong="wrong operator selected"
                      print("wrong operator selected")
                      speechtx(wrong)     
                 

        elif "story" in data1:
            story=["Five cows lived in a little forest. They ate fresh grass in a large green meadow. They were kind friends. They decided to do everything together, so the lions couldn't attack them for food. One day, the five cows fought and each one started to eat grass in a different place. The lions decided to seize the opportunity and killed them one by one. Moral of the story is :- UNITY IS STRENGTH ! ","One day, A lamb was eating sweet grass away from her flock of sheep. She didn't notice a wolf walking nearer to her. When she saw the wolf, she started pleading, Please, don't eat me. My stomach is full of grass. You can wait a while to make my meat taste much better. The grass in my stomach will be digested quickly if you let me dance.The wolf agreed.While the lamb was dancing, she had a new idea. She said,  I can dance faster if you take my bell and ring it so hard.The wolf took the bell and started to ring so hard. The shepherd heard the sound and ran quickly to save the lamb's life."]
            randomstory=random.choice(story)
            print(randomstory)  
            speechtx(randomstory)
            
        elif"tell me about your function" in data1 or "tell me your key features" in data1 or "tell me more about yourself" in data1:
            features="Hey i am new born so i don't have some typical type features, But I will try my best to assist you better everytime. One of my features include i ask password which is given by my developer to access all my features which will ensure privacy and making me more personlized. I assist you through both text or voice conversation. I can translate any words given by you in hindi. One of my best features include I have many inbuilt entertainment application which has been developed by my developers, One of Them is MUSIZ, which a music player inbuit in me , so from now whenever you want to listen arjit singh assist me through your voice, Ha ha ha ha.......,Now i am feeling shy to praise myself so much, there is so much features which is inbuilt in me"
            print(features)
            speechtx(features)

        elif ("galgotias university") in data1:
            print("Galgotias Universty is top private university in Uttar Pradesh. What you exactly want to know about galgotias university") 
            speechtx("Galgotias Universty is top private university in Uttar Pradesh.")

            
            
        elif "game" in data1 or "play game" in data1:
            def play_game():
                choices = ['stone', 'paper', 'scissors']
                while True:
                    computer_choice = random.choice(choices)
                    speechtx("Enter your choices")
                    user_choice = input("Enter your choice (stone/paper/scissors) or 'quit' to exit: ").lower()
                    

                    if user_choice == 'quit':
                        speechtx("thanks for Playing")
                        print("Thanks for playing!")
                        break

                    print(f"\nYou choose: {user_choice}")
                    print(f"Computer choose: {computer_choice}\n")
                    speechtx("you choose")
                    speechtx(user_choice)
                    speechtx("computer choose")
                    speechtx(computer_choice)

                    if user_choice not in choices:
                        print("Invalid choice. Please enter either stone, paper, scissors, or 'quit' to exit.")
                    elif user_choice == computer_choice:
                        print("It's a tie!")
                        speechtx("it's a tie")
                    elif (user_choice == 'stone' and computer_choice == 'scissors') or \
                         (user_choice == 'paper' and computer_choice == 'stone') or \
                         (user_choice == 'scissors' and computer_choice == 'paper'):
                        print("You win!")
                        speechtx("you win")
                    else:
                        print("Computer wins!")
                        speechtx("computer wins")
   
            play_game()  

        elif "news" in data1:
            print("I can not fetch news at this moment, but i can take you in news website.")     
            speechtx("I can not fetch news at this moment, but i can take you in news website.")
    
            webbrowser.open("https://www.bbc.com/news/world/asia/india")
            bbc = "opening bbc"
            speechtx(bbc)

        

        elif "wikipedia" in data1:
            search_query=data1.replace("wikipedia search","")
            wikipedia_search(search_query)

        elif "play song" in data1 or "play music" in data1 or "open music" in data1:
            print("opening musicz")
            speechtx("opening musicz now you can enjoy your playlist with musicz")

            
            mixer.init()
            class musicplayer:
                def __init__(self,Tk):
                    self.root=Tk
                    self.root.title("Music_player")
                    self.root.geometry("400x400")
                    self.root.configure(background="black")

                            #openfile
                    def Openfile():
                        global filename
                        filename=filedialog.askopenfilename()

    
        #MENU
                    self.menubar=Menu(self.root)
                    self.root.configure(menu=self.menubar)

        #submenu
                    self.submenu=Menu(self.menubar,tearoff=0)
                    self.menubar.add_cascade(label='File',menu=self.submenu)
                    self.submenu.add_command(label='Open',command=Openfile)
                    self.submenu.add_command(label='Exit',command=self.root.destroy)

                    self.submenu2=Menu(self.menubar,tearoff=0)
                    self.menubar.add_cascade(label='About us',menu=self.submenu2)
                    self.submenu2.add_command(label='We made this musiz for the Techdesk competetion')

        

         #mute
                    def mute():
                        self.scale.set(0)
                        self.mute=ImageTk.PhotoImage(file='mute.png')
                        mute=Button(self.root,image=self.mute,bd=0,bg='red',command=unmute,cursor='hand2').place(x=947,y=555,height=50,width=50)

        #volume img
                    self.volumes=ImageTk.PhotoImage(file='volume.png')
                    volumes=Button(self.root,image=self.volumes,bd=0,bg='red',command=mute,cursor='hand2').place(x=947,y=555,height=50,width=50)    

        #unmute
                    def unmute():
                        self.scale.set(100)
                        self.volumes=ImageTk.PhotoImage(file='volume.png')
                        volumes=Button(self.root,image=self.volumes,bd=0,bg='red',command=mute,cursor='hand2').place(x=947,y=555,height=50,width=50)

        #function for volume bar
                    def volume(vol):
                        volume=int(vol)/100
                        mixer.music.set_volume(volume)

        #volume bar
                    self.scale=Scale(self.root,from_=0,to=100,orient=VERTICAL,length=450,bg='black',command=volume,cursor='hand2')
                    self.scale.set(25)
                    self.scale.place(x=950,y=98)

        
         #ADDING LABEL
        
        
        #ADDING IMAGE
                    self.photo=ImageTk.PhotoImage(file='everglade.jpg')
                    photo=Label(self.root,image=self.photo).place(x=50,y=100,width=880,height=450)

                    self.photop=ImageTk.PhotoImage(file='apple.png')
                    photop=Label(self.root,image=self.photop,bg='black').place(x=50,y=100,width=880,height=450)


                    self.photo_s1=ImageTk.PhotoImage(file='music.jpg')
                    photo_s1=Label(self.root,image=self.photo_s1,bg='violet',cursor='hand2').place(x=00,y=1,width=100,height=110)

                    self.file_label = Label(text='MUSIZ', bg='black', fg='red', font=('Arial', 30),cursor='hand2')
                    self.file_label.place(x=100, y=28)

    
        #ADDING LEFT SIDE IMAGE

                    self.file_label = Label(text='My playlist', bg='black', fg='white', font=('Arial', 30),cursor='hand2')
                    self.file_label.place(x=1100, y=30)

                    def playsmusic():
                        mixer.music.load('Mere Dholna_192(Ghantalele.com).mp3')
                        mixer.music.play()
                        self.label3['text']='MUSIC playing'

                    def playssmusic():
                        mixer.music.load('song1.mp3')
                        mixer.music.play()
                        self.label3['text']='MUSIC playing'

                    def playssmusicc():
                        mixer.music.load('bajarang.mp3')
                        mixer.music.play()
                        self.label3['text']='MUSIC playing'

                    def playssmusisc():
                        mixer.music.load('Kun Faaya Kun_192(Ghantalele.com).mp3')
                        mixer.music.play()
                        self.label3['text']='MUSIC playing'

                    def playssmusiiisc():
                        mixer.music.load('128-Halki Halki Si - Asees Kaur 128 Kbps - Copy.mp3')
                        mixer.music.play()
                        self.label3['text']='MUSIC playing'
                
        

                    def playrandomss():
                
                        music_filess=['bajarang.mp3','song1.mp3','Mere Dholna_192(Ghantalele.com).mp3','128-Abrars Entry Jamal Kudu - Animal 128 Kbps.mp3','128-Galti - Vishal Mishra 128 Kbps.mp3','128-Halki Halki Si - Asees Kaur 128 Kbps.mp3','128-Mohabbat Karne Wale - Tulsi Kumar 128 Kbps.mp3','128-Saiyaan Dheere Dheere - Tony Kakkar 128 Kbps.mp3','128-Zaalim - Badshah 128 Kbps.mp3','128-Zindagi Tere Naam - Yodha 128 Kbps.mp3','Kun Faaya Kun_192(Ghantalele.com).mp3']
                        random_musicc=random.choice(music_filess)
                        mixer.music.load(random_musicc)
                        mixer.music.play()
                        data2=sptext()
                        
                    
                    
                    
                    def piics():
                        self.photop=ImageTk.PhotoImage(file='apple.png')
                        photop=Label(self.root,image=self.photop,bg='black',cursor='hand2').place(x=50,y=120,width=880,height=450)  

                    def combine11():
                        piics() 
                        playrandomss()        
            
                    def pics():
                        self.photop=ImageTk.PhotoImage(file='hai.jpg')
                        photop=Label(self.root,image=self.photop,bg='black',cursor='hand2').place(x=50,y=120,width=880,height=450)  


          

                    def combine1():
                        pics() 
                        playssmusic() 

    

                    def picss():
                        self.photop=ImageTk.PhotoImage(file='mere.jpg')
                        photop=Label(self.root,image=self.photop,bg='black',cursor='hand2').place(x=50,y=120,width=880,height=450)  

                    def combine2():
                        picss() 
                        playsmusic()

                    def picsss():
                        self.photop=ImageTk.PhotoImage(file='hari.jpg')
                        photop=Label(self.root,image=self.photop,bg='black',cursor='hand2').place(x=50,y=120,width=880,height=450) 

                    def combine3():
                        picsss()
                        playssmusicc() 

                    def piccsss():
                        self.photop=ImageTk.PhotoImage(file='15.jpg')
                        photop=Label(self.root,image=self.photop,bg='black',cursor='hand2').place(x=50,y=120,width=880,height=450) 

                    def combine4():
                        piccsss()
                        playssmusisc() 


                    def picccsss():
                        self.photop=ImageTk.PhotoImage(file='hal.jpg')
                        photop=Label(self.root,image=self.photop,bg='black',cursor='hand2').place(x=50,y=120,width=880,height=450)

                    def combine5():
                        picccsss()
                        playssmusiiisc


        

                    self.L_photo=ImageTk.PhotoImage(file='dholna.jpeg')
                    L_photo=Button(self.root,image=self.L_photo,bd=0,bg='red',command=combine2,cursor='hand2').place(x=1050,y=100,width=70,height=70)


                    self.file_label = Button(text='Mere Dholna', bg='red', fg='black', font=('Arial', 15),command=combine2,cursor='hand2')
                    self.file_label.place(x=1120, y=100,height=70,width=200)

                    self.L1_photo=ImageTk.PhotoImage(file='tu1.jpeg')
                    L1_photo=Button(self.root,image=self.L1_photo,bd=0,bg='red',command=combine1,cursor='hand2').place(x=1050,y=200,width=70,height=70)

                    self.file_label = Button(text='Tu hai Kahan', bg='red', fg='black', font=('Arial', 15),command=combine1,cursor='hand2')
                    self.file_label.place(x=1120, y=200,height=70,width=200)

                    self.L2_photo=ImageTk.PhotoImage(file='hanu.jpeg')
                    L2_photo=Button(self.root,image=self.L2_photo,bd=0,bg='red',command=combine3,cursor='hand2').place(x=1050,y=300,width=70,height=70)

                    self.file_label = Button(text='Hari aur main', bg='red', fg='black', font=('Arial', 15),command=combine3,cursor='hand2')
                    self.file_label.place(x=1120, y=300,height=70,width=200)

                    self.L3_photo=ImageTk.PhotoImage(file='5.jpeg')
                    L3_photo=Button(self.root,image=self.L3_photo,bd=0,bg='red',command=combine4,cursor='hand2').place(x=1050,y=400,width=70,height=70)

                    self.file_label = Button(text='Kun Faaya Kun', bg='red', fg='black', font=('Arial', 15),command=combine4,cursor='hand2')
                    self.file_label.place(x=1120, y=400,height=70,width=200)


                    self.L7_photo=ImageTk.PhotoImage(file='poster.jpeg')
                    L7_photo=Button(self.root,image=self.L7_photo,bd=0,bg='red',command=combine5,cursor='hand2').place(x=1050,y=500,width=70,height=70)

                    self.file_label = Button(text='Halki Halki si', bg='red', fg='black', font=('Arial', 15),command=combine5,cursor='hand2')
                    self.file_label.place(x=1120, y=500,height=70,width=200)

                    
         #FUNCTIONS FOR BUTTONS
                    def playmusic():
                      try:
                            paused
                      except NameError:
                            try:    
                               mixer.music.load(filename)
                               mixer.music.play()
                               self.label1['text']='MUSIC PLAYING!'

                
                 
                            except:
                                pass

                      else:
                            mixer.music.unpause()
                            self.label5['text']='MUSIC UNPAUSED!'
    



                
                    def pausemusic():
                        global paused
                        paused=TRUE
                        mixer.music.pause()
                        self.label2['text']='MUSIC PAUSED!'
        

                    def stopmusic():
                        mixer.music.stop()
                        self.label3['text']='MUSIC STOP!' 

        



        
    
        #CREATING BUTTONS 
                    self.photo_B1=ImageTk.PhotoImage(file='play.png')
                    photo_B1=Button(self.root,image=self.photo_B1,bd=0,bg='violet',command=playmusic,cursor='hand2').place(x=370,y=650,height=100,width=100)

        
                    self.photo_B2=ImageTk.PhotoImage(file='pause.png')
                    photo_B2=Button(self.root,image=self.photo_B2,bd=0,bg='black',command=pausemusic,cursor='hand2').place(x=210,y=650,height=100,width=100)

                    self.photo_B6=ImageTk.PhotoImage(file='stop1.jpeg')
                    photo_B6=Button(self.root,image=self.photo_B6,bd=0,bg='black',command=stopmusic,cursor='hand2').place(x=530,y=650,height=100,width=100)


                    self.photo_B3=ImageTk.PhotoImage(file='previous.png')
                    photo_B3=Button(self.root,image=self.photo_B3,bd=0,bg='black',cursor='hand2',command=playrandomss).place(x=50,y=650,height=100,width=100)

                    self.photo_B4=ImageTk.PhotoImage(file='next.png')
                    photo_B4=Button(self.root,image=self.photo_B4,bd=0,bg='black',cursor='hand2',command=playrandomss).place(x=690,y=650,height=100,width=100)             

                    self.photo_B5=ImageTk.PhotoImage(file='shuffle.jpg')
                    photo_B5=Button(self.root,image=self.photo_B5,bd=0,bg='black',cursor='hand2',command=combine11).place(x=850,y=650,height=100,width=100)

        
            root=Tk() 
            obj=musicplayer(root)
            root.mainloop()




        elif "exit" in data1:
            print("Thank you. I can assist you whenever you need help.")
            speechtx("Thank you. I can assist you whenever you need help.")
            break
        else:
            print("not understand try again")
            speechtx("not understand try again")