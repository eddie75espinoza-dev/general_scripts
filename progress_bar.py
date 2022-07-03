'''
Libreria TQDM para generar las barras de progreso,
puede anidar bucles facilmente y permite personalizar
las barras de progreso
'''
from tqdm import tqdm, trange
import random
import time

def tqdm_example_1():
    for i in tqdm(range(10)):
        time.sleep(0.2)

def tqdm_example_2():
    for i in trange(10, desc='outer_loop'):
        for j in trange(5, desc='inner_loop'):
            time.sleep(0.1)

def tqdm_example_3(add_tot=False):
    max_iter = 10
    tot = 0
    
    if add_tot:
        bar = tqdm(desc='update example', total=max_iter)
    else:
        bar = tqdm()
    
    while tot < max_iter:
        update_iter = random.randint(1,5)
        bar.update(update_iter)
        tot += update_iter
        time.sleep(0.2)

def tqdm_example_4():
    t = trange(100)
    for i in t:
        t.set_description(f'on iter {i}')
        time.sleep(0.02)

if __name__ == '__main__':
    #tqdm_example_1()
    tqdm_example_2()
    #tqdm_example_3()
    #tqdm_example_3(True)
    #tqdm_example_4()