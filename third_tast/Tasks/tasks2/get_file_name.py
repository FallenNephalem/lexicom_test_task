
def delete_dublicates_from_string(string: str):
    exist_symbols = set()
    result_string = ''
    for sym in string:
        if sym not in exist_symbols:
            result_string += sym
            exist_symbols.add(sym)
    return result_string


def get_file_name(file_names: list[str]):
    file_names = [delete_dublicates_from_string(name) for name in file_names]
    file_names_len = len(max(file_names, key=lambda name: len(name)))
    return [name+'_'*(file_names_len - len(name)) if len(name) < file_names_len else name for name in file_names]


print(get_file_name(['ssbfd', 'bb', 'aaa', 'qq']))
