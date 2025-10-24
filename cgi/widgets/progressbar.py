from ..stylesheet import Style
from .._default_styles import Border


class ProgressBarWidgetStyle(Style):
    cursor_select_border = Border()
    occupied_cells = (1, 2)
    fill_char = "█"
    empty_char = "░"
    

class ProgressBarWidget:
    def __init__(self, progress: float = 0.0, label: str = "", style: Style = None):
        self.progress = max(0.0, min(1.0, progress))
        self.label = label
        self.style = style if style else ProgressBarWidgetStyle()
        
    def set_progress(self, progress: float):
        self.progress = max(0.0, min(1.0, progress))
        
    def render(self, width: int, height: int, is_selected: bool):
        lines = []
        
        fill_char = self.style.fill_char if hasattr(self.style, "fill_char") else "█"
        empty_char = self.style.empty_char if hasattr(self.style, "empty_char") else "░"
        
        bar_width = width - 10
        filled_width = int(bar_width * self.progress)
        empty_width = bar_width - filled_width
        
        percentage = f"{int(self.progress * 100):3d}%"
        
        bar = fill_char * filled_width + empty_char * empty_width
        progress_line = f"{percentage} {bar}"
        
        label_line = self.label[:width].center(width)
        
        center_start = (height - 2) // 2
        
        for i in range(height):
            if i == center_start and self.label:
                lines.append(label_line)
            elif i == center_start + 1 or (i == center_start and not self.label):
                lines.append(progress_line.ljust(width))
            else:
                lines.append(" " * width)
                
        return lines
        
    def update(self):
        pass

