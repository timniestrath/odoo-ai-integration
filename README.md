# Odoo + KI Integrationsprojekt

Lernprojekt: KI-Assistent, der über natürliche Sprache mit einem Odoo-ERP-System spricht.

## Phase 1 – Odoo lokal zum Laufen bringen

1. Docker Desktop installieren (falls noch nicht vorhanden) und starten.
2. In diesem Ordner ein Terminal öffnen.
3. Container starten:
   ```
   docker-compose up -d
   ```
4. Kurz warten (~30 Sek.), dann im Browser öffnen:
   ```
   http://localhost:8069
   ```
5. Odoo fragt nach Erstkonfiguration: Datenbankname `odoo`, E-Mail/Passwort frei wählen (merken!), Demo-Daten aktivieren anhaken (praktisch zum Testen).
6. Nach dem Setup bist du im Odoo-Dashboard. Fertig – Odoo läuft.

## Phase 2 – API-Verbindung testen

1. `.env.example` kopieren zu `.env`:
   ```
   cp .env.example .env
   ```
2. In `.env` die Zugangsdaten eintragen, die du in Schritt 5 oben vergeben hast.
3. Python-Abhängigkeiten installieren:
   ```
   pip install -r requirements.txt --break-system-packages
   ```
4. Verbindung testen:
   ```
   python scripts/test_connection.py
   ```
5. Erwartete Ausgabe: Odoo-Version + eine Liste von Testkontakten.

## Phase 3 – KI anbinden (nächster Schritt, noch offen)

- Anthropic API-Key in `.env` eintragen (`ANTHROPIC_API_KEY`)
- Function-Calling-Tool definieren, das intern `test_connection.py`-Logik nutzt
  (z.B. `get_overdue_invoices()`, `get_open_orders()`)
- Erste Aufgabe: Auf natürliche Sprache antworten wie
  "Welche Rechnungen sind überfällig?"

## Ordnerstruktur

```
odoo-ki-projekt/
├── docker-compose.yml     # Odoo + PostgreSQL Setup
├── .env.example           # Vorlage für Zugangsdaten
├── requirements.txt       # Python-Pakete
├── addons/                # Für eigene Odoo-Module (aktuell leer)
└── scripts/
    └── test_connection.py # Testet die Odoo-API-Verbindung
```

## Speicherbedarf

- Odoo + PostgreSQL (Basis): ca. 2-3 GB
- Mit Testdaten/Logs: ca. 5-10 GB
- Für spätere lokale KI-Modelle (Ollama etc.) zusätzlich einplanen: 100+ GB
