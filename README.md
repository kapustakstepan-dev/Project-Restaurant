# RetroBite — Project Restaurant 🍔

A full-stack, retro-themed restaurant web application built with **Flask** and **PostgreSQL**. Customers can browse the menu, place orders, and book tables, while admins manage the menu, orders, reservations, and users from a dedicated dashboard.

## Features

- **Menu browsing** with categories (Salads, Drinks, Combos, Desserts, Main Dishes/Burgers) and detailed item pages (price, weight, ingredients, description).
- **User accounts** — registration and login with hashed passwords (`bcrypt`) via `Flask-Login`.
- **Shopping basket & checkout** — session-based cart, order confirmation, and order history (`My Orders`).
- **Table reservations** — book a table by date/time and table type, with a personal reservations list and cancellation.
- **Email receipts** — order receipts sent by email through `Flask-Mail` (SMTP), plus an optional macOS-only "Send via Mail.app" flow using AppleScript.
- **Admin dashboard** (`/admin`) with full CRUD for:
  - Menu items (add / edit / delete / activate-deactivate)
  - Orders (update status)
  - Reservations (update status)
  - Users (change role)
- **Internationalization** — UI available in English, Spanish, and Ukrainian, switchable at runtime (`static/js/translate.js`).
- **Light/dark theme toggle** with preference saved in the browser.
- **Animations** powered by `anime.js`.
- **SEO basics** — `robots.txt` and `sitemap.xml`.
- Custom **404** error page.

## Tech Stack

| Layer            | Technology                                              |
|-------------------|----------------------------------------------------------|
| Backend           | Python, [Flask](https://flask.palletsprojects.com/)      |
| Auth              | Flask-Login, bcrypt                                       |
| Database          | PostgreSQL, SQLAlchemy ORM (with a `JSONB` column for orders) |
| Email             | Flask-Mail (SMTP)                                          |
| Frontend          | Jinja2 templates, vanilla JavaScript, CSS                 |
| Animations        | anime.js                                                   |

## Project Structure

```
Project-Restaurant/
└── ProyectRestourant/          # Application root
    ├── online_restaurant.py    # Flask app & routes (entry point)
    ├── back/
    │   └── BD/
    │       └── online_restaurant_db.py   # SQLAlchemy models & DB setup
    ├── templates/               # Jinja2 HTML templates
    ├── static/
    │   ├── css/style.css
    │   ├── js/                  # main.js, theme.js, translate.js, animations.js, invoice.js
    │   ├── libs/anime.min.js
    │   └── image/                # Menu item photos
    ├── robots.txt
    └── sitemap.xml
```

## Data Model

- **Users** — nickname, email, hashed password, role (`client` / `admin`), plus related reservations and orders.
- **Menu** — name, weight, ingredients, description, price, category, active flag, image filename.
- **Reservation** — start time, table type, status, linked to a user.
- **Orders** — order items (stored as JSON), total price, status, order time, linked to a user.

## Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL database
- A Gmail (or other SMTP) account if you want email receipts to work

### 1. Clone the repository

```bash
git clone https://github.com/kapustakstepan-dev/Project-Restaurant.git
cd Project-Restaurant/ProyectRestourant
```

### 2. Create a virtual environment and install dependencies

The project does not currently ship a `requirements.txt`; install the packages the app imports:

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install flask flask-login flask-mail sqlalchemy psycopg2-binary bcrypt python-dotenv
```

### 3. Configure environment variables

Create a `.env` file inside `ProyectRestourant/` with:

```env
SECRET_KEY=your-secret-key

DB_USER=your_db_user
DB_PASS=your_db_password
DB_HOST=your_db_host
DB_PORT=5432
DB_NAME=your_db_name

MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_app_password
MAIL_DEFAULT_SENDER=your_email@gmail.com
```

> For Gmail, use an **App Password** rather than your regular account password.

### 4. Run the app

```bash
python online_restaurant.py
```

The database tables are created automatically on startup (`init_db()`), and the app runs on **http://localhost:5001** by default.

## Usage

- Visit `/register` to create an account, then `/login` to sign in.
- Browse `/menu`, add items to your basket, and check out at `/create_order`.
- Book a table at `/reservation` and manage bookings at `/my_reservations`.
- Promote a user to `admin` (directly in the database, or via the admin panel once one admin exists) to access `/admin` and manage menu items, orders, reservations, and user roles.
