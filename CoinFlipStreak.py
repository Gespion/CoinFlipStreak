from random import randint

def FlipHeadsTails():
    
    flip_list = []

    for i in range(100):
        if randint(0,1) == 0:
            flip_list.append('H') # 0 -> Head 
        else:
            flip_list.append('T') # 1 -> Tail

    return flip_list

def CheckStreak(flip_list_to_check):
    #print(flip_list_to_check)
    h_streak = 0
    t_streak = 0
    h_count = 0
    t_count = 0

    for i in range(len(flip_list_to_check)):
        if i+1 < len(flip_list_to_check):
            if flip_list_to_check[i] == flip_list_to_check[i+1]:
                if flip_list_to_check[i] == 'H':
                    h_count += 1
                    if h_count == 5:
                        h_streak += 1
                else: #flip_list_to_check[i] == 'T':
                    t_count += 1
                    if t_count == 5:
                        t_streak += 1
            else:
                t_count = 0
                h_count = 0
    
    #print("H-Streak: %d" % h_streak)
    #print("T-Streak: %d" % t_streak)
    return h_streak + t_streak


total_streak = 0
total_flip = 0

while total_flip < 10000:
    if int(CheckStreak(FlipHeadsTails())) > 0:
        total_streak += 1
    total_flip += 1

if total_streak > 0:
    result = (total_streak/total_flip)*100
    print("Total Streak %d - Total flip %d - Result is: %f %% Streaks" % (total_streak, total_flip, result))
else:
    print("Result is 0 %% Streak")