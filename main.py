import ipaddress

from services.abuseipdb_lookup import lookup_abuseipdb
from services.ip_lookup import lookup_ip
from services.risk_engine import calculate_risk
from services.report_generator import save_report


def validate_ip(ip):

    try:

        ipaddress.ip_address(ip)

        return True

    except ValueError:

        return False


def main():

    print("Iniciando ThreatIntelChecker...")

    with open(
        "input/ips.txt",
        "r"
    ) as file:

        ips = file.readlines()

    print(f"IPs encontradas: {len(ips)}")

    report_lines = []

    for ip in ips:

        ip = ip.strip()

        print(f"\nProcesando IP: {ip}")

        if not validate_ip(ip):

            print(f"IP inválida: {ip}")

            continue

        try:

            data = lookup_ip(ip)

            abuse_data = lookup_abuseipdb(ip)

            risk = calculate_risk(
                data,
                abuse_data
            )

        except Exception as e:

            print(f"ERROR procesando {ip}: {e}")

            continue

        print("\n====================")

        print(f"IP: {data['query']}")

        print(f"País: {data['country']}")

        print(f"Ciudad: {data['city']}")

        print(f"ISP: {data['isp']}")

        print(f"Organización: {data['org']}")

        print(
            f"Abuse Score: {risk['abuse_score']}"
        )

        print(
            f"Total Reports: {risk['total_reports']}"
        )

        print(
            f"Whitelisted: {risk['is_whitelisted']}"
        )

        print(
            f"Risk Score: {risk['score']}"
        )

        print(
            f"Risk Level: {risk['level']}"
        )

        print(
            f"Recommended Action: {risk['action']}"
        )

        # -------------------------
        # Construcción del reporte
        # -------------------------

        report_lines.append(
            f"IP: {data['query']}"
        )

        report_lines.append(
            f"Country: {data['country']}"
        )

        report_lines.append(
            f"City: {data['city']}"
        )

        report_lines.append(
            f"ISP: {data['isp']}"
        )

        report_lines.append(
            f"Organization: {data['org']}"
        )

        report_lines.append(
            f"Abuse Score: {risk['abuse_score']}"
        )

        report_lines.append(
            f"Total Reports: {risk['total_reports']}"
        )

        report_lines.append(
            f"Whitelisted: {risk['is_whitelisted']}"
        )

        report_lines.append(
            f"Risk Score: {risk['score']}"
        )

        report_lines.append(
            f"Risk Level: {risk['level']}"
        )

        report_lines.append(
            f"Recommended Action: {risk['action']}"
        )

        report_lines.append("")

        report_lines.append(
            "-" * 60
        )

        report_lines.append("")

    report_name = save_report(
        report_lines
    )

    print(
        "\nReporte generado correctamente."
    )

    print(
        f"Archivo: {report_name}"
    )


if __name__ == "__main__":
    main()