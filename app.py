#
#              AdvancedPresence
#                 by @fxcvd
#
#   main.py
#   created at 06.06.21
#   modifed at 07.06.21
#

from header import *


class App(object):
    def __init__(self):
        self.app = ""
        self.url = ""

        os.system("clear")
        print("AdvancedPresence")
        print("by @fxcvd\n")
        print("Config file -> config.json")
        print("Discord -> inited success\n")
        print("Good luck & Have fun")

        self._rpc_init()
        self._app()

    def _rpc_init(self):
        self.rpc = Presence(config["discord"]["app_id"])
        self.rpc.connect()

    def _app(self):
        while True:
            window = get_active_window()
            app = get_aliase(window)

            if self.app != app or app in config["browser"]:
                buttons = []
                state = "by @fxcvd with ❤"
                icon = icon_for_app(app)
                details = f"in {app}"

                if app in config["browser"]:
                    if config["browser_settings"]["enable"]:
                        title = get_active_title()
                        url = get_active_url()

                        if self.url == url:
                            continue

                        for plugin in config["browser_settings"]["plugins"]:
                            plugin = getattr(plugins, plugin)
                            plugin_response = plugin(title, url)

                            if plugin_response:
                                if plugin_response["button"]:
                                    buttons.append({
                                        "label": plugin_response["button"]["label"],
                                        "url": plugin_response["button"]["url"],
                                    })

                                if plugin_response["state"]:
                                    state = plugin_response["state"]

                                if plugin_response["icon"]:
                                    icon = plugin_response["icon"]

                                if plugin_response["details"]:
                                    details = plugin_response["details"]

                        self.url = url

                buttons.append({
                    "label": "AdvancedPresence",
                    "url": "https://github.com/fxcvd/AdvancedPresence"
                })

                try:
                    self.rpc.update(
                        state=state,
                        details=details,
                        large_image=icon,
                        large_text=app,
                        buttons=buttons,
                        start=time()
                    )

                except:
                    self.rpc.update(
                        state=state,
                        details=details,
                        large_image=icon,
                        large_text=app,
                        buttons=[buttons[-1]],
                        start=time()
                    )

                self.app = app

            #sleep delay
            sleep(5)


if __name__ == "__main__":
    App()  # run
