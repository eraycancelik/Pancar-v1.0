from sqlalchemy import Column, Integer, String, Float
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


class Engine(Base):
    __tablename__ = "engines"
    id = Column(Integer, primary_key=True)
    engine_name = Column(String)
    speed = Column(String)
    torque = Column(String)


class Gearbox(Base):
    __tablename__ = "gearboxes"
    gearbox_name = Column(String)
    gear_ratio_list = Column(String)
    differential_gear_ratio = Column(Float)
    powertrain_efficiency = Column(Float)


class Vehicle(Base):
    __tablename__ = "vehicles"
    vehicle_name = Column(String)
    vehicle_mass = Column(Float)
    c_aero = Column(Float)
    af_projection_area = Column(Float)
    rolling_resistance = Column(Float)
    r_dynamic_rolling = Column(Float)


class Environment(Base):
    __tablename__ = "environments"
    environment_name = Column(String)
    wind_speed = Column(Float)
    slope_angel_road = Column(Float)
    air_density = Column(Float)
    gravitational_force = Column(Float)
