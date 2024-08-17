-- Create the playlists table
CREATE TABLE IF NOT EXISTS playlists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    spotify_id INTEGER,
    spotify_name TEXT,
);

-- Create the playlist_items table
CREATE TABLE IF NOT EXISTS playlist_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    playlist_id INTEGER,
    track_name TEXT NOT NULL,
    artist_name TEXT, -- more than one artist future
    album_name TEXT,
    spotify_id INTEGER,
    isrc TEXT,
    FOREIGN KEY (playlist_id) REFERENCES playlists(id) ON DELETE CASCADE
);