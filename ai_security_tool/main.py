# ai_security_tool/main.py

from ai_security.plugins.website import WebsiteScanner
from ai_security.plugins.app import AppScanner

class SecurityScanner:
    def __init__(self):
        self.website_scanner = WebsiteScanner()
        self.app_scanner = AppScanner()

    def scan_website(self, url):
        """Initiate a scan for a website."""
        self.website_scanner.scan(url)

    def scan_application(self, app_id):
        """Initiate a scan for an application."""
        self.app_scanner.scan(app_id)

