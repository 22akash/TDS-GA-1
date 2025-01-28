from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import json
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enable CORS
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET')
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Parse query parameters
        query_components = parse_qs(urlparse(self.path).query)
        names = query_components.get('name', [])

        # Load marks data
        current_dir = os.path.dirname(os.path.realpath(__file__))
        data_path = os.path.join(current_dir, '..', 'data', 'marks.json')
        
        with open(data_path) as f:
            marks_data = json.load(f)

        # Get marks for requested names
        marks = []
        for name in names:
            mark = marks_data['students'].get(name, None)
            if mark is not None:
                marks.append(mark)

        # Return response
        response = {'marks': marks}
        self.wfile.write(json.dumps(response).encode())
