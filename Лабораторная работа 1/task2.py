# TODO Найдите количество книг, которое можно разместить на дискете
symbols_in_book = 50 * 25 * 100
bytes_in_book = 4 * symbols_in_book
size_in_kb = 1.44 * 1024
size_in_b = size_in_kb * 1024
print("Количество книг, помещающихся на дискету:", int(size_in_b // bytes_in_book))
