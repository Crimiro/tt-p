from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from utils.virustotal import scan_file, get_scan_report
import os

VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

router = APIRouter()

ALLOWED_FILE_TYPES = ["application/pdf", "image/jpeg", "image/png"]
MAX_FILE_SIZE = 32 * 1024 * 1024

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_FILE_TYPES:
        raise HTTPException(status_code=400, detail="File type not allowed")
    
    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File size exceeds limit. 32MB max")
    
    scan_result = await scan_file(file)
    scan_result = get_scan_report(scan_result.get("scan_id"))
    result = {
        "filename": file.filename,
        "content_type": file.content_type,
        "scan_result": scan_result
    }
    return JSONResponse(content=result)