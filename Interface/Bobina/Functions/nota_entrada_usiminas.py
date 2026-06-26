from pyautogui import *
from time import sleep
from keyboard import wait, is_pressed
from pyperclip import copy
import mouse







def pause(time=0.5):
    sleep(time)




def enter__(times=2, time=0):
    for c in  range(times):
        press("enter")
        sleep(time)


def wait_enter():
    while True:
        if mouse.is_pressed("x2"):
            return True  # Sai do loop quando Enter for pressionado
        elif mouse.is_pressed("x"):
            return False
        sleep(0.1)  # Pequena pausa para não sobrecarregar o CP



def usiminas_start(nota : str, lote : str, peso: str):
    print(f"""Lote: {lote}
peso: {peso}""")
    #print("Pressione Mouse_4 para iniciar")
    #wait_enter()
    pause(1)
    click(x=33, y=71)
    pause(0.5)
    click(x=126, y=129)
    pause(2)
    
    click(x=14, y=31)
    pause()
    click(x=65, y=252)
    pause()
    click(x=341, y=258)
    pause()
    click(x=530, y=293)
    pause(2)
    write("1854")
    click(x=792, y=523)
    pause()

    press("space")
    pause()
    for n in nota:
        write(n)
    enter__()
    pause(1)
    enter__(1)

    res = wait_enter()
    if not res:
        return

    for c in range(4):
        press("esc")

    click(x=14, y=31)
    pause()
    moveTo(x=103, y=274)
    pause(0.7)
    moveTo(x=366, y=315)
    pause()
    click(x=366, y=315)
    pause(5)
    doubleClick(x=354, y=330)
    press("enter")
    pause()
    click(x=606, y=364)
    enter__()
    pause()
    write("1854")
    pause()
    click(x=257, y=693)
    pause()
    enter__()  


    pause(3)
    # res = wait_enter()
    # if not res:
    #     return

    press("space")
    pause()
    for n in nota:
        write(n)
    enter__()
    pause(1)
    enter__(1)

    moveTo(x=697, y=500)

    res = wait_enter()
    if not res:
        return
    
    click(x=1182, y=653)
    pause()
    click(x=1111, y=100)
    write("0")
    enter__(3)
    pause()
    click(x=982, y=694)
    pause()
    click(x=282, y=658)
    pause()
    click(x=739, y=228)
    pause(.5)
    for l in peso:
        write(l)
    enter__(1)

    moveTo(x=909, y=580)

    res = wait_enter()
    if not res:
        return
    click(x=909, y=580)

    res = wait_enter()
    if not res:
        return
    pause()

    
    click(x=328, y=415)
    write("0")
    enter__(9)
    write("1,65")
    enter__(1)
    write("7,6")
    enter__(1)
    write("2")
    enter__(5)
    click(x=997, y=706)
    pause(1)
    enter__(1)
    res = wait_enter()
    if not res:
        return
    
    for l in lote:
        write(l)

    enter__(2)
    for p in peso:
        write(p)


    enter__(2)
    write("1")
    enter__(1)
    write("916")
    res = wait_enter()
    if not res:
        return
    enter__(6)
    pause(1)

    press("tab")

    res = wait_enter()
    if not res:
        return
    
    pause(0.5)
    enter__(4, 1)

    moveTo(x=723, y=561)
    
    res = wait_enter()
    if not res:
        print("Nessa caso a nota possui titulo anteceipando, certo?")
        pass
    else:
        enter__(6)

        write("NFe")
        enter__(3)
        write("301")
        enter__(1)
        write("3505")
        press("tab")

    

    res = wait_enter()
    if not res:
        return
    
    enter__()
    pause(1.5)
    
    for c in range(4):
        press("esc")

    click(x=40, y=75)
    pause(.5)
    click(x=153, y=380)
    pause(1)
    click(x=83, y=31)
    click(x=93, y=54)
    pause()
    click(x=518, y=79)
    pause()
    click(x=640, y=395)
    enter__()
    pause()
    click(x=796, y=480)
    pause()
    moveTo(x=1334, y=157)
    pause(1)

    click(x=610, y=199)
    press("space")
    for n in lote:
        write(n)
    
    enter__(3)
    pause()
    click(x=971, y=674)
    pause()
    num = "15"
    for  n in num:
        write(n)
    enter__()


    print("confirme a classificação")
    res = wait_enter()
    if not res:
        return
    write("eustaquio")
    press("tab")
    write("eustaqui")
    press("tab")
    press("enter")
    write(".")
    press("tab")
    enter__(2)

    pause(1)
    for c in range(4):
        press("esc")




if __name__ == "__main__":
    nota = "7522941"
    lote = "123456789"
    peso = "123456"
 
    usiminas_start(nota, lote, peso)