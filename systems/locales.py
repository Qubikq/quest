import copy
import json
import re

# Загрузка файла локализации
with open('systems/localization.json', 'r', encoding='utf-8') as file:
    localization = json.load(file)


class filter_sort:

    def rename(self, param, language, *args):
        text = f'{localization[self][param][language]}'
        count = 0

        if args:
            def replace_number(match):
                nonlocal count
                text_out = str(args[count])
                count += 1
                return text_out

            pattern = r"@[\w\s]*@"
            reformate_text = re.sub(pattern, replace_number, text)
            return reformate_text
        else:
            return text


class output:
    def referenece(self, param, language, *args):
        print(filter_sort.rename(self, param, language, *args) + f'\n')
        print(f'-------------------------------------------------- \n')
