from dotenv import load_dotenv 
from services.spotifyAPI import spotifyAPI

def main():
    
    load_dotenv()

    playlist_name = "darty mix"
    spotify = spotifyAPI()
    playlist_id = spotify.get_playlist_id_by_name(playlist_name)
    
    if playlist_id:
        print(f"Playlist ID for '{playlist_name}': {playlist_id}")
        
        playlist_items = spotify.get_playlist_items(playlist_id)
        print(f"Playlist items for '{playlist_name}': {playlist_items}")
    else:
        print(f"Playlist '{playlist_name}' not found.")

if __name__ == "__main__":
    main()