# William English Backend

Backend API service built with FastAPI and SQLAlchemy.

## Cài đặt

### Yêu cầu hệ thống

- Python 3.12+
- MySQL/MariaDB
- Redis (cho Celery task queue)

### Thiết lập môi trường phát triển

1. Clone dự án:

```bash
git clone <repository_url>
cd william_english_be
```

2. Cài đặt dependencies:

```bash
poetry install
```

3. Tạo file `.env` từ file mẫu:

```bash
cp .env.example .env
```

4. Chỉnh sửa các thông tin cấu hình trong file `.env`

5. Khởi tạo cơ sở dữ liệu:

```bash
python scripts/initialize_app.py
```

## Chạy ứng dụng

### Chế độ phát triển

```bash
poetry run uvicorn william_english_be.main:app --reload
```

### Chế độ sản xuất

```bash
poetry run gunicorn william_english_be.main:app -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000
```

## Cấu trúc dự án

```
william_english_be/
├── alembic.ini             # Cấu hình Alembic migrations
├── migrations/             # Database migrations
│   └── versions/
├── pyproject.toml          # Cấu hình project và dependencies
├── scripts/                # Utility scripts
│   ├── init_db.py
│   └── initialize_app.py
├── src/
│   └── william_english_be/ # Main package
│       ├── api/            # API endpoints
│       │   └── v1/
│       ├── core/           # Core settings, config
│       ├── db/             # Database connection
│       ├── models/         # SQLAlchemy models
│       ├── schemas/        # Pydantic schemas
│       ├── services/       # Business logic
│       └── utils/          # Utility functions
└── tests/                  # Tests
    └── api/
        └── v1/
```

## API Documentation

Sau khi chạy ứng dụng, truy cập:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
#   w i l l i a m _ e n g l i s h _ b e  
 # william_english_be
