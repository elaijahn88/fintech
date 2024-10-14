from kivy.uix.video import Video
from kivy.uix.accordion import NumericProperty
from kivy.uix.floatlayout import FloatLayout
import sqlite3
import re 
from kivy.uix.screenmanager import Screen
from kivymd.uix.snackbar import Snackbar
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivy.core.window import Window
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons


from kivymd.uix.screenmanager import ScreenManager


#create connection to the database 
conn = sqlite3.connect('elijah.db')

sql_table= "CREATE TABLE IF NOT EXISTS elijah(username,password )"

def table():
    conn.execute(sql_table)
    return conn
table()



Window.size = (350, 600)

KV = '''
ScreenManager:
    MainScreen:
    SecondScreen:
    ManScreen:
    SecondScreen:
    MainScreen:
    LessonsScreen:
    TipsScreen:
    QuizScreen:
    ShowScreen:
    Screeeno:
    
<MainScreen>
    name:'first'
    md_bg_color: 0, 0, 0, 1 

    # Background Image
    
    

    MDCard:
        orientation: "vertical"
        md_bg_color: .2, .4, .3, 1 
        size_hint: None, None
        size: "300dp", "400dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        elevation: 10
        padding: "20dp"
        spacing: "20dp"
        md_bg_color: 0, 1, 0, 1  # Card background

        MDLabel:
            text: "Login"
            font_style: "H5"
            md_bg_color: 0, 1, 0, 1 
            
            halign: "center"
            size_hint_y: None
            #height: self.texture_size[1]

        MDTextField:
            id: username
            md_bg_color: 1, 1, 1, 1 
            hint_text: "Username"
            mode: "rectangle"
            icon_right: "account"
            size_hint_x: None
            width: "250dp"
            pos_hint: {"center_x": 0.5}

        MDTextField:
            id: password
            md_bg_color: 1, 0, 1, 1 
            hint_text: "Password"
            mode: "rectangle"
            icon_right: "eye-off"
            password: True
            size_hint_x: None
            width: "250dp"
            pos_hint: {"center_x": 0.5}

        MDRaisedButton:
            text: "Login"
            md_bg_color: 0, 0, 1, 1
            pos_hint: {"center_x": 0.5}
            on_release: 
                root.login()
                app.change_screen('main') if root.login() else app.change_screen('first')

        Widget:
            size_hint_y: None
            height: "10dp"

        MDRaisedButton:
            text: "Register"
            pos_hint: {"center_x": 0.5}
            on_release: app.change_screen('second') 
            md_bg_color: 0, 0, 1, 1 






<SecondScreen>
    name:'second' 
    md_bg_color: 0, 0, 0, 1 
    
    MDCard:
        md_bg_color: 0, .8, 0, 1 
        orientation: "vertical"
        size_hint: None, None
        size: "300dp", "500dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        elevation: 10
        padding: "20dp"
        spacing: "20dp"
    

        MDLabel:
            text: "Register"
            font_style: "H5"
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            md_bg_color: 0, 0, 1, 1 

        MDTextField:
            id: username
            hint_text: "Username"
            mode: "rectangle"
            icon_right: "account"
            size_hint_x: None
            width: "250dp"
            pos_hint: {"center_x": 0.5}

        MDTextField:
            id: email
            hint_text: "Email"
            mode: "rectangle"
            icon_right: "email"
            type: "email"
            size_hint_x: None
            width: "250dp"
            pos_hint: {"center_x": 0.5}
            on_focus:root.validate_email()
            

        MDTextField:
            id: password
            hint_text: "Password"
            mode: "rectangle"
            icon_right: "eye-off"
            password: True
            size_hint_x: None
            width: "250dp"
            pos_hint: {"center_x": 0.5}

        MDTextField:
            id: confirm
            hint_text: "Confirm Password"
            mode: "rectangle"
            icon_right: "eye-off"
            password: True
            size_hint_x: None
            width: "250dp"
            pos_hint: {"center_x": 0.5}

        MDRaisedButton:
            text: "Register"
            pos_hint: {"center_x": 0.5}
            md_bg_color: 0, 0, 1, 1 
            on_release:
                root.register()
                root.validate_email()
                root.validate_password()

                app.change_screen('first') if  root.register() else app.change_screen('second')
        
            



<ManScreen>:
    name: 'main'
    md_bg_color: 0, 0, 1, 1
    MDIconButton:
        id:first
        color: 1 , 0 , 0 , 1
        md_bg_color: 0, 0, 1, 1
        icon: "menu"
        pos_hint: {'top': 1.0,'x': .1}
        on_release: app.change_screen('second')

    MDCard:
        md_bg_color: 0, 1, .0, 1 
        orientation: "horizontal"
        size_hint: None, None
        size: "400dp", "400dp"
        pos:0,300
        elevation: 10
        padding: "20dp"
        spacing: "20dp"
        
        
            
        MDLabel:
            id:label
            text: "Welcome!"
            color: 0 , 0 , 1, 1
            
            font_style: "H5"
            
            size_hint: .2,.1
        MDFloatingActionButton:
            id: button
            icon: "car"
            on_release: root.label()
       
        MDFloatingActionButton:
            id: button
            icon: "parking"
            on_release: root.parking()
        
        MDFloatingActionButton:
            id: button
            icon: "bicycle"
            on_release: root.label()
        #pos:200,400
        MDFloatingActionButton:
            id: button
            icon: "motorbike"
            on_release: root.motor()
        #pos:300,400
        
        
            
        
    
    MDIconButton:
        id:second
        icon: "fire"
        color: 1 , 0 , 0 , 1
        md_bg_color: 0, 0, 1, 1
        pos_hint: {'top': 1.0,'x': .3}
        on_release: root.motor()
    
    MDIconButton:
        id: second
        icon: "comment"
        color: 1 , 0 , 0 , 1
        md_bg_color: 0, 0, 1, 1
        pos_hint: {'top': 1.0,'x': .5}
        on_release: root.motor()
        

        


    MDIconButton:
        id:third
        icon: "lan"
        md_bg_color: 1, 0, 0, 1
        pos_hint: {'top': 1.0,'x': .7}
        on_release: app.change_screen('main')
    
        
    MDIconButton:
        icon: "star"
        
        md_bg_color: 0, 1, 0, 1
        pos_hint: {'top': 1.0,'x': .9}
        on_release:root.star()

    BoxLayout:
        orientation: 'vertical'
        padding: "20dp"
        

        
        MDBoxLayout:
            orientation: "vertical"

        
        
        
    MDCard:
        id:star
        md_bg_color: 0, 1, 0, 1 
        orientation: "horizontal"
        size_hint: None, None
        size: "350dp", "300dp"
        pos:0,0
        elevation: 10
        padding: "20dp"
        spacing: "20dp"
       

        MDRaisedButton:
            text: "Start"
            md_bg_color: 0, 0, 1, 1 
            
            color: 0 , 0 , 1, 1
            size_hint_x: None
            width: "200dp"
            pos_hint: {"center_x": 0.5}
            on_release: 
                root.star2()
                app.switch_screen('lessons')

        MDRaisedButton:
            text: "Tips"
            size_hint_x: None
            md_bg_color: 0, 0, 1, 1 
            width: "200dp"
            pos_hint: {"center_x": 0.5}
            on_release: app.switch_screen('tips')

        MDRaisedButton:
            md_bg_color: 0, 0, 1, 1 
            text: "treasure"
            size_hint_x: None
            width: "200dp"
            pos_hint: {"center_x": 0.5}
            on_release: app.switch_screen('quiz')

        
        MDFloatingActionButtonSpeedDial:
            data: app.data
            
            root_button_anim: True
            pos:0,0
        

<LessonsScreen>:
    name: 'lessons'
    md_bg_color: 0, 0, 1, 1
    
    MDIconButton:
        icon: "share"
        md_bg_color: 0, 0, 1, 1
        pos_hint: {'top': 1.0,'x': .1}
        on_release: app.change_screen('main')
    
   
    
        
    MDIconButton:
        icon: "traffic-light"
        md_bg_color: 0, 0, 1, 1
        pos_hint: {'top': 1.0,'x': .3}
        

        
    MDCard:
        md_bg_color: 0, 1, .0, 1 
        orientation: "vertical"
        size_hint: None, None
        size: "100dp", "400dp"
        pos:200,300
        elevation: 10
        padding: "20dp"
        spacing: "20dp"
        
        MDFloatingActionButton:
            id: button
            icon: "car"
        #pos:0,400
        MDFloatingActionButton:
            id: button
            icon: "church"
        #pos:100,400
        MDFloatingActionButton:
            id: button
            icon: "bicycle"
        #pos:200,400
        MDFloatingActionButton:
            id: button
            icon: "motorbike"
        #pos:300,400
        

    
    
        
    MDIconButton:
        icon: "gold"
        md_bg_color: 0, 0, 1, 1
        pos_hint: {'top': 1.0,'x': .9}
    

    MDBoxLayout:
        orientation: "vertical"
        
        MDFloatingActionButtonSpeedDial:
            data: app.data
            md_bg_color: 0, 0, 1, 1
            root_button_anim: True

    
        
    BoxLayout:
        orientation: 'vertical'
        padding: "20dp"
        spacing: "10dp"

    

        

        MDRaisedButton:
            text: "homepage"
            pos_hint: {"center_x": 0.5}
            on_release: app.switch_screen('main')

<QuizScreen>:
    name: 'quiz'
    md_bg_color: 0, 0, 1, 1
    MDIconButton:
        icon: "diamond"
        md_bg_color: 0, 0, 1, 1
        pos_hint: {'top': 1.0,'x': .1}
        on_release: app.change_screen('main')
    
   
        
    MDIconButton:
        icon: "book"
        md_bg_color: 0, 0, 1, 1
        pos_hint: {'top': 1.0,'x': .3}
    MDFloatingActionButton:
        id: button
        icon: "car"
        pos:0,400
    MDFloatingActionButton:
        id: button
        icon: "church"
        pos:100,400
    MDFloatingActionButton:
        id: button
        icon: "bicycle"
        pos:200,400
    MDFloatingActionButton:
        id: button
        icon: "motorbike"
        pos:300,400
        
    MDCard:
        md_bg_color: 0, 1, .0, 1 
        orientation: "vertical"
        size_hint: None, None
        size: "300dp", "400dp"
        pos:200,300
        elevation: 10
        padding: "20dp"
        spacing: "20dp"
        
        MDFloatingActionButton:
            id: button
            icon: "car"
        #pos:0,400
        MDFloatingActionButton:
            id: button
            icon: "church"
        #pos:100,400
        MDFloatingActionButton:
            id: button
            icon: "bicycle"
        #pos:200,400
        MDFloatingActionButton:
            id: button
            icon: "motorbike"
        #pos:300,400
        
        

    MDTextField:
        id: message
        md_bg_color: 1, .1, 1, 1 
        hint_text: "send message"
        mode: "rectangle"
        size_hint_x: None
        width: "250dp"
        pos:100,230
    MDRaisedButton:
        text: "message"
        pos:260,190
        md_bg_color: 0, 1, 0, 1 
            
    
    MDRaisedButton:
        text: "pay"
        md_bg_color: 0, 1, 0, 1
        pos:280,2
    
    MDBoxLayout:
        orientation: "vertical"
        
    

        MDFloatingActionButtonSpeedDial:
            data: app.data
            root_button_anim: True
            md_bg_color: 0, 0, 1, 1
            callback: app.speed_dial_callback


        
        
        

        
            
    BoxLayout:
        orientation: 'vertical'
        padding: "20dp"
        spacing: "10dp"
        md_bg_color: 1, 0, 1, 1

        

        

        MDRaisedButton:
            text: "Stop"
            md_bg_color: 1, 0, 0, 1
            color: 1 , 0 , 0 , 1
            
            on_release: app.show_quiz_result("Correct", "Red means stop.")

        MDRaisedButton:
            text: "Green"
            md_bg_color: 0, 0, 1, 1
            pos:200,200
            on_release: app.show_quiz_result("Incorrect", "Green means go.")

        MDRaisedButton:
            text: "lanes"
            md_bg_color: 0, 0, 1, 1
            pos_hint: {"center_x": 0.5}
            on_release: app.show_quiz_result("Correct", "Always signal when turning or changing lanes.")

        

        MDRaisedButton:
            md_bg_color: 0, 0, 1, 1
            text: "homepage"
            pos_hint: {"center_x": 0.5}
            on_release: app.switch_screen('main')
<TipsScreen>:
    name: 'tips'
    md_bg_color: 0, 1, 0, 1
    

    MDIconButton:
        icon: "share"
        md_bg_color: 0, 1, 0, 1
        pos_hint: {'top': 1.0,'x': .1}
    
    MDIconButton:
        icon: "security"
        md_bg_color: 0, 1, 0, 1
        pos_hint: {'top': 1.0,'x': .3}
    
        
    MDIconButton:
        icon: "flower"
        md_bg_color: 0, 1, 0, 1
        pos_hint: {'top': 1.0,'x': .5}
        
    MDTextField:
        id: message
        md_bg_color: 1, .1, 1, 1 
        hint_text: "send message"
        mode: "rectangle"
        size_hint_x: None
        width: "250dp"
        pos:100,230
    
        
    MDCard:
        md_bg_color: 0, 1, .0, 1 
        orientation: "vertical"
        size_hint: None, None
        size: "90dp", "400dp"
        pos:250,300
        elevation: 10
        padding: "20dp"
        spacing: "20dp"
        
        MDFloatingActionButton:
            id: button
            icon: "car"
            on_release: app.change_screen('sm')
        #pos:0,400
        MDFloatingActionButton:
            id: button
            icon: "church"
            on_release: app.change_screen('sm') 
        #pos:100,400
        MDFloatingActionButton:
            id: button
            icon: "bicycle"
            on_release: app.change_screen('sm')
        #pos:200,400
        MDFloatingActionButton:
            id: button
            icon: "motorbike"
        #pos:300,400

    
    
   
    MDBoxLayout:
        orientation: "vertical"

        MDFloatingActionButtonSpeedDial:
            data: app.data
            md_bg_color: 0, 0, 1, 1
            root_button_anim: True

        
    BoxLayout:
        orientation: 'vertical'
        padding: "20dp"
        spacing: "10dp"

    
        MDLabel:
            text: "Nationality"
            halign: "center"
            font_style: "H6"
            pos:0,400

        MDRaisedButton:
            text: "guide"
            md_bg_color: 0, 0, 1, 1 
            pos_hint: {"center_x": 0.5}
            on_release: app.show_quiz_result("Correct", "Always signal when turning or changing lanes.")

       
        MDRaisedButton:
            text: "homepage"
            md_bg_color: 0, 0, 1, 1 
            pos_hint: {"center_x": 0.5}
            on_release: app.switch_screen('main')
<ShowScreen>:
    name:'show'
    md_bg_color: 0, 0, 1, 1
    MDRaisedButton:
        text: "pay"
        on_release: app.change_screen('main') 
    MDTextField:
        id: message
        md_bg_color: 1, .1, 1, 1 
        hint_text: "send message"
        mode: "rectangle"
        size_hint_x: None
        width: "250dp"
        pos:100,230
    MDRaisedButton:
        text: "message"
        pos:260,190
        md_bg_color: 0, 1, 0, 1 
<Screeeno>:
    name:'sm'
    md_bg_color: 1, .1, 1, 1 
    Video:
        source:'x.mp4'
        state:'play'
    MDRaisedButton:
        text: "media grp"
        on_release: app.change_screen('show') 
    

        
'''
class MainScreen(MDScreen):
    #username=StringProperty('')
    #password=NumericProperty(0)
    


  
