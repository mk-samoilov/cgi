"""
Module with basic widget
"""

from ..stylesheet import Style
from .._default_styles import Border


class BaseWidgetDefaultStyle(Style):
    cursor_select_border = Border # None or border style class

    occupied_cells = (1, 1) # 1x1 widget occupies cells


class BaseWidget:
    def __init__(self, style: Style):
        self.style = style if style else BaseWidgetDefaultStyle

    def update(self):
        pass
