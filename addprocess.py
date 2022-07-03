from datetime import datetime
import random
import time

#from apd.aggregation.database import DataPoint

class DataPoint(Base):
    __tablename__ = "datapoints"
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    sensor_name = sqlalchemy.Column(sqlalchemy.String)
    collected_at = sqlalchemy.Column(TIMESTAMP)
    data = sqlalchemy.Column(JSONB)


def main():
    engine = sqlalchemy.create_engine(
        "postgresql+psycopg2://apd@localhost/apd", echo=True
    )
    sm = sessionmaker(engine)
    Session = sm()
    if False:
        Base.metadata.create_all(engine)
    print(Session.query(DataPoint).all())
    pass

def generate_points(time_to_wait):
    while True:
        time.sleep(time_to_wait)
        yield DataPoint(
            sensor_name="Fake",
            collected_at=datetime.now(),
            data=random.choice([1, 2, 3])
        )

def get_points_on_odd_seconds():
    points = generate_points(1)
    odd_seconds = filter(lambda point: point.collected_at.second % 2, points)
    yield from odd_seconds

def print_points(points):
    for point in points:
        print(point.sensor_name, point.collected_at, point.data)

if __name__ == "__main__":
    print_points(get_points_on_odd_seconds())