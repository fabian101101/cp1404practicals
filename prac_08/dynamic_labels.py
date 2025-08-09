from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy app to dynamically create labels from a list of names."""
    def __init__(self, **kwargs):
        """Initialize the app with a list of names."""
        super().__init__(**kwargs)
        self.names = ["Ada", "Bianca", "Chidi", "Obi"]

    def build(self):
        """Build the Kivy GUI and create labels."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a label for each name and add it to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
