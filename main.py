from src.downloader import YouTubeDownloader


def main():
    url = input("Enter YouTube URL: ").strip()

    downloader = YouTubeDownloader()
    downloader.download(url)

    print("Download finished ✔")


if __name__ == "__main__":
    main()