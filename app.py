import time
import csv
import os
import re

class ConcertRecorder:
    def __init__(self, concert_name):
        self.concert_name = concert_name
        self.songs = []
        self.start_time = None
        self.song_starts = []
        self.running = False

    def start_concert(self):
        self.start_time = time.time()
        self.running = True
        # Add date and time to concert name
        self.concert_name += " - " + time.strftime("%Y-%m-%d %H:%M:%S")

    def start_song(self):
        if self.running:
            song_name = f"Track {len(self.songs) + 1}"
            self.songs.append(song_name)
            elapsed_time = time.time() - self.start_time
            timecode = time.strftime('%H:%M:%S', time.gmtime(elapsed_time))
            self.song_starts.append((song_name, timecode))

    def stop_concert(self):
        if self.running:
            self.running = False

    def export_concert(self):
        if len(self.song_starts) == 0:
            return
        
        # Sanitize the concert name
        sanitized_name = re.sub(r'[^\w\s-]', '', self.concert_name)
        sanitized_name = sanitized_name.strip().replace(' ', '_')
        
        filename = sanitized_name + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['Song', 'Timecode'])
            for song, timecode in self.song_starts:
                csvwriter.writerow([song, timecode])

if __name__ == '__main__':
    concert_name = input("Enter concert name: ")
    concert_recorder = ConcertRecorder(concert_name)

    while True:
        user_input = input("Enter command (start, song, stop, export, quit): ")
        if user_input == "start":
            concert_recorder.start_concert()
            print("Concert started.")
        elif user_input == "song":
            concert_recorder.start_song()
            print("Song started.")
        elif user_input == "stop":
            concert_recorder.stop_concert()
            print("Concert stopped.")
        elif user_input == "export":
            concert_recorder.export_concert()
            print("Concert exported.")
        elif user_input == "quit":
            break
        else:
            print("Invalid command.")
