from datetime import datetime


def save_report(lines):

    timestamp = datetime.now()

    file_timestamp = timestamp.strftime(
        "%Y%m%d_%H%M%S"
    )

    report_name = (
        f"reports/report_{file_timestamp}.txt"
    )

    with open(
        report_name,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "=" * 60 + "\n"
        )

        file.write(
            "Threat Intelligence Report\n"
        )

        file.write(
            f"Generated: {timestamp}\n"
        )

        file.write(
            "=" * 60 + "\n\n"
        )

        for line in lines:

            file.write(line)

            file.write("\n")

    return report_name