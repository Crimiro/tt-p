from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
from utils.virustotal import scan_file, get_scan_report
import os

VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

router = APIRouter()

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    scan_result = await scan_file(file)
    scan_result = get_scan_report(scan_result.get("scan_id"))
    result = {
        "filename": file.filename,
        "content_type": file.content_type,
        "scan_result": scan_result
    }
    return JSONResponse(content=result)