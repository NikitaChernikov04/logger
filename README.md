## Описание проекта

1. **Flask Web-сервер**: Приложение запускает локальный сервер, обрабатывая запросы к разным маршрутам (`/`, `/debug`, `/error`, `/critical`), каждый из которых выполняет отдельные действия.

2. **Логирование**: Используется модуль `logging` для записи событий (информационных, отладочных, ошибок и критических) в файл `app.log`. Логи сохраняются с метками времени, уровня события и подробным сообщением, что помогает в мониторинге и отладке.

3. **Маршруты**:
   - **Главная страница** (`/`) — приветственный текст и информационный лог.
   - **Debug-страница** (`/debug`) — сообщение для отладки.
   - **Страница ошибки** (`/error`) — симулирует ошибку (деление на ноль), записывая ошибку в лог.
   - **Критическая страница** (`/critical`) — фиксирует критическое событие.

4. **Запуск**: Сервер запускается локально с `app.run(debug=True)`, что позволяет тестировать приложение на локальной машине.


![image](https://github.com/user-attachments/assets/d65f988d-fffc-4088-b6e3-b6ecd585a785)
