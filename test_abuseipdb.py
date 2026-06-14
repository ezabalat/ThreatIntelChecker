from services.abuseipdb_lookup import lookup_abuseipdb


result = lookup_abuseipdb(
    "8.8.8.8"
)

print(result)