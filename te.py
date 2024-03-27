from database import Environment_db

environment_instance = Environment_db(
    environment_name="ıslak mendilli",
    wind_speed=10,
    slope_angel_road=12,
    air_density=0.3,
    gravitational_force=9.8,
)
environment_instance.create_environment()