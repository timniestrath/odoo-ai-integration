"""
Testet die Verbindung zu Odoo über XML-RPC.
Voraussetzung: Odoo läuft (docker-compose up), Datenbank wurde im Browser
unter http://localhost:8069 bereits einmal eingerichtet.

Ausführen mit:  pip install python-dotenv --break-system-packages
                python scripts/test_connection.py
"""

import os
import xmlrpc.client
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("ODOO_URL", "http://localhost:8069")
DB = os.getenv("ODOO_DB", "odoo")
USERNAME = os.getenv("ODOO_USERNAME", "admin")
PASSWORD = os.getenv("ODOO_PASSWORD", "admin")


def main():
    common = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common")
    version_info = common.version()
    print("Odoo-Version:", version_info)

    uid = common.authenticate(DB, USERNAME, PASSWORD, {})
    if not uid:
        print("Login fehlgeschlagen. Prüfe DB-Name/Zugangsdaten in .env.")
        return

    print(f"Erfolgreich eingeloggt, User-ID: {uid}")

    models = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object")

    # Beispiel: die ersten 5 Partner (Kontakte) auslesen
    partner_ids = models.execute_kw(
        DB, uid, PASSWORD,
        "res.partner", "search",
        [[]], {"limit": 5}
    )
    partners = models.execute_kw(
        DB, uid, PASSWORD,
        "res.partner", "read",
        [partner_ids], {"fields": ["name", "email"]}
    )

    print("\nErste 5 Kontakte in Odoo:")
    for p in partners:
        print(f"  - {p['name']} ({p.get('email') or 'keine E-Mail'})")


if __name__ == "__main__":
    main()
