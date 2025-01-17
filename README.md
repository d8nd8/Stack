# Проверка сбалансированности скобок с использованием стека

Этот репозиторий содержит реализацию структуры данных "стек" на Python и функцию для проверки сбалансированности скобок в переданной строке.

## Возможности

- **Стек (Stack)**: Реализует основные операции со стеком, такие как `push`, `pop`, `peek`, и `is_empty`.
- **Проверка сбалансированности скобок**: Использует стек для определения, сбалансирована ли последовательность скобок (например, `()`, `{}`, `[]`).

## Класс Stack

Класс `Stack` предоставляет следующие методы:

- `is_empty()`: Проверяет, пуст ли стек.
- `push(item)`: Добавляет элемент в стек.
- `pop()`: Удаляет и возвращает верхний элемент из стека.
- `peek()`: Возвращает верхний элемент стека, не удаляя его.
- `size()`: Возвращает количество элементов в стеке.

## Функция для проверки скобок

Функция `is_balanced` принимает строку с последовательностью скобок и проверяет её на корректность вложенности. Она использует стек для хранения открывающих скобок и проверяет каждую закрывающую скобку на соответствие.

Пример работы программы:

- Вход: `"{[()]}"` 
- Выход: `"Сбалансированно"`

- Вход: `"{[(])}"` 
- Выход: `"Несбалансированно"`

## Использование

1. Создайте объект класса `Stack`.
2. Вызовите метод `is_balanced`, передав строку с последовательностью скобок.
3. Получите результат: сбалансирована ли последовательность.

## Пример кода

```python
st = Stack()
result = st.is_balanced("{[()]}")
print(result)  # Сбалансированно