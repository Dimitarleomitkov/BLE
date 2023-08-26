from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import sqlalchemy as db
from sqlalchemy import Table, Column, Integer, String, MetaData, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from kivy.graphics import Color, Rectangle
from kivy.properties import ColorProperty


Base = declarative_base()
engine = db.create_engine(f"sqlite:///safetyDB.db", echo = True, poolclass = NullPool)
Session = sessionmaker(bind = engine)
session = Session()


class Item(Base):
	__tablename__ = "items"
	ID = db.Column(db.Integer, unique = True, primary_key = True)
	item_number = db.Column(db.Integer, unique = True, primary_key = True)
	product_name = db.Column(db.String)
	SDS_BG = db.Column(db.String)
	SDS_EN = db.Column(db.String)
	SDS_DE = db.Column(db.String)
	safety_instruction = db.Column(db.String)
	explosive = db.Column(db.Boolean)
	des_explosive = db.Column(db.Boolean)
	oxidizing = db.Column(db.Boolean)
	flammable = db.Column(db.Boolean)
	toxic = db.Column(db.Boolean)
	corrosive = db.Column(db.Boolean)
	pressurized = db.Column(db.Boolean)


class Chemical_Substance(Base):
	__tablename__ = "chem_substances"
	ID = db.Column(db.Integer, unique = True, primary_key = True)
	substance = db.Column(db.String, unique = True)


class Mixture_type(Base):
	__tablename__ = "mixture_types"
	ID = db.Column(db.Integer, unique = True, primary_key = True)
	mix_type = db.Column(db.String, unique = True)


class Hazard(Base):
	__tablename__ = "hazard"
	ID = db.Column(db.Integer, unique = True, primary_key = True)
	hazardous = db.Column(db.Boolean, unique = True)


class Workplace(Base):
	__tablename__ = "workplaces"
	ID = db.Column(db.Integer, unique = True, primary_key = True)
	channel_number = db.Column(db.Integer)
	product = db.Column(db.String)
	hard_copy = db.Column(db.Integer)


class Physical_state(Base):
	__tablename__ = "physical_states"
	ID = db.Column(db.Integer, unique = True, primary_key = True)
	phys_state = db.Column(db.String, unique = True)


class Supplier(Base):
	__tablename__ = "suppliers"
	ID = db.Column(db.Integer, unique = True, primary_key = True)
	name = db.Column(db.String)
	address = db.Column(db.String)
	phone_number = db.Column(db.Integer)
	email = db.Column(db.String)


class Manufacturer(Base):
	__tablename__ = "manufacturers"
	ID = db.Column(db.Integer, unique = True, primary_key = True)
	name = db.Column(db.String)
	name = db.Column(db.String)
	address = db.Column(db.String)
	phone_number = db.Column(db.Integer)
	email = db.Column(db.String)


class Used_Chemicals(Base):
	__tablename__ = "used_chemicals"
	ID = db.Column(db.Integer, unique = True, primary_key = True)
	item_number = db.Column(db.Integer, ForeignKey('items.item_number'))
	supplier = db.Column(db.Integer, ForeignKey('suppliers.ID'))
	manufacturer = db.Column(db.Integer, ForeignKey('manufacturers.ID'))
	hazardous = db.Column(db.Integer, ForeignKey('hazard.ID'))
	chemical_substance = db.Column(db.Integer, ForeignKey('chem_substances.ID'))
	mixture = db.Column(db.Integer, ForeignKey('mixture_types.ID'))
	physical_state = db.Column(db.Integer, ForeignKey('physical_states.ID'))
	quantity = db.Column(db.Integer)


class RFS(Base):
	__tablename__ = "requirements_for_storage"
	ID = db.Column(db.Integer, unique = True, primary_key = True)
	requirement = db.Column(db.String)


class IC(Base):
	__tablename__ = "information_conformoty"
	ID = db.Column(db.Integer, unique = True, primary_key = True)
	information = db.Column(db.String, unique = True)
	

class Measurements_conformoty(Base):
	__tablename__ = "measurements_conformoty"
	ID = db.Column(db.Integer, unique = True, primary_key = True)
	measurement = db.Column(db.String, unique = True)


class Compliance_with_storage(Base):
	__tablename__ = "compliance_with_storage"
	ID = db.Column(db.Integer, unique = True, primary_key = True)
	item_number = db.Column(db.Integer, ForeignKey('items.item_number'))
	hazardous = db.Column(db.Integer, ForeignKey('hazard.ID'))
	req_for_storage = db.Column(db.Integer, ForeignKey('requirements_for_storage.ID'))
	compliance = db.Column(db.Boolean)
	info_conformoty = db.Column(db.Integer, ForeignKey('information_conformoty.ID'))
	meas_conformoty = db.Column(db.Integer, ForeignKey('measurements_conformoty.ID'))


