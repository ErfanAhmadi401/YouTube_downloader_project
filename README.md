🎬 YouTube Downloader (Python)

A simple YouTube video downloader built with Python using yt-dlp.

⚡ Features
Download YouTube videos in highest quality
Auto merge video + audio (MP4)
Simple command-line interface
Lightweight and fast
📦 Requirements

Make sure you have Python installed.

Install dependencies:

pip install yt-dlp

For best results (recommended):

Install FFmpeg for merging audio/video
Install FFmpeg:
Windows: Add FFmpeg to PATH
Linux:
sudo apt install ffmpeg
🚀 How to Use

Run the script:

python downloader.py

Then paste the YouTube link:

Enter YouTube URL: https://www.youtube.com/watch?v=example

The video will be downloaded automatically 🎉

🧠 How It Works

This project uses yt-dlp, a powerful tool that extracts video/audio streams from YouTube and downloads them in best available quality.

📁 Project Structure
project/
│
├── downloader.py
└── README.md
🛠️ Code Example
from yt_dlp import YoutubeDL

def download_video(url):
    options = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'outtmpl': '%(title)s.%(ext)s'
    }

    with YoutubeDL(options) as ydl:
        ydl.download([url])

url = input("Enter YouTube URL: ")
download_video(url)
📌 Notes
Use only for personal or legal content
Some videos may be restricted or unavailable
Requires internet connection (VPN may be needed in some regions)
📜 License

This project is open-source and free to use for educational purposes.
