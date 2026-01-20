import pygame
import random
import time

# Initialize pygame mixer
pygame.mixer.init()

# List of audio files (update these paths to your audio files)
SOUND_FILES = [
    "atmospheric-436860.mp3",  # Replace with your audio file path
    "atmospheric-epic-437187.mp3",  # Replace with your audio file path
    "euphoria-atmospheric-energetic-sound-instrumental-226758.mp3"   # Replace with your audio file path
]

def play_random_sound(sound_files):
    """Play a random sound from the provided list"""
    sound_file = random.choice(sound_files)
    sound = pygame.mixer.Sound(sound_file)
    sound.play()
    return sound_file, sound

def main():
    """Main loop for audio player"""
    print("Audio Player - Press Enter to change audio, or 'q' to quit\n")
    
    current_sound = None
    
    while True:
        # Play a random sound
        sound_file, current_sound = play_random_sound(SOUND_FILES)
        print(f"Now playing: {sound_file}")
        
        # Wait for user input
        user_input = input("Press Enter to change audio (or 'q' to quit): ").strip().lower()
        
        if user_input == 'q':
            pygame.mixer.stop()
            print("Goodbye!")
            break
        else:
            # User pressed Enter, stop current audio and play new one
            pygame.mixer.stop()
            continue

if __name__ == "__main__":
    main()
