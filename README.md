# Motivational Video Bot

## Overview
Motivational Video Bot is a simple Python script that generates motivational videos by combining random quotes, images, and audio. The script utilizes a collection of motivational quotes, images, and audio files to create unique videos.

## Prerequisites
- Python 3.x

## Project Structure
- **assets/**
  - **audio/**: Contains audio files for the videos.
  - **images/**: Holds image files for the videos.
  - **quotes/**: Stores JSON files with motivational quotes.

- **exports/**: Output directory where generated videos will be saved.

## Usage
1. Clone the repository.
2. Ensure the required Python modules are installed.
3. Run the script (`main.py`).
4. Follow the on-screen instructions:
   - Enter the number of videos you want to create (between 1 and 10).
   - The script will randomly select quotes, images, and audio to create unique videos.

## Output
Generated videos will be saved in the **exports/** directory with filenames like `video1.mp4`, `video2.mp4`, etc.

## Notes
- The script automatically creates the **exports/** directory if it does not exist.
- Ensure that the audio, image, and quote directories in the **assets/** folder contain the necessary files.
