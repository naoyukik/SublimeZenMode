import sublime
import sublime_plugin


def get_setting(key):
    return sublime.active_window().settings().get(key)


def set_setting(key, value):
    sublime.active_window().settings().set(key, value)


class EnableZenModeCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.set_minimap_visible(False)
        self.window.set_sidebar_visible(False)
        self.window.set_menu_visible(False)
        self.window.set_status_bar_visible(False)
        self.window.set_tabs_visible(False)


class DisableZenModeCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.set_sidebar_visible(get_setting('zen_mode_sidebar'))
        self.window.set_minimap_visible(get_setting('zen_mode_minimap'))
        self.window.set_menu_visible(get_setting('zen_mode_menu'))
        self.window.set_status_bar_visible(get_setting('zen_mode_status_bar'))
        self.window.set_tabs_visible(get_setting('zen_mode_tabs'))


class ToggleZenModeCommand(sublime_plugin.WindowCommand):
    def run(self):
        is_sidebar = self.window.is_sidebar_visible()
        is_minimap = self.window.is_minimap_visible()
        is_menu = self.window.is_menu_visible()
        is_status_bar = self.window.is_status_bar_visible()
        is_tabs = self.window.get_tabs_visible()

        if is_sidebar or is_minimap or is_menu or is_status_bar or is_tabs:
            set_setting('zen_mode_sidebar', is_sidebar)
            set_setting('zen_mode_minimap', is_minimap)
            set_setting('zen_mode_menu', is_menu)
            set_setting('zen_mode_status_bar', is_status_bar)
            set_setting('zen_mode_tabs', is_tabs)
            self.window.run_command('enable_zen_mode')
        else:
            self.window.run_command('disable_zen_mode')
