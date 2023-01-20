import os
import Process_game

os.system('cls')

type_game = input('Введите 1 для игры с другим игроком или другую цифру для игры с ботом ')
if (type_game == '1'):
    Process_game.player_vs_player()
else:
    intel = input('Введите 0, для играть с глупым ботом, или другую цифру для игры с умным ботом ')
    if intel == '0':
        Process_game.player_vs_stupid_bot ()
    else:
        Process_game.player_vs_smart_bot ()