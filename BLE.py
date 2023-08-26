import sys

sys.path.append("./modules/")

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.widget import Widget
from MainMenu import MainMenuWindow


class DSEMApp(App):
	# Build the main menu of the application
	def build(self):
		Builder.load_file("./modules/MainMenuWindow.kv")
		sm = ScreenManager()
		sm.add_widget(MainMenuWindow(name = 'MainMenu'))

		return sm


def main():
	DSEMApp().run()


if __name__ == "__main__":
	main()