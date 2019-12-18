import socket
import ssl

hostname = 'login.microsoftonline.com'
context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        ssock.unwrap()
        ssock.close()
