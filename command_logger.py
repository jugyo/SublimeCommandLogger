import sublime, sublime_plugin
import re

command_history = []

setting = sublime.load_settings('Preferences.sublime-settings')
history_size = setting.get("command_logger_history_size") or 100
ignore_pattern = setting.get("command_logger_ignore_pattern")

class CommandLoggerListener(sublime_plugin.EventListener):
    def on_text_command(self ,view, command, args):
        self.log("view", command, args)

    def on_window_command(self, window, command, args):
        self.log("window", command, args)

    def log(self, type, command, args):
        try:
            if ignore_pattern != None and re.match(ignore_pattern, command):
                return
            # print("CommandLogger: %s" % {"type": type, "name": command, "args": args})
            command_history.insert(0, {"type": type, "name": command, "args": args})
            if len(command_history) > limit:
                command_history.pop
        except Exception as e:
            print(e)

class CommandLogCommand(sublime_plugin.WindowCommand):
    def run(self):
        def on_done(index):
            if index >= 0:
                command = command_history[index]
                print(command)
                if command["type"] == "view":
                    self.window.active_view().run_command(command["name"], command["args"])
                elif command["type"] == "window":
                    self.window.run_command(command["name"], command["args"])

        items = [[_["name"], str(_["args"])] for _ in command_history]

        sublime.set_timeout(lambda: self.window.show_quick_panel(items, on_done), 0)
