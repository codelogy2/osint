from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


HOST = "127.0.0.1"
PORTS = (8000, 8001, 8002, 8080, 8765)


def create_server():
    last_error = None
    for port in PORTS:
        try:
            return ThreadingHTTPServer((HOST, port), SimpleHTTPRequestHandler)
        except OSError as error:
            last_error = error
            print(f"Port {port} unavailable ({error}); trying another port...")

    # Let Windows choose an available local port if the usual ports are blocked.
    try:
        return ThreadingHTTPServer((HOST, 0), SimpleHTTPRequestHandler)
    except OSError as error:
        raise RuntimeError(
            f"Could not start the local server. Last error: {error}"
        ) from last_error


if __name__ == "__main__":
    server = create_server()
    port = server.server_address[1]
    print(f"Presentation: http://{HOST}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.server_close()
