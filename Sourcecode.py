# Desktopnotification-Project

import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "All Day Reminder",
            message = "Today I have to Submit my assignment and you have "
            "not completed it till now",
            app.icon = icon.ico.htm,
            timeout = 5
        )
        time.sleep(60*60)
