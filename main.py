'''
Application example using build() + return
==========================================

An application can be built if you return a widget on build(), or if you set
self.root.
'''

import kivy
kivy.require('1.0.7')

from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout


class TestApp(App):

    def build(self):
        # return a Button() as a root widget
        f = FloatLayout()
        s = Scatter()
        l = Label(text="Hello",
        	font_size=150)

        f.add_widget(s)
        s.add_widget(l)
        return f

if __name__ == '__main__':
    TestApp().run()
