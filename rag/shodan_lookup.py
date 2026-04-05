import os
import shodan
from dotenv import load_dotenv
import socket
import re

load_dotenv()

API_KEY = os.getenv("SHODAN_API_KEY")

api = shodan.Shodan(API_KEY)


def resolve_domain(domain):
    """
    Convert domain/URL to IP address
    """
    try:
        # remove http/https if present
        domain = re.sub(r'^https?://', '', domain)
        domain = domain.split('/')[0]

        ip = socket.gethostbyname(domain)
        return ip

    except Exception:
        return None


def lookup_target(target):
    """
    Accepts either IP or URL/domain
    """

    try:

        # check if input is an IP
        if re.match(r"\d+\.\d+\.\d+\.\d+", target):
            ip_address = target

        else:
            ip_address = resolve_domain(target)

            if not ip_address:
                return {"error": "Unable to resolve domain"}

        host = api.host(ip_address)

        result = {
            "ip": host["ip_str"],
            "organization": host.get("org", "N/A"),
            "os": host.get("os", "N/A"),
            "ports": host["ports"],
            "country": host.get("country_name", "Unknown"),
            "hostnames": host.get("hostnames", [])
        }

        return result

    except Exception as e:
        return {"error": str(e)}