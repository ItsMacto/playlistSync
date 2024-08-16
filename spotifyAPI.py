import json
import tempfile
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


def get_playlist_id_by_name(playlist_name):
    scope = "playlist-read-private"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    
    # Initialize variables for pagination
    playlists = sp.current_user_playlists()
    
    while playlists:
        # Search for the playlist by name in the current page
        for playlist in playlists['items']:
            if playlist['name'].lower() == playlist_name.lower():
                return playlist['id']
        
        # If there's a next page of playlists, retrieve it
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None
    
    # If the playlist is not found after iterating through all pages
    return None

playlist_id = get_playlist_id_by_name("darty mix")

print(playlist_id)


# print(sp.playlist_items(playlist_id))
playlist_items = sp.playlist_items(playlist_id, fields='items(track(name, artists(name), id, external_ids(isrc)))')
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
    json.dump(playlist_items, f, indent=4)
    print(f.name)