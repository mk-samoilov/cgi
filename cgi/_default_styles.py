from .stylesheet import Style


class Border(Style):
    top_left_character = "┏"
    top_right_character = "┓"

    bottom_left_character = "┗"
    bottom_right_character = "┛"

    horizontal_line_character = "━"
    vertical_line_character = "┃"

    # ┏━━━━━━━━━━━━━━━━━━━━━━━━┓
    # ┃                        ┃
    # ┃      WIDGET CELL       ┃
    # ┃                        ┃
    # ┃      (6x24 size)       ┃
    # ┃                        ┃
    # ┗━━━━━━━━━━━━━━━━━━━━━━━━┛


class DoubleBorder(Style):
    top_left_character = "╔"
    top_right_character = "╗"

    bottom_left_character = "╚"
    bottom_right_character = "╝"

    horizontal_line_character = "═"
    vertical_line_character = "║"

    # ╔══════════════════════════╗
    # ║                          ║
    # ║       WIDGET CELL        ║
    # ║                          ║
    # ║       (6x24 size)        ║
    # ║                          ║
    # ╚══════════════════════════╝


class WidgetsGridDefaultStyle(Style):
    grid_size = (2, 3)
    
    one_cell_size = (6, 24)
    cells_distance = 3
    
    top_padding = 2
    left_padding = 4
