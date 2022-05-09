from fastapi import APIRouter, HTTPException

from services.PatientService import PatientService
from schemas.patientSchema import PatientCreateInput
from schemas.outputsSchema import StandardOutput, ErrorOutput

router = APIRouter(prefix="/patient", tags=["patient"])

# Create patient endpoint
@router.post("/", status_code=201, response_model=StandardOutput, responses={400: {"model": ErrorOutput}, 201: {"model": StandardOutput}})
async def create_patient(user_input: PatientCreateInput):
    
    try:
        await PatientService.create_patient(user_input.name, user_input.birth_date)
        return {"message": "Patient created successfully"}
    except Exception as error:  
        raise HTTPException(status_code=400, detail=str(error))

# Delete patient endpoint
@router.delete("/{patient_id}", status_code=200, response_model=StandardOutput, responses={404: {"model": ErrorOutput}, 200: {"model": StandardOutput}})
async def delete_patient(patient_id: int):
    try:
        await PatientService.delete_patient(patient_id)
        return {"message": "Patient deleted successfully"}
    except Exception as error:
        raise error

# Get all patients endpoint (list of all patients in database)
@router.get("/", status_code=200, responses={200: {"model": StandardOutput}})
async def get_patients():
    try:
        patients = await PatientService.get_all_patients()
        return {"patients": patients}
    except Exception as error:
        raise error

# Get a single patient by id endpoint
@router.get("/{patient_id}", status_code=200, responses={200: {"model": StandardOutput}, 404: {"model": ErrorOutput}})
async def get_patient_by_id(patient_id: int):
    try:
        patient = await PatientService.get_patient_by_id(patient_id)
        return {"patient": patient}
    except Exception as error:
        raise error

# Update patient endpoint
@router.put("/{patient_id}", status_code=200, responses={200: {"model": StandardOutput}, 404: {"model": ErrorOutput}})
async def update_patient(patient_id: int, user_input: PatientCreateInput):
    try:
        await PatientService.update_patient(patient_id, user_input.name, user_input.birth_date)
        return {"message": "Patient updated successfully"}
    except Exception as error:
        raise error
