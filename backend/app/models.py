from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Overview(Base):
    __tablename__ = "overview"
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    market = Column(String)
    vending = Column(Float)
    foodture = Column(Float)
    bay_area = Column(Float)
    revenue = Column(Float)
    cost = Column(Float)
    gross = Column(Float)
    comm = Column(Float)
    net = Column(Float)
    net_pct = Column(Float)
    visits = Column(Integer)
