from cgi import Application, TextWidget, ButtonWidget, ProgressBarWidget, InfoPanelWidget


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
    
    text1 = TextWidget("Welcome to CGI Framework")
    app.add_widget(text1, (0, 0))
    
    info = InfoPanelWidget("System Info", {"CPU": "49%"})
    app.add_widget(info, (0, 1))
    
    button1 = ButtonWidget("Click Me", on_button_click)
    app.add_widget(button1, (0, 2))
    
    progress_widget = ProgressBarWidget(0.0, "Loading...")
    app.add_widget(progress_widget, (1, 0))
    
    button2 = ButtonWidget("Exit", lambda: setattr(app, "running", False))
    app.add_widget(button2, (1, 2))
    
    app.run()


if __name__ == "__main__":
    main()

