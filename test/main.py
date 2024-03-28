from speed_torque import Speed_rpm
from pprint import pprint
from ..database import Engine_db
gtr = "gtr.xlsx"
ferrari = "ferrari.xlsx"
test = "test.xlsx"
engine = Speed_rpm(file=ferrari)

if __name__ == "__main__":
    try:
        
        pprint(engine.out()[0])
    except:
        print("an error occured while loading xlsx file")
