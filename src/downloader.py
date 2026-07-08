from pathlib import Path
from src.network import NetworkManager
from yt_dlp import YoutubeDL


class YouTubeDownloader:
    def __init__(self):
        self.network = NetworkManager()
        self.network.clean_unsupported_proxies()
        self.download_path = Path("downloads")
        self.download_path.mkdir(exist_ok=True)

    def download(self, url: str):
        options = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "outtmpl": str(self.download_path / "%(title)s.%(ext)s"),
            "cookiesfrombrowser": ("chrome",),
            "remote_components": ["ejs:github"],
        }

        with YoutubeDL(options) as ydl:
            ydl.download([url])
