from collections import Counter
from datetime import date
import json

# Load streaming history JSON file
with open("StreamingHistory.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Initialize counter
total_minutes = 0
song_counter = Counter()
artist_counter = Counter()

# Get current year
current_year = str(date.today()).split('-')[0]

# Calculate time
for row in data:
    song = row['trackName']
    artist = row['artistName']
    ms_played = row['msPlayed']
    year = row['endTime'].split('-')[0]

    # Ignore data from previous year
    if year == current_year:
        song_counter[song] += ms_played
        artist_counter[artist] += ms_played
        total_minutes += ms_played

# Prompt and validate number of records
while True:
    try:
        num = int(input('How many top songs and artists do you want: '))
        if num > 0:
            if num > len(song_counter):
                print(f'Invalid input. Only {len(song_counter)} songs found in your records.')
            elif num > len(artist_counter):
                print(f'Invalid input. Only {len(artist_counter)} artists found in your records.')
            else:
                break
        else: 
            print('Invalid input. Please enter an integer greater than 0.')
    except ValueError:
        print('Invalid input. Please enter an integer.')

# Top songs and artists
top_songs = song_counter.most_common(num)
top_artists = artist_counter.most_common(num)

# Display results
print(f"\n🎧 Total Minutes Listened: {round(total_minutes / 60000, 1)} minutes")
print("\n🎵 Top Songs:")
for i, (song, time_ms) in enumerate(top_songs, 1):
    print(f"{i}. {song} - {round(time_ms / 60000, 1)} min")

print("\n🎤 Top Artists:")
for i, (artist, time_ms) in enumerate(top_artists, 1):
    print(f"{i}. {artist} - {round(time_ms / 60000, 1)} min")
