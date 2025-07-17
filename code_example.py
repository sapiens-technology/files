from os.path import exists

class UserManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.users = []
        self.load_users()

    def load_users(self):
        if not exists(self.file_path):
            return
        with open(self.file_path, 'r') as file:
            for line in file:
                name, email = line.strip().split(',')
                self.users.append({'name': name, 'email': email})

    def save_users(self):
        with open(self.file_path, 'w') as file:
            for user in self.users:
                file.write(f"{user['name']},{user['email']}\n")

    def add_user(self, name, email):
        if '@' not in email or '.' not in email:
            print('Invalid email address.')
            return
        self.users.append({'name': name, 'email': email})
        self.save_users()
        print(f'User {name} added successfully.')

    def remove_user(self, name):
        self.users = [user for user in self.users if user['name'] != name]
        self.save_users()
        print(f'User {name} removed.')

    def list_users(self):
        print('Registered Users:')
        for user in self.users:
            print(f"{user['name']} - {user['email']}")

if __name__ == '__main__':
    manager = UserManager('users.txt')

    manager.add_user('Alice', 'alice@example.com')
    manager.add_user('Bob', 'bob@example.com')
    manager.list_users()

    manager.remove_user('Alice')
    manager.list_users()
