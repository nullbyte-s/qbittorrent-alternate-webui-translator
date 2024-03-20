import os
import fnmatch
import re


def read_translation_file(file_path):
    translations = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().strip()
        blocks = content.split('\n\n')
        for block in blocks:
            lines = block.strip().split('\n')
            english_expression = lines[0].strip()
            translated_expression = lines[1].strip()
            translations[english_expression] = translated_expression
    return translations


def translate_file(file_path, translations):
    replacements = []

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    for match in re.finditer(r'>\s', content):
        replacements.append(match.end())

    content = content.replace("> ", ">")

    for english_expression, translated_expression in translations.items():
        pattern = rf'(?<=>){re.escape(english_expression)}(?=<|\'|")|\'{re.escape(english_expression)}\'|"{re.escape(english_expression)}"'
        content = re.sub(pattern, lambda match: match.group().replace(
            english_expression, translated_expression), content)

    lines = content.split('\n')
    for i, line in enumerate(lines):
        last_occurrence = line.rfind("/>")
        if last_occurrence != -1:
            lines[i] = line[:last_occurrence] + \
                "/> " + line[last_occurrence + 2:]
    content = '\n'.join(lines)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def translate_files_in_directory(directory, translations):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if fnmatch.fnmatch(file_name, '*.html') or fnmatch.fnmatch(file_name, '*.js'):
                file_path = os.path.join(root, file_name)
                translate_file(file_path, translations)


if __name__ == "__main__":
    translation_file = "translate.txt"
    translation_directory = "webui"

    translations = read_translation_file(translation_file)
    translate_files_in_directory(translation_directory, translations)
    print("Tradução concluída!")
