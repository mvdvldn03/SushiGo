#Formation of Deck
deck = ['Salmon Nigiri', 'Salmon Nigiri', 'Salmon Nigiri', 'Salmon Nigiri', 'Salmon Nigiri', 'Salmon Nigiri', 'Salmon Nigiri', 'Salmon Nigiri', 'Salmon Nigiri', 'Salmon Nigiri', 'Egg Nigiri', 'Egg Nigiri', 'Egg Nigiri', 'Egg Nigiri', 'Egg Nigiri', 'Squid Nigiri', 'Squid Nigiri', 'Squid Nigiri', 'Squid Nigiri', 'Squid Nigiri', 'Wasabi', 'Wasabi', 'Wasabi', 'Wasabi', 'Wasabi', 'Wasabi', '3 Maki Rolls', '3 Maki Rolls', '3 Maki Rolls', '3 Maki Rolls', '3 Maki Rolls', '3 Maki Rolls', '3 Maki Rolls', '3 Maki Rolls', '2 Maki Rolls', '2 Maki Rolls', '2 Maki Rolls', '2 Maki Rolls', '2 Maki Rolls', '2 Maki Rolls', '2 Maki Rolls', '2 Maki Rolls', '2 Maki Rolls', '2 Maki Rolls', '2 Maki Rolls', '2 Maki Rolls', '1 Maki Roll', '1 Maki Roll', '1 Maki Roll', '1 Maki Roll', '1 Maki Roll', '1 Maki Roll', 'Tempura', 'Tempura', 'Tempura', 'Tempura', 'Tempura', 'Tempura', 'Tempura', 'Tempura', 'Tempura', 'Tempura', 'Tempura', 'Tempura', 'Tempura', 'Tempura', 'Sashimi', 'Sashimi', 'Sashimi', 'Sashimi', 'Sashimi', 'Sashimi', 'Sashimi', 'Sashimi', 'Sashimi', 'Sashimi', 'Sashimi', 'Sashimi', 'Sashimi', 'Sashimi', 'Dumpling', 'Dumpling', 'Dumpling', 'Dumpling', 'Dumpling', 'Dumpling', 'Dumpling', 'Dumpling', 'Dumpling', 'Dumpling', 'Dumpling', 'Dumpling', 'Dumpling', 'Dumpling', 'Pudding', 'Pudding', 'Pudding', 'Pudding', 'Pudding', 'Pudding', 'Pudding', 'Pudding', 'Pudding', 'Pudding', 'Chopsticks', 'Chopsticks', 'Chopsticks', 'Chopsticks']

