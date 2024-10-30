from flask import Flask
import logging

app = Flask(__name__)

custom_logger = logging.getLogger('custom_logger')
custom_logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

custom_logger.addHandler(file_handler)


@app.route('/')
def main_page():
    custom_logger.info("Запрошена основная страница")
    return "Добро пожаловать на главную страницу!"


@app.route('/debug')
def debug_page():
    custom_logger.debug("Запрошена страница отладки")
    return "Это страница для отладки!"


@app.route('/error')
def error_page():
    try:
        result = 1 / 0  # Искусственная ошибка
    except ZeroDivisionError as e:
        custom_logger.error("Ошибка деления на ноль!", exc_info=True)
    return "Произошла ошибка!"


@app.route('/critical')
def critical_page():
    custom_logger.critical("Критическая ошибка на этой странице!")
    return "Критическая ошибка!"


if __name__ == '__main__':
    app.run(debug=True)
