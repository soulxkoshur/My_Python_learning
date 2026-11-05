import requests
def main():
    print("Welcome to The Art Institute of Chicago")
    artist = input("Enter an artist name: ")
    try:
        response = requests.get("https://api.artic.edu/api/v1/artworks/search?q=", params={"q": artist})
        response.raise_for_status()
    except requests.HTTPError:
        print("couldn't complete request")
        return
    content = response.json()
    for artwork in content['data']:
        print(f"#* {artwork['title']}")

def get_artworks(query, limit):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            params={"q": query, "limit": limit}
        )
        response.raise_for_status()
    except requests.HTTPError:
        return []
    content = response.json()
    return content['data']


main()
