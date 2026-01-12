import speech_recognition as sr
import pyttsx3
import os
import subprocess
import time
from datetime import datetime

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)
        
    def speak(self, text):
        """Speak the given text"""
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Listen for voice input from microphone"""
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout=5)
                command = self.recognizer.recognize_google(audio)
                print(f"You said: {command}")
                return command.lower()
            except sr.UnknownValueError:
                print("Could not understand audio")
                return None
            except sr.RequestError:
                print("Network error")
                return None
    
    def execute_command(self, command):
        """Execute voice commands"""
        if 'open' in command:
            self.open_application(command)
        elif 'close' in command:
            self.close_application(command)
        elif 'time' in command:
            self.tell_time()
        elif 'shutdown' in command:
            self.shutdown_pc()
        else:
            self.speak("Command not recognized")
    
    def open_application(self, command):
        """Open applications by voice command"""
        apps = {
            'notepad': 'notepad.exe',
            'chrome': 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
            'calculator': 'calc.exe',
            'vscode': 'code'
        }
        for app, path in apps.items():
            if app in command:
                os.startfile(path)
                self.speak(f"Opening {app}")
                break
    
    def close_application(self, command):
        """Close applications by voice command"""
        if 'chrome' in command or 'browser' in command:
            os.system('taskkill /IM chrome.exe')
            self.speak("Closing Chrome")
    
    def tell_time(self):
        """Tell current time"""
        current_time = datetime.now().strftime("%H:%M")
        self.speak(f"Current time is {current_time}")
    
    def shutdown_pc(self):
        """Shutdown PC with confirmation"""
        self.speak("Are you sure you want to shutdown?")
        confirmation = self.listen()
        if confirmation and 'yes' in confirmation:
            os.system('shutdown /s /t 10')
            self.speak("Shutting down in 10 seconds")
    
    def run(self):
        """Main loop for voice assistant"""
        self.speak("Voice Assistant started")
        while True:
            command = self.listen()
            if command:
                self.execute_command(command)

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()
