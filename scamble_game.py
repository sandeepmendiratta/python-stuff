letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
#adding lower letter
letters += [letter.lower() for letter in letters]
#adding poins for lower
points *= 2
#new_dict = {k: v for k, v in zip(keys, values)}
letter_to_points = {k: v for k, v in zip(letters,points)}

letter_to_points[" "] = 0

#print(letter_to_points)

def score_word(word):
    print_total = 0
    for letter in word:
        print_total += letter_to_points.get(letter, 0)
    return print_total

brownie_points = (score_word("BROWNIE"))
print(brownie_points)
player_to_words = {"player1": ["BLUEWTTTTTTT", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINEM"]}

player_to_points ={}
def update_point_totals():
    for players, words in player_to_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
            #print(player_points)
        player_to_points[players] =  player_points
    print(player_to_points)
update_point_totals()

def play_word(player, word):
    player_to_words[player].append(word)

play_word("player1", "MY")
print(player_to_words)












