class Rect:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def intersect(self, rect: 'Rect') -> bool:
        x_s = self.x
        x_e = self.x + self.width
        x_s_ = rect.x
        x_e_ = rect.x + rect.width
        y_s = self.y
        y_e = self.y + self.height
        y_s_ = rect.y
        y_e_ = rect.y + rect.height
        if (x_s > x_s_) and (x_e > x_e_) and (x_e_ > x_s):
            if (y_s > y_s_) and (y_e > y_e_) and (y_e_ > y_s):
                return True
            if (y_s < y_s_) and (y_e < y_e_) and (y_e > y_s_):
                return True
        if (x_s < x_s_) and (x_e < x_e_) and (x_s_ < x_e):
            if (y_s > y_s_) and (y_e > y_e_) and (y_e_ > y_s):
                return True
            if (y_s < y_s_) and (y_e < y_e_) and (y_e > y_s_):
                return True
        return False
