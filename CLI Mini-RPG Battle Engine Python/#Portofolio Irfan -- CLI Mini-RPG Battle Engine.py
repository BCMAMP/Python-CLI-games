# CLI Mini-RPG Battle Engine Portofolio Irfan | Python
# • Merancang arsitektur berorientasi objek (OOP) menerapkan konsep Inheritance dan Encapsulation untuk manajemen status karakter dan efek giliran (Turn-Based System).
# • Mengimplementasikan algoritma logika kondisioner kompleks untuk kalkulasi damage, efek status (DoT/Stun), serta sistem manajemen Buff/Debuff bertempo.
# • Menerapkan Exception Handling (Try-Except) dan validasi input untuk memastikan 

import random
import time
import copy

class Character:
    def __init__(self,name,hp,mana,attack,defensive,):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.mana = mana
        self.max_mana = mana
        self.attack = attack
        self.base_attack = attack
        self.defensive = defensive
        self.status = 'Normal'
        self.buff_attack = 0
        self.buff_duration = 0
        self.debuff_duration = 0

    def deal_damage(self,target):
        random_damage = random.randint(0,self.attack)
        total_damage = max(0,random_damage - target.defensive)
        target.hp = max(0,target.hp - total_damage)
        if total_damage == 0 :
            print(f'{self.name} Attack Miss ❗')
            time.sleep(2)
        elif random_damage < self.attack:
            print(f'{self.name} Deal {total_damage} Damage')
            time.sleep(2)
        else :
            print(f'{self.name} Deal Critical {total_damage} 💥')
            time.sleep(2)


    def update_status (self):
        if self.status in ['Burned','Electrocuted','Poisoned'] and self.hp > 0:
            if self.debuff_duration > 0 :
                self.hp -= 10
                print(f'{self.name} is {self.status}, Take 10 Damage\n')
                time.sleep(2)
                self.debuff_duration -= 1
                if self.debuff_duration == 0 :
                    self.status = 'Normal'
                    print(f'Debuff Ended')

        if self.status in ['Stunned','Frozen']:
            print(f'{self.name} is {self.status}')
            self.status = 'Normal'
            time.sleep(2)
            return False

        return True

class Hero(Character) :
    def __init__(self,name,hp,mana,attack,defensive,potions=3):
        super().__init__(name,hp,mana,attack,defensive)
        self.potions = potions

    def heal(self):
        if self.potions > 0 :
            self.potions -= 1
            self.hp = min(self.hp + 20 , self.max_hp)
            print(f'Heal 20, HP : {self.hp}/{self.max_hp}  Remaining Potions {self.potions}\n')
            time.sleep(2)
            return True
        else :
            print('No Potions Left')
            time.sleep(2)
            return False

#====================== Hero Class =============
class Knight(Hero):
    def __init__(self,name,hp,mana,attack,defensive):
        super().__init__(name,hp,mana,attack,defensive)
    def skill(self,target) :
        print(f"""-----:Skill List:-----
1. Shield bash 🛡 | Cost : 20 mana , Stun for 1 turn , Deal {self.attack *0.5} Damage
2. Charge 💢 | Cost : 25 mana , Deal {self.attack*1.5} Damage
3. Sacred Strike ⚔ | Cost : 35 mana , Deal {self.attack*2.5} Damage
4. Return ↩\n""")
        try :
            choice = int(input('Skill Chose: '))
            if choice == 1 and self.mana >= 20 :
                self.mana -= 20
                total_damage = self.attack * 0.5
                target.hp = max(0,target.hp - total_damage)
                target.status = 'Stunned'
                print(f'Shield Bash Deal {total_damage} Damage , The Enemy Is Stunned')
                time.sleep(2)
                return True
            elif choice == 2 and self.mana >= 25 :
                self.mana -= 25
                total_damage = self.attack * 1.5
                target.hp = max(0,target.hp - total_damage)
                print(f'Charge Deal {total_damage} Damage')
                time.sleep(2)
                return True
            elif choice == 3 and self.mana >= 35:
                self.mana -= 35
                total_damage = self.attack * 2.5
                target.hp = max(0,target.hp - total_damage)
                print(f'Sacred Strike Deal {total_damage} Damage')
                time.sleep(2)
                return True
            elif choice == 4 :
                return False
            else :
                print("Skill Can't Be Used\n")
        except ValueError :
            print('Error: Skill Not Available')

