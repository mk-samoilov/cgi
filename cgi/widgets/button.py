from ..stylesheet import Style
from .._default_styles import Border


class ButtonWidgetStyle(Style):
    cursor_select_border = Border()
    occupied_cells = (1, 1)
    

class ButtonWidget:
    def __init__(self, label: str = "Button", callback = None, style: Style = None, hoverable: bool = True):
        self.label = label
        self.callback = callback
        self.style = style if style else ButtonWidgetStyle()
        self.hoverable = hoverable
        self.pressed = False
        
    def render(self, width: int, height: int, is_selected: bool):
        lines = []
        
        label_display = self.label[:width]
        
        center_line = height // 2
        
        for i in range(height):
            if i == center_line:
                prefix = "[X] " if self.pressed else "[ ] "
                content = prefix + label_display
                lines.append(content.center(width))
            else:
                lines.append(" " * width)
                
        return lines
        
    def on_click(self):
        self.pressed = True
        if self.callback:
            self.callback()
            
    def update(self):
        if self.pressed:
            self.pressed = False
