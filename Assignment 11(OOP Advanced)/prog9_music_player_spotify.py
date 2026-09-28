"""
Program 9: Create a MusicPlayer class and subclass Spotify to override play method.
"""

# Base Class
class MusicPlayer:
    def __init__(self, brand):
        self.brand = brand

    def play(self, song):
        print(f"[{self.brand} MusicPlayer] Playing audio file locally: '{song}'")


# Subclass Spotify overriding play method
class Spotify(MusicPlayer):
    def __init__(self, plan_type="Premium"):
        super().__init__(brand="Spotify")
        self.plan_type = plan_type

    # Overriding the play method
    def play(self, song):
        print(f"[{self.brand} App ({self.plan_type})] Streaming '{song}' in Ultra HD 320kbps over cloud...")


def main():
    print("--- Program 9: MusicPlayer and Spotify Method Overriding ---")
    
    basic_player = MusicPlayer("Sony Walkman")
    spotify_app = Spotify(plan_type="Premium Individual")
    
    song_name = "Hotel California - Eagles"
    
    print("Default Music Player:")
    basic_player.play(song_name)
    
    print("\nSpotify Subclass (Overridden):")
    spotify_app.play(song_name)


if __name__ == "__main__":
    main()
