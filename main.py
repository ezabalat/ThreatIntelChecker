import ipaddress

from services.ip_lookup import lookup_ip

from services.risk_engine import calculate_risk


def validate_ip(ip):

    try:

        ipaddress.ip_address(ip)

        return True

    except ValueError:

        return False


def main():

    with open(
        "input/ips.txt",
        "r"
    ) as file:

        ips = file.readlines()

    for ip in ips:

        ip = ip.strip()

        if not validate_ip(ip):

            print(f"IP inválida: {ip}")

            continue

        data = lookup_ip(ip)
        risk = calculate_risk(data)
        
        print("\n====================")

        print(f"IP: {data['query']}")

        print(f"País: {data['country']}")

        print(f"Ciudad: {data['city']}")

        print(f"ISP: {data['isp']}")

        print(f"Organización: {data['org']}")

        print(
            f"Risk Score: {risk['score']}"
        )

        print(
            f"Risk Level: {risk['level']}"  
        )

        print(f"Recommended Action: {risk['action']}")

if __name__ == "__main__":
    main()