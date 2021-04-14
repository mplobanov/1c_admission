# Бекапы для бинарных файлов

### Пример

```python
from binary_difference.big_files import calculate_difference
from binary_difference.recover import recover

old_file = open('files/file1', 'rb')
new_file = open('files/file2', 'rb')
diff_file = open('files/file1_diff_file2', 'wb')

calculate_difference(old_file, new_file, diff_file)

old_file.close()
new_file.close()
diff_file.close()
```
В файле file1_diff_file2 появится бинарный слепок разницы файлов.
Чтобы восстановить файл, нужно:
```python
old_file = open('files/file1', 'rb')
diff_file = open('files/file1_diff_file2', 'rb')
recovered_file = open('files/recovered_file2', 'wb')

recover(old_file, diff_file, recovered_file)

old_file.close()
diff_file.close()
recovered_file.close()
```

Данные методы работают для файлов сколь угодно больших размеров.
Подробнее в [примерах](/examples/basics.py).

Для меньших файлов доступна более эфеективные способы получения дифф. слепков, они реализованы с помощью дифференциаторов.
На данный момент доступно два: Basic (аналогичен решению для больших файлов) и Dict (оптимальнее).
Их использование аналогично примерам выше, только вместо `calculate_difference(...)` и `recover(...)`следует использовать
`small_calc` и `small_calc_recover`.

Посмотрите [тесты](/tests/).