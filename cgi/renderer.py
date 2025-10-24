from .stylesheet import Style

from ._default_styles import WidgetsGridDefaultStyle


class WidgetsGrid:
    def __init__(self, style: Style):
        self.style = style if style else WidgetsGridDefaultStyle

        self.widgets_map = [[None] * self.style.grid_size[1] for _ in range(self.style.grid_size[0])]

    def draw_widget(self, position: tuple[int, int] = (0, 0), rewrite: bool = True):
        if position[0] <= self.style.grid_size[0] and position[1] <= self.style.grid_size[1]:
            if (not self.style.grid_size[position[0]][position[1]]) and not rewrite:
                raise Exception("[2.2] Position is occupied")
        else:
            raise Exception("[2.1] Selected position are outside abroad")
