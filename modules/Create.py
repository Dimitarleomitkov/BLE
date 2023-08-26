from kivy.uix.screenmanager import Screen
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from functools import partial


Base = declarative_base()
engine = db.create_engine(f"sqlite:///safetyDB.db", echo = True, poolclass = NullPool)


class Item(Base):
	__tablename__ = "items"
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


class Workplace(Base):
	__tablename__ = "workplaces"
	ID = db.Column(db.Integer, unique = True, primary_key = True)
	channel_number = db.Column(db.Integer)
	product = db.Column(db.String)
	hard_copy = db.Column(db.Integer)


class Supplier(Base):
	__tablename__ = "suppliers"
	ID = db.Column(db.Integer, unique = True, primary_key = True)
	supplier = db.Column(db.String)
	address = db.Column(db.String)
	phone_number = db.Column(db.Integer)
	email = db.Column(db.String)


class RFS(Base):
	__tablename__ = "requirements_for_storage"
	ID = db.Column(db.Integer, unique = True, primary_key = True)
	requirement = db.Column(db.String)


class IC(Base):
	__tablename__ = "Information_conformoty"
	ID = db.Column(db.Integer, unique = True, primary_key = True)
	information = db.Column(db.String, unique = True)
	

class Measurements_conformoty(Base):
	__tablename__ = "measurements_conformoty"
	ID = db.Column(db.Integer, unique = True, primary_key = True)
	measurement = db.Column(db.String, unique = True)