#current login system implementation 
    def login(self):
        sql_query = "SELECT * FROM elijah;"
            
        cursor = conn.cursor()
        cursor.execute(sql_query)
        
        username = self.ids.username.text
        password = self.ids.password.text

        
        cursor = conn.cursor()

        # Query to check if the user exists
        cursor.execute("SELECT * FROM elijah ")
        conn.commit()
        user = cursor.fetchall()
        
        
            
            
        
        for x in range(len(user)):
            print(x)
            x=x+1
            print(x)
            us=user[x][0]
            ps=user[x][1]
            if ps==self.ids.password.text and us==self.ids.username.text:
                self.show_dialog('login','success')
             
                return True
            elif self.ids.username=='':
                self.show_dialog("missing ",'')
                return False
            else:
                self.show_dialog('login','failure')
                return False 
        return 
    conn.close()        
    

                    
                    
                    

                
        
            
            
            
    def show_dialog(self, title, text):
        dialog = MDDialog(
            title=title,
            text=text,
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ],
        )
        dialog.open()

def is_valid_email(email):
    # Regular expression for validating an email
        email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        #return re.match(email_pattern, email) is not None




# Function to validate the password based on criteria
def is_valid_password(password):
    # Password must be at least 8 characters long
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    # Password must contain at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."

    # Password must contain at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."

    # Password must contain at least one digit
    if not re.search(r'\d', password):
        return False, "Password must contain at least one number."

    # Password must contain at least one special character
    if not re.search(r'[@$!%*?&]', password):
        return False, "Password must contain at least one special character (@, $, !, %, *, ?, &, etc.)."

    return True, "Valid password!"