#Round Simulation
def plays(hand1, hand2, picked1, picked2):
  """Overall Round Function"""
  nigiri = ["Squid Nigiri", "Salmon Nigiri", "Egg Nigiri"]
  for round_number in range(1,11):
    while(True):
      print(hand1)
      player_choice = input("Select Card (Round " + str(round_number) + "):")
      if "Chopsticks" in picked1 and player_choice == "Use Chopsticks":
        hand1.append("Chopsticks")
        picked1.remove("Chopsticks")
        while(True):
          player_choice1 = input("Select Card 1 (Round " + str(round_number) + "):")
          if player_choice1 != 'Chopsticks' and player_choice1 in hand1:
            break
        while(True):
          player_choice2 = input("Select Card 2 (Round " + str(round_number) + "):")
          if player_choice2 != 'Chopsticks' and player_choice2 in hand1:
            break
        if player_choice1 in hand1 and player_choice2 in hand1:
          picked1.append(player_choice1)
          picked1.append(player_choice2)
          hand1.remove(player_choice1)
          hand1.remove(player_choice2)
          if player_choice1 in nigiri:
            if "Wasabi" in picked1:
              picked1[picked1.index("Wasabi")] = "Wasabi and " + player_choice1
              picked1.remove(player_choice1)
          if player_choice2 in nigiri:
            if "Wasabi" in picked1:
              picked1[picked1.index("Wasabi")] = "Wasabi and " + player_choice2
              picked1.remove(player_choice2)
        else:
          print("Error")
        break
      else:
        if player_choice in hand1:
          picked1.append(player_choice)
          if player_choice in nigiri:
            if "Wasabi" in picked1:
              picked1[picked1.index("Wasabi")] = "Wasabi and " + player_choice
              picked1.remove(player_choice)
          hand1.remove(player_choice)
          break
        else:
          print("Error")
    maki1_count = (picked1.count("1 Maki Roll")) + (2 * picked1.count("2 Maki Rolls")) + (3 * picked1.count("3 Maki Rolls"))
    maki2_count = (picked2.count("1 Maki Roll")) + (2 * picked2.count("2 Maki Rolls")) + (3 * picked2.count("3 Maki Rolls"))
    if "Wasabi" in picked2 and "Squid Nigiri" in hand2:
      computer_choice = "Squid Nigiri"
    elif (picked2.count("Sashimi") // 3) == 2 and "Sashimi" in hand2:
      computer_choice = "Sashimi"
    elif "Wasabi" in hand2: 
      computer_choice = "Wasabi"
    elif "Wasabi" in picked2 and "Salmon Nigiri" in hand2:
      computer_choice = "Salmon Nigiri"
    elif "Squid Nigiri" in hand2:
      computer_choice = "Squid Nigiri"
    elif (picked2.count("Tempura") // 2) == 1 and "Tempura" in hand2:
      computer_choice = "Tempura"
    elif picked2.count("Dumpling") == 4 in picked2 and "Dumpling" in hand2:
      computer_choice = "Dumpling"
    elif picked2.count("Dumpling") == 3 in picked2 and "Dumpling" in hand2:
      computer_choice = "Dumpling"
    elif "Tempura" in hand2:
      computer_choice = "Tempura"
    elif "Sashimi" in hand2:
      computer_choice = "Sashimi"
    elif picked2.count("Dumpling") == 2 in picked2 and "Dumpling" in hand2:
      computer_choice = "Dumpling"
    elif "Salmon Nigiri" in hand2:
      computer_choice = "Salmon Nigiri"
    elif (maki1_count - maki2_count) <= 2 and "3 Maki Rolls" in hand2:
      computer_choice = "3 Maki Rolls"
    elif "Dumpling" in hand2:
      computer_choice = "Dumpling"
    elif (maki1_count - maki2_count) <= 1 and "2 Maki Rolls" in hand2:
      computer_choice = "2 Maki Rolls"
    elif "3 Maki Rolls" in hand2:
      computer_choice = "3 Maki Rolls"
    elif "2 Maki Rolls" in hand2:
      computer_choice = "2 Maki Rolls"
    elif "Egg Nigiri" in hand2:
      computer_choice = "Egg Nigiri"
    elif "Pudding" in hand2:
      computer_choice = "Pudding"
    elif (maki1_count - maki2_count) == 0 and "1 Maki Roll" in hand2:
      computer_choice = "1 Maki Roll"
    elif "1 Maki Roll" in hand2:
      computer_choice = "1 Maki Roll"
    elif "Chopsticks" in hand2:
      computer_choice = "Chopsticks"
    picked2.append(computer_choice)
    if computer_choice in nigiri:
      if "Wasabi" in picked2:
        picked2[picked2.index("Wasabi")] = "Wasabi and " + computer_choice
        picked2.remove(computer_choice)
    print("You have picked: " + str(picked1))    
    print("The Computer has picked: " + str(picked2))
    hand2.remove(computer_choice)
    hand1, hand2 = hand2, hand1
    print("\n")

total_score1 = 0
total_score2 = 0 
pudding_count1 = 0
pudding_count2 = 0
for i in range(1,4):
  print("Now Beginning Round " + str(i) + ":")
  #Shuffling of Deck
  import random
  random.shuffle(deck)
  picked1 = []
  picked2 = []
  plays(deck[:10], deck[10:20], picked1, picked2)

  #Scoring
  makicounter1 = 0
  makicounter2 = 0
  points1 = 0
  points2 = 0
  def score_nigiri(cards, points):
    """Scores Nigiri Cards - With or Without Wasabi"""
    return points + (9 * cards.count("Wasabi and Squid Nigiri")) + (6 * cards.count("Wasabi and Salmon Nigiri")) + (3 * cards.count("Wasabi and Egg Nigiri")) + (3 * cards.count("Squid Nigiri")) + (2 * cards.count("Salmon Nigiri")) + (cards.count("Egg Nigiri"))
  points1 = score_nigiri(picked1, points1)
  points2 = score_nigiri(picked2, points2)

  def score_makiroll(cards, makicounter):
    """Scores Maki Cards - Total Added To Counter"""
    return makicounter + (cards.count("1 Maki Roll")) + (2 * cards.count("2 Maki Rolls")) + (3 * cards.count("3 Maki Rolls"))
  makicounter1 = score_makiroll(picked1, makicounter1)
  makicounter2 = score_makiroll(picked2, makicounter2)
  if makicounter1 > makicounter2:
    points1 += 6
    if makicounter2 > 0:
      points2 += 3
  if makicounter2 > makicounter1:
    points2 += 6
    if makicounter1 > 0:
      points1 += 3
  if makicounter1 == makicounter2:
    points1 += 3
    points2 += 3

  def score_tempura(cards, points):
    """Scores Tempura Cards"""
    a = (5 * (cards.count("Tempura") //  2))
    return points + a
  points1 = score_tempura(picked1, points1)
  points2 = score_tempura(picked2, points2)

  def score_sashimi(cards, points):
    """Scores Sashimi Cards"""
    a = (10 * (cards.count("Sashimi") //  3))
    return points + a
  points1 = score_sashimi(picked1, points1)
  points2 = score_sashimi(picked2, points2)

  def score_dumpling(cards, points):
    count = cards.count("Dumpling")
    if count == 0:
      return points + 0
    if count == 1:
      return points + 1
    if count == 2:
      return points + 3
    if count == 3:
      return points + 6
    if count == 4:
      return points + 10
    if count >= 5:
      return points + 15
  points1 = score_dumpling(picked1, points1)
  points2 = score_dumpling(picked2, points2)

  pudding_count1 += picked1.count("Pudding")
  pudding_count2 += picked2.count("Pudding")

  total_score1 += points1
  total_score2 += points2

  #Round Summary
  print ( "For this round, you selected: {} \nYou scored {} points and got {} Pudding/s.\n\n The incredibly skilled computer picked: {}\nThey scored {} points and got {} Pudding/s.\n".format(picked1, points1, pudding_count1, picked2, points2, pudding_count2))

if pudding_count1 > pudding_count2:
  total_score1 += 6
if pudding_count2 > pudding_count1:
  total_score2 += 6
if pudding_count1 == pudding_count2:
  total_score1 += 3
  total_score2 += 3

if total_score1 > total_score2:
  print("\n Congratulations! You have beaten the incredibly skilled computer with a score of " + str(total_score1) + " points to " + str(total_score2) + " points.")
if total_score2 > total_score1:
  print("\n Unfortunately, the incredibly skilled computer has beaten you with a score of " + str(total_score2) + " points to your " + str(total_score1) + " points.")
