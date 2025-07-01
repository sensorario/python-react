# 📇 Rubrica Contatti – Backend Python + FastAPI

Questo progetto implementa una **rubrica di contatti** con API RESTful scritte in Python. È parte di un'applicazione full-stack che prevede un'interfaccia utente frontend in React (in sviluppo).

---

## 🎯 Obiettivo

Fornire un'API semplice ma moderna per la gestione di contatti, includendo funzionalità come:

- Visualizzazione dei contatti
- Aggiunta di nuovi contatti
- Validazione dei dati in input (es. email)
- Struttura manutenibile e pronta per essere estesa (es. con un database)

---

## 🧰 Tecnologie e strumenti utilizzati

### 🐍 Backend

| Strumento        | Scopo                                                                 |
|------------------|-----------------------------------------------------------------------|
| **Python 3.13**  | Linguaggio principale                                                 |
| **FastAPI**      | Framework asincrono per la creazione di API                          |
| **Pydantic v2**  | Validazione dei dati e definizione degli schemi                      |
| **Uvicorn**      | Web server ASGI per eseguire l'app FastAPI                           |
| **httpx**        | Client HTTP asincrono (usato nei test)                               |

### 🧪 Testing e qualità del codice

| Strumento        | Scopo                                                                 |
|------------------|-----------------------------------------------------------------------|
| **pytest**       | Framework per i test automatici                                       |
| **mypy**         | Controllo statico dei tipi Python                                     |
| **pyright** (opz.) | Alternativa a `mypy`, supportata da VSCode                        |
| **black**        | Formatter automatico per il codice                                   |
| **ruff**         | Linter moderno e velocissimo (sostituisce `flake8`, `isort`, ecc.)   |

---

## 🗂️ Struttura del progetto

```
python-react/
├── backend/
│   ├── main.py             # Entrypoint FastAPI
│   ├── app/
│   │   ├── __init__.py     # Pacchetto vuoto per import
│   │   ├── routes.py       # API REST
│   │   ├── schemas.py      # Schemi Pydantic per validazione dati
│   │   └── models.py       # (non ancora usato, riservato a futuro DB)
│   ├── tests/              # Test automatici
│   │   └── test_contacts.py
│   └── pyproject.toml      # Configurazione di black, ruff, mypy, pytest
```

---

## 🚀 Come avviare il server

### 1. Crea ambiente virtuale

```bash
python -m venv .venv
source .venv/bin/activate  # o .venv\Scripts\activate su Windows
```

### 2. Installa le dipendenze

```bash
pip install -r requirements.txt
```

Oppure manualmente:

```bash
pip install fastapi uvicorn pydantic[email] black ruff mypy pytest httpx
```

### 3. Avvia il server FastAPI

```bash
cd backend
uvicorn main:app --reload
```

Visita [http://localhost:8000/docs](http://localhost:8000/docs) per la documentazione Swagger generata automaticamente.

---

## ✅ Come eseguire i test

Dalla root del progetto (`python-react/`):

```bash
PYTHONPATH=. pytest backend/tests
```

---

## ✨ Da fare (prossimi step)

- ✅ Aggiunta frontend React con Vite
- ⏳ Persistenza dati su database (es. SQLite o PostgreSQL)
- ⏳ Autenticazione e autorizzazione utenti
- ⏳ Deployment (Docker, Render, etc.)

---

## 📄 Licenza

Questo progetto è open-source e può essere riutilizzato liberamente per scopi didattici e personali.
