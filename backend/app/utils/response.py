from datetime import datetime

def success_response(data, source="api"):
    return {
        "status": "success",
        "source": source,
        "timestamp": datetime.utcnow().isoformat(),
        "data": data
    }

def error_response(message, source="api"):
    return {
        "status": "error",
        "source": source,
        "timestamp": datetime.utcnow().isoformat(),
        "message": message
    }
