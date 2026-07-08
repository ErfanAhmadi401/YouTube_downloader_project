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
            print("Missing dependencies:")
            for item in missing:
                print(f"- {item}")

            print("\nPlease install missing dependencies and try again.")
            return False

        print("All dependencies are installed ✓")
        return True