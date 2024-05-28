#Checkpoint Project - Codedex
#A classic mini-RPG (role-playing game)
# hp health points, 
# character moves like attack/block/heal, 
# NPCs (non-player characters) that attacks based on a random number generator.

#Charcter Attributes
import random


charhp = 100
charattack = 10
#charblock = random percentage generation
charhealing = 0
npc1hp = 75
npcattack = 25
npc2hp = 90
npc2attack = 30
lucifer = 120
luciferattack = 40

#Healing Items#
protein_bar = 10
steak_sandwhich = 20
meatloaf = 30

#Armour items#
light_armour = 5
medium_armour = 10
heavy_armour = 20

#Weapon Items#
colt=30
angel_knuckles = 10
angel_blade = 20

#Character Combines

import time
print('Welcome to the Supernatural RPG - Name Pending')
print('')
print('')
#Story intro#
print('THUD THUD THUD THUD')
print('.... ')
time.sleep(2)
print(' ')
time.sleep(2)
print('Open the door Idjits!')
print(' ')
print('THUD THUD THUD....CRACK ')
print(' ')
print('......')
print('')
time.sleep(3)
print('You find yourself awoken by the crashing of someone kicking the door down!')
print(' ')
time.sleep(3)
print('Your eyes suddenly snap open! Trying to figure out what the hell is going ong - Your head starts thumping and things are still a bit hazy')
print('')
time.sleep(3)
print('...')
print('')
time.sleep(3)
print('Strange Man: Hey - Are you okay? You look like you are in pretty bad shape!')
print(' ')
time.sleep(3)
print('You look down at your hands...deep cuts and dried bloody knuckles - Seems like you were in some sort of fight!')
time.sleep(3)
print('The strange man reaches out to you and pulls you up to your feet')
print('')
print('looking around at the trashed 10$ a night old motel room in Kanzas youve been staying at for the last 2 weeks')
time.sleep(3)
print('broken furniture, bullet holes in the wall...everything tipped and trashed...things slowly start to come back')
print(' ')
time.sleep(3)
print('You: Hmm....yeah....ahh, I think so....')


charname=input(str("Strange Man: What is your name? ")) #select your character
print(('Strange Man:....') + charname)
print('... ')
print('')
time.sleep(2)
print('Strange Man:....What a weird name for a HUNTER!😒')
time.sleep(3)
print('')
print('Strange Man: My name is Bobby, i''m a hunter...like you. We kill everything from bad angels to witches ')
print('')
print('')
time.sleep(3)
print('Bobby: Looks like you got a beat down from a couple of Deamons that you really cheesed off!')
print('')
time.sleep(3)
print('So ' + charname + ' I am assuming you''re chasing these deamons to get closer to Lucifer?...  ' )
print('')
print('1) Who is Lucifer?')
print('')
print('2) Yes - Looking for the Prince of Hell himself! ')
print('')
qlucifer = int(input('Enter # here: '))
if qlucifer == 1:
    time.sleep(2)
    print('Bobby: Many Christians believe the Devil was once a beautiful angel named Lucifer who defied God and fell from grace.') 
    print('This assumption that he is a fallen angel banished by god - who then became the leader and Prince of Hell..' )
    time.sleep(3)
    print('')
    print('Either way, hes as bad as they come - a real piece of nasty work')
    print
    print('You are going to have to find out where he is -  and get through a few of his goons along the way!')
    print('')
else:
    time.sleep(3)
    print('Cool - So you know who he is - We are going to have to find out where he is -  and get through a few of his goons along the way!')
