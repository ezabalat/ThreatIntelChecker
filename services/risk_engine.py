def calculate_risk(data):

    isp = data.get(
        "isp",
        ""
    ).lower()

    score = 0

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

    if score <= 10:

        level = "LOW"
        action = "MONITOR"

    elif score <= 30:

        level = "MEDIUM"
        action = "INVESTIGATE"

    else:

        level = "HIGH"
        action = "BLOCK IMMEDIATELY"

    return {
        "score": score,
        "level": level,
        "action": action
    }