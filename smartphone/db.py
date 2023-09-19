from tinydb import TinyDB, Query
from tinydb.table import Document


class UserDB:
    def __init__(self, file_name: str) -> None:
        self.db = TinyDB(file_name, indent=4)
        self.users = self.db.table('users')
        self.cart = self.db.table('cart')

    def is_user(self, chat_id: str) -> bool:
        return self.users.contains(doc_id=chat_id)

    def add_user(self, chat_id: str, first_name: str, last_name: str, username: str) -> int:
        if self.is_user(chat_id):
            return False

        user = Document(
            value={
                'first_name': first_name,
                'last_name': last_name,
                'username': username
            },
            doc_id=chat_id
        )
        return self.users.insert(user)

    def add_item(self, chat_id: str, brend: str, phone_id: str) -> bool:
        return self.cart.insert({
            'chat_id': chat_id,
            'brend': brend,
            'phone_id': phone_id
        })

    def get_items(self, chat_id):
        q = Query()
        return self.cart.search(q.chat_id == chat_id)


class SmartphoneDB:
    def __init__(self, file_name: str) -> None:
        self.db = TinyDB(file_name, indent=4)
    
    def brends(self) -> list:
        return self.db.tables()

    def phones(self, brend: str) -> list[Document]:
        table = self.db.table(brend)    
        return table.all()

    def phone(self, brend: str, id: str) -> Document:
        table = self.db.table(brend)
        return table.get(doc_id=id)
    