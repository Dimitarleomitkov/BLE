from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import bleak
import asyncio
import argparse
# from kivy.uix.widget import Widget
# from kivy.properties import ColorProperty
# from kivy.uix.label import Label
# from kivy.uix.image import Image
# from kivy.uix.popup import Popup
# import sqlalchemy as db
# from TablesCreation import dangeorus_substances,risk_exposed_wоrkers, ppe, precautions, storage_conditions, recommendations_for_safety, hazard_statements, classification_clp, Item, Chemical_Substance, Mixture_type, Workplace, Physical_state, Supplier
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.exc import IntegrityError
# import os
# from TablesCreation import main as tb_create

# Base = declarative_base()
# database_url = "sqlite:///safetyDB.db"
# engine = db.create_engine(database_url)
# ses = sessionmaker(bind = engine)
# session = ses()

# class ColorLabel(Label):
# 	background_color = ColorProperty()


# class BackgroundLabel(Label):
# 	background_color = ColorProperty()


#Define the different screens
class MainMenuWindow(Screen):
	g_devices = False

	def on_pre_enter(self):
		Window.size = (600, 800)
		Window.fullscreen = False
		Window.left = 0
		Window.minimum_width = 600
		Window.minimum_height = 800


	def scan_devices(self):
		self.ids.device_address_input.text = ""
		loop = asyncio.new_event_loop()
		asyncio.set_event_loop(loop)
		loop.run_until_complete(self._scan_devices())


	async def _scan_devices(self):
		connectable_devices = False

		while connectable_devices == False:
			devices = await bleak.BleakScanner.discover(30)

			for device in devices:
				if device.name != None:
					connectable_devices = True

		if len(devices) == 0:
			print("No devices found")
			return

		self.g_devices = devices

		for device in devices:
			print(f"{device}")
			print(f"{device.name}-{device.address}")
			address = "".join(device.address)
			self.ids.device_address_input.text += address + '\n'


	def connect_device(self):
		loop = asyncio.new_event_loop()
		asyncio.set_event_loop(loop)
		loop.run_until_complete(self._connect_device())


	async def _connect_device(self):
		device_address = self.ids.device_address_input.text[:-1]
		my_device = False

		for device in self.g_devices:
			if device_address == device.address:
				my_device = device
			else:
				print(f"{device_address} != {device.address}")

		try:
			async with bleak.BleakClient(my_device) as client:
				for service in client.services:
					print(f"  service {service.uuid}")
					for characteristic in service.characteristics:
						print(f"  characteristic {characteristic.uuid} {hex(characteristic.handle)} ({len(characteristic.descriptors)} descriptors)")
		except bleak.exc.BleakError as e:
			print(f"  error {e}")
			print("\n\n")


	# def error_screen(self, err_msg):
	# 	box_layout = BoxLayout(orientation = 'vertical', spacing = 10)

	# 	screen_content = Image(source = "resources/images/mgm_ah-ah_gif.zip")

	# 	error_label = Label(text = err_msg, size_hint = (None, None), size = (400, 50))

	# 	box_layout.add_widget(screen_content)
	# 	box_layout.add_widget(error_label)

	# 	popup = Popup(title = 'Error!',
	# 					content = box_layout,
	# 					size_hint = (None, None),
	# 					size = (400, 450),
	# 					auto_dismiss = True)
	# 	popup.open()


	# Close the application
	def Exit (self):
		# Close the application
		App.get_running_app().stop()
		# Remove the window
		Window.close()