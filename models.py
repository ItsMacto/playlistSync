import sqlite3

class Playlist:
    def __init__(self, db_manager):
        self.db = db_manager

    def create_playlist(self, spotify_id, spotify_name):
        query = """
        INSERT INTO playlists (spotify_id, spotify_name)
        VALUES (?, ?)
        """
        try:
            self.db.execute_query(query, [spotify_id, spotify_name])
        except sqlite3.IntegrityError as e:
            print(f"Error inserting playlist: {e}")
            return None
        return self.db.cursor.lastrowid

    def get_playlist_by_id(self, playlist_id):
        query = "SELECT * FROM playlists WHERE id = ?"
        return self.db.fetchone(query, [playlist_id])

    def get_playlist_by_spotify_id(self, spotify_id):
        query = "SELECT * FROM playlists WHERE spotify_id = ?"
        return self.db.fetchone(query, [spotify_id])

    def update_playlist(self, playlist_id, spotify_name=None):
        if not spotify_name:
            raise ValueError("Nothing to update")

        fields = []
        params = []
        if spotify_name:
            fields.append("spotify_name = ?")
            params.append(spotify_name)

        query = f"UPDATE playlists SET {', '.join(fields)} WHERE id = ?"
        params.append(playlist_id)
        self.db.execute_query(query, params)


class PlaylistItem:
    def __init__(self, db_manager):
        self.db = db_manager

    def add_item(self, playlist_id, track_name, artist_name, album_name, spotify_id, isrc):
        query = """
        INSERT INTO playlist_items (playlist_id, track_name, artist_name, album_name, spotify_id, isrc)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        try:
            self.db.execute_query(query, [playlist_id, track_name, artist_name, album_name, spotify_id, isrc])
        except sqlite3.IntegrityError as e:
            print(f"Error inserting playlist item: {e}")
            return None
        return self.db.cursor.lastrowid

    def get_items_by_playlist_id(self, playlist_id):
        query = "SELECT * FROM playlist_items WHERE playlist_id = ?"
        return self.db.fetchall(query, [playlist_id])

    def update_item(self, item_id, track_name=None, artist_name=None, album_name=None, spotify_id=None, isrc=None):
        if not track_name and not artist_name and not album_name and not spotify_id and not isrc:
            raise ValueError("Nothing to update")

        fields = []
        params = []
        if track_name:
            fields.append("track_name = ?")
            params.append(track_name)
        if artist_name:
            fields.append("artist_name = ?")
            params.append(artist_name)
        if album_name:
            fields.append("album_name = ?")
            params.append(album_name)
        if spotify_id:
            fields.append("spotify_id = ?")
            params.append(spotify_id)
        if isrc:
            fields.append("isrc = ?")
            params.append(isrc)

        query = f"UPDATE playlist_items SET {', '.join(fields)} WHERE id = ?"
        params.append(item_id)
        self.db.execute_query(query, params)