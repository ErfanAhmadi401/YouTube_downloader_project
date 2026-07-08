from pathlib import Path

from yt_dlp import YoutubeDL


class YouTubeDownloader:
    def __init__(self):
        self.download_path = Path("downloads")
        self.download_path.mkdir(exist_ok=True)

    def download(self, url: str):
        options = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "outtmpl": str(self.download_path / "%(title)s.%(ext)s"),
        }

        with YoutubeDL(options) as ydl:
            ydl.download([url])
