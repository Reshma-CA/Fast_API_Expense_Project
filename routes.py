from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal
from sqlalchemy import func

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Define a fixed total salary (or fetch from a database if needed)
TOTAL_SALARY = 50000.0  # Change this as needed

# Create Expense
@router.post("/expenses/", response_model=schemas.ExpenseResponse)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db=db, expense=expense)



# Get All Expenses
@router.get("/expenses/", response_model=list[schemas.ExpenseResponse])
def get_expenses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_expenses(db=db)

@router.get("/expenses/month/{year}/{month}/", response_model=list[schemas.ExpenseResponse])
def get_expenses_by_month(year: int, month: int, db: Session = Depends(get_db)):
    return crud.get_expenses_by_month(db, year, month)

@router.get("/totals/")
def get_totals(db: Session = Depends(get_db)):
    # Calculate total expenses
    total_expense = db.query(func.sum(models.Expense.amount)).scalar() or 0.0
    
    # Calculate remaining amount
    remaining_amount = TOTAL_SALARY - total_expense
    
    return {
        "total_expense": total_expense,
        "total_salary": TOTAL_SALARY,
        "remaining_amount": remaining_amount
    }
