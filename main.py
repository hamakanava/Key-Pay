from kivy.lang import Builder

from kivymd.app import MDApp


class KeyPay(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"
        # self.theme_cls.theme_style = "Dark"
        return Builder.load_string(
            '''
MDScreen:

    MDBottomNavigation:
        #panel_color: "#eeeaea"
        selected_color_background: "orange"
        text_color_active: "lightgrey"

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

'''
        )


KeyPay().run()