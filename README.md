# CGI Applications library
### console graphical interface applications library
### Contributing: [CONTRIBUTING.md](CONTRIBUTING.md)

<br>

## What is a library?
#### This library is a tool for creating graphical interfaces like the one below, consisting of a grid of positions occupied by widgets.

![ui_view_demo.png](demo_screenshots/ui_view_demo.png)

- pic `1` `ui view demo` (main.py script - example)

### Widgets on this example:

#### `[] Click me` and `[] Exit` - Button's widgets (1x1 grid cells),
#### Label `Welcome to CGI...` - Text widget (1x1),
#### Widget of title `System info` and content `CPU: ...` - Info-panel widget (1x1),
#### And last widget - progress bar (2x1 grid cells) widget

<br>

Widgets can be of different sizes, e.g. progress bar - 2x1 cells, buttons - 1x1 cells.

In pic `1` the widget-button `[] Click me` is surrounded by a frame - the cursor is on this:

The cursor can be moved using the arrow keys and enter to press the buttons.

<br>

### Description of the cells grid's work
![grid_cells_division_demo.png](demo_screenshots/grid_cells_division_demo.png)
- pic `2` `grid cells division`

#### In the example (on pic `1`) and by default the grid map size is 3x2 (3 columns and 2 rows, pic `2`):

```python
class WidgetsGridDefaultStyle(Style):
    grid_size = (2, 3) # Grid size here
    
    one_cell_size = (6, 24)
    cells_distance = 3
    
    top_padding = 2
    left_padding = 4
```

The cells also have a specified size (`one_cell_size`) and distance between them (`cells_distance`)

Thus, we can depict the layout of widgets in the `main.py` example (pic `1`) by cells like this:

![grid_cells_division_demo_2.png](demo_screenshots/grid_cells_division_demo_2.png)
- pic `3` `grid cells division: widget layout in example)`
