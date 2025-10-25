from cgi import Application, TextWidget, ButtonWidget, ButtonWidgetStyle, ProgressBarWidget, InfoPanelWidget, DoubleBorder


progress_widget = None
success_widget = None
app_instance = None


def on_button_click():
    global progress_widget, success_widget, app_instance
    
    if progress_widget and hasattr(progress_widget, "progress"):
        progress_widget.set_progress(progress_widget.progress + 0.05)
        
        if progress_widget.progress >= 1.0:
            for i, (widget, pos) in enumerate(app_instance.widgets):
                if widget == progress_widget:
                    app_instance.widgets.pop(i)
                    break
            
            success_widget = TextWidget("Successfully completed!")
            app_instance.add_widget(success_widget, (1, 0))
            progress_widget = None


def main():
    global progress_widget, success_widget, app_instance
    
    app = Application()
    app_instance = app
    
    text1 = TextWidget(text="Welcome to CGI Framework", hoverable=True)
    app.add_widget(text1, position=(0, 0))
    
    info = InfoPanelWidget(title="System Info", items={"CPU": "49%"}, hoverable=True)
    app.add_widget(info, position=(0, 1))
    
    button1 = ButtonWidget("Click Me", on_button_click)
    app.add_widget(button1, position=(0, 2))
    
    progress_widget = ProgressBarWidget(0.0, "Loading...")
    app.add_widget(progress_widget, position=(1, 0))
    
    exit_button_style = ButtonWidgetStyle()
    exit_button_style.cursor_select_border = DoubleBorder()
    button2 = ButtonWidget("Exit", lambda: setattr(app, "running", False), style=exit_button_style)
    app.add_widget(button2, position=(1, 2))
    
    app.run()


if __name__ == "__main__":
    main()
