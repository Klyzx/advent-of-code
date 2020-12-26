with open("inputs/25.in") as file:
    card_public = int(file.readline())
    door_public = int(file.readline())

subject_card = 7
subject_door = 7
card_loopsize = 1
door_loopsize = 1
while subject_card != card_public or subject_door != door_public:
    if subject_card != card_public:
        card_loopsize += 1
        subject_card = (subject_card * 7) % 20201227
    if subject_door != door_public:
        door_loopsize += 1
        subject_door = (subject_door * 7) % 20201227
# card_loopsize = 13330548
subject_card = subject_door
for _ in range(card_loopsize-1):
    subject_card = (subject_card * subject_door) % 20201227

print(subject_card)
