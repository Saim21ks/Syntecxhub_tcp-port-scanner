def validate_port_range(port_input):
    try:
        # Case 1: Specific ports (22,80,443)
        if "," in port_input:
            ports = [int(p.strip()) for p in port_input.split(",")]
            return ports

        # Case 2: Port range (20-80)
        if "-" in port_input:
            start, end = port_input.split("-")
            start = int(start)
            end = int(end)

            if start < 1 or end > 65535 or start > end:
                raise ValueError

            return list(range(start, end + 1))

        # Case 3: Single port
        port = int(port_input)
        return [port]

    except Exception:
        raise ValueError(
            "Invalid port input. Use formats: 80 | 20-80 | 22,80,443"
        )
