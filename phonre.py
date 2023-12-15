file_book = "phoneto.txt"

def validate_number(phone):
    if phone.isdigit() and len(phone)==9:
        return True
    else:
        print('zly numer')
        return False
def chech_number_exist(phone):
    book=read()
    if len(book)>0:
        for i in book:
            if i[1]==phone:
                print('numer istnieje')
                return True
        return False     
    else: return False
def read():
    book=[]
    try:
        with open(file_book,'r') as file:
            for line in file:
                new=line.strip().split(';')
                book.append(new)
    except: book=[]
    return book

def save(name,phone):
    if validate_number(phone)==True and chech_number_exist(phone)==False:
        with open(file_book,'a') as file:
            file.write(f"{name};{phone}\n")
        print('zapisano')

def display():
    with open(file_book,'r')as file:
        print(file.read())

def remove(phone):
    book=read()
    new_book=[]
    if chech_number_exist(phone)==True:
        for i in book:
            if not i[1] ==phone:
                new_book.append(i)
        with open(file_book,'w') as file:
            for i in new_book:
                file.write(f"{i[0]};{i[1]}\n")
    print('usunieto')
def modify(old_phone,new_name,new_phone):
    book=read()
    if validate_number(new_phone)==True and chech_number_exist(old_phone)==True and chech_number_exist(new_phone)==False:
        for i in book:
            if i[1] == old_phone:
                i[1]=new_phone
                i[0]=new_name
            with open(file_book,'w') as file:
                file.write(f"{i[0]};{i[1]}\n")
#modify('987654321','abca','987654322')
remove('987654322')
#save('www','123456789')
