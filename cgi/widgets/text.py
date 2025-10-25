from ..stylesheet import Style
from .._default_styles import Border


class TextWidgetStyle(Style):
    cursor_select_border = Border()
    occupied_cells = (1, 1)
    align = "left"


class TextWidget:
    def __init__(self, text: str = "", style: Style = None, hoverable: bool = True):
        self.text = text
        self.style = style if style else TextWidgetStyle()
        self.hoverable = hoverable
        
    def set_text(self, text: str):
        self.text = text
        
    def render(self, width: int, height: int, is_selected: bool):
        lines = []
        words = self.text.split()
        current_line = ""
        
        for word in words:
            if len(current_line) + len(word) + 1 <= width:
                current_line += word + " "
            else:
                lines.append(current_line.rstrip())
                current_line = word + " "
                
        if current_line:
            lines.append(current_line.rstrip())
            
        while len(lines) < height:
            lines.append("")
            
        result_lines = []
        for line in lines[:height]:
            if self.style.align == "center":
                result_lines.append(line.center(width))
            elif self.style.align == "right":
                result_lines.append(line.rjust(width))
            else:
                result_lines.append(line.ljust(width))
                
        return result_lines
        
    def update(self):
        pass
