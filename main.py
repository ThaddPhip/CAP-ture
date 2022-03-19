from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, ImageLeftWidget, ThreeLineIconListItem
from kivy.uix.scrollview import ScrollView
from helpers import username_helper
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager



screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:

<MenuScreen>:
    name: 'menu'
    MDTextField:
        hint_text: "Enter Username"
        helper_text: "Forgot Username"
        helper_text_mode: "on_focus"
        icon_right: "android"
        icon_right_color: app.theme_cls.primary_color
        pos_hint: {'center_x': 0.5, 'center_y': 0.75}
        size_hint: (0.6,0.1)
    MDRectangleFlatButton:
        text: 'Login'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press: root.manager.current = 'profile'


        
<ProfileScreen>:
    name: 'profile'
#    MDRectangleFlatButton:
#        text: 'Back'
#        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
#        on_press: root.manager.current = 'menu'
#    BoxLayout:
    ScrollView:
        MDList:
            ThreeLineIconListItem:
                text: ' '
                IconLeftWidget:
                    icon: 'android'
            ThreeLineIconListItem:
                text: 'Measure Your Emotion'
                secondary_text: 'Prompt MUSE1 to record your emotion'
                IconLeftWidget:
                    icon: 'record-circle'
            ThreeLineIconListItem:
                text: 'Down To Memory Lane'
                secondary_text: 'View your positive moments'
                IconLeftWidget:
                    icon: 'emoticon-happy'
            ThreeLineIconListItem:
                text: 'Inspirational Quotes'
                secondary_text: 'Motivate your mind'
                IconLeftWidget:
                    icon: 'comment'            
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
        
        
                    MDToolbar:
                        title: 'Cap-ture'
            
            
                        left_action_items: [["menu",lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["camera", lambda x: nav_drawer.set_state("open")]]
                        elevation: 10
                    MDLabel:
                        title: ""
                        halign: 'center'
                    MDBottomAppBar:
                        md_bg_color: 0, 0.1, 1, 0.8
                        MDToolbar:
                            left_action_items: [["home",lambda x: x]]
                            mode: 'end'
                            type: 'bottom'
                            icon: 'help-circle'
                            #on_action_button: app.navigation_draw()
                            on_action_button: root.manager.current = 'menu'

        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                
                Image:
                    source: '030618_LS_brain-wave_feat.jpg'    
                MDLabel:
                    text: 'Cap-ture'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: 'Record Emotions'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Profile'
                            IconLeftWidget:
                                icon: 'android'
                        OneLineIconListItem:
                            text: 'Rate Your Experience'
                            IconLeftWidget:
                                icon: 'star'
                        OneLineIconListItem:
                            text: 'Sign Out'
                            IconLeftWidget:
                                icon: 'logout'
                
        
<UploadScreen>
    name: 'upload'
    MDLabel:
        text: 'Lets upload some files!'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'menu'

"""

class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class UploadScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))


def show_data(self, obj):
    if self.username.text is "":
        check_string = 'Please enter a username'
    else:
        check_string = self.username.text + ' does exist'
    close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
    more_button = MDFlatButton(text='Open Main Menu')
    self.dialog = MDDialog(title='Login Successful',
                           text=check_string,
                           buttons=[close_button, more_button])
    self.dialog.open()


def close_dialog(self, obj):
    self.dialog.dismiss()


def navigation_draw(self):
    print("Navigation")


navigation_helper = """
Screen:
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
        
        
                    MDToolbar:
                        title: 'Cap-ture'
            
            
                        left_action_items: [["menu",lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["android", lambda x: nav_drawer.set_state("open")]]
                        elevation: 10
                    MDLabel:
                        title: ""
                        halign: 'center'
                    MDBottomAppBar:
                        MDToolbar:
                            #left_action_items: [["menu",lambda x: nav_drawer.set_state("open")]]
                            mode: 'end'
                            type: 'bottom'
                            icon: 'language-python'
                            on_action_button: app.navigation_draw()
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                spacing: '8dp'
                padding: '8dp'
                
                Image:
                    source: '030618_LS_brain-wave_feat.jpg'    
                MDLabel:
                    text: 'Cap-ture'
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: 'Record Emotions'
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Profile'
                            IconLeftWidget:
                                icon: 'android'
                        OneLineIconListItem:
                            text: 'Rate Your Experience'
                            IconLeftWidget:
                                icon: 'star'
                        OneLineIconListItem:
                            text: 'Sign Out'
                            IconLeftWidget:
                                icon: 'logout'
                
                    
            
            
"""


Window.size = (300,500)

user_toolbar = """

Screen:

    BoxLayout:
        orientation: 'vertical'
        
        
        MDToolbar:
            title: 'Cap-ture'
            
            
            left_action_items: [["menu",lambda x: app.navigation_draw()]]
            right_action_items: [["android", lambda x: app.navigation_draw()]]
            elevation: 8
        MDLabel:
            title: ""
            halign: 'center'
        MDBottomAppBar:
            MDToolbar:
                left_action_items: [["menu",lambda x: app.navigation_draw()]]
                mode: 'end'
                type: 'bottom'
                icon: 'language-python'
                on_action_button: app.navigation_draw()
            
"""

class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        self.theme_cls.primary_hue = "300"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return screen

DemoApp().run()
