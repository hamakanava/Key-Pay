from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class KeyPay(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        # self.theme_cls.theme_style = "Dark"
        return Builder.load_string('''
MDScreen:
    MDBottomNavigation:
        selected_color_background: "green"
        text_color_active: "lightgrey"
        text_color_normal: 0, 0, 0, 1
        icon_color_normal: 0, 0, 0, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Главная'
            icon: 'home'
            badge_icon: ""
            MDLabel:
                text: 'Вы в главном меню'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Профиль'
            icon: 'account-box'
            badge_icon: ""
            MDLabel:
                text: 'Ваш профиль'
                halign: 'center'
''')

KeyPay().run()