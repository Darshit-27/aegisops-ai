from fastapi import APIRouter
from app.services.cve_service import get_cve_data
from app.services.shodan_service import get_shodan_data

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "OK"}

@router.get("/cve")
def fetch_cve():
    return get_cve_data()

@router.get("/shodan")
def fetch_shodan():
    return get_shodan_data()