class SecondScreen(MDScreen):
    username=StringProperty('')
    password=NumericProperty(0)
    email=StringProperty('')
    #password validation
    def validate_password(self):
        password = self.ids.password.text
        is_valid, message = is_valid_password(password)
        
        if is_valid:
            self.show_dialog("log",'strong password')

        else:
            # Show error in the helper text
            self.ids.password.error = True
            #self.show_dialog("answer ",'loose password ')
            

    
    
    def validate_email(self):
        email = self.ids.email.text
        if is_valid_email(email):
            self.show_dialog("email ",'valid')

        else:
            # Trigger the error mode on the MDTextField
            self.ids.email.error = True
            #self.show_dialog("error ",'missing@ . gmail/yahoo')

    

    

# current registeration implementation 
    def register(self):
        username = self.ids.username.text
        password = self.ids.password.text

        cursor = conn.cursor()

        # Check if the username already exists
        cursor.execute("SELECT * FROM elijah WHERE username=?", (username,))
        user=cursor.fetchall()
        
        passw=user
        print(passw)
        for i in range(20):
            #this returns all tuples in the database 
            usernam=user[i]
            ps_w=usernam[1]
            user_w=usernam[0]
             
            if self.ids.username.text in user_w and self.ids.password.text in ps_w:
                #continue
                
                
                
                self.show_dialog('user there !','')

                return True
            
            else:
                try:
                # Insert new user into the database
                    cursor.execute("INSERT INTO elijah (username, password) VALUES (?, ?)", (username, password))
                    conn.commit()
                    self.show_dialog('registered','')
            
                except sqlite3.IntegrityError as e:
                    self.show_dialog('same user','there')
                return False
        
        
        
        
        

            
            
            
                
    


    
    def show_dialog(self, title, text,color=(1,0,0,1)):
        dialog = MDDialog(
            title=title,
            text=text,
           
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda x: dialog.dismiss()
                )
            ],
        )
        dialog.open()
