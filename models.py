from sqlalchemy import Column, Integer, String, Float,DateTime
from sqlalchemy.sql import func
from database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    amount = Column(Float, nullable=False)
    category = Column(String, index=True)
    created_at = Column(DateTime, default=func.now())

class Finance(Base):
    __tablename__ = "finance"

    id = Column(Integer, primary_key=True, index=True)
    total_salary = Column(Float, nullable=False, default=50000.0)