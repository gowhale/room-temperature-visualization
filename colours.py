from colour import Color


class ColourScale:

    def __init__(self, starting_colour, finishing_colour, resolution):
        self.starting_colour = starting_colour
        self.finishing_colour = finishing_colour
        self.resolution = resolution
        self.colour_scale = self.generate_colours()

    def generate_colours(self):
        start = Color(self.starting_colour)
        end = Color(self.finishing_colour)
        colours = list(start.range_to(end, self.resolution))
        return colours

    def set_max_temp(self, temp):
        self.max_temp = temp

    def set_min_temp(self, temp):
        self.min_temp = temp

    def get_colours(self):
        return self.colour_scale

    def get_tempreture_colours_pigame_format(self, val):
        colour_object = self.get_tempreture_colours(val)
        colour_rgb = (int(colour_object.get_red(
        )*255), int(colour_object.get_green()*255), int(colour_object.get_blue()*255))
        return colour_rgb

    def get_tempreture_colours(self, val):

        max_temp = self.max_temp
        min_temp = self.min_temp
        all_colours = self.colour_scale

        if val < min_temp:
            return all_colours[0]
        if val > max_temp:
            return all_colours[-1]
        else:
            top = max_temp - min_temp
            bottom = val - min_temp
            percentage = bottom/top

            colour_index = int(percentage*len(all_colours)) - 1
            print("Percentage: {}, Colour: {}".format(
                percentage, all_colours[colour_index]))
            return all_colours[colour_index]
