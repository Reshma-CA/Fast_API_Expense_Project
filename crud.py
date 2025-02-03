from sqlalchemy.orm import Session
import models, schemas
from datetime import datetime
from sqlalchemy import extract

# Create Expense
def create_expense(db: Session, expense: schemas.ExpenseCreate):
    db_expense = models.Expense(name=expense.name, amount=expense.amount, category=expense.category)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

# Get All Expenses
def get_expenses(db: Session):
    return db.query(models.Expense).all()

# Filter Expenses by Month
# def get_expenses_by_month(db: Session, year: int, month: int):
#     return db.query(models.Expense).filter(
#         models.Expense.created_at.between(f"{year}-{month}-01", f"{year}-{month}-31")
#     ).all()

def get_expenses_by_month(db: Session, year: int, month: int):
    return db.query(models.Expense).filter(
        extract("year", models.Expense.created_at) == year,
        extract("month", models.Expense.created_at) == month
    ).all()
