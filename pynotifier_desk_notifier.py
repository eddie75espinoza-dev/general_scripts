# pip install py-notifier
import time
from pynotifier import Notification

def send_notification(sec):
    time.sleep(sec)
    Notification(
        title = "It Worked!",
        description = "Awesome!",
        icon_path = None,#"C:\\Users\\Usuario\\Desktop\\Backup\\Desktop\\Python\\PyGeneral\\Iconarchive-Red-Orb-Alphabet-Letter-E.ico", #https://iconarchive.com/show/red-orb-alphabet-icons-by-iconarchive/Letter-E-icon.html
        duration = 7,
        urgency = "normal"
    ).send()

send_notification(2)

