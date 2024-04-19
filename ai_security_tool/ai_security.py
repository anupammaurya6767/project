# ai_security/ai_security.py

from ai_security.scanner import Scanner
from ai_security.reporting import Reporting

class SecurityScanner:
    def __init__(self):
        self.scanner = Scanner()
        self.reporting = Reporting()

    def scan_website(self, url):
        """Initiate a scan for a website."""
        scan_results = self.scanner.scan_website(url)
        self.reporting.generate_report(scan_results)

    def scan_application(self, app_id):
        """Initiate a scan for an application."""
        scan_results = self.scanner.scan_application(app_id)
        self.reporting.generate_report(scan_results)