class ColorLabel(Label):
	background_color = ColorProperty()

class ReadWindow(Screen):

	def visualize_all_items(self):
		entries = session.query(Item)

		layout = GridLayout(cols = 14, row_force_default = True, row_default_height = 40, col_default_width = 50)

		title_labels = []

		title_labels.append(ColorLabel(bold = True,
										text = f"ID",
										font_size = 14,
										background_color = [251/255, 185/255, 0, 1]
										)
		)
		title_labels.append(ColorLabel(bold = True,
										text = f"item\nnumber",
										font_size = 14,
										background_color = [251/255, 185/255, 0, 1]
										)
		)
		title_labels.append(ColorLabel(bold = True,
										text = f"product\nname",
										font_size = 14,
										background_color = [251/255, 185/255, 0, 1]
										)
		)
		title_labels.append(ColorLabel(bold = True,
										text = f"SDS BG",
										font_size = 14,
										background_color = [251/255, 185/255, 0, 1]
										)
		)
		title_labels.append(ColorLabel(bold = True,
										text = f"SDS EN",
										font_size = 14,
										background_color = [251/255, 185/255, 0, 1]
										)
		)
		title_labels.append(ColorLabel(bold = True,
										text = f"SDS DE",
										font_size = 14,
										background_color = [251/255, 185/255, 0, 1]
										)
		)
		title_labels.append(ColorLabel(bold = True,
										text = f"safety\ninstruction",
										font_size = 14,
										background_color = [251/255, 185/255, 0, 1]
										)
		)
		title_labels.append(ColorLabel(bold = True,
										text = f"explosive",
										font_size = 14,
										background_color = [251/255, 185/255, 0, 1]
										)
		)
		title_labels.append(ColorLabel(bold = True,
										text = f"desensibilized\nexplosive",
										font_size = 14,
										background_color = [251/255, 185/255, 0, 1]
										)
		)
		title_labels.append(ColorLabel(bold = True,
										text = f"oxidizing",
										font_size = 14,
										background_color = [251/255, 185/255, 0, 1]
										)
		)
		title_labels.append(ColorLabel(bold = True,
										text = f"flammable",
										font_size = 14,
										background_color = [251/255, 185/255, 0, 1]
										)
		)
		title_labels.append(ColorLabel(bold = True,
										text = f"toxic",
										font_size = 14,
										background_color = [251/255, 185/255, 0, 1]
										)
		)
		title_labels.append(ColorLabel(bold = True,
										text = f"corrosive",
										font_size = 14,
										background_color = [251/255, 185/255, 0, 1]
										)
		)
		title_labels.append(ColorLabel(bold = True,
										text = f"pressurized",
										font_size = 14,
										background_color = [251/255, 185/255, 0, 1]
										)
		)

		for title_label in title_labels:
			layout.add_widget(title_label)

		index = 0
		for entry in entries:
			index += 1

			layout.add_widget(Label(text = f"{entry.ID}",
									font_size = 14,
									color = [251/255, 185/255, 0, 1]
									))
			layout.add_widget(Label(text = f"{entry.item_number}",
									font_size = 14
									))
			layout.add_widget(Label(text = f"{entry.product_name}",
									font_size = 14
									))
			layout.add_widget(Label(text = f"{entry.SDS_BG}",
									font_size = 14
									))
			layout.add_widget(Label(text = f"{entry.SDS_EN}",
									font_size = 14
									))
			layout.add_widget(Label(text = f"{entry.SDS_DE}",
									font_size = 14
									))
			layout.add_widget(Label(text = f"{entry.safety_instruction}",
									font_size = 14
									))
			layout.add_widget(Label(text = f"{entry.explosive}",
									font_size = 14
									))
			layout.add_widget(Label(text = f"{entry.des_explosive}",
									font_size = 14
									))
			layout.add_widget(Label(text = f"{entry.oxidizing}",
									font_size = 14
									))
			layout.add_widget(Label(text = f"{entry.flammable}",
									font_size = 14
									))
			layout.add_widget(Label(text = f"{entry.toxic}",
									font_size = 14
									))
			layout.add_widget(Label(text = f"{entry.corrosive}",
									font_size = 14
									))
			layout.add_widget(Label(text = f"{entry.pressurized}",
									font_size = 14
									))


		session.close()
		self.add_widget(layout)

		exit_btn = Button(text = "Main Menu",
								size_hint_y = None,
								height = 40,
								size_hint_x = None,
								width = 200
								)

		def exit_callback(instance):
			self.manager.current = "MainMenu"
			self.manager.transition.direction = "right"
			self.read_close()

		exit_btn.bind(on_press = exit_callback)

		self.add_widget(exit_btn)


	def read_close(self):
		engine.dispose()
