#!/usr/bin/env python
# -*- coding: utf-8 -*-

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.grid import SmartTileWithLabel

from utils import get_data


Builder.load_string("""
<DashboardScreen>
    name: 'dashboard'
    MDSpinner:
        id: spinner
        active: True
        size_hint: None, None
        size: dp(46), dp(46)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    ScrollView:
        do_scroll_x: False
        GridLayout:
            id: dashboards_grid
            cols: 1
            row_default_height: dp(150)
            row_force_default: True
            size_hint_y: None
            height: self.minimum_height
            padding: dp(4), dp(4)
            spacing: dp(4)
""")


class DashboardScreen(Screen):
    def on_enter(self):
        dashboard = get_data('dashboard')
        grid = self.ids.dashboard_grid
        color = [0.64, 0.84, 0.98, 0.5]
        for dashboard in dashboard:
            grid.add_widget(SmartTileWithLabel(mipmap=True, keep_ratio=True,
                                               box_color=color, overlap=False,
                                               text=dashboard['name'],
                                               source=dashboard['logo']))
        self.ids.spinner.active = False
