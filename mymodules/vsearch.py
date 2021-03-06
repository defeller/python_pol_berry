def search4letters(phrase:str, letters:str='aeiou') -> set:
     """Возвращает множество букв из 'letters', найденных
     в указанной фразе."""
     return set(letters).intersection(set(phrase))


def search4vowels(word:str) -> set:
    """Выводит гласные, найденные в указанном слове."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))