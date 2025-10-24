import os
import sys
import msvcrt
import time
from .renderer import WidgetsGrid
from .stylesheet import Style


class Application:
    def __init__(self, widgets: list = None, style: Style = None):
        self.widgets = widgets if widgets else []
        self.renderer = WidgetsGrid(style)
        self.running = False
        self.selected_widget_index = 0
        
    def add_widget(self, widget, position: tuple[int, int]):
        self.widgets.append((widget, position))
        
    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")
        
    def render(self):
        self.clear_screen()
        buffer = self.renderer.render(self.widgets, self.selected_widget_index)
        sys.stdout.write(buffer)
        sys.stdout.flush()
        
    def handle_input(self):
        if msvcrt.kbhit():
            key = msvcrt.getch()
            
            if key == b"\xe0":
                key = msvcrt.getch()
                if key == b"H":
                    self.move_selection(-1, 0)
                elif key == b"P":
                    self.move_selection(1, 0)
                elif key == b"K":
                    self.move_selection(0, -1)
                elif key == b"M":
                    self.move_selection(0, 1)
            elif key == b"\r":
                if self.selected_widget_index < len(self.widgets):
                    widget, _ = self.widgets[self.selected_widget_index]
                    if hasattr(widget, "on_click"):
                        widget.on_click()
            elif key == b"q" or key == b"\x1b":
                self.running = False
                
    def move_selection(self, dy: int, dx: int):
        if len(self.widgets) == 0:
            return
            
        positions = [pos for _, pos in self.widgets]
        current_pos = positions[self.selected_widget_index]
        
        candidates = []
        for idx, pos in enumerate(positions):
            if idx == self.selected_widget_index:
                continue
            
            diff_y = pos[0] - current_pos[0]
            diff_x = pos[1] - current_pos[1]
            
            if dy != 0 and dx == 0:
                if diff_y * dy > 0:
                    priority = abs(diff_y) * 100 + abs(diff_x)
                    candidates.append((priority, idx))
            elif dx != 0 and dy == 0:
                if diff_x * dx > 0:
                    priority = abs(diff_x) * 100 + abs(diff_y)
                    candidates.append((priority, idx))
        
        if candidates:
            candidates.sort()
            self.selected_widget_index = candidates[0][1]
            
    def update(self):
        for widget, _ in self.widgets:
            if hasattr(widget, "update"):
                widget.update()
                
    def run(self):
        self.running = True
        while self.running:
            self.update()
            self.render()
            self.handle_input()
            time.sleep(0.05)
