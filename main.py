from pydub import AudioSegment
import numpy as np

def split_audio(input_audio_file, output_directory):
    # Load the input audio file
    audio = AudioSegment.from_file(input_audio_file)

    # Calculate the duration of the input audio in milliseconds
    audio_duration = len(audio)

    # Define the desired segment duration in milliseconds (5 minutes)
    segment_duration = 5 * 60 * 1000

    # Calculate the number of segments required
    num_segments = int(np.ceil(audio_duration / segment_duration))

    # Create and save each segment
    for i in range(num_segments):
        start_time = i * segment_duration
        end_time = min((i + 1) * segment_duration, audio_duration)
        segment = audio[start_time:end_time]

        # Save the segment to the output directory
        segment.export(f"{output_directory}/segment_{i+1}.mp3", format="mp3")

    print("Operation complete. Audio file split into segments.")

input_audio_file = r"C:\Users\User\Downloads\GC-10 - Progress of Reform in Germany.mp3"  # Replace with your input audio file path
output_directory = r"C:\Users\User\Documents\AudioSlice-GC-Reading"   # Replace with your desired output directory

# Create the output directory if it doesn't exist`
import os
os.makedirs(output_directory, exist_ok=True)

split_audio(input_audio_file, output_directory)
