from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):# реалізація класу
    def __init__(self,name):
        super().__init__(name)   

class Phone(Field):
    def __init__(self,numder):
        if not numder.isdigit() or len(numder) !=10:
            raise ValueError("Phone number must be 10 digits")
        super().__init__(numder)
            
class Record:

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,number):
        phone=Phone(number)
        self.phones.append(phone)
            
    def remove_phone(self, number):
        phone = self.find_phone(number)  # Знаходимо об'єкт Phone
        if phone:  # Перевіряємо, чи знайшли номер
            self.phones.remove(phone)  # Видаляємо об'єкт Phone
        else:
            raise ValueError(f"Phone number {number} not found")


    def edit_phone(self, old_number, new_number):
        phone = self.find_phone(old_number)  # Шукаємо старий номер
        
        if phone:  
            self.remove_phone(old_number)  # Видаляємо знайдений номер
            self.add_phone(new_number)  # Додаємо новий номер
        else:
            raise ValueError(f"Phone number {old_number} not found")
            
    def find_phone (self,number:str): 
        for phone in self.phones:
           if phone.value == number:  
               return phone
        return None
           

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
    def add_record(self,record):
        self.data[record.name.value]=record
        

    def find(self,name):
        return self.data.get(name,None)
        

    def delete(self,name):
        if name in self.data :
           del self.data[name]
        else :
            raise ValueError(f"Contact {name} not found") 

    def __str__(self):
       return "\n".join(str(record) for record in self.data.values())


def main ():
    
   # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
     
    print(book)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

if __name__=='__main__':
        main()



        