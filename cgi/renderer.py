from .stylesheet import Style

from ._default_styles import WidgetsGridDefaultStyle


class WidgetsGrid:
    def __init__(self, style: Style):
        self.style = style if style else WidgetsGridDefaultStyle
