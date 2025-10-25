import os
import sys
import time
from .renderer import WidgetsGrid
from .stylesheet import Style

try:
    import msvcrt
    WINDOWS = True

except ImportError:
    WINDOWS = False

    import tty
    import termios
    import select


class Application:
    def __init__(self, widgets: list = None, style: Style = None):
        self.widgets = widgets if widgets else []
        self.renderer = WidgetsGrid(style)
        self.running = False
        self.selected_widget_index = 0
        self.first_render = True
        
    def add_widget(self, widget, position: tuple[int, int]):
        self.widgets.append((widget, position))
        
    def clear_screen(self):
        if self.first_render:
            os.system("cls" if os.name == "nt" else "clear")
            sys.stdout.write("\033[?25l")
            sys.stdout.flush()
            self.first_render = False
        else:
            sys.stdout.write("\033[H")
            sys.stdout.flush()
        
    def render(self):
        self.clear_screen()
        buffer = self.renderer.render(self.widgets, self.selected_widget_index)
        sys.stdout.write(buffer)
        sys.stdout.flush()
        
    @staticmethod
    def get_key_windows():
        if msvcrt.kbhit():
            key = msvcrt.getch()
            
            if key == b"\xe0":
                key = msvcrt.getch()
                if key == b"H":
                    return "up"
                elif key == b"P":
                    return "down"
                elif key == b"K":
                    return "left"
                elif key == b"M":
                    return "right"
            elif key == b"\r":
                return "enter"
            elif key == b"q" or key == b"\x1b":
                return "quit"
        return None
    
    @staticmethod
    def get_key_unix():
        if select.select([sys.stdin], [], [], 0)[0]:
            key = sys.stdin.read(1)
            
            if key == "\x1b":
                seq = sys.stdin.read(2)
                if seq == "[A":
                    return "up"
                elif seq == "[B":
                    return "down"
                elif seq == "[D":
                    return "left"
                elif seq == "[C":
                    return "right"
                else:
                    return "quit"
            elif key == "\r" or key == "\n":
                return "enter"
            elif key == "q":
                return "quit"
        return None
    
    def handle_input(self):
        if WINDOWS:
            key = self.get_key_windows()
        else:
            key = self.get_key_unix()

        match key:
            case "up": self.move_selection(-1, 0)
            case "down": self.move_selection(1, 0)
            case "left": self.move_selection(0, -1)
            case "right": self.move_selection(0, 1)
            case "quit": self.running = False
            case "enter":
                if self.selected_widget_index < len(self.widgets):
                    widget, _ = self.widgets[self.selected_widget_index]
                    if hasattr(widget, "on_click"):
                        widget.on_click()

    def move_selection(self, dy: int, dx: int):
        if len(self.widgets) == 0:
            return
            
        positions = [pos for _, pos in self.widgets]
        current_pos = positions[self.selected_widget_index]
        
        candidates = []
        for idx, pos in enumerate(positions):
            if idx == self.selected_widget_index:
                continue
            
            widget, _ = self.widgets[idx]
            if not getattr(widget, 'hoverable', True):
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
        
        if not WINDOWS:
            old_settings = termios.tcgetattr(sys.stdin)
            try:
                tty.setcbreak(sys.stdin.fileno())
                while self.running:
                    self.update()
                    self.render()
                    self.handle_input()
                    time.sleep(0.05)
            finally:
                termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
                sys.stdout.write("\033[?25h")
                sys.stdout.flush()
        else:
            try:
                while self.running:
                    self.update()
                    self.render()
                    self.handle_input()
                    time.sleep(0.05)
            finally:
                sys.stdout.write("\033[?25h")
                sys.stdout.flush()
