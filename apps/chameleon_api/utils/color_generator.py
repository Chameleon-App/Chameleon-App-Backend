import random

import numpy as np

from apps.chameleon_api.utils.color_convertor import ColorConvertor
from apps.chameleon_api.utils.disntance_calculator import DistanceCalculator


class Color:
    def __init__(self, r=None, g=None, b=None, color_obj=None, color_dict=None):
        if color_obj is None and color_dict is None:
            self.r = r
            self.g = g
            self.b = b
        elif color_obj is not None:
            self.r, self.g, self.b = ColorConvertor.hex_to_rgb(color_obj.hex)
        elif color_dict is not None:
            self.r, self.g, self.b = ColorConvertor.hex_to_rgb(color_dict["hex"])

    def __str__(self):
        return f"Color({self.r},{self.g},{self.b})"

    def get_rgb_components(self) -> (int, int, int):
        return self.r, self.g, self.b

    def get_hsv_components(self) -> (float, float, float):
        return ColorConvertor.rgb_to_hsv(self.r, self.g, self.b)

    def get_np_from_components(self) -> np.array:
        return np.array([self.r, self.g, self.b])


class ColorGenerator:
    def __init__(self, repo):
        self.repo = repo

    def generate_daily_colors(self):
        color_p1 = self.repo.get_random_color()
        color_1 = Color(color_obj=color_p1)

        generate_method = random.choice(
            [self.generate_triangle_method, self.generate_triangle_method]
        )

        color_2, color_3 = generate_method(color_1)

        color_p2 = self.map_color_to_pantone(color_2)
        color_p3 = self.map_color_to_pantone(color_3)

        return color_p1, color_p2, color_p3

    @staticmethod
    def generate_triangle_method(base_color: Color):
        h, s, v = base_color.get_hsv_components()
        hue_shift1 = (h + 1 / 3) % 1
        hue_shift2 = (h + 2 / 3) % 1

        r, g, b = ColorConvertor.hsv_to_rgb(hue_shift1, s, v)
        additional_color_1 = Color(r, g, b)

        r, g, b = ColorConvertor.hsv_to_rgb(hue_shift2, s, v)
        additional_color_2 = Color(r, g, b)

        return additional_color_1, additional_color_2

    @staticmethod
    def generate_complimentary_method(base_color: Color):
        h, s, v = base_color.get_hsv_components()
        complementary_hue1 = (h + 150) % 360
        complementary_hue2 = (h + 210) % 360

        # TODO: add return result of colors :)

    def map_color_to_pantone(self, base_color):
        prototypes_objects = self.repo.get_all_prototypes()
        prototypes_id = self.find_nearest_colors(
            base_color=base_color, colors=prototypes_objects
        )

        colors_objects = self.repo.get_prototype_colors(prototypes_id)
        return self.find_nearest_colors(
            base_color=base_color, colors=colors_objects, k=1, return_ids=False
        )[0]

    @staticmethod
    def find_nearest_colors(
        base_color: Color, colors, k: int = 10, return_ids: bool = True
    ):
        colors_coords = np.zeros(shape=(len(colors), 3))

        for i, color in enumerate(colors):
            colors_coords[i] = ColorConvertor.hex_to_rgb(color.hex)

        base_color_coords = np.expand_dims(base_color.get_np_from_components(), axis=0)

        dists = DistanceCalculator.compute_euclidean_distance(
            base_color_coords, colors_coords
        )[0]

        closest_ids = dists.argsort()[:k]

        if return_ids:
            return closest_ids

        return np.array(colors)[closest_ids]
