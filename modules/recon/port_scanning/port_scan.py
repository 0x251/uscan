import socket
import urllib.request
import re
from messages import DetectionMessages

def strip_http_from_url(data: str) -> str:
        url = re.compile(r"https?://(www\.)?")
        return url.sub('', data).strip().strip('/')


def port_scan(url: str):
    url = strip_http_from_url(url)
    common_ports = {
        20: "FTP Data Transfer",
        21: "FTP Control",
        22: "SSH Remote Login Protocol",
        23: "Telnet",
        25: "SMTP Mail Transfer",
        53: "DNS service",
        80: "HTTP",
        110: "POP3 Mail Access",
        143: "IMAP Mail Access",
        443: "HTTPS",
        465: "SMTP over SSL",
        587: "SMTP Mail Submission",
        993: "IMAP over SSL",
        995: "POP3 over SSL",
        3306: "MySQL Database system",
        3389: "MS Remote Desktop",
        5900: "VNC Remote Desktop",
        8080: "HTTP Alternate"
    }

    for port, service in common_ports.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((url, port))
        if result == 0:
            print(f"{DetectionMessages.FOUND_OPEN_PORT} {port} - [{service}]")
            if port in [80, 443, 8080]:
                try:
                    response = urllib.request.urlopen(f"http://{url}:{port}")
                    print(f"{DetectionMessages.FOUND_WEB_SERVER} {port} - status [{response.getcode()}]")
                except Exception as e:
                   pass
        sock.close()

