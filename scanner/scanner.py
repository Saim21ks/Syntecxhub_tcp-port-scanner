import socket
import argparse
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from scanner.logger import setup_logger
from scanner.utils import validate_port_range

logger = setup_logger()


def scan_port(host, port, timeout):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((host, port))

            if result == 0:
                logger.info(f"[OPEN] {host}:{port}")
                return f"[OPEN] {port}"
            else:
                logger.info(f"[CLOSED] {host}:{port}")
                return f"[CLOSED] {port}"

    except socket.timeout:
        logger.info(f"[TIMEOUT] {host}:{port}")
        return f"[TIMEOUT] {port}"
    except Exception as e:
        logger.error(f"[ERROR] {host}:{port} - {e}")
        return f"[ERROR] {port}"


def run_scan():
    parser = argparse.ArgumentParser(description="Multithreaded TCP Port Scanner")
    parser.add_argument("host", help="Target host (IP or domain)")
    parser.add_argument("-p", "--ports", required=True, help="Port range (e.g., 20-80)")
    parser.add_argument("-t", "--timeout", type=float, default=1)
    parser.add_argument("-th", "--threads", type=int, default=100)

    args = parser.parse_args()

    start_port, end_port = validate_port_range(args.ports)

    print(f"\nScanning {args.host} ({start_port}-{end_port})")
    print(f"Start time: {datetime.now()}\n")

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        futures = [
            executor.submit(scan_port, args.host, port, args.timeout)
            for port in range(start_port, end_port + 1)
        ]

        for future in futures:
            print(future.result())

    print(f"\nScan completed at: {datetime.now()}")