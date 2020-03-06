import random

def menu():
    print("Kő-Papír-Olló játék!")
    print()
    print("[1] Egy körös játék kezdése")
    print("[2] Több körös játék kezdése")
    print("[3] Szabályok és játékmenet")
    print("[4] Kilépés")
    print()

def select_menu_item():
    n_condition = True
    while n_condition == True:
        number = int(input("Kérem válasszon menüpontot: "))
        if number<5 or number > 0 : n_condition=False
    return number
        
def rules():
    print("----------Szabályok----------")
    print("     A kő eltöri az ollót.")
    print("A papír becsomagolja a követ.")
    print(" Az olló elvágja a papírt.")
    print("_____________________________")
    print("Több körös játékmenet esetén ")
    print(" a játék 3 győzelemig tart.")
    print("-----------------------------")
    print("")
    
def menu_item_1():
    condition=True

    while condition==True:
         human_tip = input('Adj egy tippet: ')
         human_tip = human_tip.lower()
         if human_tip == 'kő' or human_tip == 'papír' or human_tip == 'olló' : condition=False

    human_tip_value = answers[human_tip]
    cpu_tip = random.choice(list(answers.keys()))
    cpu_tip_value = answers[cpu_tip]

    
    print('\nJátékos tippje: {} \nGép tippje: {}'.format(human_tip, cpu_tip))
    result = (human_tip_value-cpu_tip_value) % 3
    print()
    for key in results:
        if(results[key] == result):
            print("\n>>>",key,"<<<\n")

    return result

def menu_item_2():
    human_score = 0
    cpu_score = 0

    score_condition = True
    while score_condition == True:
        win = menu_item_1()
        if win == 1:
            human_score += 1
        if win == 2:
            cpu_score += 1
        print("A játék állása:\n  Játékos ponszáma: ",human_score,"\n  Számítógép pontszáma: ",cpu_score)
        if human_score == 3 or cpu_score == 3: score_condition=False
        
    if human_score == 3:
        print("\n\n>>>[A játék nyertese a Játékos!]<<<\n\n")
    else:
        print("\n\n>>>[A játék nyertese a Számítógép!]<<<\n\n")

while True:
    menu()
    num = select_menu_item()
    answers = { 'kő' : 0, 'papír' : 1, 'olló' : 2 }
    results = { 'Döntetlen' : 0, 'Játékos győzőtt' : 1, 'Gép győzőtt' : 2 }

    if num == 1:
        menu_item_1()
    if num == 2:
        menu_item_2()
    if num == 3:
        rules()
        
    if num == 4: 
        break

print("\nKöszönöm a játékot!\n")
