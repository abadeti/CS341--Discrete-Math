# Anuja Badeti
# ab2253
# CS 341 Project 1

import sys

#establish all values in gamma
gamma = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z']

def follows_dfa(st):
    # traverse through each character in email address and determine what state it is in
    # output the character and state at each letter of the email address
    # finally output if the email address is accepted or rejected
    current_state = 1
    print("Starting processing state: q1")
    for i in range(len(st)):
        ch = st[i]
        if current_state == 1:
            # q1 -> q2/trap
            if ch not in gamma:
                current_state= "Trap State"
            else:
                current_state = 2
        elif current_state == 2:
            # q2 -> q2/q3/q4
            if ch not in gamma:
                if ch =='@':
                    current_state = 4
                elif ch == '.':
                    current_state = 3
        elif current_state == 3:
            # q3 -> q2/trap
            if ch not in gamma:
                current_state="Trap State"
            else:
                current_state = 2
        elif current_state == 4:
            # q4 -> q5/trap
            if ch in gamma:
                current_state = 5
            else:
                current_state = "Trap State"
        elif current_state == 5:
            # q5 -> q5/q6/trap
            if ch == '.':
                current_state = 6
            elif ch in gamma:
                current_state = 5
            else:
                current_state = "Trap State"
        elif current_state == 6:
            # q6 -> q7/q9/trap
            if ch == 'e':
                current_state = 9
            elif ch in gamma:
                current_state = 7
            else:
                current_state = "Trap State"
        elif current_state == 7:
            # q7 -> q7/q8/trap
            if ch == '.':
                current_state = 8
            elif ch not in gamma:
                current_state = "Trap State"
        elif current_state == 8:
            # q8 -> q7/q9/trap
            if ch == 'e':
                current_state = 9
            elif ch in gamma:
                current_state = 7
            else:
                current_state = "Trap State"
        elif current_state == 9:
            # q9 -> q7/q8/q10/trap
            if ch == 'd':
                current_state = 10
            elif ch in gamma:
                current_state = 7
            elif ch == '.':
                current_state = 8
            else:
                current_state = "Trap State"
        elif current_state == 10:
            # q10 -> q7/q8/q11/trap
            if ch == 'u':
                current_state = 11
                if i == len(st) - 1:
                    # accepting state
                    print("Current character: " + ch)
                    print("Current state: q" + str(current_state))
                    print("Reached final state - This string is ACCEPTED")
                    return
            elif ch in gamma:
                current_state = 7
            elif ch == '.':
                current_state = 8
            elif ch == '@':
                current_state = "Trap State"
        elif current_state == 11:
            # q11 -> q7/q8/trap
            if ch in gamma:
                current_state = 7
            elif ch == '.':
                current_state = 8
            else:
                current_state = "Trap State"
        print("Current character: " + ch)
        print("Current state: " + str(current_state))
    if current_state != 11:
        print("Did not reach final state - This string is REJECTED")

def main():
    # ask for y and email or n until n is given
    print('Project 1 for CS 341')
    print('Semester: Fall 2020')
    print('Written by: Anuja Badeti, ab2253')
    print('Instructor: Marvin Nakayama, marvin@njit.edu')
    is_yes = False
    f = open(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin
    print("Enter y, enter, and the email address to continue or n to end the program")
    for line in f:
        line = line.strip()
        if line == 'y':
            is_yes = True
        elif line == 'n':
            break
        elif is_yes:
            print(line)
            follows_dfa(line)
            is_yes = False

if __name__ == "__main__":
    main()