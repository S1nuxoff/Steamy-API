from fastapi import APIRouter, HTTPException

from app.services.currency_service import currencies, update_currencies

router = APIRouter()

@router.get("/", summary="Get list of currencies")
async def list_currencies():
    currencies_list = await currencies()
    if not currencies_list:
        raise HTTPException(status_code=404, detail="No currencies found")
    return currencies_list

@router.get("/update", summary="Update currencies ratio")
async def update_currencies_endpoint():
    result = await update_currencies()
    if not result.get("success"):
        raise HTTPException(status_code=500, detail=result.get("error"))
    return result
