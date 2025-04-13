import pygame
import os

class SoundManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SoundManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
            
        self._initialized = True
        self.sounds = {}
        self.music = None
        self.sound_enabled = True
        self.music_enabled = True
        self.sound_volume = 0.7
        self.music_volume = 0.5
        
        # Initialize the mixer
        pygame.mixer.init()
    
    def load_sound(self, name, file_path):
        """Load a sound effect and store it with the given name."""
        if name in self.sounds:
            return  # Already loaded
            
        if not os.path.exists(file_path):
            print(f"Warning: Sound file {file_path} not found")
            return
            
        try:
            sound = pygame.mixer.Sound(file_path)
            sound.set_volume(self.sound_volume)
            self.sounds[name] = sound
        except pygame.error as e:
            print(f"Error loading sound {file_path}: {e}")
    
    def load_music(self, file_path):
        """Load background music."""
        if not os.path.exists(file_path):
            print(f"Warning: Music file {file_path} not found")
            return False
            
        try:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.set_volume(self.music_volume)
            self.music = file_path
            return True
        except pygame.error as e:
            print(f"Error loading music {file_path}: {e}")
            return False
    
    def play_sound(self, name):
        """Play a sound by its name."""
        if not self.sound_enabled or name not in self.sounds:
            return
            
        self.sounds[name].play()
    
    def play_music(self, loops=-1):
        """Play the loaded background music."""
        if not self.music_enabled or not self.music:
            return
            
        pygame.mixer.music.play(loops)
    
    def stop_music(self):
        """Stop the background music."""
        pygame.mixer.music.stop()
    
    def pause_music(self):
        """Pause the background music."""
        pygame.mixer.music.pause()
    
    def unpause_music(self):
        """Resume the paused background music."""
        pygame.mixer.music.unpause()
    
    def set_sound_volume(self, volume):
        """Set the volume for all sound effects (0.0 to 1.0)."""
        self.sound_volume = max(0.0, min(1.0, volume))
        for sound in self.sounds.values():
            sound.set_volume(self.sound_volume)
    
    def set_music_volume(self, volume):
        """Set the volume for background music (0.0 to 1.0)."""
        self.music_volume = max(0.0, min(1.0, volume))
        pygame.mixer.music.set_volume(self.music_volume)
    
    def toggle_sound(self):
        """Toggle sound effects on/off."""
        self.sound_enabled = not self.sound_enabled
        return self.sound_enabled
    
    def toggle_music(self):
        """Toggle background music on/off."""
        self.music_enabled = not self.music_enabled
        if self.music_enabled:
            self.unpause_music()
        else:
            self.pause_music()
        return self.music_enabled
    
    def preload_game_sounds(self):
        """Preload all game sounds at once."""
        sounds_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sounds')
        
        # Create sounds directory if it doesn't exist
        if not os.path.exists(sounds_dir):
            os.makedirs(sounds_dir)
            print(f"Created sounds directory: {sounds_dir}")
            print("Please add sound files to this directory")
            return
        
        # Game sound effects (these files should be added to the sounds directory)
        sound_files = {
            'shoot': 'laser.wav',
            'explosion_large': 'explosion_large.wav',
            'explosion_medium': 'explosion_medium.wav',
            'explosion_small': 'explosion_small.wav',
            'game_over': 'game_over.wav',
            'menu_select': 'menu_select.wav',
            'menu_change': 'menu_change.wav'
        }
        
        for name, file_name in sound_files.items():
            file_path = os.path.join(sounds_dir, file_name)
            self.load_sound(name, file_path)
