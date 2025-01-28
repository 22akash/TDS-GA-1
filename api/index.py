from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
import json

# Mock database of student marks
student_marks = [{"name":"23610","marks":41},{"name":"6MKZ7e5D","marks":8},{"name":"Oo491","marks":17},{"name":"w9","marks":19},{"name":"T","marks":7},{"name":"3lrcMilv9","marks":81},{"name":"2FcWizQ915","marks":73},{"name":"q1KEz9","marks":72},{"name":"PkWn","marks":15},{"name":"kULckoJM","marks":6},{"name":"SwT","marks":87},{"name":"mTCvuW","marks":65},{"name":"y55C","marks":97},{"name":"mWOlrt","marks":61},{"name":"Nvi0g6J","marks":23},{"name":"6w4xkz3H","marks":49},{"name":"kq7o30q","marks":78},{"name":"hRLFj","marks":54},{"name":"b7WdTLORc","marks":97},{"name":"x","marks":66},{"name":"kq","marks":75},{"name":"kUEBs6qkD","marks":73},{"name":"1C6FcO36X","marks":52},{"name":"k3xY0AQ","marks":2},{"name":"Dqh","marks":25},{"name":"8QrKAr","marks":22},{"name":"I46ekZCh","marks":59},{"name":"FY","marks":41},{"name":"t8CPqd1W","marks":70},{"name":"V0JG8U","marks":68},{"name":"meiIeX3Ewj","marks":26},{"name":"1H","marks":71},{"name":"VA","marks":54},{"name":"1lCRw","marks":58},{"name":"4","marks":32},{"name":"z411","marks":74},{"name":"W","marks":34},{"name":"tnIwY15yA","marks":16},{"name":"TZLGAe1Tu","marks":35},{"name":"4FRR1A","marks":66},{"name":"U","marks":22},{"name":"qYLT","marks":12},{"name":"YeEs4ZZ","marks":43},{"name":"QwgtOG","marks":11},{"name":"lsIFy","marks":67},{"name":"OtDiF","marks":48},{"name":"fi0D","marks":29},{"name":"2pdmvgKIY","marks":7},{"name":"8aRo4ec5gG","marks":71},{"name":"1G","marks":53},{"name":"UZwaD1o","marks":65},{"name":"cGe4Ow22","marks":49},{"name":"VhmcK","marks":42},{"name":"61bmw","marks":80},{"name":"A1DKfS82U","marks":46},{"name":"sC2dtWz","marks":69},{"name":"0rGlF","marks":66},{"name":"87ie3TED","marks":95},{"name":"jGdaA5Mq","marks":65},{"name":"8w44a","marks":19},{"name":"TzzDUaT","marks":62},{"name":"sHvBf","marks":4},{"name":"gYeSU","marks":91},{"name":"B","marks":21},{"name":"NP0cDj","marks":63},{"name":"j96VxdDF","marks":16},{"name":"lU","marks":51},{"name":"nNPMX7","marks":61},{"name":"kKHIuu","marks":94},{"name":"TyOhiRC","marks":44},{"name":"4xF6","marks":45},{"name":"78","marks":73},{"name":"Y","marks":18},{"name":"E0SjNX","marks":63},{"name":"JKUeWR","marks":62},{"name":"tOizkPRZL","marks":27},{"name":"vz","marks":98},{"name":"44dVjTrT","marks":2},{"name":"Tn","marks":26},{"name":"Fm","marks":70},{"name":"OmVCLQGku","marks":97},{"name":"tGTWqj7n4","marks":87},{"name":"tF7","marks":39},{"name":"t","marks":57},{"name":"g","marks":49},{"name":"gDTT","marks":59},{"name":"Kxd","marks":50},{"name":"ZMoEI","marks":65},{"name":"2","marks":14},{"name":"i49w4","marks":11},{"name":"1M3Q4EJ2K","marks":0},{"name":"l8Mob","marks":60},{"name":"HKuoE","marks":75},{"name":"Ju","marks":83},{"name":"UfrmirOZhX","marks":33},{"name":"3zu209","marks":56},{"name":"R","marks":96},{"name":"fflIPQTo","marks":89},{"name":"CXKOD","marks":72},{"name":"NQmq","marks":40}]

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL and query parameters
        path = urlparse(self.path)
        query_params = parse_qs(path.query)
        
        # Get the requested names
        requested_names = query_params.get('name', [])
        
        # Find marks for requested names
        result_marks = []
        for name in requested_names:
            for student in marks:
                if student['name'] == name:
                    result_marks.append(student['marks'])
                    break
        
        # Prepare the response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Send the response
        response = json.dumps({"marks": result_marks})
        self.wfile.write(response.encode('utf-8'))
