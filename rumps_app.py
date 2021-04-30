import rumps

from src.app_functions.initialize_app import initialize_app
from src.app_functions.menu.change_auto_login import change_auto_login
from src.app_functions.menu.change_countdown_statusbar import change_countdown_statusbar
from src.app_functions.menu.change_credentials import change_credentials
from src.app_functions.menu.change_interval import change_interval
from src.app_functions.menu.change_strength_levels import change_strength_level
from src.app_functions.menu.load_vocabulary import load_vocabulary
from src.app_functions.menu.login_sequence import login
from src.app_functions.menu.notification_prompt import notification_prompt
from src.app_functions.notification_handler import notification_handler
from src.app_functions.settings.load_settings import load_settings
from src.app_functions.settings.save_settings import save_settings
from src.app_functions.statistics.load_statistics import load_statistics
from src.app_functions.statistics.save_statistics import save_statistics
from src.app_functions.statistics.show_statistics import show_statistics
from src.app_functions.update_menu import update_menu
from src.app_functions.update_title import update_title_bar


class DuolingoPomodoroApp(rumps.App):  # pylint: disable=too-many-instance-attributes
    """The base App class that is .run() on start-up

    Args:
        rumps (rumps.App): Class from which basic functionality is inherited
    """

    def __init__(self):
        """Initialize app, run upon opening app"""
        # Variables for rumps initialization
        super().__init__("Duolingo Pomodoro")
        self.icon = "static/icons/duolingo_icon.png"
        self.quit_button = "Quit"
        self.menu = [
            rumps.MenuItem("Login to Duolingo", callback=self.login_wrapper),
            rumps.MenuItem("Reload vocabulary", callback=self.load_vocabulary_wrapper),
            None,
            {
                "Settings": [
                    rumps.MenuItem(
                        "Change username and password",
                        callback=self.change_credentials_wrapper,
                    ),
                    rumps.MenuItem(
                        "Change prompt frequency", callback=self.change_interval_wrapper
                    ),
                    rumps.MenuItem("Auto-login", callback=self.change_auto_login_wrapper),
                    rumps.MenuItem(
                        "Show countdown in status bar",
                        callback=self.change_countdown_statusbar,
                    ),
                    {
                        "Change strength levels to be included": [
                            rumps.MenuItem(
                                "Level 1",
                                callback=self.change_strength_level_1,
                            ),
                            rumps.MenuItem(
                                "Level 2",
                                callback=self.change_strength_level_2,
                            ),
                            rumps.MenuItem(
                                "Level 3",
                                callback=self.change_strength_level_3,
                            ),
                            rumps.MenuItem(
                                "Level 4",
                                callback=self.change_strength_level_4,
                            ),
                        ],
                    },
                ],
            },
            rumps.MenuItem("Stats", callback=self.stats_wrapper),
            rumps.MenuItem("Test prompt", callback=notification_prompt),
            None,
        ]

        # Loading settings and statistics
        self.settings = load_settings()
        save_settings(self)
        self.statistics = load_statistics()
        save_statistics(self)

        # Variables used in app
        self.logged_in = False
        self.lingo = object
        self.global_timer = rumps.Timer(notification_prompt, self.settings["timer_interval"])
        self.vocabulary = {}

        # Loading sequence
        if self.settings["auto_login"]:
            initialize_app(self)
        update_menu(self)

    ## Wrappers for menu functions to allow passing self object
    def login_wrapper(self, _):
        """Wrapper for the login button

        Args:
            _ (rumps.rumps.MenuItem): The menu item that called the function
        """
        login(self)

    def load_vocabulary_wrapper(self, _):
        """Wrapper for the load vocabulary button

        Args:
            _ (rumps.rumps.MenuItem): The menu item that called the function
        """
        load_vocabulary(self)

    def change_credentials_wrapper(self, _):
        """Wrapper for the change credentials button

        Args:
            _ (rumps.rumps.MenuItem): The menu item that called the function
        """
        change_credentials(self)

    def change_interval_wrapper(self, _):
        """Wrapper for the change interval button

        Args:
            _ (rumps.rumps.MenuItem): The menu item that called the function
        """
        change_interval(self)

    def change_auto_login_wrapper(self, _):
        """Wrapper for the change auto-login setting button

        Args:
            _ (rumps.rumps.MenuItem): The menu item that called the function
        """
        change_auto_login(self)

    def change_countdown_statusbar(self, _):
        """Wrapper for the change interval setting button

        Args:
            _ (rumps.rumps.MenuItem): The menu item that called the function
        """
        change_countdown_statusbar(self)

    def change_strength_level_1(self, _):
        """Wrapper for the change strength level 1 button

        Args:
            _ (rumps.rumps.MenuItem): The menu item that called the function
        """
        change_strength_level(self, 1)

    def change_strength_level_2(self, _):
        """Wrapper for the change strength level 2 button

        Args:
            _ (rumps.rumps.MenuItem): The menu item that called the function
        """
        change_strength_level(self, 2)

    def change_strength_level_3(self, _):
        """Wrapper for the change strength level 3 button

        Args:
            _ (rumps.rumps.MenuItem): The menu item that called the function
        """
        change_strength_level(self, 3)

    def change_strength_level_4(self, _):
        """Wrapper for the change strength level 4 button

        Args:
            _ (rumps.rumps.MenuItem): The menu item that called the function
        """
        change_strength_level(self, 4)

    def stats_wrapper(self, _):
        """Wrapper for the show statistics button

        Args:
            _ (rumps.rumps.MenuItem): The menu item that called the function
        """
        show_statistics(self)

    ## Functions regulating timers
    @rumps.timer(1)
    def update_title_bar_wrapper(self, _):
        """Wrapper for the function that updates the title in the menu every second

        Args:
            _ (rumps.rumps.Timer): The timer that called the function
        """
        update_title_bar(self)

    ## Notification handler with appropriate decorator
    @rumps.notifications
    def notification_handler_wrapper(self, _):
        """Wrapper for the function that is called when a notification is clicked

        Args:
            _ (rumps.notifications.Notification): The notification that called the function
        """
        notification_handler(self)


if __name__ == "__main__":
    DuolingoPomodoroApp().run()
