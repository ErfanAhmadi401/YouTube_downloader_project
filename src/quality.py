class QualitySelector:

    STANDARD_QUALITIES = [
        144,
        240,
        360,
        480,
        720,
        1080,
        1440,
        2160,
    ]

    @staticmethod
    def normalize_quality(height):
        """
        تبدیل کیفیت واقعی به کیفیت نمایشی
        """

        return min(
            QualitySelector.STANDARD_QUALITIES,
            key=lambda q: abs(q - height)
        )

    @staticmethod
    def format_size(size):

        if not size:
            return "Unknown size"

        mb = size / (1024 * 1024)

        return f"{mb:.2f} MB"

    @staticmethod
    def show(formats):

        qualities = {}


        for fmt in formats:
            
            print(
                fmt.get("format_id"),
                fmt.get("height"),
                fmt.get("vcodec"),
                fmt.get("tbr"),
                fmt.get("filesize")
            )

            height = fmt.get("height")


            if (
                not height
                or fmt.get("vcodec") == "none"
                or fmt.get("ext") == "mhtml"
            ):
                continue


            size = (
                fmt.get("filesize")
                or fmt.get("filesize_approx")
            )


            item = {
                "quality": height,
                "format_id": fmt.get("format_id"),
                "size": size
            }


            if height not in qualities:

                qualities[height] = item

            else:

                old = qualities[height]

                # اگر جدید حجم دارد و قبلی ندارد
                if not old["size"] and size:

                    qualities[height] = item

                # اگر هر دو حجم دارند، بزرگتر را نگه دار
                elif size and old["size"]:

                    if size > old["size"]:
                        qualities[height] = item



        result = list(qualities.values())


        result.sort(
            key=lambda x: x["quality"]
        )


        print("\nAvailable qualities:")


        for index, item in enumerate(result, start=1):

            if item["size"]:

                size = item["size"] / (1024 * 1024)
                text = f"{size:.2f} MB"

            else:

                text = "Unknown size"


            print(
                f"{index}. {item['quality']}p - {text}"
            )


        return result

    @staticmethod
    def choose(qualities):

        while True:

            try:

                choice = int(
                    input("\nChoose quality: ")
                )

                if 1 <= choice <= len(qualities):

                    return qualities[choice - 1]

                print("Invalid choice")

            except ValueError:

                print("Enter a number")
