from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from crud import calculate_pph

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Perhitungan PPh Karyawan")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/employee")
def register_employee(name: str, npwp: str, salary: float, db: Session = Depends(get_db)):
    emp = models.Employee(name=name, npwp=npwp, salary=salary)
    db.add(emp)
    db.commit()
    return {"status": "ok", "message": "Karyawan terdaftar"}

@app.get("/calculate/{employee_id}")
def calculate_tax(employee_id: int, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).get(employee_id)
    rules = db.query(models.TaxRule).all()
    tax = calculate_pph(emp.salary, rules)
    return {"nama": emp.name, "pph": tax}