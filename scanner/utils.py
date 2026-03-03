def validate_port_range(port_range):
    try:
        start, end = port_range.split("-")
        start = int(start)
        end = int(end)

        if start < 1 or end > 65535 or start > end:
            raise ValueError

        return start, end
    except Exception:
        raise ValueError("Invalid port range. Use format: 20-80")