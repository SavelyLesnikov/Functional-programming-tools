def all_variants(text):
    """
    На первом этапе функция возвращает каждый символ поочерёдно, выводя его в отдельную строку.
    На втором этапе функция возвращает два символа поочерёдно, выводя их в отдельную строку.
    На третьем этапе функция возвращает три символа поочерёдно, выводя их в отдельную строку.
    """
    for i in text:
        yield i
    for j in range(0, len(text)-1):
        yield text[j:j + 2]
    for k in range(0, len(text)-2):
        yield text[k:k + 3]


a = all_variants('Pedro')
for i in a:
    print(i)
