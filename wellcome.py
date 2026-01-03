import json
from textual.app import App
from textual.widgets import Input, RichLog
from textual.containers import Vertical

class WellcomeApp(App):
    CSS = """
    Screen {
        background: black;
        color: green;
    }
    """
    def compose(self):
        yield Vertical(
            RichLog(id="output"),
            Input(placeholder=">"),
        )
        def on_input_submitted(self, event: Input.Submitted) -> None:
            log = self.query_one("#output", RichLog)
            log.write(f" {event.value}")
    
def main():
    with open('config.json', 'r') as f:
        config = json.load(f)
    print("Hello", config.get("Name"))

if __name__ == "__main__":
   WellcomeApp().run()