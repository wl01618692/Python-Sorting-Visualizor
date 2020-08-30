class Data:
    # Total of data to sort
    data_count = 40

    def __init__(self, value):
        self.value = value
        self.set_color()

    def set_color(self, rgba = None):
        if not rgba:
            rgba = (0,
                    1 - self.value / (self.data_count * 2),
                    self.value / (self.data_count * 2) + 0.5,
                    1)
        self.color = rgba
