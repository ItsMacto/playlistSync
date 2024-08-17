import spotipy
from spotipy.oauth2 import SpotifyOAuth

class spotifyAPI:
    def __init__(self, scope="playlist-read-private"):
            self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    
    def get_playlist_id_by_name(self, playlist_name: str):
        playlists = self.sp.current_user_playlists()
        
        while playlists:
            for playlist in playlists['items']:
                if playlist['name'].lower() == playlist_name.lower():
                    return playlist['id']
            if playlists['next']:
                playlists = self.sp.next(playlists)
            else:
                playlists = None
        
        return None
    
    def get_playlist_name_by_id(self, playlist_id: str):
        playlist = self.sp.playlist(playlist_id)
        return playlist['name']

    def get_playlist_items(self, playlist_id: str):
        all_items = []
        results = self.sp.playlist_items(playlist_id, fields='items(track(name, artists(name), id, external_ids(isrc))), next')

        while results:
            all_items.extend(results['items'])
            if results['next']:
                results = self.sp.next(results)
            else:
                break

        return all_items