#CV irfan portofolio Scramble game

import time
import random

class Core:
    def __init__(self,question) :
        self.question = question

    def gameplay(self):
        key = random.choice(list(self.question.keys())) #choose 1 random key from dictionary
        val = self.question.pop(key) # remove choosen word from dictionary and return value its value and store it in val (hint)
        mix_word = "".join(random.sample(key,len(key))) # shuffle the letters of the chosen key
        print(f"{mix_word} | hint : {val}")
        answer = input('').lower()
        is_correct = key == answer # check is answer matches the original key if same return true if not return false
        print(f'correct \n'if is_correct else 'wrong \n')
        return is_correct
    
# game data    
fruit = {'banana': 'Monkey Favorite', 'carrot':'Rabbit Favorite','pineapple':'Very Good Toping On Pizza'}
country = {'japan': 'Samurai', 'china':'Panda','italy':'Pizza'}
animal = {'cat': 'Tom', 'mouse':'Jerry', 'squirrel':'Love Nut'} 
topic = [fruit,country,animal]

count_correct = 0
count_wrong = 0
while True :
    if count_correct < 3 and count_wrong < 3 :
        try :
            print("""choose topic
            1.fruit
            2.country
            3.animal""")
            topic_choice = int(input('choose topic :'))
            if topic_choice < 1 or topic_choice > len(topic) :
                print('topic not available\n')
                continue
            
        except ValueError :
            print('topic not available\n')
            continue

        selected_topic = (topic[topic_choice -1])

        if len(selected_topic) == 0:
            print("No word left, choose other topic")
            continue
        play = Core(selected_topic)
        
        result = play.gameplay()

        if result :
            count_correct += 1
        else :
            count_wrong += 1

    else :
        print(f"=====Game Over===== \n correct answer : {count_correct} | wrong answer {count_wrong}")
        break