time.sleep(2)    
print(' ')
print('Bobby: Maybe you should get your self a shower - i''ll go and get some pancakes and bacon for your hangover and we can head to our bunker to resupply and explain how we can take out these damn Deamons and Lucifer!')
print(' ')
print('You shower up - feeling a little bit more awake and jump into your vintage Gran Torino and start driving to pick up some pancakes')
time.sleep(5)
print('_________________________________________________________________________________________')
print(' ') 
time.sleep(2)
print('You approach your safe house - The Men of Letters Bunker')
print('')
print('Hiden beneath an old metals factory and built in the 1600s, this bunker is warded against all deamons and witches and monsters, a safe haven for hunters to rest and recover')
time.sleep(1)
print('It used to be used by the nerds of the monster world - full of lore and spell books to help human hunters in the war against monsters')
time.sleep(1)
print('Bobby:Not so many of us here lately - we have been losing the war against monsters...')
time.sleep(1)
print('Bobby:Lucifers been powering his deamons up - getting ready for something - we need to find him stop him... ')
time.sleep(2)
print('')
print('Bobby unpacks the pankackes on the large mahogany desk covered in old papers and readings from books about hell and lucifer..')
print('The delightful smelling pancakes with a side of bacon - you feel right at home again...')
print('')
print('...but the memories of your parents cooking you sunday breakfast quickly get clouded by the day it all went down..the reason you''re a hunter.')
time.sleep(2)
print('')
print('...the day Lucifer killed your parents')
print('')
time.sleep(3)
print('______________________________________________________________________________________')
print('')
print('Bobby: So - Thinking about a plan to find Lucifer - We need to find out where he is...')
time.sleep(2)
print('')
print('Bobby: Probably worth trapping and finding out some information from a lower level deamon on where Lucifers base is..')
time.sleep(2)
print('')
print('Bobby: There is a truck stop about 3 hours drive from here where some other hunters had spotted a few deamons...probably our best place to start!')#
print('')
time.sleep(2)
print('Bobby: Before we head out - we have to get you some weapons..')
print('')
time.sleep(1)
print('Bobby: Listen carefully ' + charname + ' there are a few weapon packs for you to pick from....')
print('')
print('Each one will impact your attack/HP and healing ability - so pick what you think will give you the best chance of winning and surviving this battle to the end!...')
time.sleep(1)
print('')
print('Bobby: Lets see what youre working with at the moment:')
print('')
time.sleep(1)
print('Your current stats: ')
print('')
print('Attack: ' + str(charattack))
print('Starting HP: ' + str(charhp))
print('Healing Capability: ' + str(charhealing))
print('')
time.sleep(1)
print('Packs Available: ')
print('Attack Pack (1): The Colt, Light armour, Protein bar (Attack + 30/HP + 5/Healing + 10)')
print('')
print('Defence Pack (2): Angel Knuckle Dusters, Heavy Armour, Healing Meatloaf (Attack + 10/HP + 20/Healing + 30)')
print('')
print('All rounder Pack (3): Angel Blade, Medium Armour, Steak Sandwhich (Attack + 20/HP + 10/Healing + 20)')
print('')
time.sleep(2)
pack = int(input('Bobby: So which pack will it be kid?...'))

if pack ==1:
    newcharattack = int(charattack) + int(colt)
    newcharhp = int(charhp) + int(light_armour)
    newhealing = int(protein_bar)
    print('Your new stats: ')
    print('HP:' + str(newcharhp))
    print('Attack:' + str(newcharattack))
    print('Healing:' + str(newhealing))

elif pack ==2:
    newcharattack = int(charattack) + int(angel_knuckles)
    newcharhp = int(charhp) + int(heavy_armour)
    newhealing = int(meatloaf)
    print('Your new stats: ')
    print('HP:' + str(newcharhp))
    print('Attack:' + str(newcharattack))
    print('Healing:' + str(newhealing))

else: 
    newcharattack = int(charattack) + (angel_blade)
    newcharhp = int(charhp) + (medium_armour)
    newhealing = int(steak_sandwhich)
    print('Your new stats: ')
    print('HP:' + str(newcharhp))
    print('Attack:' + str(newcharattack))
    print('Healing:' + str(newhealing))

