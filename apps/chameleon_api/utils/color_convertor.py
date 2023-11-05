class ColorConvertor:
    @staticmethod
    def rgb_to_hex(r: int, g: int, b: int) -> str:
        return f"{r:02x}{g:02x}{b:02x}"

    @staticmethod
    def hex_to_rgb(hex_str: str) -> (int, int, int):
        return int(hex_str[0:2], 16), int(hex_str[2:4], 16), int(hex_str[4:6], 16)

    @staticmethod
    def rgb_to_hsv(r: int, g: int, b: int) -> (int, int, int):
        r, g, b = r / 255, g / 255, b / 255

        max_value = max(r, g, b)
        min_value = min(r, g, b)

        delta = max_value - min_value

        h = 0

        if delta != 0:
            diff, angle = 0, 0
            if max_value == r:
                diff, angle = g - b, 360
            elif max_value == g:
                diff, angle = b - r, 120
            elif max_value == b:
                diff, angle = r - g, 240
            h = ((60 * (diff / delta) + angle) % 360) / 360

        s = 0 if max_value == 0 else (delta / max_value)
        v = max_value

        return h, s, v

    @staticmethod
    def hsv_to_rgb(h: float, s: float, v: float) -> (int, int, int):
        chroma = v * s
        hue_sector = h * 6

        x = chroma * (1 - abs(hue_sector % 2 - 1))
        m = v - chroma

        r, g, b = 0, 0, 0

        if hue_sector <= 1:
            r, g, b = chroma, x, 0
        elif hue_sector <= 2:
            r, g, b = x, chroma, 0
        elif hue_sector <= 3:
            r, g, b = 0, chroma, x
        elif hue_sector <= 4:
            r, g, b = 0, x, chroma
        elif hue_sector <= 5:
            r, g, b = x, 0, chroma
        elif hue_sector <= 6:
            r, g, b = chroma, 0, x

        r = (r + m) * 255
        g = (g + m) * 255
        b = (b + m) * 255

        r, g, b = int(r), int(g), int(b)

        return r, g, b
