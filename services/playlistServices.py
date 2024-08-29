from models import PlaylistItem, Playlist

def create_playlist(db_manager, spotify_id, spotify_name):
    """
    Creates a new playlist in the database.

    :param db_manager: The DatabaseManager instance to interact with the database.
    :param spotify_id: The Spotify ID of the playlist.
    :param spotify_name: The name of the playlist.
    :return: The ID of the newly created playlist.
    """
    if Playlist(db_manager).get_playlist_by_spotify_id(spotify_id) is not None:
        print("Playlist already exists", spotify_id)
        # print(Playlist(db_manager).get_playlist_by_spotify_id(spotify_id)['spotify_name'])
        return Playlist(db_manager).get_playlist_by_spotify_id(spotify_id)['id']
    
    return Playlist(db_manager).create_playlist(spotify_id, spotify_name)


def save_playlist_items(db_manager, playlist_id, playlist_items):
    """
    Saves a list of playlist items to the database.

    :param db_manager: The DatabaseManager instance to interact with the database.
    :param playlist_id: The ID of the playlist in the local database.
    :param playlist_items: A list of playlist items fetched from the Spotify API.
    """
    
    if Playlist(db_manager).get_playlist_by_id(playlist_id) is None:
        print("Playlist not found", playlist_id)
        return False
    
    
    
    for item in playlist_items:
        track = item['track']
        # print(track)
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        album_name = track['album']['name']
        spotify_id = track['id']
        # isrc = track.get('external_ids', None)
        isrc = track['external_ids']['isrc']
        # print(track_name, artist_name, album_name, spotify_id, isrc)   

        PlaylistItem(db_manager).add_item(playlist_id, track_name, artist_name, album_name, spotify_id, isrc)

    return True


def get_playlist_items(db_manager, playlist_id):
    """
    Retrieves all items from a playlist in the database.

    :param db_manager: The DatabaseManager instance to interact with the database.
    :param playlist_id: The ID of the playlist in the local database.
    :return: A list of playlist items.
    """
    return PlaylistItem(db_manager).get_items_by_playlist_id(playlist_id)