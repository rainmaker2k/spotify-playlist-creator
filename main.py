
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import spotipy
import sys
import codecs

scope = "user-library-read playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def create_playlist(name):
    scope = "playlist-modify-public"
    user_id = sp.me()['id']
    playlist = sp.user_playlist_create(user_id, name)
    return playlist

def get_first_track_from_results(query):
    result = sp.search(query)
    if (len(result['tracks']['items']) > 0):
        track = result['tracks']['items'][0]
        return track['id']
    
    return None

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        tids = []

        with codecs.open(filename, encoding='utf-8') as f:
            for l in f:
                id = get_first_track_from_results(l.rstrip())
                if (id is not None):
                    tids.append(id)
        
        new_playlist = create_playlist(filename)
        sp.playlist_add_items(new_playlist['id'], tids)

        f.close()

if __name__ == "__main__":
    main()