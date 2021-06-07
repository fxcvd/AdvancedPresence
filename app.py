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
    def __init__(self, cfg=None):
        self.app = ""
        self.url = ""

        print("AdvancedPresence\nby @fxcvd\n\nConfig file -> config.json\nDiscord -> inited success\n\nGood luck & Have fun")

        if not cfg:
            cfg = config

        # init rich presence
        self.rpc = Presence(cfg["discord"]["app_id"])
        self.rpc.connect()

        self._app(cfg)

    def _app(self, config):
        while True:
            app = get_active_window()

            try:
                app = config["aliases"][app]
            except:
                pass

            if self.app != get_active_window() or app in config["browser"]:
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
                            p = getattr(plugins, plugin)
                            rsp = p(title, url)

                            if rsp:
                                if rsp["button"]:
                                    buttons.append({
                                        "label": rsp["button"]["label"],
                                        "url": rsp["button"]["url"],
                                    })

                                if rsp["state"]:
                                    state = rsp["state"]

                                if rsp["icon"]:
                                    icon = rsp["icon"]

                                if rsp["details"]:
                                    details = rsp["details"]

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
                        buttons=[{
                            "label": "AdvancedPresence",
                            "url": "https://github.com/fxcvd/AdvancedPresence"
                        }],
                        start=time()
                    )

                self.app = app

            sleep(60)


if __name__ == "__main__":
    App() #run