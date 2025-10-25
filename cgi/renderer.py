from .stylesheet import Style
from ._default_styles import WidgetsGridDefaultStyle


class WidgetsGrid:
    def __init__(self, style: Style = None):
        self.style = style if style else WidgetsGridDefaultStyle()

        self.widgets_map = [[None] * self.style.grid_size[1] for _ in range(self.style.grid_size[0])]

    def calculate_position(self, grid_pos: tuple[int, int]) -> tuple[int, int]:
        cell_height, cell_width = self.style.one_cell_size
        top_padding = getattr(self.style, "top_padding", 0)
        left_padding = getattr(self.style, "left_padding", 0)
        y = grid_pos[0] * (cell_height + self.style.cells_distance) + top_padding
        x = grid_pos[1] * (cell_width + self.style.cells_distance) + left_padding
        return y, x

    @staticmethod
    def draw_widget_content(widget, content_size: tuple[int, int], is_selected: bool):
        content_height, content_width = content_size
        lines = []
        
        if hasattr(widget, "render"):
            widget_lines = widget.render(content_width, content_height, is_selected)
            if isinstance(widget_lines, str):
                widget_lines = widget_lines.split("\n")
        else:
            widget_lines = [" " * content_width for _ in range(content_height)]
        
        is_hoverable = getattr(widget, "hoverable", True)
        if (is_selected and is_hoverable and hasattr(widget.style, "cursor_select_border")
                and widget.style.cursor_select_border):
            border_style = widget.style.cursor_select_border
            
            top_line = border_style.top_left_character + border_style.horizontal_line_character * content_width + \
                       border_style.top_right_character
            lines.append(top_line)
            
            for i in range(content_height):
                if i < len(widget_lines):
                    content = widget_lines[i][:content_width].ljust(content_width)
                else:
                    content = " " * content_width
                lines.append(border_style.vertical_line_character + content + border_style.vertical_line_character)
            
            bottom_line = border_style.bottom_left_character + border_style.horizontal_line_character * \
                          content_width + border_style.bottom_right_character
            lines.append(bottom_line)
        else:
            for i in range(content_height):
                if i < len(widget_lines):
                    content = widget_lines[i][:content_width].ljust(content_width)
                else:
                    content = " " * content_width
                lines.append(content)
                
        return lines

    def render(self, widgets: list, selected_index: int = -1):
        grid_height = self.style.grid_size[0]
        grid_width = self.style.grid_size[1]
        cell_height, cell_width = self.style.one_cell_size
        top_padding = getattr(self.style, "top_padding", 0)
        left_padding = getattr(self.style, "left_padding", 0)
        
        total_height = grid_height * cell_height + (grid_height - 1) * self.style.cells_distance + 3 + top_padding
        total_width = grid_width * cell_width + (grid_width - 1) * self.style.cells_distance + 3 + left_padding
        
        buffer = [[" " for _ in range(total_width)] for _ in range(total_height)]
        
        for idx, (widget, position) in enumerate(widgets):
            is_selected = (idx == selected_index)
            
            occupied = widget.style.occupied_cells if hasattr(widget.style, "occupied_cells") else (1, 1)
            
            content_height = occupied[0] * cell_height + (occupied[0] - 1) * self.style.cells_distance
            content_width = occupied[1] * cell_width + (occupied[1] - 1) * self.style.cells_distance
            
            content_y, content_x = self.calculate_position(position)
            content_y += 1
            content_x += 1
            
            widget_lines = self.draw_widget_content(widget, (content_height, content_width), is_selected)
            
            is_hoverable = getattr(widget, "hoverable", True)
            if (is_selected and is_hoverable and hasattr(widget.style, "cursor_select_border")
                    and widget.style.cursor_select_border):
                start_y = content_y - 1
                start_x = content_x - 1
            else:
                start_y = content_y
                start_x = content_x
            
            for i, line in enumerate(widget_lines):
                y = start_y + i
                if y < 0 or y >= total_height:
                    continue
                for j, char in enumerate(line):
                    x = start_x + j
                    if 0 <= x < total_width:
                        buffer[y][x] = char
                        
        result = "\n".join("".join(row) for row in buffer)
        return result
