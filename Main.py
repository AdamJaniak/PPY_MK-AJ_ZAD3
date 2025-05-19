from ShoppingList import *

lista_do_biedronki = ShoppingList()

ShoppingList.show_actions()
action = input("what action you want to do: ")
lista_do_biedronki.chose_actions(action)
while not action == "0":
    ShoppingList.show_actions()
    action = input("what action you want to do: ")
    lista_do_biedronki.chose_actions(action)