class Mage(Hero):
    def __init__(self,name,hp,mana,attack,defensive):
        super().__init__(name,hp,mana,attack,defensive)
    def skill(self,target) :
        print(f"""-----:Skill List:-----
    {'1. Fire Ball 🔥 | Cost : 50 mana , Burn Target for 1 turn , Deal'} {self.attack*2.5} Damage
    {'2. Ice Spike ❄ | Cost : 50 mana , Freeze Target for 1 turn , Deal'} {self.attack*3} Damage
    {'3. Thunderbolt ⚡ | Cost : 80 mana , Electrocuted Target for 1 turn , Deal'} {self.attack*3.5} Damage
    {'4. Return ↩'}\n""")
        try :
            choice = int(input("Skill Chose :"))
            if choice == 1 and self.mana >= 50 :
                self.mana -= 50
                total_damage = self.attack * 2.5
                target.hp = max(0,target.hp - total_damage)
                target.status = 'Burned'
                target.debuff_duration = 2
                print(f'Fire Ball Deal {total_damage} Damage, The Enemy Is Burning For 2 Turn')
                return True
            elif choice == 2 and self.mana >= 50 :
                self.mana -= 50
                total_damage = self.attack * 3
                target.hp = max(0,target.hp - total_damage)
                target.status = 'Frozen'
                print(f'Ice Spike Deal {total_damage} Damage, The Enemy Is Frozen')
                return True
            elif choice == 3 and self.mana >= 80 :
                self.mana -= 80
                total_damage = self.attack * 3.5
                target.hp = max(0,target.hp - total_damage)
                target.status = 'Electrocuted'
                target.debuff_duration = 2
                print(f'Thunderbolt {total_damage} Damage, The Enemy Is Electrocuted For 2 Turn')
                return True
            elif choice == 4 :
                return False
            else :
                print("Skill Can't Be Used\n")
        except ValueError :
            print('Error: Skill Not Available')
        
class Archer(Hero):
    def __init__(self,name,hp,mana,attack,defensive):
        super().__init__(name,hp,mana,attack,defensive)
    def skill(self,target) :
        print(f"""-----:Skill List:-----
    {'1. Poison Arrow ⚠ | Cost : 20 mana , Poison Target for 1 turn , Deal '}{self.attack*1.5} Damage
    {'2. Assassinate 🤕 | Cost : 50 mana , Deal '}{self.attack*4} Damage
    {'3. Focus🎯 | Cost : 30 mana , Attack Increase 15 For 2 Turn'}
    {'4. Return ↩'}\n""")
        try :
            choice = int(input('Skill Chose: ' ))
            if choice == 1 and self.mana >= 20:
                self.mana -= 20
                total_damage = (self.attack*1.5 )- target.defensive
                target.hp = max(0,target.hp - total_damage)
                target.status = 'Poisoned'
                target.debuff_duration = 1
                print(f'Poison Arrow Deal {total_damage}, The Enemy Is Poisoned For 1 Turn')
                return True
            elif choice == 2 and self.mana >= 50 :
                self.mana -= 50
                total_damage = self.attack * 4
                target.hp = max(0,target.hp - total_damage)
                print(f"Assasinate Deal {total_damage} Damage")
                return True
            elif choice == 3 and self.mana >= 30 :
                self.mana -= 30
                self.buff_attack = 15
                self.buff_duration = 2
                self.attack = self.base_attack + self.buff_attack
                print(f'Attack Increase For 2 Turn')
                return True
            elif choice == 4 :
                return False
            else :
                print("Skill Can't Be Used\n")
        except ValueError :
            print('Error: Skill Not Available')

