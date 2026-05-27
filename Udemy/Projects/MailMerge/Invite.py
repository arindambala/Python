# Day 24 - 100 Days of Code

PLACEHOLDER = '[name]'

print(f"\n ---- Invite ^ People ---- \n")

with open('./Input/People/People.txt') as guest_list:
    guests = guest_list.readlines()
    # print(guests)

with open('./Input/Letter/Letter.txt') as note:
    contents = note.read()
    for name in guests:
        letter = contents.replace(PLACEHOLDER, name.strip())
        print(letter)
        
        with open(f'./Output/ToSend/Invite_{name.strip()}.txt', 'w') as invite:
            invite.write(letter)