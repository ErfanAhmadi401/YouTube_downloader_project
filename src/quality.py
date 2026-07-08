class QualitySelector:

    @staticmethod
    def show(formats):
        qualities = []

        for fmt in formats:
            height = fmt.get("height")
            ext = fmt.get("ext")

            if (
                height
                and ext != "mhtml"
                and height not in qualities
            ):
                qualities.append(height)

        qualities.sort()

        print("\nAvailable qualities:")

        for index, quality in enumerate(qualities, start=1):
            print(f"{index}. {quality}p")

        return qualities

    @staticmethod
    def choose(qualities):

        while True:
            try:
                choice = int(input("\nChoose quality: "))

                if 1 <= choice <= len(qualities):
                    return qualities[choice - 1]

                print("Invalid choice")

            except ValueError:
                print("Enter a number")
