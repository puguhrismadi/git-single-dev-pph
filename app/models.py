from sqlalchemy import Column, Integer, String, Float
from database import Base

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    npwp = Column(String, nullable=False)
    salary = Column(Float, nullable=False)

class TaxRule(Base):
    __tablename__ = "tax_rules"
    id = Column(Integer, primary_key=True, index=True)
    min_income = Column(Float)
    max_income = Column(Float)
    rate = Column(Float)