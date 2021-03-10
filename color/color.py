class Color():
    def __init__(self, i, r, g, b):
        self._i = i
        self._r = r
        self._g = g
        self._b = b

    @property
    def sum(self):
        return self._r+self._g+self._b

    def debug_string(self):
        return f"({self._i}) {self._r} {self._g} {self._b} Sum={self._r+self._g+self._b}"


colors = []

i = 0

for r in range(0, 6):
    for g in range(0, 6):
        for b in range(0, 6):
            color = Color(i, r, g, b)
            colors.append(color)
            # print(color.debug_string())
            i += 1

sorted_colors = sorted(colors, key=lambda color: color.sum, reverse=True)

for color in sorted_colors:
    print(color.debug_string())
