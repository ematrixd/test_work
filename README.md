# Сортировка по среднему значению рейтинга

### Установка

```git
// клонирование проекта
git clone
cd tests_worck

// создаем виртуальное окружение
python3 -m venv venv
sourse venv/bin/activate

// установка зависимостей
pip3 install -r requrements.txt

// запуск приложения
python3 main.py --files products1.csv products2.csv --report average_rating

// запуск тестов
python3 -m unittest tests.test_avarage_rating -v
python3 -m unittest tests.test_csv_reader -v

```
