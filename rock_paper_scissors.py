import random
moves= ["Rock 🪨","Paper 📄","Scissors ✂️"]
shortcuts= {
    "r":"Rock 🪨",
    "p":"Paper 📄",
    "s":"Scissors ✂️"
}
#initiating score
user_score = 0
comp_score = 0
#Welcome not and instructions for control
print("\n✨ Welcome to Rock-Paper-Scissors! ✨")
print("First to 5 points wins the match 🏆")
print("Type 'quit' anytime to exit.\n")
print("👉 Controls: type 'r' for Rock, 'p' for Paper, 's' for Scissors.\n")
#user and computer inputs
while True:
    user_input = input("").strip().lower()
    comp_input = random.choice(moves)
    
    if user_input == 'quit':
        print("Thank You for playing!")
        break
    if user_input not in shortcuts:
        print('Please enter a valid input')
        continue
    user_input = shortcuts[user_input]
    print(f'You chose: {user_input}')
    print(f"Computer chose: {comp_input}")
    if user_input == comp_input:
        print("It's a tie")
    elif (user_input == "Rock 🪨" and comp_input == "Scissors ✂️") or \
         (user_input == "Paper 📄" and comp_input == "Rock 🪨") or \
         (user_input == "Scissors ✂️" and comp_input == "Paper 📄"):
        print("🎖️ You won this round!!")
        user_score+=1
    else:
        print("🎖️ Computer won this round")
        comp_score += 1
    #print scores
    print(f"📊The scores of this round are You {user_score} - {comp_score} Computer")
    #end the game(loop)
    if comp_score == 5:
        print("👏 Well played! The computer reached 5 points this time. Don't worry, try again! 💪\n")
        break
    elif user_score == 5:
        print("🏆 Congratulations! You reached 5 points and won the match! 🎉\n")
        break


        