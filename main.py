from src.downloader import YouTubeDownloader
from src.dependencies import DependencyChecker


def main():

    if not DependencyChecker.check():
        return

    url = input("Enter YouTube URL: ").strip()

    downloader = YouTubeDownloader()
    downloader.download(url)

    print("Download finished ✔")


if __name__ == "__main__":
    main()
