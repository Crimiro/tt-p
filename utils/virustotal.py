import requests
import os
import time

VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

async def scan_file(file):
    file_content = await file.read()
    response = requests.post(
        "https://www.virustotal.com/vtapi/v2/file/scan",
        files={"file": (file.filename, file_content)},
        params={"apikey": VIRUSTOTAL_API_KEY}
    )
    
    try:
        scan_result = response.json()
    except ValueError:
        raise Exception("Error decoding VirusTotal response")
    
    return scan_result

def get_scan_report(scan_id):
    waiting_for_result = True
    scan_result_get = {}
    while waiting_for_result:
        time.sleep(10)
        response = requests.get(
            "https://www.virustotal.com/vtapi/v2/file/report",
            params={"apikey": VIRUSTOTAL_API_KEY, "resource": scan_id}
        )
        try:
            scan_result_get = response.json()
        except ValueError:
            continue
        
        if scan_result_get.get("response_code") == 1:
            waiting_for_result = False
    
    return formatter(scan_result_get)


def formatter(scan_result):
    return {
        "md5": scan_result.get("md5"),
        "sha1": scan_result.get("sha1"),
        "sha256": scan_result.get("sha256"),
        "scan_date": scan_result.get("scan_date"),
        "positives": scan_result.get("positives"),
        "total": scan_result.get("total"),
        "verbose_msg": scan_result.get("verbose_msg"),
        "permalink": scan_result.get("permalink"),
        "scans": scan_result.get("scans")
    }