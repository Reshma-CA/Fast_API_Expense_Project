from pydantic import BaseModel

class ExpenseBase(BaseModel):
    name: str
    amount: float
    category: str

class ExpenseCreate(ExpenseBase):
    pass  # No additional fields

class ExpenseResponse(ExpenseBase):
    id: int

    class Config:
        orm_mode = True
