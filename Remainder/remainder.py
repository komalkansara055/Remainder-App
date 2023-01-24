# use pythonw.exe .\remainder.py for remainder to run after program ended

import time
from plyer import notification 

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Pending Assignments..!!",
            message = "complete your assignment today only you have lot of work to complete!!!",
            app_icon = "C:/Users/admin/Desktop/Project/book.ico",
            timeout=10
        )
        time.sleep(10)