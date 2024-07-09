import sqlite3

con = sqlite3.connect('opayclone.db')
db = con.cursor()

db.execute('''CREATE TABLE IF NOT EXISTS users(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           first_name TEXT NOT NULL,
           last_name TEXT NOT NULL,
           other_name NOT NULL,
           username TEXT NOT NULL UNIQUE,
           email TEXT NOT NULL UNIQUE,
           password TEXT NOT NULL,
           phone_number TEXT NOT NULL,
           account_number TEXT NOT NULL,
           address TEXT NOT NULL,
           nin INTEGER NOT NULL,
           created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
           )''')

# C. r. u. d
def create_users(
        first_name,
        last_name,
        other_name,
        username,
        email,
        password,
        phone_number,
        account_number,
        address,
        nin
):
    
    db.execute("INSERT INTO users (first_name, last_name, other_name, username, email, password, phone_number, account_number, address, nin) VALUES (?,?,?,?,?,?,?,?,?,?)",
               (first_name,
                last_name,
                other_name,
                username,
                email,
                password,
                phone_number,
                account_number,
                address,
                nin))
    
    con.commit()
    return "New user has successfully been created."

# c. R. u. d
def get_all():
    db.execute("SELECT * FROM users")
    rows = db.fetchall()
    return rows

def get_by_id(id):
    db.execute("SELECT * FROM users WHERE id = ?", (id,))
    row = db.fetchone()
    return row

# c. r. U. d
def update(
        id,
        first_name,
        last_name,
        other_name,
        username,
        email,
        password,
        phone_number,
        account_number,
        address,
        nin
):
    
    db.execute("UPDATE users SET first_name = ?, last_name = ?, other_name = ?, username = ?, email = ?, password = ?, phone_number = ?, account_number = ?, address = ?, nin = ?, WHERE id = ?",
               (
                   first_name,
                   last_name,
                   other_name,
                   username,
                   email,
                   password,
                   phone_number,
                   account_number,
                   address,
                   nin,
                   id
               ))
    con.commit()
    return 'New user successfully added.'

# c. r. u. D
def delete(id):
    db.execute("DELETE FROM users WHERE id = ?", (id,))
    con.commit()
    return 'User successfully deleted.'