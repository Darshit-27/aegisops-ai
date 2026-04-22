import requests

def get_cve_data():
    url = "https://services.nvd.nist.gov/rest/json/cves/2.0?resultsPerPage=5"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        results = []
        for item in data.get("vulnerabilities", []):
            cve_id = item["cve"]["id"]
            description = item["cve"]["descriptions"][0]["value"]

            results.append({
                "cve_id": cve_id,
                "description": description
            })

        return {"data": results}

    except Exception as e:
        return {"error": str(e)}