#==========================enemy class===========================================

class Slime(Character):
    def __init__(self,name,hp,mana,attack,defensive):
        super().__init__(name,hp,mana,attack,defensive)
    def skill(self,target) :
        if self.mana >= 10 :
            self.mana -= 10
            total_damage = (self.attack*1.5) - target.defensive
            target.hp = max(0,target.hp - total_damage)
            target.status = 'Poisoned'
            target.debuff_duration = 2
            print(f"SLime Using Poison Spit {total_damage} Damage , {target.name} Poisoned For 2 Turn")
            time.sleep(2)
            return True
        else :
            return False

class Skeleton(Character):
    def __init__(self,name,hp,mana,attack,defensive):
        super().__init__(name,hp,mana,attack,defensive)
    def skill(self,target) :
        if self.mana >= 20 :
            self.mana -= 20
            total_damage = self.attack*1.5
            target.hp = max(0,target.hp - total_damage)
            print(f"Skeleton Using Charge Deal {self.attack} Damage")
            time.sleep(2)
            return True
        else :
            return False


class Hound(Character):
    def __init__(self,name,hp,mana,attack,defensive):
        super().__init__(name,hp,mana,attack,defensive)
    def skill(self,target) :
        if self.mana >= 15 :
            self.mana -= 15
            total_damage = (self.attack*1.5) - target.defensive
            target.status = 'Burned'
            target.hp = max(0,target.hp - total_damage)
            target.debuff_duration = 2
            print(f"Hound Using Breath Fire Deal {total_damage} Damage , {target.name} Burned For 2 Turn")
            time.sleep(2)
            return True
        else :
            return False
        

class Boss(Character):
    def __init__(self,name,hp,mana,attack,defensive):
        super().__init__(name,hp,mana,attack,defensive)
    def skill(self,target) :
        if self.mana >= 10 :
            self.mana -= 10
            total_damage = self.attack - target.defensive
            target.status = 'Frozen'
            target.hp = max(0,target.hp - total_damage)
            target.debuff_duration = 1
            print(f"Boss Using Chill Touch Deal {total_damage} Damage , {target.name} Frozen for 1 Turn")
            time.sleep(2)
            return True
        else :
            return False
    
#Hero Pool - HP,Mana,Attack,defensive
A_Knight = Knight('Knight',200,50,15,20)
A_Mage = Mage('Mage',80,150,30,5)
A_Archer = Archer('Archer',100,70,25,10)
#Enemy Pool - HP,Mana,Attack,defensive
A_slime = Slime('Slime',70,40,15,5)
A_skeleton = Skeleton('Skeleton',100,20,25,10)
A_hound = Hound('Hound',120,10,20,15)
A_boss = Boss('Boss',500,100,40,20)

#list Hero
Data_Heroes = [A_Knight,A_Mage,A_Archer]
#list Enemy
Data_Enemy = [A_slime,A_skeleton,A_hound]

def display_status(hero):
    print(f"""Class : {hero.name}
HP : {hero.hp}
Mana : {hero.mana}
Attack : {hero.attack}
Defensive : {hero.defensive}""")
    
def Character_selection(Data_Heroes):
    print('====Character Selection====')
    for idx, hero in enumerate (Data_Heroes, 1) :
        print(f'{idx}.{hero.name}')
    print()  
    
    while True :
        try :
            Character = int(input('Choose number of your character : '))

            if Character < 1 or Character > len(Data_Heroes) :
                print('Character not avalible\n')
                continue
        
        except ValueError :
            print("It's not a number\n")
            continue

        return Data_Heroes[Character-1]

