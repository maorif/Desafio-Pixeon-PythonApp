from fastapi import HTTPException
from sqlalchemy import delete
from sqlalchemy.future import select
from database.models import Patient
from database.config import database_async_session

# Methos for crud 
class PatientService:
    async def create_patient(name, birth_date):
        async with database_async_session() as session:
            session.add(Patient(nome=name, data_de_nascimento=birth_date))
            await session.commit()

    async def delete_patient(patient_id):
        async with database_async_session() as session:
            patient = await session.get(Patient, patient_id)
            if not patient:
                raise HTTPException(status_code=404, detail=f"Patient with id {patient_id} not found")
            await session.execute(delete(Patient).where(Patient.id == patient_id))
            await session.commit()

    async def get_all_patients():
        async with database_async_session() as session:
            patients = await session.execute(select(Patient))
            return patients.scalars().all()
    
    async def get_patient_by_id(patient_id):
        async with database_async_session() as session:
            patient = await session.get(Patient, patient_id)
            if not patient:
                raise HTTPException(status_code=404, detail=f"Patient with id {patient_id} not found")
            return patient
    
    async def update_patient(patient_id, name, birth_date):
        async with database_async_session() as session:
            patient = await session.get(Patient, patient_id)
            if not patient:
                raise HTTPException(status_code=404, detail=f"Patient with id {patient_id} not found")
            patient.nome = name
            patient.data_de_nascimento = birth_date
            await session.commit()