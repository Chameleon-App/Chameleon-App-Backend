class ColorConvertor:
    @staticmethod
    def rgb_to_hex(r: int, g: int, b: int):
        return "#{:02x}{:02x}{:02x}".format(r, g, b)
