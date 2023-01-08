#!/bin/bash

echo "ВЫПОЛНЯЮ МИГРАЦИИ"
python3 manage.py migrate

echo "ЗАПУСКАЮ СЕРВЕР"
python3 manage.py runserver 0:8000

