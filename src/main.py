from model.item import Item

STR_FILE_PATH = ""

def add_item():
    str_id = "1"
    str_name = "Relogio Rolex"
    str_amount = 4 
    dub_price = 4000.00
    str_description = "CF28"
    str_file_path = STR_FILE_PATH
    new_item = Item.add_new_item(str_id, str_name, str_amount, dub_price, str_description, str_file_path)

    if new_item:
        print('True')
    else:
        print('False')

def remove_item():
    str_id = "2"
    str_file_path = STR_FILE_PATH
    remove_item = Item.delete_item(str_id, str_file_path)
    if remove_item:
        print('True')
    else:
        print('False')

def list_one():
    str_id = "2"
    str_file_path = STR_FILE_PATH
    str_id_spreadsheet, str_name_spreadsheet, str_amount_spreadsheet, str_price_spreadsheet, str_description_spreadsheet, bool_found_return = Item.list_one_item(str_id, str_file_path)
    if bool_found_return:
        print(f'+-----------------------------------------------------+')
        print(f'| id: {str_id_spreadsheet}')
        print(f'| name: {str_name_spreadsheet}')
        print(f'| mount: {str_amount_spreadsheet}')
        print(f'| price: {str_price_spreadsheet}')
        print(f'| mount: {str_description_spreadsheet}')
        print(f'+-----------------------------------------------------+')
    else:
        print('Nao encontrado')
    
def list_all():
        str_file_path = STR_FILE_PATH
        list = Item.list_all_items(str_file_path)
        for item in list:
            print(f'+-----------------------------------------------------+')
            print(f'| id: {item[0]}')
            print(f'| name: {item[1]}')
            print(f'| mount: {item[2]}')
            print(f'| price: {item[3]}')
            print(f'| mount: {item[4]}')
            print(f'+-----------------------------------------------------+')

def update():
    str_id = "1"
    str_name = "Relogio Rolex"
    str_amount = 4 
    dub_price = 4000.00
    str_description = "CF2321"
    str_file_path = STR_FILE_PATH
    update_item = Item.update_one_item(str_id, str_name, str_amount, dub_price, str_description, str_file_path)
    
    if update_item:
        print('atualizado')
    else:
        print('Erro')

def main():
    opcao = input("op: ")
    if opcao == "1":
        add_item()
    elif opcao == "2":
        print('remover')
        remove_item()
    elif opcao == "3":
        print('listar 1')
        list_one()
    elif opcao == "4":
        print('listar todos')
        list_all()
    elif opcao == "5":
        update()
        print('atualizar')

if __name__ == "__main__":
    main()