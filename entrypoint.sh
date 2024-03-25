#!/bin/bash

# 데이터베이스 초기화
aerich init-db

exec uvicorn app.main:app --proxy-headers --host 0.0.0.0 --port 8000
