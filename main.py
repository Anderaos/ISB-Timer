import os
from concert_recorder import ConcertRecorder
from track_timecode_exporter import TrackTimecodeExporter

def main():
    concert_name = input("Enter concert name: ")
    recorder = ConcertRecorder(concert_name)

    while True:
        user_input = input("Enter command (start, song, stop, export, quit): ")

        if user_input == "start":
            recorder.start_concert()
            print("Concert started.")

        elif user_input == "song":
            recorder.start_song()
            print("Song started.")

        elif user_input == "stop":
            recorder.stop_concert()
            print("Concert stopped.")

        elif user_input == "export":
            recorder.export_concert()
            print("Concert exported.")

            csv_path = recorder.concert_name.replace(' ', '_') + ".csv"
            exporter = TrackTimecodeExporter(csv_path)

            output_path = os.path.splitext(csv_path)[0] + ".txt"
            exporter.export_timecodes(output_path)

            print(f"Timecodes exported to {output_path}.")

        elif user_input == "quit":
            break

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
