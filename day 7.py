filename = "calibration_document"

with open(filename) as f:
    lines = f.readlines()


def create_hands(file):
    hands = []
    for line in file:
        hand = line.split()
        hand[1] = int(hand[1])
        hands.append(hand)
    return hands


def sort_type_part1(hands):
    six = 0
    five = 0
    four = 0
    three = 0
    two = 0
    one = 0
    zero = 0
    for hand in hands:
        check1 = hand[0].count(hand[0][0])
        check2 = hand[0].count(hand[0][1])
        check3 = hand[0].count(hand[0][2])
        check4 = hand[0].count(hand[0][3])
        check5 = hand[0].count(hand[0][4])
        checks = [check1, check2, check3, check4, check5]

        if checks.count(5) == 5:      # 5 of a kind
            hand.append(6)
            six += 1
        elif checks.count(4) == 4:    # 4 of a kind
            hand.append(5)
            five += 1
        elif checks.count(3) == 3:
            if checks.count(2) == 2:  # full house
                hand.append(4)
                four += 1
            else:                     # 3 of a kind
                hand.append(3)
                three += 1
        elif checks.count(2) == 4:    # 2 pairs
            hand.append(2)
            two += 1
        elif checks.count(2) == 2:    # 1 pair
            hand.append(1)
            one += 1
        else:                         # nothing
            hand.append(0)
            zero += 1
    for i in range(len(hands)):
        for j in range(len(hands)):
            if i < j:
                if hands[i][2] < hands[j][2]:
                    hands[i], hands[j] = hands[j], hands[i]
    five += six
    four += five
    three += four
    two += three
    one += two
    zero += one
    return card_power(hands, six, five, four, three, two, one, zero, 0, 1)


def sort_type_part2(hands):
    six = 0
    five = 0
    four = 0
    three = 0
    two = 0
    one = 0
    zero = 0
    for hand in hands:
        if "J" not in hand[0]:
            check1 = hand[0].count(hand[0][0])
            check2 = hand[0].count(hand[0][1])
            check3 = hand[0].count(hand[0][2])
            check4 = hand[0].count(hand[0][3])
            check5 = hand[0].count(hand[0][4])
            checks = [check1, check2, check3, check4, check5]

            if checks.count(5) == 5:  # 5 of a kind
                hand.append(6)
                six += 1
            elif checks.count(4) == 4:  # 4 of a kind
                hand.append(5)
                five += 1
            elif checks.count(3) == 3:
                if checks.count(2) == 2:  # full house
                    hand.append(4)
                    four += 1
                else:  # 3 of a kind
                    hand.append(3)
                    three += 1
            elif checks.count(2) == 4:  # 2 pairs
                hand.append(2)
                two += 1
            elif checks.count(2) == 2:  # 1 pair
                hand.append(1)
                one += 1
            else:  # nothing
                hand.append(0)
                zero += 1
        elif hand[0] == "JJJJJ":          # 5 of a kind all jokers case
            hand.append(6)
            six += 1
        else:
            checks = []
            for card in hand[0]:
                if card != "J":
                    checks.append(hand[0].count(card))
            js = hand[0].count("J")
            if max(checks) + js == 5:
                hand.append(6)
                six += 1
            elif max(checks) + js == 4:
                hand.append(5)
                five += 1
            elif max(checks) + js == 3:
                if checks.count(2) == 4:
                    hand.append(4)
                    four += 1
                else:
                    hand.append(3)
                    three += 1
            else:
                hand.append(1)
                one += 1
    for i in range(len(hands)):
        for j in range(len(hands)):
            if i < j:
                if hands[i][2] < hands[j][2]:
                    hands[i], hands[j] = hands[j], hands[i]
    five += six
    four += five
    three += four
    two += three
    one += two
    zero += one
    return card_power(hands, six, five, four, three, two, one, zero, 0, 2)


def card_power(hands, six, five, four, three, two, one, zero, start, part):
    types = [start, six, five, four, three, two, one, zero]
    for hand in hands:
        for card in hand[0]:
            if card in "23456789":
                hand.append(int(card))
            else:
                match card:
                    case "T":
                        hand.append(10)
                    case "J":
                        if part == 2:
                            hand.append(1)
                        if part == 1:
                            hand.append(11)
                    case "Q":
                        hand.append(12)
                    case "K":
                        hand.append(13)
                    case "A":
                        hand.append(14)
    for card in list(range(3, 8)):
        for index in range(len(types)-1):
            for i in range(types[index], types[index+1]):
                for j in range(types[index], types[index+1]):
                    if i < j and hands[i][2:card] == hands[j][2:card]:
                        if hands[i][card] < hands[j][card]:
                            hands[i], hands[j] = hands[j], hands[i]
    print(hands)
    return earnings(hands)


def earnings(hands):
    answer = 0
    for hand in range(len(hands)):
        answer += hands[hand][1] * (len(hands) - hand)
    return answer


print(sort_type_part2(create_hands(lines)))
