from kivy.uix.screenmanager import Screen
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool


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


class DeleteWindow(Screen):

	def hide_all(self):
		self.label_1.opacity = 0;
		self.label_1.disabled = True;
		self.label_1.text = ""
		self.text_1.opacity = 0;
		self.text_1.disabled = True;
		self.text_1.text = "";
		self.label_2.opacity = 0;
		self.label_2.disabled = True;
		self.label_2.text = ""
		self.text_2.opacity = 0;
		self.text_2.disabled = True;
		self.text_1.text = "";

		self.label_3.opacity = 0;
		self.label_3.disabled = True;
		self.label_3.text = ""
		self.text_3.opacity = 0;
		self.text_3.disabled = True;
		self.text_3.text = "";
		self.label_4.opacity = 0;
		self.label_4.disabled = True;
		self.label_4.text = ""
		self.text_4.opacity = 0;
		self.text_4.disabled = True;
		self.text_4.text = "";

		self.label_5.opacity = 0;
		self.label_5.disabled = True;
		self.label_5.text = ""
		self.text_5.opacity = 0;
		self.text_5.disabled = True;
		self.text_5.text = "";
		self.label_6.opacity = 0;
		self.label_6.disabled = True;
		self.label_6.text = ""
		self.text_6.opacity = 0;
		self.text_6.disabled = True;
		self.text_6.text = "";

		self.label_7.opacity = 0;
		self.label_7.disabled = True;
		self.label_7.text = ""
		self.text_7.opacity = 0;
		self.text_7.disabled = True;
		self.text_7.text = "";
		self.label_8.opacity = 0;
		self.label_8.disabled = True;
		self.label_8.text = ""
		self.text_8.opacity = 0;
		self.text_8.disabled = True;
		self.text_8.text = "";

		self.label_9.opacity = 0;
		self.label_9.disabled = True;
		self.label_9.text = ""
		self.text_9.opacity = 0;
		self.text_9.disabled = True;
		self.text_9.text = "";
		self.label_10.opacity = 0;
		self.label_10.disabled = True;
		self.label_10.text = ""
		self.text_10.opacity = 0;
		self.text_10.disabled = True;
		self.text_10.text = "";

		self.label_11.opacity = 0;
		self.label_11.disabled = True;
		self.label_11.text = ""
		self.text_11.opacity = 0;
		self.text_11.disabled = True;
		self.text_11.text = "";
		self.label_12.opacity = 0;
		self.label_12.disabled = True;
		self.label_12.text = ""
		self.text_12.opacity = 0;
		self.text_12.disabled = True;
		self.text_12.text = "";

		self.label_13.opacity = 0;
		self.label_13.disabled = True;
		self.label_13.text = ""
		self.text_13.opacity = 0;
		self.text_13.disabled = True;
		self.text_13.text = "";
		self.label_14.opacity = 0;
		self.label_14.disabled = True;
		self.label_14.text = ""
		self.text_14.opacity = 0;
		self.text_14.disabled = True;
		self.text_14.text = "";


	def visualize_items(self):
		self.hide_all()

		self.label_1.opacity = 1;
		self.label_1.disabled = False;
		self.label_1.text = "Item number"
		self.text_1.opacity = 1;
		self.text_1.disabled = False;
		self.label_2.opacity = 1;
		self.label_2.disabled = False;
		self.label_2.text = "Product name"
		self.text_2.opacity = 1;
		self.text_2.disabled = False;

		self.label_3.opacity = 1;
		self.label_3.disabled = False;
		self.label_3.text = "SDS BG"
		self.text_3.opacity = 1;
		self.text_3.disabled = False;
		self.label_4.opacity = 1;
		self.label_4.disabled = False;
		self.label_4.text = "SDS EN"
		self.text_4.opacity = 1;
		self.text_4.disabled = False;

		self.label_5.opacity = 1;
		self.label_5.disabled = False;
		self.label_5.text = "SDS DE"
		self.text_5.opacity = 1;
		self.text_5.disabled = False;
		self.label_6.opacity = 1;
		self.label_6.disabled = False;
		self.label_6.text = "Safety instruction"
		self.text_6.opacity = 1;
		self.text_6.disabled = False;

		self.label_7.opacity = 1;
		self.label_7.disabled = False;
		self.label_7.text = "Explosive"
		self.text_7.opacity = 1;
		self.text_7.disabled = False;
		self.label_8.opacity = 1;
		self.label_8.disabled = False;
		self.label_8.text = "Desensibilized explosive"
		self.text_8.opacity = 1;
		self.text_8.disabled = False;

		self.label_9.opacity = 1;
		self.label_9.disabled = False;
		self.label_9.text = "Oxidizing"
		self.text_9.opacity = 1;
		self.text_9.disabled = False;
		self.label_10.opacity = 1;
		self.label_10.disabled = False;
		self.label_10.text = "Flammable"
		self.text_10.opacity = 1;
		self.text_10.disabled = False;

		self.label_11.opacity = 1;
		self.label_11.disabled = False;
		self.label_11.text = "Toxic"
		self.text_11.opacity = 1;
		self.text_11.disabled = False;
		self.label_12.opacity = 1;
		self.label_12.disabled = False;
		self.label_12.text = "Corrosive"
		self.text_12.opacity = 1;
		self.text_12.disabled = False;

		self.label_13.opacity = 1;
		self.label_13.disabled = False;
		self.label_13.text = "Pressurized"
		self.text_13.opacity = 1;
		self.text_13.disabled = False;


	def visualize_chemicals(self):
		self.hide_all()

		self.label_1.opacity = 1;
		self.label_1.disabled = False;
		self.label_1.text = "Substance"
		self.text_1.opacity = 1;
		self.text_1.disabled = False


	def visualize_workplaces(self):
		self.hide_all()

		self.label_1.opacity = 1;
		self.label_1.disabled = False;
		self.label_1.text = "Channel number"
		self.text_1.opacity = 1;
		self.text_1.disabled = False;
		self.label_2.opacity = 1;
		self.label_2.disabled = False;
		self.label_2.text = "Product"
		self.text_2.opacity = 1;
		self.text_2.disabled = False;

		self.label_3.opacity = 1;
		self.label_3.disabled = False;
		self.label_3.text = "Hard copy"
		self.text_3.opacity = 1;
		self.text_3.disabled = False;


	def visualize_suppliers(self):
		self.hide_all()

		self.label_1.opacity = 1;
		self.label_1.disabled = False;
		self.label_1.text = "Supplier"
		self.text_1.opacity = 1;
		self.text_1.disabled = False;
		self.label_2.opacity = 1;
		self.label_2.disabled = False;
		self.label_2.text = "Address"
		self.text_2.opacity = 1;
		self.text_2.disabled = False;

		self.label_3.opacity = 1;
		self.label_3.disabled = False;
		self.label_3.text = "Phone number"
		self.text_3.opacity = 1;
		self.text_3.disabled = False;
		self.label_4.opacity = 1;
		self.label_4.disabled = False;
		self.label_4.text = "Email"
		self.text_4.opacity = 1;
		self.text_4.disabled = False;


	def visualize_mix_types(self):
		self.hide_all()

		self.label_1.opacity = 1;
		self.label_1.disabled = False;
		self.label_1.text = "Mixture type"
		self.text_1.opacity = 1;
		self.text_1.disabled = False;


	def visualize_rfs(self):
		self.hide_all()

		self.label_1.opacity = 1;
		self.label_1.disabled = False;
		self.label_1.text = "Requirements for storage"
		self.text_1.opacity = 1;
		self.text_1.disabled = False;


	def visualize_ic(self):
		self.hide_all()

		self.label_1.opacity = 1;
		self.label_1.disabled = False;
		self.label_1.text = "Information conformoty"
		self.text_1.opacity = 1;
		self.text_1.disabled = False;


	def visualize_mc(self):
		self.hide_all()

		self.label_1.opacity = 1;
		self.label_1.disabled = False;
		self.label_1.text = "Measurements conformoty"
		self.text_1.opacity = 1;
		self.text_1.disabled = False;


	def show_entry(self, table_name, entries):
		if table_name == "Items": self.show_item(entries)
		elif table_name == "Chemicals": self.show_chemical(entries)
		elif table_name == "Workplaces": self.show_workplace(entries)
		elif table_name == "Suppliers": self.show_supplier(entries)
		elif table_name == "Mixture types": self.show_mix_type(entries)
		elif table_name == "RFS": self.show_rfs(entries)
		elif table_name == "IC": self.show_ic(entries)
		elif table_name == "MC": self.show_mc(entries)


	def show_item(self, data_entries):
		pass
		# Session = sessionmaker(bind = engine)
		# session = Session()

		# pop_item = Item(item_number = data_entries[0], product_name = data_entries[1], SDS_BG = data_entries[2],
		# 				SDS_EN = data_entries[3], SDS_DE = data_entries[4], safety_instruction = data_entries[5],
		# 				explosive = data_entries[6], des_explosive = data_entries[7], oxidizing = data_entries[8],
		# 				flammable = data_entries[9], toxic = data_entries[10], corrosive = data_entries[11],
		# 				pressurized = data_entries[12]
		# 				)

		# session.add(pop_item)
		# session.commit()
		# session.close()


	def show_chemical(self, data_entries):
		Session = sessionmaker(bind = engine)
		session = Session()

		entries = session.query(Chemical_Substance).filter(Chemical_Substance.substance == data_entries[0])
		
		ids = ''

		for entry in entries:
			ids += str(entry.ID) + '; '

		self.text_IDs.text = ids

		session.close()


	def show_workplace(self, data_entries):
		pass
	# 	Session = sessionmaker(bind = engine)
	# 	session = Session()

	# 	pop_workplace = Workplace(channel_number = data_entries[0], product = data_entries[1], hard_copy = data_entries[2])

	# 	session.add(pop_workplace)
	# 	session.commit()
	# 	session.close()


	def show_supplier(self, data_entries):
		pass
	# 	Session = sessionmaker(bind = engine)
	# 	session = Session()

	# 	pop_supplier = Supplier(supplier = data_entries[0], address = data_entries[1], phone_number = data_entries[2],
	# 						email = data_entries[3]
	# 						)

	# 	session.add(pop_supplier)
	# 	session.commit()
	# 	session.close()


	def show_mix_type(self, data_entries):
		pass
	# 	Session = sessionmaker(bind = engine)
	# 	session = Session()

	# 	pop_mix_type = Mixture_type(mix_type = data_entries[0])

	# 	session.add(pop_mix_type)
	# 	session.commit()
	# 	session.close()


	def show_rfs(self, data_entries):
		pass
	# 	Session = sessionmaker(bind = engine)
	# 	session = Session()

	# 	pop_rfs = RFS(requirement = data_entries[0])

	# 	session.add(pop_rfs)
	# 	session.commit()
	# 	session.close()


	def show_ic(self, data_entries):
		pass
	# 	Session = sessionmaker(bind = engine)
	# 	session = Session()

	# 	pop_ic = IC(information = data_entries[0])

	# 	session.add(pop_ic)
	# 	session.commit()
	# 	session.close()


	def show_mc(self, data_entries):
		pass
	# 	Session = sessionmaker(bind = engine)
	# 	session = Session()

	# 	pop_mc = Measurements_conformoty(measurement = data_entries[0])

	# 	session.add(pop_mc)
	# 	session.commit()
	# 	session.close()


	def delete_item(self):
		Session = sessionmaker(bind = engine)
		session = Session()

		session.commit()
		session.close()


	def delete_chemical(self):
		Session = sessionmaker(bind = engine)
		session = Session()

		entries = session.query(Chemical_Substance).filter(Chemical_Substance.substance == data_entries[0])
		first_entry = session.query(Chemical_Substance).get(1)
		session.delete(first_entry)


		session.commit()
		session.close()


	def delete_workplace(self):
		Session = sessionmaker(bind = engine)
		session = Session()

		session.commit()
		session.close()


	def delete_supplier(self):
		Session = sessionmaker(bind = engine)
		session = Session()

		session.commit()
		session.close()


	def delete_mix_type(self):
		Session = sessionmaker(bind = engine)
		session = Session()

		session.commit()
		session.close()


	def delete_rfs(self):
		Session = sessionmaker(bind = engine)
		session = Session()

		session.commit()
		session.close()


	def delete_ic(self):
		Session = sessionmaker(bind = engine)
		session = Session()

		session.commit()
		session.close()


	def delete_mc(self):
		Session = sessionmaker(bind = engine)
		session = Session()

		session.commit()
		session.close()
