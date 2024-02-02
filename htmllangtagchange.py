
import os
import re
from pathlib import Path


def replace_lang_in_file(file_path,x):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 安全に lang="ja" を lang="en" に置換
    new_content = re.sub(r'lang="ja"', 'lang="' + x + '"', content)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'Updated {file_path}')

def search_files(directory,x):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = Path(root) / file
                replace_lang_in_file(file_path,x)

# ここで、検索するディレクトリを指定します


dlla_list = ["de", "en", "es", "fr", "hu",  "id", "it", "ko", "nl", "pl", "pt-pt", "ru", "tr", "zh"]
for x in dlla_list:

    search_directory = '/home/seanworld9/wp/docs/'+x+'/'
    search_files(search_directory, x)
