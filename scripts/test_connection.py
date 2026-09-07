"""
Tests the connection to Odoo via XML-RPC.
Prerequisite: Odoo is running (docker compose up), and the database has
already been set up once in the browser at http://localhost:8069.

Run with:  pip install python-dotenv --break-system-packages
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
    print("Odoo version:", version_info)

    uid = common.authenticate(DB, USERNAME, PASSWORD, {})
    if not uid:
        print("Login failed. Check the DB name/credentials in .env.")
        return

    print(f"Successfully logged in, user ID: {uid}")

    models = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object")

    # Example: read the first 5 partners (contacts)
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

    print("\nFirst 5 contacts in Odoo:")
    for p in partners:
        print(f"  - {p['name']} ({p.get('email') or 'no email'})")


if __name__ == "__main__":
    main()
