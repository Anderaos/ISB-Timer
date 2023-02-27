# Instrumental Sesc Brasil - Livestream Tools

## Description
This is a small command line tool to help tracking timecodes for each individual track during the Instrumental Sesc Brasil live broadcast and exporting it for the Youtube video description.

## Instructions for the Timecode Recorder
1. Make sure you have Python installed. You can download it in https://www.python.org/downloads/
2. Clone or download the repo.
3. Open a command prompt, navigate to the file folder and run `python main.py`.
4. Give the Concert a name. It's usually the artist name. Date and time will be added automatically.
5. Enter `start` to start tracking the overall time. This must be as synchronized as possible with the Youtube livestream start.
6. Enter `song` to recorded a timecode for a given song.
7. Enter `stop` to end the time recording.
8. Enter `export` to save a .csv file in the app folder with the timecodes and a .txt file for the Youtube description.
9. Enter `quit` to end the script.

## To do
- [ ] Add a graphical user interface.