from ..stylesheet import Style
from .._default_styles import Border


class InfoPanelWidgetStyle(Style):
    cursor_select_border = Border()
    occupied_cells = (1, 1)
    

class InfoPanelWidget:
    def __init__(self, title: str = "Info", items: dict = None, style: Style = None):
        self.title = title
        self.items = items if items else {}
        self.style = style if style else InfoPanelWidgetStyle()
        
    def set_item(self, key: str, value: str):
        self.items[key] = value
        
    def render(self, width: int, height: int, is_selected: bool):
        lines = []
        
        title_line = self.title[:width].center(width)
        lines.append(title_line)
        
        if height > 1:
            lines.append("─" * width)
        
        for key, value in list(self.items.items())[:height - 2]:
            item_str = f"{key}: {value}"
            lines.append(item_str[:width].ljust(width))
            
        while len(lines) < height:
            lines.append(" " * width)
            
        return lines[:height]
        
    def update(self):
        pass

