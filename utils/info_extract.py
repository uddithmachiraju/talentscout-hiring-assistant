def extract_user_info(text):
    fields = [
        "Full Name",
        "Email Address",
        "Phone Number",
        "Years of Experience",
        "Desired Position"
    ]
    info = {field: "" for field in fields}
    parts = text.split(",")
    for part in parts:
        if ":" in part:
            key, val = part.split(":", 1)
            key = key.strip()
            val = val.strip()
            for field in fields:
                if field.lower() == key.lower():
                    info[field] = val
                    break
    return info
