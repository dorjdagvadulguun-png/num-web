# num-web

Монгол Улсын Их Сургууль (National University of Mongolia) - Admin Panel & Website

## Project Structure

- `index.html` - Main public website
- `admin.html` - Admin dashboard
- `backend/app.py` - Flask API server
- `style.css` - Shared styles
- `docker-compose.yml` - Docker orchestration

## Features

- Admin login system
- Manage Introduction, Teachers, Programs, and Menu
- MySQL database
- RESTful API
- Responsive Bootstrap UI

## Setup

### Docker (Recommended)

```bash
docker-compose up
```

Access:
- Website: http://localhost:8080
- Admin: http://localhost:8080/admin.html
- API: http://localhost:5001

### Default Credentials

- Username: `admin`
- Password: `admin123`

## Database

MySQL 8.0 with tables for:
- admin
- menu
- introduction
- teachers
- programs
