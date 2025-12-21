# Lab 2: Docker Compose

## Docker Compose
Проект состоит из трех сервисов:
1. **app**: Приложение на FastAPI (сборка из Dockerfile)
2. **db**: База данных Redis 
3. **init_service**: Init-контейнер 

Сервисы `app` и `db` общаются через общую сеть. Данные Redis сохраняются в volume

## Запуск
```bash
docker-compose up --build
```

## Ответы на вопросы

### 1. Можно ли ограничивать ресурсы (например, память или CPU) для сервисов в docker-compose.yml?
Да, ресурсы ограничивать можно

Пример:
```yaml
services:
  app:
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
```


### 2. Как можно запустить только определенный сервис из docker-compose.yml, не запуская остальные?
Для этого нужно передать имя сервиса аргументом команде `up`:
```bash
docker-compose up <service_name>
```
Например:
```bash
docker-compose up db
```

