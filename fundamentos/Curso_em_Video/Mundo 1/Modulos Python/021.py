# O programa deve abrir e reproduzir um arquivo mp3
import pygame

pygame.init()
pygame.mixer.music.set_volume(1.0) 
pygame.mixer.music.load('sounds/Memories and Dreams.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
pygame.event.wait()
