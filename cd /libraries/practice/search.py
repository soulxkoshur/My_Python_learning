from museum.artwork import get_artworks
from museum.artist import get_artist

def main():
    x = int(input("To get artist: input 1,\nTo get Artworks: input 2\n"))
    if x == 2:

        artwork = input("Artwork: ")
        artworks = get_artworks(query=artwork, limit=3)
        for artwork in artworks:
            print(f"* {artwork}")
    elif x == 1:
        artist = input("Artist: ")
        artists = get_artist(query=artist, limit=3)
        for artist in artists:
            print(f"# {artist}")
    else:
        print("Not a valid Input")


main()
