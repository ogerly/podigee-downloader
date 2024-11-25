import requests
from bs4 import BeautifulSoup

def extract_mp3_url(page_url):
    try:
        # HTML der Seite abrufen
        response = requests.get(page_url)
        response.raise_for_status()
        
        # HTML parsen
        soup = BeautifulSoup(response.text, "html.parser")
        
        # MP3-URL aus Meta-Tags suchen
        mp3_url = None
        for tag in soup.find_all("meta"):
            if tag.get("content") and "audio.podigee-cdn.net" in tag["content"]:
                mp3_url = tag["content"]
                break
        
        if not mp3_url:
            raise Exception("Keine MP3-URL gefunden.")
        
        return mp3_url
    except Exception as e:
        print(f"Fehler beim Extrahieren der MP3-URL: {e}")
        return None

def download_mp3(mp3_url, output_filename):
    try:
        # MP3-Datei herunterladen
        response = requests.get(mp3_url, stream=True)
        response.raise_for_status()
        
        # Datei speichern
        with open(output_filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"Podcast erfolgreich heruntergeladen: {output_filename}")
    except Exception as e:
        print(f"Fehler beim Herunterladen: {e}")

# Beispiel-URL // https://example-podcast.podigee.io/42-die-zukunft-des-podcasting
page_url = "https://example-podcast.podigee.io/episode-id"

# Extrahiere MP3-URL und lade die Datei herunter
mp3_url = extract_mp3_url(page_url)
if mp3_url:
    download_mp3(mp3_url, "podcast_episode.mp3")
