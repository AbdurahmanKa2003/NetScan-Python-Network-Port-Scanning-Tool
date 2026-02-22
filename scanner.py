import socket


def scan(target, max_port):
    print(f"\n[*] Scanning target: {target}")

    for port in range(1, max_port + 1):
        port_scanner(target, port)


def port_scanner(ip_address, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((ip_address, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")

        sock.close()

    except Exception as e:
        print(f"Error: {e}")


targets = input("[*] Enter IPs (separate by comma): ")
port = int(input("[*] Enter max port to scan: "))

if "," in targets:
    print("[*] Scanning multiple targets...")

    for ip_addr in targets.split(","):
        scan(ip_addr.strip(), port)

else:
    scan(targets.strip(), port)