print('Bobby: Awesome - Think this should do you just fine!')
#####Update the text below to describe the game rules questions/attack/heal
print('Bobby: Now...before you go - i''m sure you already know this - but let me tell you how a deamon battle works!')
print('   ')
time.sleep(2)
print('Bobby: Once you enter a deamon battle - you will each get a turn to make a move...')
time.sleep(2)
print('   ')
print('Bobby: Within your turn you will be able to choose a two options; ')
print('   ')
time.sleep(2)
print('1) Attack: This attack strength will be based off the pack you have chosen and your new attack stat..You wont make each attack fully but youll definitely hit him')
time.sleep(2)
print('BUT before you get to ATTACK - youll have to answer a question to the supernatural GODs..Get it right - youll be allowed to attack')
print('   ')
time.sleep(2)
print('2) Heal - You wont get too much time to heal - wont be a full heal but itll give you some HP back to stay in the fight....')
print('   ')
time.sleep(2)
print('Bobby: The deamon you are facing wont just sit there and take the hits - They will also Attack and heal')
print('')
print('Bobby:....before I forget - this may be of use. I found this angel charm - It will help make sure the deamon you are fighting isnt able to get a 100% strike on you..throw it before your opponent attacks and it SHOULD cut his power down...apprently...' )
print('   ')
time.sleep(2)
print('You put the angel charm around your neck - it gives off a radient warming glow 🌟...  ')
print('   ')
time.sleep(1)
print('Bobby: Well we better be on our way - Long drive ahead!...')
print('   ')
print('You and Bobby jump into your 1964 Gran Tarino 🚗 with your supplies and set away...with the radio belting Livin on a Prayer...🤘   ')
print('   ')
time.sleep(2)
print('______________________________________________________________________________________________________________ ')
print('   ')
print('...   ')
time.sleep(1)
print('....')
time.sleep(1)
print('As the moonlight casted eerie shadows on the deserted truck station, a sulfurous stench wafted through the cars air vents.. Your Gran Tarino slowly approaches a crawl...the humming of the V8 engine abruptly stops as you turn the car off...')
print('')
print('As you sit there silently scoping the area to sense any sign of life...the only thing you can hear is your heart thumping against your chest... ')
print('')
time.sleep(2)
print('Nothing... ')
print('Suddenly the radio crackles to life.....')
time.sleep(2)
print('***Static*****')
print(charname + ' ....')
print('')
time.sleep(2)
print(' faint whispering of your name echoes through the vitage car radio......')
print(charname + 'Weve been expecting you...')
time.sleep(2)
print('')
print('You look at Bobby...Bobby looks at you expressionless...')
print('Bobby: Well seems like these sons of bitches they know who you are...')
time.sleep(2)
print('')
print('Something suddenly catches your eye in the torinos wing mirror...')
print('')
time.sleep(2)
print('a blinking red light coming from the diner connected to the truck stop...')
print('You nudge Bobby to get him to notice the continued red flashing from the diner..')
print('')
time.sleep(2)
print('Bobby: I think thats our invitation in kid..grab your stuff, lets go say hi to whatevers in there...')
print(' ')
print('You open the Torinos trunk - sling your Weapons pack on your shoulder and draw your weapon...ready for whatever is in there...')
print('Bobby: Before we head in, do you need me to remind you of what the rules of a battle are?')
time.sleep(2)
print('1) Yes - quiuck reminder please!...')
print('2) Nope- I get it - Lets go kick some ass.. ')
rules_answer = int(input('What will it be ' + charname + '?  Do you need me to remind you of what the rules of a battle are?  ' ))

if int(rules_answer) == 1:
    print('Bobby: Once you enter a deamon battle - you will each get a turn to make a move...')
    print('   ')
    print('Bobby: Within your turn you will be able to choose a two options; ')
    print('   ')
    print('1) Attack: This attack strength will be based off the pack you have chosen and your new attack stat..You wont make each attack fully but youll definitely hit him')
    print('BUT before you get to ATTACK - youll have to answer a question to the supernatural GODs..Get it right - youll be allowed to attack')
    print('   ')
    print('2) Heal - You wont get too much time to heal - wont be a full heal but itll give you some HP back to stay in the fight....')
    print('   ')
    print('Bobby: The deamon you are facing wont just sit there and take the hits - They will also Attack and heal')
    
else:
    time.sleep(3)
    print('Good stuff Kid - Lets go get this son of a bitch...')
    time.sleep(2)
