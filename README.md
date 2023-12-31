# QRKot

## Технологии
- Python 3.9
- FastAPI 0.78
- FastAPI-Users 10.0.4
- SQLAlchemy 1.4.36
- aioSQLite 0.17.0
- Pydantic 1.9.1
- Alembic 1.7.7
## Описание
### Проекты
В Фонде QRKot может быть открыто несколько целевых проектов. У каждого проекта есть название, описание и сумма, которую планируется собрать. После того, как нужная сумма собрана — проект закрывается.
Пожертвования в проекты поступают по принципу First In, First Out: все пожертвования идут в проект, открытый раньше других; когда этот проект набирает необходимую сумму и закрывается — пожертвования начинают поступать в следующий проект.
### Пожертвования
Каждый пользователь может сделать пожертвование и сопроводить его комментарием. Пожертвования не целевые: они вносятся в фонд, а не в конкретный проект. Каждое полученное пожертвование автоматически добавляется в первый открытый проект, который ещё не набрал нужную сумму. Если пожертвование больше нужной суммы или же в Фонде нет открытых проектов — оставшиеся деньги ждут открытия следующего проекта. При создании нового проекта все неинвестированные пожертвования автоматически вкладываются в новый проект.
### Пользователи
Целевые проекты создаются администраторами сайта. Любой пользователь может видеть список всех проектов, включая требуемые и уже внесенные суммы. Это касается всех проектов — и открытых, и закрытых. Зарегистрированные пользователи могут отправлять пожертвования и просматривать список своих пожертвований.

## Установка и запуск проекта
Загрузите проект:
```bash
git clone https://github.com/Semavova/cat_charity_fund
```
Создайте виртуальное окружение и обновите pip:
```bash
python -m venv venv
python -m pip install --upgrade pip
```
Установите зависимости:
```bash
pip install -r requirements.txt
```
Примените миграции:
```bash
alembic upgrade head
```
Запустите проект:
```bash
uvicorn app.main:app
```
В корневой папке создайте файл *.env* и добавьте в него свои данные (при необходимости):

```bash
APP_TITLE=         # Название приложения
APP_DESCRIPTION=   # Описание приложения
DATABASE_URL=      # Путь подключения к БД
```


## Документации проекта QRKot

При запущенном проекте откройте ссылку с документацией:

```bash
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```

Автор: [Владимир Семочкин](https://github.com/Semavova)
