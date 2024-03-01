from test import Vehicle_db, Engine_db, Environment_db, Gearbox_db

vehicle_instance = Vehicle_db(
    vehicle_name="Car2",
    vehicle_mass=2500.0,
    c_aero=0.3,
    af_projection_area=5.0,
    rolling_resistance=0.01,
    r_dynamic_rolling=0.02,
)
environment_instance = Environment_db(
    environment_name="test ortamı 1",
    wind_speed=10,
    slope_angel_road=12,
    air_density=0.3,
    gravitational_force=9.8,
)
environment_instance.create_environment()
vehicle_instance.create_vehicle()
