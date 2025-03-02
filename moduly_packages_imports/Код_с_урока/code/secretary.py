if __name__ == '__main__':
    print(f'Выполняется код из {__name__}')

class Secretary:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def work_with(self, documents, directories):
        self.documents = documents
        self.directories = directories

    def print_owner_by_docnumber(self):
        number = input('Введите номер документа: ')
        for doc in self.documents:
            if doc['number'] == number:
                print(doc['name'])
                break

    def print_docs(self):
        for document in self.documents:
            print(f'{document["type"]} {document["number"]} {document["name"]}')
        for k, v in self.directories.items():
            print(f'{k} -> {v}')


    def print_shelf_by_document(self):
        number = input('Введите номер документа: ')
        for directory, list_docs in self.directories.items():
            if number in list_docs:
                print(f'Документ с номером {number} находится на полке {directory}')
                break
        else:
            print('отсутствует документ с таким номером')


    def add_new_document(self):
        doc_number = input('Введите номер документа: ')
        doc_name = input('Введите имя и фамилию: ')
        doc_type = input('Введите тип документа: ')
        directory_number = input('Введите номер полки: ')
        self.documents.append({
            'type': doc_type,
            'number': doc_number,
            'name': doc_name,
        })
        if directory_number in self.directories:
            self.directories[directory_number].append(doc_number)
        else:
            self.directories[directory_number] = [doc_number]