# TrabalhoToni

CRUD de cadastro de cachorros — Svelte 5 + Django REST.

## Rodar

**Backend:**
```
cd TrabalhoTonibe
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Frontend:**
```
cd Frontend
npm install
npm run dev
```

## API

- `GET /api/cachorros` — lista todos
- `POST /api/cadastrar` — cadastra novo