class CreateWindow(Screen):
	widgets_list = []


	def check_length(self, *args, **kwargs):
		if len(args[1].text) > args[0]:
			args[1].text = args[1].text[0:-1]


	def check_number(self, *args, **kwargs):
		try:
			int(args[1])
		except Exception as e:
			args[0].text = args[0].text[0:-1]
			self.ids.error_label.text = "That was not a number :)"


	def check_text(self, *args, **kwargs):
		pass


	def cmd_handler(self, table_name):
		try:
			if table_name == "Items": self.visualize_items()
			elif table_name == "Chemicals": self.visualize_chemicals()
			elif table_name == "Workplaces": self.visualize_workplaces()
			elif table_name == "Suppliers": self.visualize_suppliers()
			elif table_name == "Mixture types": self.visualize_mix_types()
			elif table_name == "RFS": self.visualize_rfs()
			elif table_name == "IC": self.visualize_ic()
			elif table_name == "MC": self.visualize_mc()
		except Exception as e:
			self.ids.error_label.text = str(e)
			return


	def remove_all_widgets(self):
		for widget in self.widgets_list:
			self.ids.entry_grid.remove_widget(widget)

		self.widgets_list = []


	def visualize_items(self):
		self.remove_all_widgets()
		self.ids.error_label.text = ""

		ti_item_number = TextInput(text = "")
		ti_item_number.bind(text = partial(self.check_number))
		ti_item_number.bind(text = partial(self.check_length, 10))

		self.widgets_list.append(Label(text = "Item number"))
		self.widgets_list.append(ti_item_number)
		self.widgets_list.append(Label(text = "Product name"))
		self.widgets_list.append(TextInput())

		self.widgets_list.append(Label(text = "SDS BG"))
		self.widgets_list.append(CheckBox())
		self.widgets_list.append(Label(text = "SDS EN"))
		self.widgets_list.append(CheckBox())

		self.widgets_list.append(Label(text = "SDS DE"))
		self.widgets_list.append(CheckBox())
		self.widgets_list.append(Label(text = "Safety instruction"))
		self.widgets_list.append(TextInput())

		self.widgets_list.append(Label(text = "Explosive"))
		self.widgets_list.append(CheckBox())
		self.widgets_list.append(Label(text = "Desensibilized explosive"))
		self.widgets_list.append(CheckBox())

		self.widgets_list.append(Label(text = "Oxidizing"))
		self.widgets_list.append(CheckBox())
		self.widgets_list.append(Label(text = "Flammable"))
		self.widgets_list.append(CheckBox())

		self.widgets_list.append(Label(text = "Toxic"))
		self.widgets_list.append(CheckBox())
		self.widgets_list.append(Label(text = "Corrosive"))
		self.widgets_list.append(CheckBox())

		self.widgets_list.append(Label(text = "Pressurized"))
		self.widgets_list.append(CheckBox())

		for widget in self.widgets_list:
			self.ids.entry_grid.add_widget(widget)

	def visualize_chemicals(self):
		self.remove_all_widgets()

		self.widgets_list.append(Label(text = "Substance"))
		self.widgets_list.append(TextInput())

		for widget in self.widgets_list:
			self.ids.entry_grid.add_widget(widget)


	def visualize_workplaces(self):
		self.remove_all_widgets()

		self.widgets_list.append(Label(text = "Channel number"))
		self.widgets_list.append(TextInput())
		self.widgets_list.append(Label(text = "Product"))
		self.widgets_list.append(TextInput())

		self.widgets_list.append(Label(text = "Hard copy"))
		self.widgets_list.append(CheckBox())

		for widget in self.widgets_list:
			self.ids.entry_grid.add_widget(widget)

	def visualize_suppliers(self):
		self.remove_all_widgets()

		self.widgets_list.append(Label(text = "Supplier"))
		self.widgets_list.append(TextInput())
		self.widgets_list.append(Label(text = "Address"))
		self.widgets_list.append(TextInput())

		self.widgets_list.append(Label(text = "Phone number"))
		self.widgets_list.append(TextInput())
		self.widgets_list.append(Label(text = "Email"))
		self.widgets_list.append(TextInput())

		for widget in self.widgets_list:
			self.ids.entry_grid.add_widget(widget)


	def visualize_mix_types(self):
		self.remove_all_widgets()

		self.widgets_list.append(Label(text = "Mixture type"))
		self.widgets_list.append(TextInput())

		for widget in self.widgets_list:
			self.ids.entry_grid.add_widget(widget)


	def visualize_rfs(self):
		self.remove_all_widgets()

		self.widgets_list.append(Label(text = "Requirements for storage"))
		self.widgets_list.append(TextInput())

		for widget in self.widgets_list:
			self.ids.entry_grid.add_widget(widget)


	def visualize_ic(self):
		self.remove_all_widgets()

		self.widgets_list.append(Label(text = "Information conformoty"))
		self.widgets_list.append(TextInput())

		for widget in self.widgets_list:
			self.ids.entry_grid.add_widget(widget)


	def visualize_mc(self):
		self.remove_all_widgets()

		self.widgets_list.append(Label(text = "Measurements conformoty"))
		self.widgets_list.append(TextInput())

		for widget in self.widgets_list:
			self.ids.entry_grid.add_widget(widget)


	def submit_entry(self, table_name):
		entries = []

		try:
			for widget in self.widgets_list[1::2]:
				if type(widget) == type(TextInput()):
					entries.append(widget.text)
				elif type(widget) == type(CheckBox()):
					if widget.active:
						entries.append(1)
					else:
						entries.append(0)

			if table_name == "Items": self.submit_new_item(entries)
			elif table_name == "Chemicals": self.submit_new_chemical(entries)
			elif table_name == "Workplaces": self.submit_new_workplace(entries)
			elif table_name == "Suppliers": self.submit_new_supplier(entries)
			elif table_name == "Mixture types": self.submit_new_mix_type(entries)
			elif table_name == "RFS": self.submit_new_rfs(entries)
			elif table_name == "IC": self.submit_new_ic(entries)
			elif table_name == "MC": self.submit_new_mc(entries)
		except Exception as e:
			self.ids.error_label.text = str(e)
			return



	def submit_new_item(self, data_entries):
		Session = sessionmaker(bind = engine)
		session = Session()

		pop_item = Item(item_number = data_entries[0], product_name = data_entries[1], SDS_BG = data_entries[2],
						SDS_EN = data_entries[3], SDS_DE = data_entries[4], safety_instruction = data_entries[5],
						explosive = data_entries[6], des_explosive = data_entries[7], oxidizing = data_entries[8],
						flammable = data_entries[9], toxic = data_entries[10], corrosive = data_entries[11],
						pressurized = data_entries[12]
						)

		session.add(pop_item)
		session.commit()
		session.close()


	def submit_new_chemical(self, data_entries):
		Session = sessionmaker(bind = engine)
		session = Session()

		pop_chem = Chemical_Substance(substance = data_entries[0])

		session.add(pop_chem)
		session.commit()
		session.close()


	def submit_new_workplace(self, data_entries):
		Session = sessionmaker(bind = engine)
		session = Session()

		pop_workplace = Workplace(channel_number = data_entries[0], product = data_entries[1], hard_copy = data_entries[2])

		session.add(pop_workplace)
		session.commit()
		session.close()


	def submit_new_supplier(self, data_entries):
		Session = sessionmaker(bind = engine)
		session = Session()

		pop_supplier = Supplier(supplier = data_entries[0], address = data_entries[1], phone_number = data_entries[2],
							email = data_entries[3]
							)

		session.add(pop_supplier)
		session.commit()
		session.close()


	def submit_new_mix_type(self, data_entries):
		Session = sessionmaker(bind = engine)
		session = Session()

		pop_mix_type = Mixture_type(mix_type = data_entries[0])

		session.add(pop_mix_type)
		session.commit()
		session.close()


	def submit_new_rfs(self, data_entries):
		Session = sessionmaker(bind = engine)
		session = Session()

		pop_rfs = RFS(requirement = data_entries[0])

		session.add(pop_rfs)
		session.commit()
		session.close()


	def submit_new_ic(self, data_entries):
		Session = sessionmaker(bind = engine)
		session = Session()

		pop_ic = IC(information = data_entries[0])

		session.add(pop_ic)
		session.commit()
		session.close()


	def submit_new_mc(self, data_entries):
		Session = sessionmaker(bind = engine)
		session = Session()

		pop_mc = Measurements_conformoty(measurement = data_entries[0])

		session.add(pop_mc)
		session.commit()
		session.close()

