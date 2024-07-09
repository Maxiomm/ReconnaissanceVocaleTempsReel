import keyboard
import pyautogui
import time



def presser(commande):
    keyboard.press(commande)
    


def relacher(commande):
    keyboard.release(commande)



def presser_relacher(commande, delai = 0.5):
    keyboard.press(commande)
    time.sleep(delai)
    keyboard.release(commande)



def presser_relacher_double(commande1, commande2, delai = 0.5):
    keyboard.press(commande1)
    keyboard.press(commande2)
    time.sleep(delai)
    keyboard.release(commande1)
    keyboard.release(commande2)



def presser_relacher_souris(duree=0.1):
    pyautogui.mouseDown()
    time.sleep(duree)
    pyautogui.mouseUp()



def gerer_commande_mariobros1985(commande):

    if "avance" in commande:
        print("-----Action: Avancer-----")
        presser_relacher('d')
        return True

    if "recule" in commande:
        print("-----Action: Reculer-----")
        presser_relacher('a')
        return True

    if "saute" in commande:
        print("-----Action: Sauter-----")
        presser_relacher('space')
        return True

    if "bidet" in commande:
        print("-----Action: Sauter à droite-----")
        presser_relacher_double('space', 'd')
        return True

    if "remorque" in commande:
        print("-----Action: Sauter à gauche-----")
        presser_relacher_double('space', 'a')
        return True
    
    if "soude" in commande:
        print("-----Action: Avancer légèrement-----")
        presser_relacher('d', 0.25)
        return True
    
    if "percussion" in commande:
        print("-----Action: Reculer légèrement-----")
        presser_relacher('a', 0.25)
        return True

    if "acheter" in commande:
        print("-----Action: Avancer à l'infini-----")
        presser('d')
        return True
    
    if "suce" in commande:
        print("-----Action: Stopper l'avancement-----")
        relacher('d')
        return True

    if "criminel" in commande:
        print("-----Action: Gros saut à droite-----")
        presser_relacher_double('space', 'd', 0.75)
        return True
    
    if "goutte" in commande:
        print("-----Action: Gros saut à gauche-----")
        presser_relacher_double('space', 'a', 0.75)
        return True

    return False



def gerer_commande_supermario64(commande):

    if "manchot" in commande:
        print("-----Action: Avancer-----")
        presser_relacher('w')
        return True

    if "lourdaud" in commande:
        print("-----Action: Avancer léger-----")
        presser_relacher('w', 0.25)
        return True

    if "auberge" in commande:
        print("-----Action: Gauche-----")
        presser_relacher('a')
        return True
    
    if "chine" in commande:
        print("-----Action: Droite-----")
        presser_relacher('d')
        return True

    if "passeport" in commande:
        print("-----Action: Gauche léger-----")
        presser_relacher('a', 0.25)
        return True
    
    if "effacer" in commande:
        print("-----Action: Droite léger-----")
        presser_relacher('d', 0.25)
        return True

    if "parle" in commande:
        print("-----Action: Avancer à l'infini-----")
        presser('w')
        return True

    if "sucer" in commande:
        print("-----Action: Stopper l'avancement-----")
        relacher('w')
        return True

    if "princesse" in commande:
        print("-----Action: Sauter-----")
        presser_relacher_souris()
        return True

    return False



def gerer_commande_smashmelee(commande):

    if "cocon" in commande:
        print("-----Action: Sauter-----")
        presser_relacher('num 5')
        return True
    
    if "dvd" in commande:
        print("-----Action: Droite-----")
        presser_relacher('num 3')
        return True
    
    if "plein" in commande:
        print("-----Action: Gauche-----")
        presser_relacher('num 1')
        return True

    if "misérable" in commande:
        print("-----Action: Bouton A-----")
        presser_relacher('x', 0.25)
        return True
    
    if "transylvanie" in commande:
        print("-----Action: Bouton B-----")
        presser_relacher('z', 0.25)
        return True

    if "ping-pong" in commande:
        print("-----Action: B + bas-----")
        presser_relacher_double('z', 'num 2', 0.1)
        return True

    if "bataillon" in commande:
        print("-----Action: A + gauche-----")
        presser_relacher_double('x', 'num 1', 0.1)
        return True
    
    if "parier" in commande:
        print("-----Action: A + droite-----")
        presser_relacher_double('x', 'num 3', 0.1)
        return True

    return False