import shodan
from app.core.config import settings
from app.utils.response import success_response, error_response


def get_shodan_data(ip="8.8.8.8"):
    try:
        api = shodan.Shodan(settings.SHODAN_API_KEY)
        host = api.host(ip)

        data = {
            "ip": host.get("ip_str"),
            "org": host.get("org"),
            "ports": host.get("ports"),
            "country": host.get("country_name")
        }

        return success_response(data, source="shodan")

    except Exception as e:
        return error_response(str(e), source="shodan")
