from crud import listing, detail, entry, patch, delete

def base():
    print('Привет! Тебе доступны следующие функции:\n\tПолный список-1\n\tДетально-2\n\tСоздать-3\n\tОбновить-4\n\tУдалить-5')
    choice = input('Введите действия(1,2,3,4,5): ')

    if choice.strip() == '1':
        print(listing())
    elif choice.strip() == '2':
        print(detail())
    elif choice.strip() == '3':
        print(entry())
    elif choice.strip() == '4':
        print(patch())
    elif choice.strip() == '5':
        print(delete())
    else:
        print('Сделайте правильный выбор!')
        
    answer = input('Желаете продолжить?(yes/no): ')
    if answer.lower().strip() == 'yes':
        base()
    else:
        print('Досвидания!')
base()