import sqlite3
import string
import random


class PasswordRegistry:
    def __init__(self, website, name, email, identification, password, last_logged, serial=None):
        self.website = website
        self.name = name
        self.email = email
        self.identification = identification
        self.password = password
        self.last_logged = last_logged
        self.serial = f'{random.choice(string.ascii_letters)}{random.randrange(1, 10**3):03}{random.choice(string.punctuation)}-' \
                      f'{random.choice(string.ascii_letters)}{random.choice(string.ascii_letters)}' \
                      f'{random.choice(string.ascii_letters)}{random.choice(string.punctuation)}'


class PasswordDatabase:
    def __init__(self):
        """It is a Sample Line"""
        # self.con = sqlite3.connect("saved_passwords.db")
        self.con = sqlite3.connect("databases_source/saved_passwords.db")
        self.c = self.con.cursor()

    def create_table(self):
        self.c.execute(''' CREATE TABLE IF NOT EXISTS passwords(
                        website TEXT NOT NULL,
                        name TEXT NOT NULL, 
                        email TEXT NOT NULL,
                        id TEXT NOT NULL,
                        password TEXT NOT NULL,
                        last_logged TEXT NOT NULL,
                        serial TEXT NOT NULL UNIQUE)''')
        self.con.commit()

    def add_pass(self, user):
        try:
            self.c.execute('''INSERT INTO passwords(
                            website, name, email, id, password, last_logged, serial)
                            VALUES(?, ?, ?, ?, ?, ?, ?)''', (user.website, user.name, user.email, user.identification, user.password, user.last_logged, user.serial))
            self.con.commit()
        except sqlite3.IntegrityError:
            return {'Password is already Registered!'}

    def delete_pass(self, serial):
        self.c.execute('''SELECT * FROM passwords WHERE serial=?''', (serial,))
        value = self.c.fetchone()
        if not value:
            return {'No Password registered to delete!'}
        try:
            self.c.execute('''DELETE FROM passwords WHERE serial=?''', (serial,))
            self.con.commit()
            return {"PASSWORD ACCOUNT SUCCESSFULLY DELETED"}
        except:
            return {'password account cant find'}

    def update(self, serial, name, email, identification, password, last_logged):
        self.c.execute("""SELECT * FROM passwords WHERE serial =?""", (serial,))
        value = self.c.fetchone()
        if not value:
            return {"No admin registered to Update"}
        try:
            self.c.execute('''UPDATE passwords
                          SET name = ?, email = ?, id = ?, password =?, last_logged = ?
                          WHERE serial = ?''', (name, email, identification, password, last_logged, serial))
            self.con.commit()
        except sqlite3.IntegrityError:
            return {"Pass is already added"}

    def update_logged(self, serial, user):
        self.c.execute("""SELECT * FROM passwords WHERE serial =?""", (serial,))
        value = self.c.fetchone()
        if not value:
            return {"No admin registered to Update"}
        try:
            self.c.execute('''UPDATE passwords
                          SET last_logged = ?
                          WHERE serial = ?''', (user.last_logged, serial))
            self.con.commit()
        except sqlite3.IntegrityError:
            return {"Pass is already added"}

    def show_all_pass(self):
        self.c.execute('''SELECT * FROM passwords''')
        value = self.c.fetchall()
        return value

    def get_item(self, serial):
        self.c.execute('''SELECT * FROM passwords WHERE serial = ?''', (serial,))
        value = self.c.fetchone()
        return value



#run = PasswordRegistry("Facebook", "Kurt", "Trial", "trial", "tRial", "trial")
#run1 = PasswordRegistry("Gmail", "Kurt", "Trial", "trial", "tRial", "trial")
#run2 = PasswordRegistry("Riot Games Sign In", "Kurt", "Trial", "trial", "tRial", "trial")
#run3 = PasswordRegistry("Github", "Kurt", "Trial", "trial", "tRial", "trial")
#run4 = PasswordRegistry("OpenAI-ChatGPT", "Kurt", "Trial", "trial", "tRial", "trial")
#run5 = PasswordRegistry("ARIS TIP", "Kurt", "Trial", "trial", "tRial", "trial")
#run6 = PasswordDatabase()
# run2.create_table()
# run6.add_pass(run)
# run6.add_pass(run2)
# run6.add_pass(run3)
# run6.add_pass(run4)
# run6.add_pass(run5)
# run6.add_pass()