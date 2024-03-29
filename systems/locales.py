import json
import re
import asyncio

language = None


async def language_input():
    global language
    language_chose = await get_input("Выберите язык / Select a language \n 1 - RU \n 2 - EN \n")
    if language_chose == '1':
        language = 'ru'
    elif language_chose == '2':
        language = 'en'
    return language


async def get_input(prompt):
    return await asyncio.get_event_loop().run_in_executor(None, input, prompt)


async def main():
    global language
    language = await language_input()
    print("Выбранный язык:", language)


asyncio.run(main())

# Загрузка файла локализации
with open('systems/localization.json', 'r', encoding='utf-8') as file:
    localization = json.load(file)


class filter_sort:

    def rename(self, param, lang=language, *args):
        text = f'{localization[self][param][lang]}'
        count = 0

        def replace_number(match):
            nonlocal count
            text_out = str(args[count])
            count += 1
            return text_out

        if args:
            pattern = r"@[\w\s]*@"
            reformate_text = re.sub(pattern, replace_number, text)
            return reformate_text
        else:
            return text


class output:

    def referenece(self, param, lang=language, *args):
        print(filter_sort.rename(self, param, lang, *args) + f'\n')
        print(f'-------------------------------------------------- \n')
