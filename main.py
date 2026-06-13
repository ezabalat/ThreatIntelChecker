import ipaddress

from services.ip_lookup import lookup_ip


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

        print("\n====================")

        print(f"IP: {data['query']}")

        print(f"País: {data['country']}")

        print(f"Ciudad: {data['city']}")

        print(f"ISP: {data['isp']}")

        print(f"Organización: {data['org']}")


if __name__ == "__main__":
    main()