print('_____________________________________________________________________________________')
print('')
time.sleep(2)
print('You and Bobby walk towards the Diner - the red glowing get brighter, the air starts to smell more and metallic.... ')
print('')
time.sleep(2)
print('Bobby: I smell a deamon about - Keep your eyes open kid...')
print('')
time.sleep(2)
print('You come closer to the door for the diner and reach out to pull the handle, when you notice blood dripping off it...')
print('')
time.sleep(2)
print('A quick glance to Bobby you start to sense a some worry coming through on his tired and experienced face...')
print('')
time.sleep(2)
print('prinnggg....')
print('')
time.sleep(2)
print('The bell above the diner door echoes a ring through the truck stop as you swing the door open...')
print('...')
time.sleep(2)
print('Bobby: So much for stealth kid...')
print('...')
time.sleep(2)
print('As you walk into the mostly destroyed food establishment with tables and chairs tipped and broken...you get a growing feeling of sorrow and emptyness in the air...')
print('')
print('Suddenly you see a black figure emerging at the counter...but what strikes you first is the figures red pulsating eyes...')
print('')
print('The figure emerges from the shadow - its the diners chef, hes been possessed. Blood splattered over his apron, wiping his hand with a rough dish cloth..probably having finished butchering an innocent human..')
print('')
time.sleep(3)
print('Bobby: Stop hiding you asshat!')
print('')
time.sleep(2)
print('Bobby:(holding his gun steady at the dark figure, eyes narrowing)...Alright, deamon.')
print('')
time.sleep(2)
print('Bobby: I think you know why we are here....Where is your scum boss Lufifer?..Where is he?')
print('')
time.sleep(2)
print('Demon: *smirking, its eyes glowing red*...Hunter, you think you can just demand answers from me? How amusing...Do you know who I am?..Im Agaliarept..General of hell...Lucifers right hand.')
print('')
time.sleep(1)
print('')
print('Bobby: *clicking his safety off on his gun*.. "Dont really care who you are...your just another piece of crap demon. Now talk, where is he?')
time.sleep(1)
print('Agaliarept: *laughing, a guttural sound*...Do you really believe threats will work on me? Lucifers location isnt for the likes of you to know')
print('')
time.sleep(1)
print('Bobby: *cocking the gun, voice cold*..I’m not here to play games. Tell me, or Ill send you back to hell the hard way.')
print('')
time.sleep(1)
print('Agaliarept eyes glow brighter and suddenly....suddenly Bobby starts to choke...his body starts levitating off the ground...')
print('')
time.sleep(1)
print('Bobby: unhand me you scum!...')
print('...CRASH!!!')
print('')
time.sleep(1)
print('Bobbys body is flung through the diner window by Agaliarept..his body writing around from the pain..Bobby falls unconcious')
print('...')
time.sleep(1)
print('Agaliarept: Now kid - Its just you and me...Lucifers going to LOVE me for bringing you in for dinner...just like your parents..')
print('')
time.sleep(1)
print('A sense of rage overcomes your mind - your blood boiling with anger...')
print('Agaliarept: Ready to fight?....')
print('')
time.sleep(1)
print('__________________________________________________________________________')

##Battle code###
import random

#define player name and npc name
player_name = charname 
npc_name = "Agaliarept" #replace with deamon name for next round

#Set HP for player and NPC
player_hp = newcharhp #set hp as characters new healing
npc_hp = 100 #set npc hp as 100

#Add attack and healing strength variables
attack = newcharattack
healing = newhealing

# Random questions and answers for the player to answer

#define questions  - Update questions to reflect the game theme

questions = {                                           
    "What is the capital of France?": "Paris",
    "What is 5 + 7?": "12",
    "What is the color of the sky on a clear day?": "Blue",
    "What is the opposite of 'up'?": "Down"
    "What "
}
#define ask question

def ask_question():                                     
    question, answer = random.choice(list(questions.items()))
    user_answer = input(f"Answer the question to attack: {question} ")
    return user_answer.strip().lower() == answer.lower()

#define players attack - if they ask question correctly --->attack is random percentage of charracters attack ability
#return damage inflicted if correct
#return 0 attack if answer is wrong

def player_attack():                            
    if ask_question(): 
        attack = random.uniform(0.1, 1.0)
        damage = int(attack * newcharattack)
        print(f"Correct answer! {player_name} attacks {npc_name} for {damage} damage.")
        return damage
    else:
        print("Wrong answer! No attack this turn.")
        return 0

#define the npc attack ---> random perfectage * 30 (30 is first npc attack multiplyer - this will go up for subsequent battles)

def npc_attack():
    attack_percentage = random.uniform(0.1, 1.0)
    damage = int(attack_percentage * 30)
    print(f"{npc_name} attacks for {damage} damage.")
    return damage

#define player heal - healing capability is based on characters newhealing stats * a multiplyer percentage - Based of which pack they picked)

