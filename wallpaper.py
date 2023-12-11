import os
import random
import speech_recognition as sr
import pygame
import time


image_directory = "/Users/krishsarin/Downloads/Spider-Man"


def display_with_fade(image_path):
    
    pygame.init()

   
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Image Display")

    
    image = pygame.image.load(image_path)

    
    screen = pygame.display.set_mode(image.get_size())

    
    fade_in_surface = pygame.Surface(screen.get_size())
    fade_in_surface.fill((0, 0, 0))
    for alpha in range(0, 256, 8):
        fade_in_surface.set_alpha(alpha)
        screen.blit(image, (0, 0))
        screen.blit(fade_in_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(30)

    
    screen.blit(image, (0, 0))
    pygame.display.flip()

    
    time.sleep(3)  

   
    fade_out_surface = pygame.Surface(screen.get_size())
    fade_out_surface.fill((0, 0, 0))
    for alpha in range(255, -1, -8):
        fade_out_surface.set_alpha(alpha)
        screen.blit(image, (0, 0))
        screen.blit(fade_out_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(30)

    
    pygame.quit()


def display_random_image():
    
    image_files = [f for f in os.listdir(
        image_directory) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    
    random_image_file = random.choice(image_files)

   
    image_path = os.path.join(image_directory, random_image_file)

    
    display_with_fade(image_path)


def listen_for_change():
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Say 'change' to display a random image or 'stop' to end the program.")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            
            command = recognizer.recognize_google(audio).lower()

            if "change" in command:
                display_random_image()
            elif "stop" in command:
                print("Program stopped.")
                break
            else:
                print("Command not recognized. Try saying 'change' or 'stop'.")

        except sr.UnknownValueError:
            print("Speech recognition could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")


if __name__ == "__main__":
    listen_for_change()
