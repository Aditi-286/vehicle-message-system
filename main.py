from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

messages = [
    {
        "title": "Welcome",
        "content": "Welcome to the vehicle messaging system."
    },
    {
        "title": "Maintenance",
        "content": "Your vehicle maintenance is due next week."
    },
    {
        "title": "Fuel Alert",
        "content": "Fuel level is running low."
    },
    {
        "title": "Battery Warning",
        "content": "Battery health needs attention."
    },
    {
        "title": "Navigation",
        "content": "New route suggestions are available."
    }
]

class MessageListScreen(Screen):

    def on_enter(self):
        self.clear_widgets()

        layout = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=10
        )

        title = Label(
            text="Messages",
            font_size=30,
            size_hint=(1, 0.2)
        )

        layout.add_widget(title)

        for msg in messages:
            btn = Button(
                text=msg["title"],
                size_hint=(1, 0.15)
            )

            btn.bind(on_press=lambda x, m=msg: self.open_message(m))

            layout.add_widget(btn)

        self.add_widget(layout)

    def open_message(self, message):
        detail_screen = self.manager.get_screen("detail")
        detail_screen.show_message(message)
        self.manager.current = "detail"

class DetailScreen(Screen):

    def show_message(self, message):

        self.clear_widgets()

        layout = BoxLayout(
            orientation='vertical',
            padding=20,
            spacing=20
        )

        title = Label(
            text=message["title"],
            font_size=28,
            size_hint=(1, 0.2)
        )

        content = Label(
            text=message["content"],
            font_size=22,
            size_hint=(1, 0.5)
        )

        back_button = Button(
            text="Back",
            size_hint=(1, 0.15)
        )

        back_button.bind(on_press=self.go_back)

        layout.add_widget(title)
        layout.add_widget(content)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = "list"

class MessageApp(App):

    def build(self):

        sm = ScreenManager()

        sm.add_widget(MessageListScreen(name="list"))
        sm.add_widget(DetailScreen(name="detail"))

        return sm

if __name__ == "__main__":
    MessageApp().run()
