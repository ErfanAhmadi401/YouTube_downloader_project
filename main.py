from src.downloader import YouTubeDownloader
from src.dependencies import DependencyChecker
from src.quality import QualitySelector


def main():

    if not DependencyChecker.check():
        return

    url = input("Enter YouTube URL: ").strip()

    downloader = YouTubeDownloader()

    info = downloader.get_info(url)

    qualities = QualitySelector.show(info["formats"])

    quality = QualitySelector.choose(qualities)

    print(f"Selected quality: {quality}p")
    
    downloader.download(url, quality)

    print("Download finished ✔")


if __name__ == "__main__":
    main()