# Odoo + AI Integration Project

Learning project: an AI assistant that talks to an Odoo ERP system using natural language.

## Phase 1 – Get Odoo running locally

1. Install Docker Engine (native in WSL2/Ubuntu) and start it.
2. Open a terminal in this folder.
3. Start the containers:
```
   docker compose up -d
```
4. Wait a bit (~30 sec), then open in your browser:
```
   http://localhost:8069
```
5. Odoo asks for initial setup: database name `odoo`, choose any email/password (remember them!), check "Load demo data" (handy for testing).
6. After setup you land in the Odoo dashboard. Done — Odoo is running.

## Phase 2 – Test the API connection

1. Copy `.env.example` to `.env`:
```
   cp .env.example .env
```
2. Fill in `.env` with the credentials you chose in step 5 above.
3. Install Python dependencies:
```
   pip install -r requirements.txt --break-system-packages
```
4. Test the connection:
```
   python scripts/test_connection.py
```
5. Expected output: the Odoo version + a list of test contacts.

## Phase 3 – Connect the AI (next step, still open)

- Add the Anthropic API key to `.env` (`ANTHROPIC_API_KEY`)
- Define a function-calling tool that internally reuses the `test_connection.py` logic
  (e.g. `get_overdue_invoices()`, `get_open_orders()`)
- First task: answer natural-language questions like
  "Which invoices are overdue?"

## Folder structure

```
odoo-ai-integration/
├── docker-compose.yml     # Odoo + PostgreSQL setup
├── .env.example           # Template for credentials
├── requirements.txt       # Python packages
├── addons/                # For custom Odoo modules (currently empty)
└── scripts/
    └── test_connection.py # Tests the Odoo API connection
```

## Storage requirements

- Odoo + PostgreSQL (base): approx. 2-3 GB
- With test data/logs: approx. 5-10 GB
- Additional space for future local AI models (Ollama etc.): 100+ GB

## Setup notes

- Runs on native Docker Engine inside WSL2 (Ubuntu), not Docker Desktop.
- Uses `docker compose` (Compose V2 plugin), not the legacy `docker-compose` binary.
