from yt_dlp import YoutubeDL

def download_video(url):
    options = {
        "format": "best",
    }

    with YoutubeDL(options) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    url = input("Enter YouTube URL: ").strip()
    download_video(url)
    print("Download finished ✔")