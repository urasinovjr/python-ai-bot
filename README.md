# Python Ai Bot

## 📌 Описание проекта
Проект **"Python Ai Bot"** основан на готовой модели GigaChat, разработанной компанией "Sber". Идея заключается в разработке своего собственного бота-помощника, который будет помогать решать разнообразные задачи: написание кода, ответы на вопросы, подготовка к собеседованиям и так далее.

### 🔧 Основные компоненты:
- 🚀 **GigaChat-2-Max** – модель от компании "Sber".
- 🎨 **Requests** – библиотека для интеграции модели GigaChat в созданный чат-бот.
- 🌐 **Streamlit UI** – веб-интерфейс для удобного тестирования чат-бота.

## 🛠️ Технологический стек
Проект использует следующие технологии:
- 🐍 **Python 3.10+** – основной язык разработки
- 🚀 **GigaChat-2-Max** – модель от компании "Sber".
- 🖥️ **Streamlit** – веб-интерфейс
- 🛠️ **Requests** – интеграция модели GigaChat в чат-бот

## 🚀 Установка и настройка
### 1️⃣ Клонирование репозитория
```bash
git clone https://github.com/urasinovjr/python-ai-bot.git
cd python-ai-bot
```

### 2️⃣ Создание виртуальной среды и установка зависимостей
```bash
python3 -m venv venv # для Linux/Mac
# или
python -m venv venv # для Windows

source venv/bin/activate  # для Linux/Mac
# или
venv\Scripts\activate  # для Windows

pip install -r requirements.txt
```
### 3️⃣ Регистрация GigaChat API
```bash
В папке "/.streamlit" находится файл "secrets.toml";

В нем отображено две строчки: "CLIENT_ID" и "SECRET";

Эти данные берутся здесь -> "https://developers.sber.ru/studio/";

Создаем бесплатно "GigaChat API" -> называем, как угодно;

В левой части экрана будет нарисован ключик с подписью ("Настройка API")

Генерируем "Authorization Key" -> Нажимаем "Вы также можете использовать пару Client ID:Client Secret" и у Вас откроется пара "Client ID" и "Client Secret"

Вставляем "Client ID" в файл "secrets.toml" в строчку "CLIENT"

Вставляем "Client Secrets" в файл "secrets.toml" в строчку "SECRET"

Не забываем сохранить!
```

### 4️⃣ Запуск Streamlit-интерфейса
```bash
streamlit run main.py
```

После запуска откройте [🌍 http://localhost:8501](http://localhost:8501) в браузере.

---
### 🆘 Изменение названия бота
```bash
В файле "main.py" находится строчка -> "st.title("AbionaBot")"

Замените "AbionaBot" на любое название
```
---

🚀 **Спасибо за фидбек!** 🔥
