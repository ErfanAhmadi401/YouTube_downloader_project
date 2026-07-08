import os


class NetworkManager:
    """
    Manage network configuration before downloading.
    """

    def __init__(self):
        self.removed_proxies = []

    def clean_unsupported_proxies(self):
        """
        Remove proxies that yt-dlp cannot handle.
        """

        unsupported_proxies = [
            "ftp_proxy",
            "FTP_PROXY",
        ]

        for proxy in unsupported_proxies:
            if proxy in os.environ:
                self.removed_proxies.append(proxy)
                os.environ.pop(proxy)

    def show_status(self):
        if self.removed_proxies:
            print(
                f"Removed unsupported proxy settings: {self.removed_proxies}"
            )