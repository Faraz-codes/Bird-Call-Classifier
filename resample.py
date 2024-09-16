#Do not run this code, it has been utilized to transform audio files already
import os
from pydub import AudioSegment as am

directory = "data/Parsed_Capuchinbird_Clips"
for filename in os.scandir(directory):
    sound = am.from_file(filename, format='wav', frame_rate=44100)
    sound = sound.set_frame_rate(16000)
    sound.export(filename, format='wav')

directory2 = "data/Parsed_Not_Capuchinbird_Clips"
for filename in os.scandir(directory2):
    sound = am.from_file(filename, format='wav', frame_rate=44100)
    sound = sound.set_frame_rate(16000)
    sound.export(filename, format='wav')