def player_heal():
    heal_percentage = random.uniform(0.1, 1.0)
    heal_amount = int(newhealing)
    print(f"{player_name} heals for {heal_amount} HP.")
    return heal_amount

#define npc heal - heal amount is random heal percentage * 20 (20 is the first npc heal multiplyer - will go up for subsequent battles)

def npc_heal():
    heal_percentage = random.uniform(0.1, 1.0)
    heal_amount = int(heal_percentage * 20)
    print(f"{npc_name} heals for {heal_amount} HP.")
    return heal_amount

# Battle loop - Battle needs to continue until either player or npc has HP <=0 - So while they have >0 - battle continues. Each go should update and display current HP.

while player_hp > 0 and npc_hp > 0:
    print(f"\n{player_name} HP: {player_hp}")
    print('')
    print(f"{npc_name} HP: {npc_hp}\n")
    
    move = input("Do you want to 'attack' or 'heal'? ").strip().lower() #define move choice - input will be non case sensistive

#define actions if 'attack' or 'heal' has been chosen 
#define variable damage to = player attack (defined above) and take it away from NPC HP
#define variable heal_amount = player heal (defined above) and add it to charhp variable (if hp goes over 120 it should = 120) 
  
    if move == 'attack':
        damage = player_attack()
        npc_hp -= damage
    elif move == 'heal':
        heal_amount = player_heal()
        player_hp += heal_amount
        if player_hp > newcharhp:
            player_hp = newcharhp
    else:
        print("Invalid move. Try again.")

#npc move: if npc health is still above 0 then continue to ramdomly pick to either heal or attack
#define damage as npc attack (defined above)
#define heal amount as npc heal (defined above) - if heal amount takes HP above 100 this should = 100

    if npc_hp > 0:
        npc_move = random.choice(['attack', 'heal'])
        if npc_move == 'attack':
            damage = npc_attack()
            player_hp -= damage
        elif npc_move == 'heal':
            heal_amount = npc_heal()
            npc_hp += heal_amount
            if npc_hp > 100:
                npc_hp = 100

#define what happens when either player or npc goes below 0 HP 
#return - you have won/you have been defeated - try again. 

    if player_hp <= 0:
        print(f"{npc_name} wins! {player_name} has been defeated.")
        print('{npc_name} stands over your body - your body beaten to a pulp...your energy draining...you pass you..')
        time.sleep(1)
        print('')
        print('GAME OVER')
        break
    elif npc_hp <= 0:
        print(f"{player_name} wins! {npc_name} has been defeated.")
        #sleep.time(1)
        print('')
        print(f"{player_name} stands over {npc_name} body - his body beaten to a pulp....")
        #sleep.time(1)
        print('')
        print(f"{npc_name}: *painfully coughing*...Okay okay okay....dont kill me - Ill tell you what I know...")
        #sleep.time(1)
        print('')
        print(f'{npc_name}: I dont know where the big man Lucifer is - But I know someone who does...')
        #sleep.time(1)
        print('')
        print(f'{npc_name}: Satanachia...he will know - He was the commander in cheif of hells army, been by the side of Lucifer since the start of his fall from heaven')
        #sleep.time(1)
        print('')
        print(f'{npc_name}: Last I heard, he was stirring up trouble near the old church ruins a few hundred miles north from here,')
        #sleep.time(1)
        print('')
        print(f'{npc_name}: Now let me go!')
        #sleep.time(1)
        print('')
        print(f'BOOM....a bullet wizzes past your head and into the head of {npc_name}')
        #sleep.time(1)
        print('')
        print(f'You turn around and see Bobby holding a smoking gun...')
        print('')
        #sleep.time(1)
        print(f'Bobby: No way in hell am I going to let him live...')
        break

####add text and story around where the next deamon is in the chain. 

print('...')
#time.sleep(1)
print('...Bobby dusts himself of and holsters his gun.')
print('')
#sleep.time(1)
print('Bobby: So looks like we know where we need to go.')
print('')
print('Bobby: Lets get you healed up and lets get on the road..')
#sleep.time(1)
print('Bobby heals you back to full hp as you get back to the torino')
print('')
print('Your stats: ')
print(' ')
print('HP:' + str(newcharhp))
print('Attack:' + str(newcharattack))
print('Healing:' + str(newhealing))