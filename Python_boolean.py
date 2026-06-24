genre = "lo-fi"
bpm = 136

# Match target running pace to the beats per minute.
is_running_song = bpm >= 150 and bpm <= 180
print("Are the beats per minute between 150 and 180? " + str(is_running_song))

# Count alternative spellings of lo-fi as a single genre.
is_lo_fi = genre == "lo-fi" or genre == "low-fi" or genre == "lofi"
print("Is the genre any of the spellings of lo-fi? " + str(is_lo_fi))

# Chill background tunes help maintain focus.
is_study_song = is_lo_fi and bpm < 100
if is_study_song:
    print("This slow, lo-fi song is perfect for studying!")

# Don't play activity-specific songs at other times of the day.
if not is_study_song and not is_running_song:
    print("This is not one of my study or running songs.") 
