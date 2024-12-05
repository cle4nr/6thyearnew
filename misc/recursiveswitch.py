import time
def switch(ammo):
    if ammo < 0:
        return
        
    time.sleep(0.1)
    print(f'Ammo:{ammo}')
    return switch(ammo -1)
switch(19)
        