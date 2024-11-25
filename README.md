Hier ist ein Beispiel für eine anonymisierte `README.md`-Datei für dein GitHub-Repository:


# Podcast Downloader

Ein einfaches Python-Skript, um MP3-Dateien von Podcasts zu extrahieren und herunterzuladen. Dieses Skript ist speziell für Seiten geeignet, die auf der Podigee-Plattform gehostet werden.

## Funktionsweise

Das Skript:
1. Ruft die HTML-Seite der Podcast-Episode ab.
2. Extrahiert die MP3-URL aus den Meta-Tags der Seite.
3. Lädt die MP3-Datei herunter und speichert sie lokal.

## Voraussetzungen

- Python 3.x
- Die folgenden Python-Bibliotheken:
  - `requests`
  - `beautifulsoup4`

Installiere die Bibliotheken mit:

```bash
pip install requests beautifulsoup4
```

## Nutzung

1. Klone das Repository:
   ```bash
   git clone https://github.com/your-username/podcast-downloader.git
   cd podcast-downloader
   ```

2. Bearbeite die `page_url`-Variable im Skript und ersetze sie mit der URL der gewünschten Podcast-Episode:
   ```python
   page_url = "https://example-podcast.podigee.io/episode-id"
   ```

3. Führe das Skript aus:
   ```bash
   python podcast_downloader.py
   ```

4. Die MP3-Datei wird in das aktuelle Verzeichnis heruntergeladen.

## Beispiel

Für eine Podcast-Episode unter der URL:

```
https://example-podcast.podigee.io/42-die-zukunft-des-podcasting
```

wird die MP3-Datei heruntergeladen und unter `podcast_episode.mp3` gespeichert.

## Hinweise

- Das Skript ist nur für den persönlichen Gebrauch bestimmt.
- Bitte stelle sicher, dass der Download der Inhalte mit den Nutzungsbedingungen der Plattform und geltendem Recht übereinstimmt.
- Dieses Projekt unterstützt nur öffentlich zugängliche Episoden.

## Lizenz

Dieses Projekt ist unter der [MIT-Lizenz](LICENSE) lizenziert.


 