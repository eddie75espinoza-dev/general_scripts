from plyer import notification
import time

def notifyme():
    notification.notify(
        title='It worked', 
        message='Take a break now!', 
        app_name='Relax', 
        app_icon="Iconarchive-Red-Orb-Alphabet-Letter-E.ico", 
        timeout=10, 
        ticker='Relax - Take a break!', 
        toast=False
    )

if __name__ == '__main__':
    while True:
        notifyme()
        time.sleep(30)
