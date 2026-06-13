import requests


def lookup_ip(ip):

    url = f"http://ip-api.com/json/{ip}"

    response = requests.get(url)

    return response.json()