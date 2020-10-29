import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time
import smtplib
import random

jokes = ('Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them.', 'Why do we tell actors to break a leg? Because everyone has a cast', 'Yesterday I saw a guy spill all his Scrabble letters on the road. I asked him what the word was on the street', 'Knock Knock, whose there? Control Freak. Con- OK now you say Control Freak who?', 'Hear about the new restaurant called Karma? Theres no menu. You get what you deserve')

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Good Morning!")

	elif hour>=12 and hour <18:
		speak("Good Afternoon")

	else:
		speak("Good Evening")

	speak("What can I do for you")

def takeCommand():
	#It takes microphone input from user and returns string output

	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

		try:
			print("Recognizing...")
			query = r.recognize_google(audio, language='us-EN')
			print(f"User said: {query}\n")


		except Exception as e:
			# print(e)

			print("Say that again please...")
			return "None"
		return query

def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login('nyasa.luharuka@gmail.com', 'N302612l')
	server.sendmail('nyasa.luharuka@gmail.com', to, content)
	server.close()

if __name__ == "__main__":
	wishMe()
	while True:
		query = takeCommand().lower()
		#logic for executing tasks based on query
		if 'wikipedia' in query:
			speak('Searching wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences=2)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif 'open youtube' in query:
			webbrowser.open("https://youtube.com")
			query2 = takeCommand().lower()
			webbrowser.open("https://www.youtube.com/results?search_query=%s" % query2)
		elif 'open google' in query:
			speak("What would you like to search?")
			query1 = takeCommand().lower()
			webbrowser.open("https://google.com/search?q=%s" % query1)
		elif 'open python' in query:
			webbrowser.open("https://python.org")
		elif 'open pygame' in query:
			webbrowser.open("https://pygame.org/docs/ref/draw.html")
		elif 'play music' in query:
			music_dir = 'D:\\videos'
			songs = os.listdir(music_dir)
			print(songs)
			os.startfile(os.path.join(music_dir, songs[0]))

		elif 'the time' in query:
			strTime = time.asctime()
			print(time.asctime())
			speak(f"the time is {strTime}")

		elif 'open minecraft' in query:
			codePath = "C:\\Program Files (x86)\\Minecraft Launcher\\MinecraftLauncher.exe"
			os.startfile(codePath)

		elif 'open sublime' in query:
			codePath1 = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
			os.startfile(codePath1)

		elif 'email to my friend' in query:
			try:
				speak("What should I say to her?")
				content = takeCommand()
				to = "amiramanzanares@gmail.com"
				sendEmail(to, content)
				speak("Email has been sent!")
			except Exception as e:
				print(e)
				speak("Sorry mate. Just can't quite send it...")
		elif 'email to my dad' in query:
			try:
				speak("What should I say to your father?")
				content = takeCommand()
				to = "luharuka@gmail.com"
				sendEmail(to, content)
				speak("Email has been sent!")
			except Exception as e:
				print(e)
				speak("Sorry mate. Just can't quite send it...")
		elif 'email to my sophia' in query:
			try:
				speak("What should I say to your boomer?")
				content = takeCommand()
				to = "sophiajoon33@gmail.com"
				sendEmail(to, content)
				speak("Email has been sent!")
			except Exception as e:
				print(e)
				speak("Sorry mate. Just can't quite send it...")
		elif 'email to my sister' in query:
			try:
				speak("What should I say to your little sister?")
				content = takeCommand()
				to = "myra.luharuka@gmail.com"
				sendEmail(to, content)
				speak("Email has been sent!")
			except Exception as e:
				print(e)
				speak("Sorry mate. Just can't quite send it...")
		elif 'email to myself' in query:
			try:
				speak("What should I say to you?")
				content = takeCommand()
				to = "nyasa.luharuka@gmail.com"
				sendEmail(to, content)
				speak("Email has been sent!")
			except Exception as e:
				print(e)
				speak("Sorry mate. Just can't quite send it...")
		elif 'math' in query:
			num1 = float(input("Enter first number: "))
			op = input("Enter operator: ")
			num2 = float(input("Enter another number: "))
			if op == "+":
				print(num1 + num2)
				speak(num1 + num2)
			elif op == "-":
				print(num1 - num2)
				speak(num1 - num2)
			elif op == "*":
				print(num1 * num2)
				speak(num1 * num2)
			elif op == "/":
				print(num1 * num2)
				speak(num1 * num2)
			else:
				speak("Invalid Operator")
		elif 'thank you' in query:
			speak("You are welcome. Anything else?")
		elif 'weather' in query:
			speak("Pulling up the Weather")
			speak("Search a Place, Then Press Get Weather.")
			import tkinter as tk
			import requests
			import time
			from tkinter import font

			HEIGHT = 500
			WIDTH = 600


			#95202b9e858eaca7c063bd13e776006c
			#pro.openweathermap.org/data/2.5/forecast/hourly?id={city ID}&appid={your api key}


			def format_response(weather):
				try:
					name = weather['name']
					desc = weather['weather'][0]['description']
					temp = weather['main']['temp']

					final_str = 'Place: %s \nConditions: %s \nTemprature (℉): %s' % (name, desc, temp)
				except:
					final_str = 'There was a problem :('
				return final_str

			def get_weather(city):
				weather_key = '95202b9e858eaca7c063bd13e776006c'
				url = 'https://api.openweathermap.org/data/2.5/weather'
				params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
				response = requests.get(url, params=params)
				weather = response.json()

				label['text'] = format_response(weather)


			root = tk.Tk()

			canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
			canvas.pack()


			backround_image = tk.PhotoImage(file='landscape.png')
			backround_label = tk.Label(root, image=backround_image)
			backround_label.place(x=0, y=0, relwidth=1, relheight=1)

			frame = tk.Frame(root, bg='#80ccff', bd=5)
			frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

			entry = tk.Entry(frame, font=('Segoe Print', 18))
			entry.place(relwidth=0.65, relheight=1)

			button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
			button.place(relx=0.7, relwidth=0.3, relheight=1)

			lower_frame = tk.Frame(root, bg='#80ccff', bd=10)
			lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


			label = tk.Label(lower_frame, font=('Segoe Print', 18), anchor='nw', justify='left', bd=4)
			label.place(relwidth=1, relheight=1)
			root.mainloop()
		elif 'news' in query:
				webbrowser.open("www.cnn.com/cnn10")
		elif 'your name' in query:
			speak("My name is Bryce")

		elif 'your age' in query:
			speak("My age is 20")

		elif 'hello' in query:
			speak("Hi there!")

		elif 'what can you do' in query:
			speak("I can send messages, play songs, be a calculator, show the weather, time, and open some apps and websites!")

		elif 'cool' in query:
			speak("Thanks I try")
		elif 'joke' in query:
			speak(random.choice(jokes))

		elif 'go to my mail' in query:
			webbrowser.open("gmail.com")

		elif 'open coding with kids' in query:
			webbrowser.open("codingwithkids.com")

		elif 'open video' in query:
			codePath2 = "C:\\Users\\nyasa\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
			os.startfile(codePath2)
		elif 'you have emotions' in query:
			speak("I have some emotions")
		elif 'you are nice' in query:
			speak("Thank you, so are you")
		elif 'improve' in query:
			speak("let me know what I can do to improve")
			speak("Send a message to Nyasa and tell her how I can improve")
			speak("What should I say to you?")
			content = takeCommand()
			to = "nyasa.luharuka@gmail.com"
			sendEmail(to, content)
			speak("Email has been sent!")
		elif 'exit' in query:
			speak("Shutting Down. Thank you for your time")
			exit()
		elif 'mean' in query:
			speak("Ouch are you calling me mean?")
		elif 'how are you' in query:
			speak("Im good, anything I can do for you")
		elif 'bored' in query:
			speak("I will send an email to myra letting her know.")
			speak("What should I say to your little sister?")
			content = takeCommand()
			to = "myra.luharuka@gmail.com"
			sendEmail(to, content)
			speak("Email has been sent!")
		elif 'wow' in query:
			speak("I know right!!!")
		elif 'recommend me games' in query:
			webbrowser.open('https://www.metacritic.com/browse/games/scwore/metascore/year/all/filtered')
		elif 'boomer' in query:
			speak("No you are. Stop calling me a boomer.")
		elif 'amazon' in query:
			speak("What would you like to search?")
			printamazon = input("What would you like to search: ")
			webbrowser.open("https://www.amazon.com/s?k=%s" % printamazon)
		elif 'school' in query:
			webbrowser.open("https://myapps.classlink.com/home")
			codePath3 = "C:\\Users\\nyasa\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams"
			os.startfile(codePath3)
			webbrowser.open("https://www.office.com/?auth=2")
			webbrowser.open("https://www.fortbendisd.com/studentshome")
			webbrowser.open("https://fortbendisd.schoology.com/home")
		elif 'anxiety' in query:
			speak("Chill, you got this. Just be calm and you'll be fine")
