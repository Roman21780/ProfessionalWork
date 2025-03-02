# виртуальное окружение в Python https://timeweb.cloud/tutorials/python/kak-sozdat-virtualnoe-okruzhenie
# Основные команды Pip https://habr.com/ru/companies/productstar/articles/826732/
# Импорт в Python https://medium.com/nuances-of-programming/%D0%B8%D0%BC%D0%BF%D0%BE%D1%80%D1%82-%D0%B2-python-%D0%BF%D1%80%D0%BE%D0%B4%D0%B2%D0%B8%D0%BD%D1%83%D1%82%D1%8B%D0%B5-%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D0%BA%D0%B8-%D0%B8-%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8-%D1%87%D0%B0%D1%81%D1%82%D1%8C-1-a8117b0635b5


from config.bd.dirs import directories
from config.bd.docs import documents
from secretary import Secretary
from config.settings import LOGIN
from config.settings import PASSWORD

print(f'Выполняется код из {__name__}')
if __name__ == '__main__':
    secretary = Secretary(LOGIN, PASSWORD)
    secretary.work_with(documents, directories)
    while True:
        command = input('Введите команду: ')
        if command == 'p':
            secretary.print_owner_by_docnumber()
        elif command == 'l':
            secretary.print_docs()
        elif command == 's':
            secretary.print_shelf_by_document()
        elif command == 'a':
            secretary.add_new_document()
        elif command == 'e':
            break
        else:
            print('нет такой команды')