class ShowScreen(MDScreen):
    pass 
        
class ManScreen(MDScreen):
    def label(self):
        self.ids.label.text="kia"
        self.ids.label.md_bg_color=(.4,0,1,1)
        self.ids.label.size_hint= .3, .1
    def motor(self):
        self.ids.label.text='bike'
        self.ids.label.md_bg_color=(1,0,0,1)
    def parking(self):
        self.ids.label.text='park'
        self.ids.label.md_bg_color=(1,0,0,1)
    def star(self):
        self.ids.star.size_hint= 1, 1
    def star2(self):
        self.ids.star.size_hint= 1, .5

class LessonsScreen(MDScreen):
    pass

class TipsScreen(MDScreen):
    pass

class QuizScreen(MDScreen):
    pass
class Screeeno(Screen):
    pass

class DriveApp(MDApp):
    icons = list(md_icons.keys())[15:30]
    data = {
        'volvo': 'car',
        'toyota': 'motobike',
        'wagon': 'bicycle',
        'rover':'car'
    }

    username=StringProperty()

    def build(self):
        return Builder.load_string(KV)
    

    def speed_dial_callback(self, button_text):
        # Handle the button press
        if button_text == "volvo":
            print("chose avolvo")
        elif button_text == "toyota":
            print("chose amotorbike")
        elif button_text == "wagon":
            print("wagon")
        else:
            print("chose arover ")
    def change_screen(self, screen_name):
        self.root.current = screen_name

    def switch_screen(self, screen_name):
        self.root.current = screen_name


    

    def show_lesson(self, lesson_title):
        lesson_content = {
            "Traffic Signs": "Traffic signs are visual indicators of the rules and guidelines on the road...",
            "Parking": "Parking correctly requires careful attention to the surrounding space.."
        }.get(lesson_title, "Lesson content not found.")

        self.show_dialog(lesson_title, lesson_content)

    def show_quiz_result(self, title, text):
        self.show_dialog(title, text)

    def show_dialog(self, title, text):
        dialog = MDDialog(
            title=title,
            text=text,
            buttons=[
                MDRaisedButton(
                    text="dismiss",
                    on_release=lambda x: dialog.dismiss()
                )
            ],
        )
        dialog.open()

    


if __name__ == "__main__":
    DriveApp().run()




