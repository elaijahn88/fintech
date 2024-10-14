from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import sqlite3

# Database setup
conn = sqlite3.connect('financial_system.db')
c = conn.cursor()

# Create Tables
c.execute('''CREATE TABLE IF NOT EXISTS users 
            (username TEXT PRIMARY KEY, 
            password TEXT, 
            email TEXT, 
            phone TEXT)''')

c.execute('''CREATE TABLE IF NOT EXISTS financial_statements 
            (username TEXT, 
            account_balance REAL, 
            FOREIGN KEY(username) REFERENCES users(username))''')

c.execute('''CREATE TABLE IF NOT EXISTS loans 
            (username TEXT, 
            loan_amount REAL, 
            loan_status TEXT, 
            FOREIGN KEY(username) REFERENCES users(username))''')
conn.commit()

# Screens
class LoginScreen(Screen):
    pass

class SignupScreen(Screen):
    pass

class HomeScreen(Screen):
    user_name = StringProperty('')

class AccountDetailsScreen(Screen):
    account_balance = StringProperty('')
    loan_status = StringProperty('')

    def on_pre_enter(self):
        app = MDApp.get_running_app()
        username = app.username
        c.execute('SELECT account_balance FROM financial_statements WHERE username = ?', (username,))
        balance = c.fetchone()
        self.account_balance = f"Account Balance: ${balance[0]}" if balance else "Account Balance: $0.00"

        c.execute('SELECT loan_amount, loan_status FROM loans WHERE username = ?', (username,))
        loan_info = c.fetchone()
        if loan_info:
            self.loan_status = f"Loan: ${loan_info[0]}, Status: {loan_info[1]}"
        else:
            self.loan_status = "No loan account"

class AtomicsApp(MDApp):
    username = StringProperty('')

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

    def login(self, username, password):
        c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = c.fetchone()
        if user:
            self.username = username
            self.root.current = 'home'
        else:
            self.show_dialog("Login Failed", "Invalid username or password.")

    def signup(self, username, password, email, phone):
        try:
            c.execute('INSERT INTO users (username, password, email, phone) VALUES (?, ?, ?, ?)', 
                      (username, password, email, phone))
            conn.commit()
            self.show_dialog("Signup Success", "You have successfully signed up!")
            self.root.current = 'login'
        except sqlite3.IntegrityError:
            self.show_dialog("Signup Failed", "Username already exists.")

    def show_dialog(self, title, text):
        dialog = MDDialog(
            title=title,
            text=text,
            buttons=[
                MDFlatButton(text="OK", on_release=lambda x: dialog.dismiss())
            ]
        )
        dialog.open()

KV = '''
ScreenManager:
    LoginScreen:
    SignupScreen:
    HomeScreen:
    AccountDetailsScreen:

<LoginScreen>:
    name: 'login'
    MDTextField:
        id: username
        hint_text: "Username"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint_x: 0.8
    MDTextField:
        id: password
        hint_text: "Password"
        password: True
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint_x: 0.8
    MDRaisedButton:
        text: "Login"
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        on_release: root.manager.current='account_details'
    MDTextButton:
        text: "Don't have an account? Sign Up"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        on_release: root.manager.current = 'signup'

<SignupScreen>:
    name: 'signup'
    MDTextField:
        id: username
        hint_text: "Username"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        size_hint_x: 0.8
    MDTextField:
        id: password
        hint_text: "Password"
        password: True
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint_x: 0.8
    MDTextField:
        id: email
        hint_text: "Email"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint_x: 0.8
    MDTextField:
        id: phone
        hint_text: "Phone"
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        size_hint_x: 0.8
    MDRaisedButton:
        text: "Sign Up"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        on_release: app.signup(username.text, password.text, email.text, phone.text)

<HomeScreen>:
    name: 'home'
    MDLabel:
        text: "Welcome to the Financial System"
        halign: "center"
        pos_hint: {"center_y": 0.8}
    MDRaisedButton:
        text: "View Account Details"
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        on_release: root.manager.current = 'account_details'

<AccountDetailsScreen>:
    name: 'account_details'
    MDLabel:
        text: root.account_balance
        halign: "center"
        pos_hint: {"center_y": 0.6}
    MDLabel:
        text: root.loan_status
        halign: "center"
        pos_hint: {"center_y": 0.5}
    MDRaisedButton:
        text: "Back to Home"
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        on_release: root.manager.current = 'home'
'''

if __name__ == '__main__':
    AtomicsApp().run()