def gameplay(hero, Enemy):
    print(f"""{'='*40}\n{'Status':^40}\n{'='*40}
{'Class':<12}:{hero.name:<13} | {Enemy.name:<13}
{'HP':<12}:{hero.hp:<13} | {Enemy.hp:<13}
{'Mana':<12}:{hero.mana:<13} | {Enemy.mana:<13}
{'Attack':<12}:{hero.attack:<13} | {Enemy.attack:<13}
{'Defensive':<12}:{hero.defensive:<13} | {Enemy.defensive:<13}
{'Status':<12}:{hero.status:<13} | {Enemy.status:<13}""")

Hero_pick = Character_selection(Data_Heroes)  

print(f'\nYou Choose {Hero_pick.name}\n')

display_status(Hero_pick)
stage_counter = [copy.deepcopy(random.choice(Data_Enemy)) for count in range (3)] + [copy.deepcopy(A_boss)]
for wave, enemy in enumerate(stage_counter, start = 1):
    print(f"""{'='*10} Wave {wave} {'='*10}
    Encounter {enemy.name}""")
    buff = "normal"
    turn = 1
    while Hero_pick.hp > 0 and enemy.hp > 0 :
#================= Hero Turn ====================== 
        hero_move = Hero_pick.update_status()
        if Hero_pick.hp <= 0 :
            print(f'{Hero_pick.name} Defeated By {enemy.name}')
            break
        
        gameplay(Hero_pick,enemy)
        print(f"\n{'='*15} Turn {turn} {'='*15}\n")
   
        if hero_move :
            while True :
                print(f"""{'1. Attack':<13}
{'2. Skill':<13}
{'3. Heal':<13}""")
                try :
                    choice = int(input('Choice Action :'))
                    print('')
                    if choice == 1 :
                        Hero_pick.deal_damage(enemy)
                        break
                    elif choice == 2 :
                        used_skill = Hero_pick.skill(enemy)
                        if not used_skill :
                            continue
                        break
                    elif choice == 3 :
                        use_heal = Hero_pick.heal()
                        if not use_heal :
                            continue
                        break
                    else :
                        print('not available')
                except ValueError :
                    print('Error Choice again')
        else :
            print(f'{Hero_pick.name} Skip Turn')

                
# update buff status
        if Hero_pick.buff_duration > 0 :
            Hero_pick.buff_duration -= 1
            if Hero_pick.buff_duration == 0 :
                Hero_pick.attack = Hero_pick.base_attack
                Hero_pick.buff_attack = 0
                print('Buff Ended')
#======================== enemy turn ======================
        if enemy.hp > 0 :
            enemy_move = enemy.update_status()
            print(f'\n----Enemy Turn-----\n')
            if enemy_move :
                enemy_choice = random.randint(1,2)
                if enemy_choice == 2 :
                    used_skill = enemy.skill(Hero_pick)
                    if used_skill == False:
                        enemy.deal_damage(Hero_pick)
                else :
                    enemy.deal_damage(Hero_pick)
            else :
                print(f'{enemy.name} Skip Turn')
        else :
            print(f"{enemy.name} Defeated 🎉 ")
            Hero_pick.hp = min(Hero_pick.max_hp, Hero_pick.hp + 30)
            Hero_pick.mana = min(Hero_pick.max_mana, Hero_pick.mana + 20)
            print(f"{Hero_pick.name} recovered 30 HP and 20 Mana \n")
            time.sleep(2)
            break
# regeneration every turn
        if Hero_pick.hp > 0 and enemy.hp > 0:
            turn += 1
            print(f"{'='*40}")
            print(f"{'Mana Restored':^30}")
            time.sleep(2)
            Hero_pick.mana += 15
            Hero_pick.mana = min(Hero_pick.mana,Hero_pick.max_mana)
            enemy.mana += 10
            enemy.mana = min(enemy.mana,enemy.max_mana)


    if Hero_pick.hp <= 0 :
        print('---------| You Lose |--------')
        break

if Hero_pick.hp > 0 :
    print(f'{"="*10} Congratulation You Win ! {"="*10}')
    