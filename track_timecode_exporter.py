import csv

class TrackTimecodeExporter:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.song_dict = {}
        self.parse_csv()
    
    def parse_csv(self):
        with open(self.csv_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                song_name = row['Song']
                timecode = row['Timecode']
                self.song_dict[song_name] = timecode
    
    def export_timecodes(self, output_path):
        with open(output_path, 'w') as txt_file:
            for song_name, timecode in self.song_dict.items():
                new_song_name = input(f"Enter new name for {song_name} (or leave blank to keep current name): ")
                if new_song_name:
                    song_name = new_song_name
                txt_file.write(f"{timecode} - {song_name}\n")
