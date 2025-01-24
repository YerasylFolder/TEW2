def remove_lines_from_file(file_path, text_to_remove):
    # Чтение содержимого файла
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Запись обратно в файл, исключая строки, содержащие text_to_remove
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            if text_to_remove not in line:
                file.write(line)

# Пример использования
file_path = 'student11.html'  # Укажите путь к вашему файлу
text_to_remove = 'C:\Users\User\Downloads\TEW2\'  # Укажите подстроку, которую нужно удалить

remove_lines_from_file(file_path, text_to_remove)
