## Трекер полезных привычек

### О проекте:

Приложение "Трекер полезных привычек" создано для помощи людям в привитии полезных привычек. Создайте привычку, выберете
с какой периодичностью и в какое время вы хотите выполнять ее, и вам в Telegram будет приходить сообщение, что пришло
время для выполнения привычки. С нашим приложением вы никогда не пропустите свои полезные занятия и закрепите их
выполнение на постоянной основе.

### Используемые технологии:

- Python
- Django
- Django REST Framework
- PostgreSQL
- Redis
- Celery
- CORS

### Настройка проекта:

#### 1. Клонирование проекта

Клонируйте репозиторий используя команду:

```sh
git clone https://github.com/Fish8558/Course_7_habit_tracker.git
```

#### 2. Настройка виртуального окружения и установка зависимостей

Создает виртуальное окружение:

```text
python3 -m venv venv
```

Активирует виртуальное окружение:

```text
source venv/bin/activate          # для Linux и Mac
venv\Scripts\activate.bat         # для Windows
```

Устанавливает зависимости:

```text
pip install -r requirements.txt
```

#### 3. Редактирование настроек .env.sample:

В корне проекта переименуйте файл .env.sample в .env и отредактируйте параметры:

```text
# Postgresql
POSTGRES_ENGINE="postgresql_psycopg2" - используем psycopg
POSTGRES_DB="db_name" - название вашей БД
POSTGRES_USER="postgres" - имя пользователя БД
POSTGRES_PASSWORD="secret" - пароль пользователя БД
POSTGRES_HOST="host" - можно указать "localhost" или "127.0.0.1"
POSTGRES_PORT=port - указываете порт для подключения по умолчанию 5432

# Django
SECRET_KEY=secret_key - секретный ключ django проекта
DEBUG=True - режим DEBUG

# Telegram API
TELEGRAM_API_KEY='secret key' - секретный ключ для подключения бота Telegram  

# Redis
REDIS=redis://redis:6379 - данные redis
```

#### 4. Настройка БД:

Примените миграции:
```text
python manage.py migrate
```

Для создания суперюзера используйте команду:

```text
python manage.py csu
```

Установите Redis:

- Linux команда:
```text
sudo apt install redis; 
или 
sudo yum install redis;
```

- macOS команда:
```text
brew install redis;
```

- Windows инструкция: [перейти на Redis docs](https://redis.io/docs/install/install-redis/install-redis-on-windows/)

### Использование

> Для запуска локально проекта наберите в терминале команду:

```text
python manage.py runserver
```

Для запуска периодических задач запустите worker и beat в соседних окнах терминала проекта:

- Для запуска worker:
```text
celery -A config worker -l INFO
```

- Для запуска beat:
```text
celery -A config beat -l INFO
```

> Для запуска проекта через Docker:

- установите Docker себе в систему, перейдя по [ссылке](https://docs.docker.com/engine/install/)
- для сборки проекта и запуска введите команду:

```text
docker-compose up -d --build
```

- перейдите по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)