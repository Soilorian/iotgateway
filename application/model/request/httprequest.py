from urllib.parse import urlparse, parse_qs


class HttpRequest:
    def __init__(self):
        self.method = None
        self.path = None
        self.query_params = {}
        self.headers = {}
        self.body = None
        self.raw = None
        self.sender_addr = None

    def decode(self, raw_data, sender_addr):
        """
        Decodes raw HTTP request data and populates the class attributes.
        """
        self.raw = raw_data
        self.sender_addr = sender_addr
        lines = raw_data.split("\r\n")
        if not lines:
            raise ValueError("Empty HTTP request")

        # Parse the request line
        request_line = lines[0].split()
        if len(request_line) < 3:
            raise ValueError("Invalid HTTP request line")

        self.method, url, _ = request_line
        parsed_url = urlparse(url)
        self.path = parsed_url.path
        self.query_params = parse_qs(parsed_url.query)

        # Parse headers
        header_lines = iter(lines[1:])
        for line in header_lines:
            if not line:  # Blank line signals end of headers
                break
            key, value = line.split(":", 1)
            self.headers[key.strip()] = value.strip()

        # Parse body (if any)
        self.body = "\r\n".join(header_lines)

    def __repr__(self):
        return (
            f"HTTPRequest(method={self.method}, path={self.path}, "
            f"query_params={self.query_params}, headers={self.headers}, body={self.body})"
        )
