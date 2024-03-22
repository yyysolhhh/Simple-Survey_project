#!/bin/bash

# 데이터베이스 초기화
#flask init-db
#aerich init
#aerich init -t app.configs.database_settings.TORTOISE_ORM
#aerich init-db
aerich migrate
aerich update

# Gunicorn으로 Flask 애플리케이션 실행
#exec gunicorn -w 4 -b 0.0.0.0:5000 "app:create_app()"

exec uvicorn app.main:app --proxy-headers --host 0.0.0.0 --port 8000
#exec uvicorn main:app --host 0.0.0.0 --port 80
