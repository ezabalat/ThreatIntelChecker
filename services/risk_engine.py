def calculate_risk(
    ip_data,
    abuse_data
):

    isp = ip_data.get(
        "isp",
        ""
    ).lower()

    abuse = abuse_data.get(
        "data",
        {}
    )

    abuse_score = abuse.get(
        "abuseConfidenceScore",
        0
    )

    total_reports = abuse.get(
        "totalReports",
        0
    )

    is_whitelisted = abuse.get(
        "isWhitelisted",
        False
    )

    score = 0

    # -------------------
    # ISP Rules
    # -------------------

    if "google" in isp:
        score += 0

    elif "cloudflare" in isp:
        score += 0

    elif "opendns" in isp:
        score += 0

    elif "amazon" in isp:
        score += 30

    elif "digitalocean" in isp:
        score += 40

    elif "linode" in isp:
        score += 40

    elif "vultr" in isp:
        score += 40

    else:
        score += 20

    # -------------------
    # AbuseIPDB Rules
    # -------------------

    if is_whitelisted:

        score = 0

    else:

        if abuse_score >= 75:
            score += 60

        elif abuse_score >= 50:
            score += 40

        elif abuse_score >= 25:
            score += 20

        if total_reports > 100:
            score += 10

    # -------------------
    # Risk Level
    # -------------------

    if score <= 10:

        level = "LOW"
        action = "MONITOR"

    elif score <= 40:

        level = "MEDIUM"
        action = "INVESTIGATE"

    else:

        level = "HIGH"
        action = "BLOCK IMMEDIATELY"

    return {
        "score": score,
        "level": level,
        "action": action,
        "abuse_score": abuse_score,
        "total_reports": total_reports,
        "is_whitelisted": is_whitelisted
    }