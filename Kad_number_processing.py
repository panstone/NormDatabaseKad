import os
import re

print("Если вы хотите проверить все файлы и папки с \"обмена\" \nВы должны ввести Да \nЕсли Вам не нужно введите Нет")
qast = input()
if qast =='Да':
    search_folders = open('search_of_name_folders.txt','w')
    search_files = open('search_of_name_files.txt','w')
    for foldername, subfolders, filenames in os.walk(r'\\10.56.113.5\обмен\!!Документы реестрового дела\Перечень объектов от 27.12.2017\Сканированные образы от Управления'):
        for filename in filenames:
            str_file = filename.split(".")[0]
            new_str_file = str_file.replace(' ',':').replace('_',':').replace('!',':')
            search_files.write(new_str_file+ '\n')
            #print(new_str_file)   
        for subfolder in subfolders:
            str_folder = subfolder.split(".")[0]
            new_str_folder = str_folder.replace(' ',':').replace('_',':').replace('!',':')
            search_folders.write(new_str_folder+ '\n')
            #print(new_str_folder)
    with open("14chast.txt") as file:
        array = [row.strip() for row in file]
    ##print('\n'.join(array))

    with open("search_of_name_folders.txt") as gile:
        arr = [row.strip() for row in gile]
    ##print('\n'.join(arr))

    with open("search_of_name_files.txt") as rile:
        arrr = [row.strip() for row in rile]
    ##print('\n'.join(arr))
    
    result=list(set(arr) & set(array))
    resulti=list(set(arrr) & set(array))
    print('\n'.join(result))
    print('\n'.join(resulti))
elif qast!='Да':
    print('Вы молодец')
    search_folders = open('search_of_name_folders.txt','r')
    search_files = open('search_of_name_files.txt','r')

search_folders.close()
search_files.close()
