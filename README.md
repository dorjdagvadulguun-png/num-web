# МУИС - Монгол Улсын Их Сургууль
## Вэб систем

---

## Технологи
- **Database:** Docker + MySQL
- **Backend:** Python Flask (REST API)
- **Frontend:** HTML + CSS (Bootstrap) + JavaScript

---

## Эхлүүлэх

### 1. Docker асаах
```bash
cd ~/num-web
docker-compose up -d
```

### 2. Вэб сервер асаах
```bash
cd ~/num-web/frontend
python3 -m http.server 8080
```

### 3. Браузерт нээх
| Хуудас | Хаяг |
|--------|------|
| Үндсэн хуудас | http://localhost:8080 |
| Админ хуудас | http://localhost:8080/admin.html |
| API | http://localhost:5001 |

---

## Админ нэвтрэх
| | |
|--|--|
| Нэвтрэх нэр | admin |
| Нууц үг | admin123 |

---

## API Endpoints
| Метод | Хаяг | Тайлбар |
|-------|------|---------|
| GET | /api/introduction | Танилцуулга харах |
| POST | /api/introduction | Танилцуулга нэмэх |
| PUT | /api/introduction/:id | Танилцуулга засах |
| DELETE | /api/introduction/:id | Танилцуулга устгах |
| GET | /api/teachers | Багш нар харах |
| POST | /api/teachers | Багш нэмэх |
| PUT | /api/teachers/:id | Багш засах |
| DELETE | /api/teachers/:id | Багш устгах |
| GET | /api/programs | Хөтөлбөр харах |
| POST | /api/programs | Хөтөлбөр нэмэх |
| PUT | /api/programs/:id | Хөтөлбөр засах |
| DELETE | /api/programs/:id | Хөтөлбөр устгах |

---

## Файлын бүтэц
num-web/
├── docker-compose.yml
├── README.md
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
└── frontend/
├── index.html
├── admin.html
└── style.css
# num-web
