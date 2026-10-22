levels = [1, 2, 3, 4, 5]
coins = [5, 8, 3, 10, 7]
enemies = [2, 4, 1, 5, 3]
power_ups = ["Mushroom", "Star", "Flower", "Mushroom", "Star"]

print("===== PLATFORM ADVENTURE =====")

print()
for i in range(0, len(levels)):
    print("Levels:", levels[i])
    print("Coins:", coins[i])
    print("Enemies:", enemies[i])
    print("Power-Ups:", power_ups[i])
    print()
player_name = "Hero"
lives = 3
score = 0
total_coins = 0

print("===== PLAYER INFORMATION =====")

print(f"Player: {player_name}")
print(f"Lives: {lives}")
print(f"Score: {score}")
print(f"Total Coins: {total_coins}")
print()

print("===== LEVEL SCORES =====")

level_scores = []
for i in range(0, len(levels)):
    level_score= (coins[i] * 10) - (enemies[i] * 5)
    if power_ups[i] == "Star":
        level_score += 25
    level_scores.append(level_score)
    print(f"Level {i+1} Score: {level_scores[i]}", )

actions = [0, 1, 0, 2, 1]
print()

print("===== ADVENTURE ACTIONS =====")

for i in range(0, len(actions)):
    if actions[i] == 0:
        print(f"Level {i+1}: Collect Coins")
    elif actions[i] == 1:
        print(f"Level {i+1}: Fight Enemies")
    else :
        print(f"Level {i+1}: Use Power-Ups")
print()

print("==== LIFE HISTORY =====")

life_history = []
for i in range(0, len(levels)):
    if enemies[i] >=4 and power_ups[i] != "Star":
        lives-=1
    life_history.append(lives)
    print(f"After Level {i+1}: {lives}")
print()

print("===== COIN COLLECTION =====")

total_coins = 0
for coin in coins:
    total_coins += coin

bonus_coin_levels = []
for i in range(0, len(coins)):
    if coins[i] >= 7:
        bonus_coin_levels.append(coins[i])

print(f"Coins collected: {total_coins}")
print(f"Levels with 7 or more coins: {bonus_coin_levels}")

print()

print("===== POWER-UP INVENTORY =====")

inventory = ["Mushroom", "Star", "Flower"]
used_powerups = ["Mushroom", "Star"]
remaining_inventory = list.copy(inventory)

for used_powerup in used_powerups:
    remaining_inventory.pop(remaining_inventory.index(used_powerup))

print(f"Starting Inventory: {inventory}")
print(f"Used Power-Ups: {used_powerups}")
print(f"Remaining Inventory: {remaining_inventory}")

print()

print("===== LEVEL ANALYSIS =====")
print(f"Total Coins: {total_coins}")
print(f"Most Coins in One Level: {max(coins)}")
print(f"Fewest Coins in One Level: {min(coins)}")
print(f"Average Coins in One Level: {total_coins/len(coins)}")
totalEnemies=0
for enemy in enemies:
    totalEnemies+=enemy
print(f"Total Enemies: {totalEnemies}")
print(f"Most Enemies in One Level: {max(enemies)}")

print()

print("===== HIGH SCORES =====")
high_scores = []
for score in level_scores:
    if score >= 50:
        high_scores.append(score)
print(f"Scores of 50 or Higher: {high_scores}")

print()

print("===== SCORE HISTORY =====")
score=0
score_history = []
for i in range(0, len(level_scores)):
    score += level_scores[i]
    score_history.append(score)
    print(f"After Level {i+1}: {score_history[i]}")
print()
print(f"First Two Scores: {score_history[0:2]}")
print(f"Last Two Scores: {score_history[-2:]}")

print()

print("===== FINAL STATUS =====")
if lives == 0:
    print("Game Over")
elif score >= 250:
    print("Adventure Champion")
elif score >= 150:
    print("Great Adventure")
else:
    print("Keep Practicing")
print()

print("===== ADVENTURE RANKING =====")

print(f"Final Score: {score}")
print(f"Final Lives: {lives}")
print("Rank: Legend")