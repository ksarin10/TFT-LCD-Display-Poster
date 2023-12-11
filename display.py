import pygame
import serial

ser = serial.Serial('/dev/cu.usbserial-10', 9600)

pygame.init()

image_directory = "/Users/krishsarin/Downloads/Spider-Man"
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if ser.in_waiting > 0:
        arduino_data = ser.readline().decode('utf-8').strip()
        if arduino_data == "Sound Change Detected":

            print("Displaying Random Image")

    pygame.display.flip()
    clock.tick(30)
