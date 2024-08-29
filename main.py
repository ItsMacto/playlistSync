from dotenv import load_dotenv 
from services.spotifyAPI import spotifyAPI
from services.playlistServices import save_playlist_items, create_playlist
from database.db import DatabaseManager
from models import Playlist, PlaylistItem

def initialize_database():
    with DatabaseManager() as db_manager:
        db_manager.create_tables()


def main():
    
    load_dotenv()
    initialize_database()
    
    playlist_name = "darty mix"
    spotify = spotifyAPI()
    spotify_playlist_id = spotify.get_playlist_id_by_name(playlist_name)
    
    if spotify_playlist_id:
        # print(f"Playlist ID for '{playlist_name}': {spotify_playlist_id}")
        
        # playlist_items = spotify.get_playlist_items(spotify_playlist_id)
        # with DatabaseManager() as db_manager:
        #     playlist_id = create_playlist(db_manager, spotify_playlist_id, playlist_name)
        #     save_playlist_items(db_manager, playlist_id, playlist_items)
        
        # # print(f"Playlist items for '{playlist_name}': {playlist_items}")
        
        with DatabaseManager() as db_manager:
            playlist_id = Playlist(db_manager).get_playlist_by_spotify_id(spotify_playlist_id)['id']
            playlist_items = PlaylistItem(db_manager).get_items_by_playlist_id(playlist_id)
            print(f"Playlist items for '{playlist_name}': ")
            
            for item in playlist_items:
                print(f"Item ID: {item['id']}, Track Name: {item['track_name']}")
        
    else:
        print(f"Playlist '{playlist_name}' not found.")

if __name__ == "__main__":
    main()