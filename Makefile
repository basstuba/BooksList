# 仮想環境作成
venv:
	python3 -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip && pip install django django-debug-toolbar

# アプリ名は make APP=yourappname createapp のように使う
APP?=yourappname

# Django コンテナでコマンドを実行する
exec := docker compose exec django

# シークレットキー作成
secretkey:
	$(exec) python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# アプリ作成（例: make APP=core createapp）
createapp:
	mkdir -p src/apps
	docker compose exec django bash -c "cd apps && django-admin startapp $(APP)"

# マイグレーションファイル作成
makemigrations:
	$(exec) python manage.py makemigrations

# マイグレーション適用
migrate:
	$(exec) python manage.py migrate

# スーパーユーザー作成
createsuperuser:
	$(exec) python manage.py createsuperuser

# コンテナにシェルで入る
shell:
	docker compose exec django bash

# Dockerコンテナのビルド
up:
	docker compose up -d --build