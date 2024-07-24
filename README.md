# Библиотека для взаимодействия с фигурами

## Описание
В файле **main.py** находится класс **Figure** который является интерфейсом для создания фигур. Есть два класса **Circle** и **Triangle** с определенными методами **.area**, для вычисления площади. У **Triangle** также есть метод для проверки является ли треугольник прямоугольным **.is_right()**.
Чтобы добавить новый класс фигуры, достаточно наследовать его от **Figure** и определить метод **.area**.

## Структура
- **main.py** - основной файл с фигурами
- **tests** - директория с юнит-тестами