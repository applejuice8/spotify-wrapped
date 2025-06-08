# Spotify Streaming Stats Analyzer

This script analyzes your Spotify streaming history and displays:

- Total listening time for the current year
- Your top N most-listened-to songs
- Your top N most-listened-to artists

## 📁 How to Use

1. [Request your Spotify data](https://www.spotify.com/account/privacy/) from the Privacy settings page.
2. Once you receive the `my_spotify_data.zip` file, unzip it.
3. Inside the `Spotify Account Data` folder, find the file named `StreamingHistory_music_0.json`.
4. Rename it to `StreamingHistory.json`.
5. Move `StreamingHistory.json` to the same folder as this script.
6. Run the script:

```bash
python streaming_stats.py
```

4. Enter how many top songs and artists you'd like to see.

## 📦 Requirements

- Python 3.7+
- No external libraries needed — only built-in Python modules.

## 📂 Output Example

```
🎧 Total Minutes Listened: 1234.5 minutes

🎵 Top Songs:
1. Song A - 120.3 min
2. Song B - 110.0 min

🎤 Top Artists:
1. Artist A - 220.3 min
2. Artist B - 180.4 min
```

## 📝 Notes

- The script only includes data from the **current year**.
- Make sure your JSON file contains fields like `trackName`, `artistName`, `msPlayed`, and `endTime`.

## 🧑‍💻 Author

Created by Colin Leong
