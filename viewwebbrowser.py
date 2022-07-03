''' 
abre una pagina web en las pestanas o en una pagina nueva

'''
import random
import time
import webbrowser

url = 'http://docs.python.org/'

# Open URL in a new tab, if a browser window is already open.
webbrowser.open_new_tab(url)

# Open URL in new window, raising the window if possible.
webbrowser.open_new(url)

while True:
    sites = random.choice(['google.com','youtube.com','pinterest.com'])
    visit = 'https://{}'.format(sites)
    webbrowser.open(visit, new = 2) # new = 1 (tab), 2 = (win)
    seconds = random.randint(2,5)
    time.sleep(seconds)