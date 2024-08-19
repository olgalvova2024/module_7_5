import os
import time

directory = '.'     #r'C:\Users\Admin\Desktop\Курс\модуль 7\module_7_4'
directory_normalized = os.path.normpath(directory)

for dirpath, dirnames, filenames in os.walk(directory_normalized):
    for file in filenames:
        filepath = os.path.join(dirpath, file)
        secs = os.path.getmtime(filepath)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

