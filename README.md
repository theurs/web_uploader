# Простой сервис загрузки аудиофайлов для Telegram бота

Этот проект представляет собой простой веб-сервис на Python с использованием Flask, который позволяет пользователям загружать аудиофайлы через веб-интерфейс. После загрузки генерируется специальная ссылка для Telegram бота, которую пользователь может использовать для дальнейшей обработки файла в боте.

## Особенности

*   Веб-интерфейс для загрузки аудиофайлов.
*   Поддержка загрузки с мобильных устройств и компьютеров (адаптивный дизайн).
*   Отображение процесса загрузки.
*   Генерация уникальных имен файлов.
*   Ограничение на размер загружаемого файла и общий размер папки с загрузками.
*   Автоматическая очистка старых файлов при превышении лимита размера папки.
*   Формирование ссылки для Telegram бота с командой `/start`, передающей имя загруженного файла.

## Технологии

*   **Python:** Основной язык программирования.
*   **Flask:** Микрофреймворк для создания веб-приложений на Python.
*   **HTML:**  Структура веб-страницы.
*   **CSS:**  Стилизация веб-страницы для адаптивности.
*   **JavaScript:**  Обработка отправки формы и отображение прогресса загрузки на стороне клиента.

## Как запустить

Следуйте этим инструкциям, чтобы запустить проект на своем локальном компьютере:

1. **Клонируйте репозиторий:**

    ```bash
    git clone <адрес_вашего_репозитория>
    cd <название_репозитория>
    ```

2. **Создайте виртуальное окружение (рекомендуется):**

    ```bash
    python -m venv venv
    ```

    *   Для Linux/macOS:

        ```bash
        source venv/bin/activate
        ```

    *   Для Windows:

        ```bash
        venv\Scripts\activate
        ```

3. **Установите зависимости:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Настройте конфигурацию:**

    *   Откройте файл `cfg.py` и настройте следующие параметры:
        *   `BOT_LINK`: Ссылка на вашего Telegram бота (например, `https://t.me/your_bot`).
        *   `UPLOAD_FOLDER`: Папка для хранения загруженных файлов (по умолчанию `uploads`).
        *   `ALLOWED_EXTENSIONS`:  Список разрешенных расширений файлов для загрузки.
        *   `MAX_FILE_SIZE`: Максимальный размер загружаемого файла в байтах.
        *   `MAX_UPLOAD_FOLDER_SIZE`: Максимальный общий размер папки с загрузками в байтах.
        *   `ADDRESS`: IP-адрес для запуска сервера (по умолчанию `127.0.0.1`).
        *   `PORT`: Порт для запуска сервера (по умолчанию `35709`).
        *   `DEBUG`: Включить режим отладки Flask (установите `True` для разработки, `False` для продакшена).

5. **Запустите приложение:**

    ```bash
    python app.py
    ```

    После запуска вы увидите сообщение о том, что сервер запущен, например: `* Running on http://127.0.0.1:35709`.

## Как использовать

1. Откройте веб-браузер и перейдите по адресу, указанному при запуске приложения (например, `http://127.0.0.1:35709`).
2. На странице вы увидите форму для загрузки аудиофайла.
3. Нажмите кнопку "Выберите файл" и выберите аудиофайл на своем устройстве.
4. Нажмите кнопку "Загрузить".
5. Вы увидите индикатор процесса загрузки.
6. После успешной загрузки, ссылка для вашего Telegram бота откроется в новой вкладке браузера. Вы можете нажать "Start" в Telegram, чтобы ваш бот обработал загруженный файл.

## Конфигурация (`cfg.py`)

| Параметр                | Описание                                                                                   | По умолчанию                           |
| ----------------------- | ------------------------------------------------------------------------------------------ | -------------------------------------- |
| `BOT_LINK`              | Ссылка на вашего Telegram бота.                                                           | `'https://t.me/kun_test_sun_bot'`      |
| `UPLOAD_FOLDER`         | Папка для хранения загруженных файлов.                                                     | `'uploads'`                            |
| `ALLOWED_EXTENSIONS`    | Набор разрешенных расширений файлов для загрузки.                                          | `{'mp3', 'wav', 'ogg', ...}`           |
| `MAX_FILE_SIZE`         | Максимальный размер загружаемого файла в байтах.                                            | `314572800` (300 MB)                   |
| `MAX_UPLOAD_FOLDER_SIZE`| Максимальный общий размер папки с загрузками в байтах.                                     | `524288000` (500 MB)                   |
| `ADDRESS`               | IP-адрес для запуска сервера.                                                            | `'127.0.0.1'`                          |
| `PORT`                  | Порт для запуска сервера.                                                                 | `35709`                                |
| `DEBUG`                 | Включает режим отладки Flask. Установите `True` для разработки, `False` для продакшена. | `False`                                |

## Планируемые улучшения

*   Добавление аутентификации для ограничения доступа к загрузке.
*   Реализация удаления загруженных файлов через веб-интерфейс.
*   Интеграция с более продвинутыми сервисами транскрибации.
*   Возможность предпросмотра загруженных файлов.

## Лицензия

[Здесь можно указать тип лицензии, например, MIT License]
