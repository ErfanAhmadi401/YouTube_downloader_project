class DependencyInstaller:

    INSTALL_GUIDES = {
        "ffmpeg": {
            "linux": "sudo apt install ffmpeg",
            "windows": "winget install Gyan.FFmpeg",
        },
        "deno": {
            "linux": "curl -fsSL https://deno.land/install.sh | sh",
            "windows": "irm https://deno.land/install.ps1 | iex",
        },
    }

    @classmethod
    def show_guide(cls, dependency):
        dependency = dependency.lower()

        print(f"\nHow to install {dependency}:")

        guides = cls.INSTALL_GUIDES.get(dependency)

        if not guides:
            print("No installation guide available.")
            return

        print("\nLinux:")
        print(guides["linux"])

        print("\nWindows:")
        print(guides["windows"])