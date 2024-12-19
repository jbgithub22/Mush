# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 21:43:31 2020

@author: jbarc
"""

#-------------STRING-FORMAT-------------#
            
ctre_fmt = '{:^48}'
info_fmt = '{:<24}'
left_info_fmt = '{:<26}'
right_info_fmt = '{:>6}'
action_fmt = '{:<26}{:>24}'
action_ctr = '{:^50}'
quot_left_fmt = '{:<26}'
quot_right_fmt = '{:>50}'

#-------------DICTIONARIES-------------#

player = {'Name':'Name', 'Weapon':'Weapon', 'Attack_Modifier': 1.5, 'HP':1000}
monster = {'HP':1000,'Atk':100,'Def':100, 'Agi':100}
inventory = {'1':'Sword', '2':'Laptop', '3':'Water Bottle'}


# Counters
clear_cupboard_counter = 0
clear_table_counter = 0
giveup_table_counter = 0
giveup_cupboard_counter = 0
side_table_clear = 0
window_clear = 0
cupboard_clear = 0

# Frame Listing

## Title Frame
Title_Screen_1 = [*range(0,20)]

## Story Frame
Story_Graphic = list(map(str,[*range(0,20)]))


## Battle Frame

### Header Display
header_0 = ""
header_1 = ""
header_2 = ""

Header_Graphic = [header_0, header_1, header_2]

### Mushroom & Player Display

Monster_Graphic = list(map(str,[*range(0,10)]))
Info_Graphic = list(map(str,[*range(0,10)]))
Footer_Graphic = list(map(str,[*range(0,7)]))

### Combined Display
Middle_Graphic = zip(Info_Graphic, Monster_Graphic)
Middle_Graphic = [' '.join(tups) for tups in Middle_Graphic]
Battle_Screen = Header_Graphic + Middle_Graphic + Footer_Graphic



def display_graphic(graphics_list, player, monster):
    for line in graphics_list:
        print(line)

def main_menu(player, monster, inventory):

    while True:
        # Reset Player & Monster Dictionaries
        player = {'Name': 'Name', 'Weapon': 'Weapon', 'Attack_Modifier': 1.5, 'HP': 1000}
        monster = {'HP': 1000, 'Atk': 100, 'Def': 100, 'Agi': 100}
        inventory = {'1': 'Sword', '2': 'Laptop', '3': 'Water Bottle'}

        # Reset counters
        global clear_cupboard_counter
        clear_cupboard_counter = 0
        global clear_table_counter
        clear_table_counter = 0
        global giveup_table_counter
        giveup_table_counter = 0
        global giveup_cupboard_counter
        giveup_cupboard_counter = 0
        global side_table_clear
        side_table_clear = 0
        global window_clear
        window_clear = 0
        global cupboard_clear
        cupboard_clear = 0

        Title_Screen_1[0] = ''
        Title_Screen_1[1] = ''
        Title_Screen_1[2] = ''
        Title_Screen_1[3] = ctre_fmt.format(' __  __           _     _ ')
        Title_Screen_1[4] = ctre_fmt.format('|  \/  |         | |   | |')
        Title_Screen_1[5] = ctre_fmt.format('| \  / |_   _ ___| |__ | |')
        Title_Screen_1[6] = ctre_fmt.format("| |\/| | | | / __| '_ \| |")
        Title_Screen_1[7] = ctre_fmt.format('| |  | | |_| \__ \ | | |_|')
        Title_Screen_1[8] = ctre_fmt.format('|_|  |_|\__,_|___/_| |_(_)')
        Title_Screen_1[9] = ''
        Title_Screen_1[10] = ''
        Title_Screen_1[11] = ''
        Title_Screen_1[12] = ctre_fmt.format('[Main Menu]')
        Title_Screen_1[13] = '' 
        Title_Screen_1[14] = ctre_fmt.format('<Start>')
        Title_Screen_1[15] = ctre_fmt.format('<Options>')
        Title_Screen_1[16] = ctre_fmt.format('<End>')
        Title_Screen_1[17] = ''
        Title_Screen_1[18] = ctre_fmt.format('Copyright 2020  Group7')
        Title_Screen_1[19] = ''
        
        display_graphic(Title_Screen_1, player, monster)
        
        player_input = input('Type the text between < > here to select: ')
        if 'start' in player_input.lower():
            game(player, monster, inventory)
            continue
        if 'option' in player_input.lower():
            option()
            continue
        if ('end' in player_input.lower()) or ('exit' in player_input.lower()):
            exit_frame()
            continue
        else:
            continue
            
def option():
    Title_Screen_1[12] = ctre_fmt.format('[Options]')
    Title_Screen_1[14] = ctre_fmt.format('=================================')
    Title_Screen_1[15] = ctre_fmt.format('||       Sorry no options      ||')
    Title_Screen_1[16] = ctre_fmt.format("|| we're still noobs at coding ||")
    Title_Screen_1[17] = ctre_fmt.format('=================================')
    Title_Screen_1[18] = ctre_fmt.format('>>> Press enter to go back <<<')
    display_graphic(Title_Screen_1, player, monster)
    input()
            
    
def exit_frame():
    while True:
        Title_Screen_1[12] = ' '
        Title_Screen_1[14] = ctre_fmt.format('===================')
        Title_Screen_1[15] = ctre_fmt.format('|| End the game? ||')
        Title_Screen_1[16] = ctre_fmt.format('===================')
        Title_Screen_1[18] = ctre_fmt.format('Please type <Yes>  or <No>')
        display_graphic(Title_Screen_1, player, monster)
        pl_inp = input()
        if 'yes' in pl_inp.lower():
            exit()
        elif 'no' in pl_inp.lower():
            break
        else:
            continue
    
def weapon_selection(player, monster, inventory):
    ## Weapon select prompt
    Title_Screen_1[10] = 'Now choose your weapon!'
    Title_Screen_1[12] = "Fight close quarters with a [Sword]?"
    Title_Screen_1[13] = "Smack it with you [Laptop]?"
    Title_Screen_1[14] = "Or throw your [Water Bottle] at it?"
    display_graphic(Title_Screen_1, player, monster)
    while True:
        try:
            Weapon = str(input('Type your chosen weapon here: '))
            if ('sword' in Weapon.lower()) or ('laptop' in Weapon.lower()) or ('water bottle' in Weapon.lower()):
                Wpn = {'Weapon':Weapon}
                player.update(Wpn)
                return player
            else:
                Title_Screen_1[18] = ctre_fmt.format('Not one of the choices. Please type one of the listed weapons between []')
                display_graphic(Title_Screen_1, player, monster)
                continue
        except ValueError:
            print('Not a word! Please try again.')
    print("So you've choseen a " + Weapon + '!')
    print()
    print("Oh no! An agitated wild Mushroom appeared while you were about to leave the Weapon's Store")
    print()
    print("You need to fight!")



def game(player, monster, inventory):
    
    # Name Input Screen
    
    Title_Screen_1[12] = ''
    Title_Screen_1[13] = '' 
    Title_Screen_1[14] = ''
    Title_Screen_1[15] = ctre_fmt.format('========================')
    Title_Screen_1[16] = ctre_fmt.format('|| What is your name? ||')
    Title_Screen_1[17] = ctre_fmt.format('========================')
    Title_Screen_1[18] = ''
    display_graphic(Title_Screen_1, player, monster)
    name = input('Type your name here: ')

    name_input = 1
    while name_input == 1:
        if name.isdigit() is False and name.isalpha() is False:
            name = input('Please type something else: ')
        elif len(name) > 10:
            name = input('Please enter a name of up to 10 characters: ')
        else:
            name_input = 0
            p_name = {'Name':name}
            player.update(p_name)
            story(player, monster, inventory)

def story(player, monster, inventory):

    #storyline

    Story_Graphic[0] = ''
    Story_Graphic[1] = ''
    Story_Graphic[2] = ''
    Story_Graphic[3] = ''
    Story_Graphic[4] = ''
    Story_Graphic[5] = ''
    Story_Graphic[6] = ''
    Story_Graphic[7] = quot_left_fmt.format('"')
    Story_Graphic[8] = ''
    Story_Graphic[9] = ctre_fmt.format(player['Name'])
    Story_Graphic[10] = ''
    Story_Graphic[11] = quot_right_fmt.format('"')
    Story_Graphic[12] = ''
    Story_Graphic[13] = ''
    Story_Graphic[14] = ''
    Story_Graphic[15] = ''
    Story_Graphic[16] = ''
    Story_Graphic[17] = ''
    Story_Graphic[18] = ''
    Story_Graphic[19] = ''
    display_graphic(Story_Graphic, player, monster)
    input('Press enter to continue')

    Story_Graphic[7] = ''
    Story_Graphic[8] = ''
    Story_Graphic[9] = ctre_fmt.format('?')
    Story_Graphic[10] = ''
    Story_Graphic[11] = ''
    display_graphic(Story_Graphic, player, monster)
    input('Press enter to continue')

    Story_Graphic[7] = quot_left_fmt.format('"')
    Story_Graphic[8] = ''
    Story_Graphic[9] = ctre_fmt.format('Wake up.')
    Story_Graphic[10] = ''
    Story_Graphic[11] = quot_right_fmt.format('"')
    display_graphic(Story_Graphic, player, monster)
    input('Press enter to continue')

    Story_Graphic[7] = ''
    Story_Graphic[8] = ctre_fmt.format('==================================')
    Story_Graphic[9] = ctre_fmt.format('You open your eyes slowly...')
    Story_Graphic[10] = ctre_fmt.format('waking up to an unfamiliar place.')
    Story_Graphic[11] = ctre_fmt.format('==================================')
    display_graphic(Story_Graphic, player, monster)
    input('Press enter to continue')

    Story_Graphic[8] = ''
    Story_Graphic[9] = ctre_fmt.format('Where am I?')
    Story_Graphic[10] = ctre_fmt.format("Who's calling me??")
    Story_Graphic[11] = ''
    display_graphic(Story_Graphic, player, monster)
    input('Press enter to continue')
    three_objects_choice(player, monster, inventory)
    return

def side_table(player, monster, inventory):
    Story_Graphic[3] = '         .----------------------------.'
    Story_Graphic[4] = '         |' + ' ' * 14 + '*' + ' ' * 14 + '|         '
    Story_Graphic[5] = '         |' + ' ' * 29 + '|         '
    Story_Graphic[6] = '         |' + ' ' * 29 + '|         '
    Story_Graphic[7] = '         |-----------------------------|'
    Story_Graphic[8] = ''
    Story_Graphic[9] = ''
    Story_Graphic[10] = ctre_fmt.format('<Open>        <Go back>')
    Story_Graphic[11] = ''
    Story_Graphic[13] = ctre_fmt.format("----------------------------------------------")
    Story_Graphic[14] = ctre_fmt.format('You approach the wooden side table.')
    Story_Graphic[15] = ctre_fmt.format("----------------------------------------------")
    display_graphic(Story_Graphic, player, monster)

    side_table_decision = input('What would you like to do? ')

    act_choice2_side_table_decisions = 1
    while act_choice2_side_table_decisions == 1:
        if side_table_decision.lower() == 'open':
            act_choice2_side_table_decisions == 0
            side_table_interaction(player, monster, inventory)
            return
        elif side_table_decision.lower() == 'go back' or side_table_decision.lower() == 'back' or side_table_decision.lower() == 'goback':
            act_choice2_side_table_decisions == 0
            three_objects_choice(player, monster, inventory)
            return
        else:
            side_table_decision = input('Please enter one of the options between < >: ')


def window(player, monster, inventory):
    Story_Graphic[0] = ''
    Story_Graphic[1] = '         -------------------------------'
    Story_Graphic[2] = '         |' + ' ' * 14 + '|' + ' ' * 14 + '|         '
    Story_Graphic[3] = '         |' + ' ' * 14 + '|' + ' ' * 14 + '|         '
    Story_Graphic[4] = '         |--------------|--------------|'
    Story_Graphic[5] = '         |' + ' ' * 14 + '|' + ' ' * 14 + '|         '
    Story_Graphic[6] = '         |' + ' ' * 14 + '|' + ' ' * 14 + '|         '
    Story_Graphic[7] = '         -------------------------------'
    Story_Graphic[8] = ''
    Story_Graphic[9] = ''
    Story_Graphic[10] = ctre_fmt.format('<Look under>    <Look outside>    <Go back>')
    Story_Graphic[11] = ''
    Story_Graphic[12] = ''
    Story_Graphic[13] = ctre_fmt.format("----------------------------------------------")
    Story_Graphic[14] = ctre_fmt.format('You approach the window.')
    Story_Graphic[15] = ctre_fmt.format("----------------------------------------------")
    Story_Graphic[16] = ''
    Story_Graphic[17] = ''
    Story_Graphic[18] = ''
    Story_Graphic[19] = ''
    display_graphic(Story_Graphic, player, monster)

    window_decision = input('What would you like to do? ')

    act_choice3_window_decisions = 1
    while act_choice3_window_decisions == 1:
        if window_decision.lower() == 'look under' or window_decision.lower() == 'under' or window_decision.lower() == 'lookunder':
            act_choice3_window_decisions == 0
            look_under_window(player, monster, inventory)
            return
        elif window_decision.lower() == 'look outside' or window_decision.lower() == 'outside' or window_decision.lower() == 'lookoutside':
            act_choice3_window_decisions == 0
            look_outside_window(player, monster, inventory)
            return
        elif window_decision.lower() == 'go back' or window_decision.lower() == 'back' or window_decision.lower() == 'goback':
            act_choice3_window_decisions == 0
            three_objects_choice(player, monster, inventory)
            return
        else:
            window_decision = input('Please enter one of the options between < >: ')

def cupboard(player, monster, inventory):
    Story_Graphic[0] = ''
    Story_Graphic[1] = '                 ----------------'
    Story_Graphic[2] = '                 |' + ' ' * 14 + '|'
    Story_Graphic[3] = '                 |' + ' ' * 14 + '|'
    Story_Graphic[4] = '                 |--------------|'
    Story_Graphic[5] = '                 |' + ' ' * 6 + "|" + ' ' * 7 + '|'
    Story_Graphic[6] = '                 |' + ' ' * 6 + "|" + ' ' * 7 + '|'
    Story_Graphic[7] = '                 |' + ' ' * 6 + "|" + ' ' * 7 + '|'
    Story_Graphic[8] = '                 |' + ' ' * 6 + "|" + ' ' * 7 + '|'
    Story_Graphic[9] = '                 |--------------|'
    Story_Graphic[10] = ''
    Story_Graphic[11] = ''
    Story_Graphic[12] = ctre_fmt.format('<Look inside>        <Go back>')
    Story_Graphic[13] = ''
    Story_Graphic[14] = ''
    Story_Graphic[15] = ctre_fmt.format("----------------------------------------------")
    Story_Graphic[16] = ctre_fmt.format('You approach the cupboard.')
    Story_Graphic[17] = ctre_fmt.format("----------------------------------------------")
    Story_Graphic[18] = ''
    Story_Graphic[19] = ''

    display_graphic(Story_Graphic, player, monster)

    cupboard_decision = input('What would you like to do? ')

    act_choice4_cupboard_decisions = 1
    while act_choice4_cupboard_decisions == 1:
        if cupboard_decision.lower() == 'look inside' or cupboard_decision.lower() == 'inside' or cupboard_decision.lower() == 'lookinside' or cupboard_decision.lower() == 'in':
            act_choice4_cupboard_decisions == 0
            look_inside_cupboard(player, monster, inventory)
            return
        elif cupboard_decision.lower() == 'go back' or cupboard_decision.lower() == 'back' or cupboard_decision.lower() == 'goback':
            act_choice4_cupboard_decisions == 0
            three_objects_choice(player, monster, inventory)
            return
        else:
            cupboard_decision = input('Please enter one of the options between < >: ')

def three_objects_choice(player, monster, inventory):
    Story_Graphic[0] = ''
    Story_Graphic[1] = ''
    Story_Graphic[2] = ''
    Story_Graphic[3] = ''
    Story_Graphic[4] = ''
    Story_Graphic[5] = ''
    Story_Graphic[6] = ctre_fmt.format('=============================')
    Story_Graphic[7] = ctre_fmt.format('You look around and decide')
    Story_Graphic[8] = ctre_fmt.format('to take a closer look at...')
    Story_Graphic[9] = ctre_fmt.format('=============================')
    Story_Graphic[10] = ''
    Story_Graphic[11] = ''
    Story_Graphic[12] = ''
    Story_Graphic[13] = ctre_fmt.format('<Side table>   <Window>   <Cupboard>')
    Story_Graphic[14] = ''
    Story_Graphic[15] = ''
    Story_Graphic[16] = ''
    Story_Graphic[17] = ''
    Story_Graphic[18] = ''

    #counters to check if the player has cleared/tried out the stage
    global giveup_table_counter
    global giveup_cupboard_counter
    if (clear_table_counter + clear_cupboard_counter) == 2:
        three_objects_cleared(player, monster, inventory)
        return
    elif (clear_table_counter + giveup_cupboard_counter) == 2:
        three_objects_proceed_or_not(player, monster, inventory)
        return
    elif (giveup_table_counter + clear_cupboard_counter) == 2:
        three_objects_proceed_or_not(player, monster, inventory)
        return
    elif (giveup_table_counter + giveup_cupboard_counter) == 2:
        three_objects_proceed_or_not(player, monster, inventory)
        return

    display_graphic(Story_Graphic, player, monster)

    object = input('Which you would like to investigate? ')

    act_choice1_objects = 1
    while act_choice1_objects == 1:
        if object.lower() == "side table" or object.lower() == "sidetable" or object.lower() == "side" or object.lower() == "table":
            if side_table_clear == 1:
                object = input('There is nothing interesting here.\nPlease select another object: ')
            else:
                #to exit from while loop
                act_choice1_objects = 0
                side_table(player, monster, inventory)
                return
        elif object.lower() == "window":
            act_choice1_objects = 0
            window(player, monster, inventory)
            return
        elif object.lower() == "cupboard":
            if cupboard_clear == 1:
                object = input('There is nothing interesting here.\nPlease select another object: ')
            else:
                act_choice1_objects = 0
                cupboard(player, monster, inventory)
                return
        else:
            object = input ('Please enter one of the objects between < >: ')

def open_side_table(player, monster, inventory):
    Story_Graphic[0] = ''
    Story_Graphic[1] = ''
    Story_Graphic[2] = ''
    Story_Graphic[3] = '         .----------------------------.'
    Story_Graphic[4] = '         |' + ' ' * 14 + '*' + ' ' * 14 + '|         '
    Story_Graphic[5] = '         |' + ' ' * 29 + '|         '
    Story_Graphic[6] = '         |' + ' ' * 29 + '|         '
    Story_Graphic[7] = '         |-----------------------------|'
    Story_Graphic[8] = ''
    Story_Graphic[9] = ''
    Story_Graphic[10] = ctre_fmt.format("Attack Strength +50")
    Story_Graphic[11] = ''
    Story_Graphic[12] = ''
    Story_Graphic[13] = ctre_fmt.format("----------------------------------------------")
    Story_Graphic[14] = ctre_fmt.format("You found a bottle of red solution!")
    Story_Graphic[15] = ctre_fmt.format("This is added to your inventory.")
    Story_Graphic[16] = ctre_fmt.format("----------------------------------------------")
    Story_Graphic[17] = ''
    Story_Graphic[18] = ''
    Story_Graphic[19] = ''
    display_graphic(Story_Graphic, player, monster)

    #update inventory with secret attack potion
    inventory['4'] = 'Red solution'

    #update player Attack Modifier
    player['Attack_Modifier'] += 1

    #cleared stage
    global clear_table_counter
    clear_table_counter += 1
    global side_table_clear
    side_table_clear = 1

    # return to object selection
    input('Press enter to return to object selection')
    three_objects_choice(player, monster, inventory)
    return

def side_table_interaction(player, monster, inventory):
    Story_Graphic[0] = ''
    Story_Graphic[1] = ''
    Story_Graphic[2] = ''
    Story_Graphic[3] = '         .----------------------------.'
    Story_Graphic[4] = '         |' + ' ' * 14 + '*' + ' ' * 14 + '|         '
    Story_Graphic[5] = '         |' + ' ' * 29 + '|         '
    Story_Graphic[6] = '         |' + ' ' * 29 + '|         '
    Story_Graphic[7] = '         |-----------------------------|'
    Story_Graphic[8] = ''
    Story_Graphic[9] = ''
    Story_Graphic[10] = ctre_fmt.format('<Try again>        <Give up>')
    Story_Graphic[11] = ''
    Story_Graphic[12] = ''
    Story_Graphic[13] = ctre_fmt.format("----------------------------------------------")
    Story_Graphic[14] = ctre_fmt.format("Hmm... the drawer doesn't seem to barge.")
    Story_Graphic[15] = ctre_fmt.format("----------------------------------------------")
    Story_Graphic[16] = ''
    Story_Graphic[17] = ''
    Story_Graphic[18] = ''
    Story_Graphic[19] = ''
    display_graphic(Story_Graphic, player, monster)

    side_table_action = input('What would you like to do? ')

    act_choice3_side_table_actions = 1
    while act_choice3_side_table_actions == 1:
        if side_table_action.lower() == 'try again' or side_table_action.lower() == 'tryagain' or side_table_action.lower() == 'try' or side_table_action.lower() == 'again':
            act_choice3_side_table_actions == 0
            open_side_table(player, monster, inventory)
            return
        elif side_table_action.lower() == 'give up' or side_table_action.lower() == 'giveup' or side_table_action.lower() == 'back':
            act_choice3_side_table_actions == 0
            global giveup_table_counter
            giveup_table_counter += 1
            three_objects_choice(player, monster, inventory)
            return
        else:
            side_table_action = input('Please enter one of the options between < >: ')

def look_under_window(player, monster, inventory):
    Story_Graphic[0] = ''
    Story_Graphic[1] = '         -------------------------------'
    Story_Graphic[2] = '         |' + ' ' * 14 + '|' + ' ' * 14 + '|         '
    Story_Graphic[3] = '         |' + ' ' * 14 + '|' + ' ' * 14 + '|         '
    Story_Graphic[4] = '         |--------------|--------------|'
    Story_Graphic[5] = '         |' + ' ' * 14 + '|' + ' ' * 14 + '|         '
    Story_Graphic[6] = '         |' + ' ' * 14 + '|' + ' ' * 14 + '|         '
    Story_Graphic[7] = '         -------------------------------'
    Story_Graphic[8] = ''
    Story_Graphic[9] = ''
    Story_Graphic[10] = ''
    Story_Graphic[11] = ''
    Story_Graphic[12] = ctre_fmt.format("----------------------------------------------")
    Story_Graphic[13] = ctre_fmt.format('You notice a small carving under the window.')
    Story_Graphic[14] = ctre_fmt.format("You can roughly make it out as '0812'.")
    Story_Graphic[15] = ctre_fmt.format("----------------------------------------------")
    Story_Graphic[16] = ''
    Story_Graphic[17] = ''
    Story_Graphic[18] = ''
    Story_Graphic[19] = ''
    display_graphic(Story_Graphic, player, monster)

    input('Press enter to return to window action selection')
    window(player, monster, inventory)
    return

def look_outside_window(player, monster, inventory):
    Story_Graphic[0] = ''
    Story_Graphic[1] = '         -------------------------------'
    Story_Graphic[2] = '         |' + ' ' * 14 + '|' + ' ' * 14 + '|         '
    Story_Graphic[3] = '         |' + ' ' * 14 + '|' + ' ' * 14 + '|         '
    Story_Graphic[4] = '         |--------------|--------------|'
    Story_Graphic[5] = '         |' + ' ' * 14 + '|' + ' ' * 14 + '|         '
    Story_Graphic[6] = '         |' + ' ' * 14 + '|' + ' ' * 14 + '|         '
    Story_Graphic[7] = '         -------------------------------'
    Story_Graphic[8] = ''
    Story_Graphic[9] = ''
    Story_Graphic[10] = ''
    Story_Graphic[11] = ''
    Story_Graphic[12] = ctre_fmt.format("----------------------------------------------")
    Story_Graphic[13] = ctre_fmt.format('You discovered that you are in a tall building')
    Story_Graphic[14] = ctre_fmt.format("and it is surrounded by colourful mushrooms!")
    Story_Graphic[15] = ctre_fmt.format("----------------------------------------------")
    Story_Graphic[16] = ''
    Story_Graphic[17] = ''
    Story_Graphic[18] = ''
    Story_Graphic[19] = ''
    display_graphic(Story_Graphic, player, monster)

    input('Please enter to return to window action selection')
    window(player, monster, inventory)
    return

def look_inside_cupboard(player, monster, inventory):
    Story_Graphic[0] = ''
    Story_Graphic[1] = '                 ----------------'
    Story_Graphic[2] = '                 |' + ' ' * 14 + '|'
    Story_Graphic[3] = '                 |' + ' ' * 14 + '|'
    Story_Graphic[4] = '                 |--------------|'
    Story_Graphic[5] = '                 |' + ' ' * 6 + "|" + ' ' * 7 + '|'
    Story_Graphic[6] = '                 |' + ' ' * 6 + "|" + ' ' * 7 + '|'
    Story_Graphic[7] = '                 |' + ' ' * 6 + "|" + ' ' * 7 + '|'
    Story_Graphic[8] = '                 |' + ' ' * 6 + "|" + ' ' * 7 + '|'
    Story_Graphic[9] = '                 |--------------|'
    Story_Graphic[10] = ''
    Story_Graphic[11] = ''
    Story_Graphic[12] = ctre_fmt.format('<Try 4-digit code>        <Go back>')
    Story_Graphic[13] = ''
    Story_Graphic[14] = ''
    Story_Graphic[15] = ctre_fmt.format("----------------------------------------------")
    Story_Graphic[16] = ctre_fmt.format('You found a safe secured with a number lock.')
    Story_Graphic[17] = ctre_fmt.format("----------------------------------------------")
    Story_Graphic[18] = ''
    Story_Graphic[19] = ''

    display_graphic(Story_Graphic, player, monster)

    cupboard_input = input("Enter the 4-digit code or enter 'back'\nto return to object selection: ")

    act_choice5_cupboard_actions = 1
    while act_choice5_cupboard_actions == 1:
        num_check = cupboard_input.isdigit()
        if num_check is True:
            if cupboard_input == '0812':
                act_choice5_cupboard_actions == 0
                open_safe(player, monster, inventory)
                return
            elif len(cupboard_input) < 4 or len(cupboard_input) > 4:
                cupboard_input = input("Please enter a valid 4-digit code: ")
            else:
                act_choice5_cupboard_actions == 0
                global giveup_cupboard_counter
                giveup_cupboard_counter += 1
                input("\nThe safe doesn't open.\nPress enter to continue")
                look_inside_cupboard(player, monster, inventory)
                return
        elif cupboard_input.lower() == 'go back' or cupboard_input.lower() == 'back' or cupboard_input.lower() == 'goback':
            act_choice5_cupboard_actions == 0
            three_objects_choice(player, monster, inventory)
            return
        else:
            cupboard_input = input('Please choose one of the options above: ')

def open_safe(player, monster, inventory):
    Story_Graphic[0] = ''
    Story_Graphic[1] = '                 ----------------'
    Story_Graphic[2] = '                 |' + ' ' * 14 + '|'
    Story_Graphic[3] = '                 |' + ' ' * 14 + '|'
    Story_Graphic[4] = '                 |--------------|'
    Story_Graphic[5] = '                 |' + ' ' * 6 + "|" + ' ' * 7 + '|'
    Story_Graphic[6] = '                 |' + ' ' * 6 + "|" + ' ' * 7 + '|'
    Story_Graphic[7] = '                 |' + ' ' * 6 + "|" + ' ' * 7 + '|'
    Story_Graphic[8] = '                 |' + ' ' * 6 + "|" + ' ' * 7 + '|'
    Story_Graphic[9] = '                 |--------------|'
    Story_Graphic[10] = ''
    Story_Graphic[11] = ctre_fmt.format("Defense +75")
    Story_Graphic[12] = ''
    Story_Graphic[13] = ''
    Story_Graphic[14] = ctre_fmt.format("----------------------------------------------")
    Story_Graphic[15] = ctre_fmt.format("You've unlocked the safe and found some armour!")
    Story_Graphic[16] = ctre_fmt.format('It fits you perfectly~')
    Story_Graphic[17] = ctre_fmt.format("----------------------------------------------")
    Story_Graphic[18] = ''
    Story_Graphic[19] = ''
    display_graphic(Story_Graphic, player, monster)

    #update counter - cleared stage
    global clear_cupboard_counter
    clear_cupboard_counter += 1
    global cupboard_clear
    cupboard_clear = 1

    #return to object selection
    input('Press enter to return to object selection')
    three_objects_choice(player, monster, inventory)
    return

def three_objects_cleared(player, monster, inventory):
    Story_Graphic[0] = ''
    Story_Graphic[1] = ''
    Story_Graphic[2] = ''
    Story_Graphic[3] = ''
    Story_Graphic[4] = ''
    Story_Graphic[5] = ''
    Story_Graphic[6] = ctre_fmt.format('=====================================')
    Story_Graphic[7] = ctre_fmt.format('You have explored the whole room.')
    Story_Graphic[8] = ctre_fmt.format('The only way out is through the door.')
    Story_Graphic[9] = ctre_fmt.format('=====================================')
    Story_Graphic[10] = ''
    Story_Graphic[11] = ''
    Story_Graphic[12] = ''
    Story_Graphic[13] = ''
    Story_Graphic[14] = ''
    Story_Graphic[15] = ''
    Story_Graphic[16] = ''
    Story_Graphic[17] = ''
    Story_Graphic[18] = ''
    display_graphic(Story_Graphic, player, monster)

    input("Press enter to proceed to the door")
    before_battle(player, monster, inventory)
    return

def three_objects_proceed_or_not(player, monster, inventory):
    Story_Graphic[0] = ''
    Story_Graphic[1] = ''
    Story_Graphic[2] = ''
    Story_Graphic[3] = ''
    Story_Graphic[4] = ''
    Story_Graphic[5] = ''
    Story_Graphic[6] = ctre_fmt.format('=============================')
    Story_Graphic[7] = ctre_fmt.format('Seems like you have looked')
    Story_Graphic[8] = ctre_fmt.format('through all objects.')
    Story_Graphic[9] = ctre_fmt.format('=============================')
    Story_Graphic[10] = ''
    Story_Graphic[11] = ''
    Story_Graphic[12] = ''
    Story_Graphic[13] = ctre_fmt.format('<Side table>   <Window>   <Cupboard>')
    Story_Graphic[14] = ''
    Story_Graphic[15] = ctre_fmt.format('<Proceed to door>')
    Story_Graphic[16] = ''
    Story_Graphic[17] = ''
    Story_Graphic[18] = ''
    display_graphic(Story_Graphic, player, monster)

    object_proceed = input('What would you like to do? ')

    act_choice1_objects = 1
    while act_choice1_objects == 1:
        if object_proceed.lower() == "side table" or object_proceed.lower() == "sidetable" or object_proceed.lower() == "side" or object_proceed.lower() == "table":
            if side_table_clear == 1:
                object_proceed = input('You have already investigated this area.\nPlease select another object: ')
            else:
                # to exit from while loop
                act_choice1_objects = 0
                side_table(player, monster, inventory)
        elif object_proceed.lower() == "window":
            act_choice1_objects = 0
            window(player, monster, inventory)
            break
        elif object_proceed.lower() == "cupboard":
            act_choice1_objects = 0
            cupboard(player, monster, inventory)
            break
        elif object_proceed.lower() == "proceed to door" or object_proceed.lower() == "proceed" or object_proceed.lower() == "door":
            act_choice1_objects = 0
            before_battle(player, monster, inventory)
            break
        else:
            object_proceed = input('Please enter one of the objects between < >: ')

def before_battle(player, monster, inventory):
    Story_Graphic[0] = ''
    Story_Graphic[1] = ''
    Story_Graphic[2] = ''
    Story_Graphic[3] = ''
    Story_Graphic[4] = ''
    Story_Graphic[5] = ''
    Story_Graphic[6] = ''
    Story_Graphic[7] = ''
    Story_Graphic[8] = ctre_fmt.format('=====================================')
    Story_Graphic[9] = ctre_fmt.format('You open the door to a long hallway.')
    Story_Graphic[10] = ctre_fmt.format('You take a step forward.')
    Story_Graphic[11] = ctre_fmt.format('=====================================')
    Story_Graphic[12] = ''
    Story_Graphic[13] = ''
    Story_Graphic[14] = ''
    Story_Graphic[15] = ''
    Story_Graphic[16] = ''
    Story_Graphic[17] = ''
    Story_Graphic[18] = ''
    Story_Graphic[19] = ''
    display_graphic(Story_Graphic, player, monster)
    input('Press enter to continue')

    Story_Graphic[0] = ''
    Story_Graphic[1] = ''
    Story_Graphic[2] = ''
    Story_Graphic[3] = ''
    Story_Graphic[4] = ''
    Story_Graphic[5] = ''
    Story_Graphic[6] = ''
    Story_Graphic[7] = ctre_fmt.format('====================================')
    Story_Graphic[8] = ctre_fmt.format('Oh no!')
    Story_Graphic[9] = ctre_fmt.format("You've encountered a mushroom guard!")
    Story_Graphic[10] = ctre_fmt.format('Prepare for battle!')
    Story_Graphic[11] = ctre_fmt.format('====================================')
    Story_Graphic[12] = ''
    Story_Graphic[13] = ''
    Story_Graphic[14] = ''
    Story_Graphic[15] = ''
    Story_Graphic[16] = ''
    Story_Graphic[17] = ''
    Story_Graphic[18] = ''
    Story_Graphic[19] = ''
    display_graphic(Story_Graphic, player, monster)
    input('Press enter to continue')
    set_stats(player, monster, inventory)
    return

def set_stats(player, monster, inventory):
    Title_Screen_1[0] = ''
    Title_Screen_1[2] = ''
    Title_Screen_1[3] = ''
    Title_Screen_1[4] = 'But first, please set your stats:'
    Title_Screen_1[5] = ''
    Title_Screen_1[6] = 'Attack:   (Min 0; Max 100)'
    Title_Screen_1[7] = 'Defence:  (Min 0; Max 100)'
    Title_Screen_1[8] = 'Agility:  (Min 0; Max 100)'
    Title_Screen_1[15] = ''
    Title_Screen_1[16] = ''
    Title_Screen_1[17] = ''
    display_graphic(Title_Screen_1, player, monster)

    ## Attack Value
    Attack = stat_input('Attack')
    Title_Screen_1[6] = 'Attack:   '+ str(Attack)
    Title_Screen_1[18] = ' '
    display_graphic(Title_Screen_1, player, monster)

    Atk = Attack
    Atk = {'Attack':Atk}
    player.update(Atk)

    ## Defense Value
    Defense = stat_input('Defense')
    Title_Screen_1[7] = 'Defense:  ' + str(Defense)
    Title_Screen_1[18] = ' '
    display_graphic(Title_Screen_1, player, monster)

    Def = Defense
    Def = {'Defense':Def}
    player.update(Def)

    ## Agility Value
    Agility = stat_input('Agility')
    Title_Screen_1[8] = 'Agility:  ' + str(Agility)
    Title_Screen_1[18] = ' '

    Agi = Agility
    Agi = {'Defense':Agi}
    player.update(Agi)

    weapon_selection(player, monster, inventory)

    Battle_Action(player, monster, inventory)


def stat_input(stat):
    while True:
        try:
            value = int(input('Enter value for ' + stat + ': '))
            if value < 0 or value > 100:
                Title_Screen_1[18] = ctre_fmt.format('Please type a number from 0 to 100')
                display_graphic(Title_Screen_1, player, monster)
                continue
            else:
                return value
        except ValueError:
            Title_Screen_1[18] = ctre_fmt.format('Not a number! Please try again.')
            display_graphic(Title_Screen_1, player, monster)

# Attack = Monster_HP - Player_Attack_Val
# Taunt = Monster_Attack_Val + (Player_Defense*0.5)
# Inventory = "There is nothing in your inventory"
# Run = "The only exit is being blocked by the Wild Mushroom, try to run past it anyway?" - JB           

def Battle_Action(player, monster, inventory):
    Info_Graphic[0] = left_info_fmt.format("Monster: Wild Mushroom")
    Info_Graphic[1] = left_info_fmt.format("HP:   1000")
    Info_Graphic[2] = left_info_fmt.format("Atk:   100")
    Info_Graphic[3] = left_info_fmt.format("Def:   100")
    Info_Graphic[4] = left_info_fmt.format("Agi:   100")
    Info_Graphic[5] = left_info_fmt.format(" ")
    Info_Graphic[6] = left_info_fmt.format("Player: "+ player['Name'])
    Info_Graphic[7] = left_info_fmt.format("HP:   1000")
    Info_Graphic[8] = left_info_fmt.format("Atk:   100")
    Info_Graphic[9] = left_info_fmt.format("Def:   100")
    
    while True:
        Monster_Graphic[0] = "          *& ..*#@.        "
        Monster_Graphic[1] = "    .@,.,******..../((     "
        Monster_Graphic[2] = " @./////(**/((/(/**,//(    "
        Monster_Graphic[3] = "@/((#(/**'''''''**\((((((, "
        Monster_Graphic[4] = " @(&(   @ .,,. @   @(//((#,"
        Monster_Graphic[5] = "    @.  =      = .,**@#((( "
        Monster_Graphic[6] = "  %.               ,*(     "
        Monster_Graphic[7] = "  .                ,*/,    "
        Monster_Graphic[8] = "  ,             ..,**(     "
        Monster_Graphic[9] = "     @.,,,.,,,,**/(        "
        
        Footer_Graphic[0] = ''
        Footer_Graphic[1] = ''
        Footer_Graphic[2] = ("What does " + player['Name'] + " want to do?" )
        Footer_Graphic[3] = "------------------------------------------------------"
        Footer_Graphic[4] = "| " + action_fmt.format("<Attack> with " + player['Weapon'], "<Taunt> Mushroom>") + " |"
        Footer_Graphic[5] = "| " + action_fmt.format("Look at <Inventory>", "<Run> Away>") + " |"
        Footer_Graphic[6] = "------------------------------------------------------"

        Middle_Graphic = zip(Info_Graphic, Monster_Graphic)
        Middle_Graphic = [' '.join(tups) for tups in Middle_Graphic]
        Battle_Screen = Header_Graphic + Middle_Graphic + Footer_Graphic

        display_graphic(Battle_Screen, player, monster)
        Player_Action = input("Type <Action> here: ")
        

        if 'at' in Player_Action.lower():
            attack_sequence(player, monster, inventory)
            if monster['HP'] <= 0:
                Footer_Graphic[4] = "| " + action_ctr.format("You've defeated the monster!") + " |"
                Footer_Graphic[5] = "| " + action_ctr.format("Congratulations!") + " |"
                
                Middle_Graphic = zip(Info_Graphic, Monster_Graphic)
                Middle_Graphic = [' '.join(tups) for tups in Middle_Graphic]
                Battle_Screen = Header_Graphic + Middle_Graphic + Footer_Graphic
        
                display_graphic(Battle_Screen, player, monster)
                
                input('Press enter to continue')
        
                Monster_Graphic[0] = " "
                Monster_Graphic[1] = " "
                Monster_Graphic[2] = " "
                Monster_Graphic[3] = " "
                Monster_Graphic[4] = " "
                Monster_Graphic[5] = " "
                Monster_Graphic[6] = " "
                Monster_Graphic[7] = " "
                Monster_Graphic[8] = " "
                Monster_Graphic[9] = " "
                
                Footer_Graphic[4] = "| " + action_ctr.format("The game has ended") + " |"
                Footer_Graphic[5] = "| " + action_ctr.format("You will now return to the main menu") + " |"
                
                Middle_Graphic = zip(Info_Graphic, Monster_Graphic)
                Middle_Graphic = [' '.join(tups) for tups in Middle_Graphic]
                Battle_Screen = Header_Graphic + Middle_Graphic + Footer_Graphic
        
                display_graphic(Battle_Screen, player, monster)

                input('Press enter to continue')
                
                break

            else:
                Monster_Graphic[0] = "    \\    *& ..*#@.        "
                Monster_Graphic[1] = "    .\\\,******..../((     "
                Monster_Graphic[2] = " @.///\\\**/((/(/**,//(    "
                Monster_Graphic[3] = "@/((#(/*\\\'''''**\((((((, "
                Monster_Graphic[4] = " @(&(   @ \\\. @   @(//((#,"
                Monster_Graphic[5] = "    @.  =   \\\= .,**@#((( "
                Monster_Graphic[6] = "  %.          \\\  ,*(     "
                Monster_Graphic[7] = "  .             \\\,*/,    "
                Monster_Graphic[8] = "  ,             ..\\\(     "
                Monster_Graphic[9] = "     @.,,,.,,,,**/( \\     "
                
                Footer_Graphic[4] = "| " + action_ctr.format("The monster is still alive!") + " |"
                Footer_Graphic[5] = "| " + action_ctr.format("You need to attack again!") + " |"
                
                Middle_Graphic = zip(Info_Graphic, Monster_Graphic)
                Middle_Graphic = [' '.join(tups) for tups in Middle_Graphic]
                Battle_Screen = Header_Graphic + Middle_Graphic + Footer_Graphic
        
                display_graphic(Battle_Screen, player, monster)

                input('Press enter to continue')
                continue
            
        elif 'taunt' in Player_Action.lower():
            monster['Atk'] = round(monster['Atk'] + 100)
            monster['Def'] = round(monster['Def'] - 5)
            
            Info_Graphic[2] = left_info_fmt.format("Atk:" + right_info_fmt.format(monster['Atk']))
            Info_Graphic[3] = left_info_fmt.format("Def:" + right_info_fmt.format(monster['Def']))
                                  
            Footer_Graphic[4] = "| " + action_ctr.format("The Monster's Attack went up") + " |"
            Footer_Graphic[5] = "| " + action_ctr.format("But it's Defense went down!") + " |"
            
            Middle_Graphic = zip(Info_Graphic, Monster_Graphic)
            Middle_Graphic = [' '.join(tups) for tups in Middle_Graphic]
            Battle_Screen = Header_Graphic + Middle_Graphic + Footer_Graphic
    
            display_graphic(Battle_Screen, player, monster)
            
            input('Press enter to continue')
            continue

        elif 'inv' in Player_Action.lower():
            if ("4" in inventory) is True:
                Footer_Graphic[4] = "| " + action_ctr.format("You have a bottle of red solution!") + " |"
                Footer_Graphic[5] = "| " + action_ctr.format("Do you want to use it?") + " |"

                Middle_Graphic = zip(Info_Graphic, Monster_Graphic)
                Middle_Graphic = [' '.join(tups) for tups in Middle_Graphic]
                Battle_Screen = Header_Graphic + Middle_Graphic + Footer_Graphic

                display_graphic(Battle_Screen, player, monster)

                red_solution_choice = input('<Yes> or <No> : ')

                use_solution_or_not = 1
                while use_solution_or_not == 1:
                    if red_solution_choice.lower() == "yes":
                        use_solution_or_not = 0

                        # update player Attack Modifier
                        player['Attack_Modifier'] += 1

                        # update inventory to remove red solution
                        del inventory['4']

                        Footer_Graphic[4] = "| " + action_ctr.format("You feel stronger after drinking") + " |"
                        Footer_Graphic[5] = "| " + action_ctr.format("the bottle of red solution!") + " |"

                        Middle_Graphic = zip(Info_Graphic, Monster_Graphic)
                        Middle_Graphic = [' '.join(tups) for tups in Middle_Graphic]
                        Battle_Screen = Header_Graphic + Middle_Graphic + Footer_Graphic

                        display_graphic(Battle_Screen, player, monster)
                        input('Press enter to continue')
                        continue

                    elif red_solution_choice.lower() == "no":
                        use_solution_or_not = 0

                    else:
                        red_solution_choice = input('Please enter one of the objects between < >: ')

            elif ("4" in inventory) is False:
                Footer_Graphic[4] = "| " + action_ctr.format("There is nothing") + " |"
                Footer_Graphic[5] = "| " + action_ctr.format("in your inventory.") + " |"

                Middle_Graphic = zip(Info_Graphic, Monster_Graphic)
                Middle_Graphic = [' '.join(tups) for tups in Middle_Graphic]
                Battle_Screen = Header_Graphic + Middle_Graphic + Footer_Graphic

                display_graphic(Battle_Screen, player, monster)

                input('Press enter to continue')

        elif 'run' in Player_Action.lower():
            Footer_Graphic[4] = "| " + action_ctr.format("The only exit is being blocked by the Monster") + " |"
            Footer_Graphic[5] = "| " + action_ctr.format("Try to run past it anyway?") + " |"
            
            Middle_Graphic = zip(Info_Graphic, Monster_Graphic)
            Middle_Graphic = [' '.join(tups) for tups in Middle_Graphic]
            Battle_Screen = Header_Graphic + Middle_Graphic + Footer_Graphic
            
            display_graphic(Battle_Screen, player, monster)
            
            run_input = input('<Yes> or <No> : ')
            
            if 'yes' in run_input.lower():
                #player hp - 100 (Player dies, game end)
                Footer_Graphic[4] = "| " + action_ctr.format("You try to run pass the monster") + " |"
                Footer_Graphic[5] = "| " + action_ctr.format("Is this a good idea?") + " |"
                
                Middle_Graphic = zip(Info_Graphic, Monster_Graphic)
                Middle_Graphic = [' '.join(tups) for tups in Middle_Graphic]
                Battle_Screen = Header_Graphic + Middle_Graphic + Footer_Graphic
                
                display_graphic(Battle_Screen, player, monster)
                
                input('Press enter to continue')
                
                Footer_Graphic[4] = "| " + action_ctr.format("Not a good idea! The monster hit you!") + " |"
                Footer_Graphic[5] = "| " + action_ctr.format("You are dead.") + " |"
                
                player['HP'] = player['HP'] - 1000
                
                Info_Graphic[7] = left_info_fmt.format("HP:" + right_info_fmt.format(player['HP']))
                
                Middle_Graphic = zip(Info_Graphic, Monster_Graphic)
                Middle_Graphic = [' '.join(tups) for tups in Middle_Graphic]
                Battle_Screen = Header_Graphic + Middle_Graphic + Footer_Graphic
                
                display_graphic(Battle_Screen, player, monster)
                
                input('Press enter to continue')
                
                Footer_Graphic[4] = "| " + action_ctr.format("Game Over") + " |"
                Footer_Graphic[5] = "| " + action_ctr.format("Press Enter to return to Main Menu") + " |"
                
                Middle_Graphic = zip(Info_Graphic, Monster_Graphic)
                Middle_Graphic = [' '.join(tups) for tups in Middle_Graphic]
                Battle_Screen = Header_Graphic + Middle_Graphic + Footer_Graphic
                
                display_graphic(Battle_Screen, player, monster)

                input('Press enter to continue')
            
                break
            
            elif 'no' in run_input.lower():
                continue

            else:
                input('Please enter <Yes> or <No>')
                continue
            
            break

        else:
            Player_Action = input("Please enter one of the <Actions>!")
            continue


def attack_sequence(player, monster, inventory):
    Monster_Graphic = list(map(str, [*range(0, 10)]))

    Monster_Graphic[0] = "    \\    *& ..*#@.        "
    Monster_Graphic[1] = "    .\\\\,******..../((     "
    Monster_Graphic[2] = " @.///\\\\\**/((/(/**,//(    "
    Monster_Graphic[3] = "@/((#(/*\\\\\\'''''**\((((((, "
    Monster_Graphic[4] = " @(&(   @ \\\\\. @   @(//((#,"
    Monster_Graphic[5] = "    @.  =   \\\\\= .,**@#((( "
    Monster_Graphic[6] = "  %.          \\\\\  ,*(     "
    Monster_Graphic[7] = "  .             \\\\\,*/,    "
    Monster_Graphic[8] = "  ,             ..\\\(     "
    Monster_Graphic[9] = "     @.,,,.,,,,**/( \\     "

    monster['HP'] = round(monster['HP'] - player['Attack'] * player['Attack_Modifier'])

    Info_Graphic[0] = left_info_fmt.format("Monster: Wild Mushroom")
    Info_Graphic[1] = left_info_fmt.format("HP: " + right_info_fmt.format(monster['HP']))
    Info_Graphic[2] = left_info_fmt.format("Atk:" + right_info_fmt.format(monster['Atk']))
    Info_Graphic[3] = left_info_fmt.format("Def:" + right_info_fmt.format(monster['Def']))
    Info_Graphic[4] = left_info_fmt.format("Agi:   100")
    Info_Graphic[5] = left_info_fmt.format(" ")
    Info_Graphic[6] = left_info_fmt.format("Player: " + player['Name'])
    Info_Graphic[7] = left_info_fmt.format("HP: " + right_info_fmt.format(player['HP']))
    Info_Graphic[8] = left_info_fmt.format("Atk:   100")
    Info_Graphic[9] = left_info_fmt.format("Def:   100")

    Footer_Graphic[4] = "| " + action_ctr.format("You used your weapon!") + " |"
    Footer_Graphic[5] = "| " + action_ctr.format("The monster is hit!") + " |"

    Middle_Graphic = zip(Info_Graphic, Monster_Graphic)
    Middle_Graphic = [' '.join(tups) for tups in Middle_Graphic]
    Battle_Screen = Header_Graphic + Middle_Graphic + Footer_Graphic

    display_graphic(Battle_Screen, player, monster)

    input('Press enter to continue')

        
main_menu(player, monster, inventory)
