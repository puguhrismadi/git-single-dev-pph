from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models
from app.crud import calculate_pph

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
@app.get("/employees")
def get_employees(db: Session = Depends(get_db)):
    return db.query(models.Employee).all()

@app.put("/employee/{employee_id}")
def update_employee(employee_id: int, name: str, npwp: str, salary: float, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).get(employee_id)
    emp.name = name
    emp.npwp = npwp 
    emp.salary = salary
    db.commit()
    return {"status": "ok", "message": "Karyawan terupdate"}
@app.get("/calculate/{employee_id}")
def calculate_tax(employee_id: int, db: Session = Depends(get_db)):
    emp = db.query(models.Employee).get(employee_id)
    rules = db.query(models.TaxRule).all()
    tax = calculate_pph(emp.salary, rules)
    return {"nama": emp.name, "pph": tax}

@app.post("/tax_rule")
def insert_tax_rule(min_income: float, max_income: float, rate: float, db: Session = Depends(get_db)):
    insert_tax_rule(db, min_income, max_income, rate)
    return {"status": "ok", "message": "Pajak terdaftar"}