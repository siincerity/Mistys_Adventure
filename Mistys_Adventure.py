import os
import time
import random
from gtts import gTTS
import pygame
import RPi.GPIO as GPIO
import pygame.mixer
import sys


# Define arrays of five possible outcome statements for each detected outcome
# Read the contents of the file "clam.txt" and store each line as a separate element in the "clam_statements" array
with open(os.path.join("input", "clam.txt")) as f:
    clam_statements = f.read().splitlines()

# Read the contents of the file "turtle.txt" and store each line as a separate element in the "turtle_statements" array
with open(os.path.join("input", "turtle.txt")) as f:
    turtle_statements = f.read().splitlines()

# Read the contents of the file "starfish.txt" and store each line as a separate element in the "starfish_statements" array
with open(os.path.join("input", "starfish.txt")) as f:
    starfish_statements = f.read().splitlines()

# Read the contents of the file "coral.txt" and store each line as a separate element in the "coral_statements" array
with open(os.path.join("input", "coral.txt")) as f:
    coral_statements = f.read().splitlines()

# Read the contents of the file "shark.txt" and store each line as a separate element in the "shark_statements" array
with open(os.path.join("input", "shark.txt")) as f:
    shark_statements = f.read().splitlines()

print('Start')
sys.stdout.flush()  # Alternative way to flush output (so it will be seen immediately)

# Initialize the TTS engine
pygame.mixer.init()
# Play the splash sound effect
sound_effect = pygame.mixer.Sound("blue.wav")
sound_effect.play()
#Change lights to blue
os.popen("sudo python3 blue.py")
while True:


    #print("Scan your RFID")
    output = os.popen("python3 Read.py").read()
    if "clam" in output:
        #Change lights to purple
        os.popen("sudo python3 purple.py")
        # Select a random statement from the clam_statements array
        statement = random.choice(clam_statements)
        with open("Website/current_statement", "w") as file:
            file.write(statement)
        print('=' + statement)
        sys.stdout.flush()  # Alternative way to flush output (so it will be seen immediately)
        # Convert the text to speech
        tts = gTTS(text=statement, lang='en', tld='co.uk')
        tts.save(os.path.join("TTS", "clam.mp3"))
        pygame.mixer.music.load(os.path.join("TTS", "clam.mp3"))
        pygame.mixer.music.play()
        time.sleep(6)
        sound_effect.play()
        os.popen("sudo python3 blue.py")
        # Wait until the new RFID is scanned
        while pygame.mixer.music.get_busy() or "clam" in output:
            output = os.popen("python3 Read.py").read()

    elif "turtle" in output:
        #Change lights to green
        os.popen("sudo python3 green.py")
        # Select a random statement from the turtle_statements array
        statement = random.choice(turtle_statements)
        with open("Website/current_statement", "w") as file:
            file.write(statement)
        print('=' + statement)
        sys.stdout.flush()  # Alternative way to flush output (so it will be seen immediately)
        # Convert the text to speech
        tts = gTTS(text=statement, lang='en', tld='us')
        tts.save(os.path.join("TTS", "turtle.mp3"))
        pygame.mixer.music.load(os.path.join("TTS", "turtle.mp3"))
        pygame.mixer.music.play()
        time.sleep(6)
        sound_effect.play()
        os.popen("sudo python3 blue.py")
        # Wait until the new RFID is scanned
        while pygame.mixer.music.get_busy() or "turtle" in output:
            output = os.popen("python3 Read.py").read()

    elif "starfish" in output:
        #Change lights to orange
        os.popen("sudo python3 orange.py")
        # Select a random statement from the starfish_statements array
        statement = random.choice(starfish_statements)
        with open("Website/current_statement", "w") as file:
            file.write(statement)
        print('=' + statement)
        sys.stdout.flush()  # Alternative way to flush output (so it will be seen immediately)
        # Convert the text to speech
        tts = gTTS(text=statement, lang='en', tld='com.au')
        tts.save(os.path.join("TTS", "starfish.mp3"))
        pygame.mixer.music.load(os.path.join("TTS", "starfish.mp3"))
        pygame.mixer.music.play()
        time.sleep(6)
        sound_effect.play()
        os.popen("sudo python3 blue.py")
        # Wait until the new RFID is scanned
        while pygame.mixer.music.get_busy() or "starfish" in output:
            output = os.popen("python3 Read.py").read()

    elif "coral" in output:
        #Change lights to pink
        os.popen("sudo python3 pink.py")
        # Select a random statement from the coral_statements array
        statement = random.choice(coral_statements)
        with open("Website/current_statement", "w") as file:
            file.write(statement)
        print('=' + statement)
        sys.stdout.flush()  # Alternative way to flush output (so it will be seen immediately)
        # Convert the text to speech
        tts = gTTS(text=statement, lang='en', tld='co.in')
        tts.save(os.path.join("TTS", "coral.mp3"))
        pygame.mixer.music.load(os.path.join("TTS", "coral.mp3"))
        pygame.mixer.music.play()
        time.sleep(6)
        sound_effect.play()
        os.popen("sudo python3 blue.py")
        # Wait until the new RFID is scanned
        while pygame.mixer.music.get_busy() or "coral" in output:
            output = os.popen("python3 Read.py").read()

    elif "shark" in output:
        #Change lights to red
        os.popen("sudo python3 red.py")
        # Select a random statement from the shark_statements array
        statement = random.choice(shark_statements)
        with open("Website/current_statement", "w") as file:
            file.write(statement)
        print('=' + statement)
        sys.stdout.flush()  # Alternative way to flush output (so it will be seen immediately)
        # Convert the text to speech
        tts = gTTS(text=statement, lang='en', tld='co.za')
        tts.save(os.path.join("TTS", "shark.mp3"))
        pygame.mixer.music.load(os.path.join("TTS", "shark.mp3"))
        pygame.mixer.music.play()
        time.sleep(6)
        sound_effect.play()
        os.popen("sudo python3 blue.py")
        # Wait until the new RFID is scanned
        while pygame.mixer.music.get_busy() or "shark" in output:
            output = os.popen("python3 Read.py").read()

    else:
        print('Jingle!')
        sys.stdout.flush()  # Alternative way to flush output (so it will be seen immediately)
        pygame.mixer.music.load(os.path.join("jingle.mp3"))
        pygame.mixer.music.play()





    time.sleep(0.5)
