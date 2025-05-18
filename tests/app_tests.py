import unittest
from app.api.ping import ping
import requests
import json
from datetime import date
import subprocess
import time
import os

date_today = date.today()
class TestCashman(unittest.TestCase):
    def test_ping(self):
        self.assertEqual(ping(), "PONG!")
    def test_ping_endpoint(self):
        response = requests.get("http://127.0.0.1:5000")
        self.assertEqual(response.text, "PONG!")
    def test_evidence_endpoint(self):
        response = requests.get("http://localhost:5000/evidence")
        self.assertEqual(response.status_code, 200)
    def test_get_evidence(self):
        expected = [
  {
    "date": "Thu, 01 Nov 2001 00:00:00 GMT",
    "description": "BLE BLE BLE BLE",
    "id": 1,
    "name": "BLE BLE"
  },
  {
    "date": "Sat, 01 Dec 2001 00:00:00 GMT",
    "description": "BLE BLE BLE BLE2",
    "id": 2,
    "name": "BLE BLE2"
  },
  {
    "date": "Sun, 27 Apr 2025 00:00:00 GMT",
    "description": "This is a sample description.",
    "id": 3,
    "name": "Sample Evidence"
  },
  {
    "date": "Sun, 27 Apr 2025 00:00:00 GMT",
    "description": "This is a sample description.",
    "id": 4,
    "name": "Sample Evidence"
  },
  {
    "date": "Sun, 27 Apr 2025 00:00:00 GMT",
    "description": "This is a sample description.",
    "id": 5,
    "name": "Sample Evidence"
  },
  {
    "date": "Sun, 27 Apr 2025 00:00:00 GMT",
    "description": "This is a sample description.",
    "id": 6,
    "name": "Sample Evidence"
  },
  {
    "date": "Sun, 27 Apr 2025 00:00:00 GMT",
    "description": "This is a sample description.",
    "id": 7,
    "name": "Sample Evidence"
  },
  {
    "date": "Sun, 27 Apr 2025 00:00:00 GMT",
    "description": "This is a sample description.",
    "id": 8,
    "name": "Sample Evidence"
  },
  {
    "date": "Sun, 27 Apr 2025 00:00:00 GMT",
    "description": "This is a sample description.",
    "id": 9,
    "name": "Sample Evidence"
  }
]
        response = requests.get("http://localhost:5000/evidence")
        self.assertEqual(response.status_code, 200)
        actual = json.loads(response.text)  # Converts response to Python list/dict
        self.assertEqual(json.dumps(actual, sort_keys=True), json.dumps(expected, sort_keys=True))