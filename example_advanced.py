from cgi import Application, TextWidget, ButtonWidget, ProgressBarWidget, InfoPanelWidget, Style
import time


counter = {"value": 0}
progress_widget = None
success_widget = None
app_instance = None


def increment_counter():
    global progress_widget, success_widget, app_instance
    counter["value"] += 1
    
    if progress_widget and hasattr(progress_widget, "progress"):
        progress_widget.set_progress(min(1.0, progress_widget.progress + 0.05))
        
        if progress_widget.progress >= 1.0:
            for i, (widget, pos) in enumerate(app_instance.widgets):
                if widget == progress_widget:
                    app_instance.widgets.pop(i)
                    break
            
            success_widget = TextWidget("Successfully!")
            success_widget.style.align = "center"
            app_instance.add_widget(success_widget, (1, 1))
            progress_widget = None


def decrement_counter():
    counter["value"] -= 1


class CounterWidget(TextWidget):
    def render(self, width, height, is_selected):
        self.text = f"Counter: {counter['value']}"
        return super().render(width, height, is_selected)


def main():
    global progress_widget, success_widget, app_instance
    
    app = Application()
    app_instance = app
    
    title = TextWidget("Advanced CGI Demo")
    title_style = Style(cursor_select_border=None, occupied_cells=(1, 1), align="center")
    title.style = title_style
    app.add_widget(title, (0, 0))
    
    info = InfoPanelWidget("Stats", {"FPS": "20", "Widgets": "6"})
    app.add_widget(info, (0, 1))
    
    counter_widget = CounterWidget("Counter: 0")
    app.add_widget(counter_widget, (0, 2))
    
    btn_inc = ButtonWidget("Increment", increment_counter)
    app.add_widget(btn_inc, (1, 0))
    
    progress_widget = ProgressBarWidget(0.0, "Progress")
    app.add_widget(progress_widget, (1, 1))
    
    btn_dec = ButtonWidget("Decrement", decrement_counter)
    app.add_widget(btn_dec, (1, 2))
    
    app.run()


if __name__ == "__main__":
    main()

