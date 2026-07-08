import shutil


class DependencyChecker:

    REQUIRED_TOOLS = {
        "ffmpeg": "FFmpeg",
        "deno": "Deno",
    }

    @classmethod
    def check(cls):
        missing = []

        for command, name in cls.REQUIRED_TOOLS.items():
            if shutil.which(command) is None:
                missing.append(name)

        if missing:
            from src.installer import DependencyInstaller

            print("Missing dependencies:")

            for item in missing:
                print("-", item)
                DependencyInstaller.show_guide(item)

            return False

        return True
