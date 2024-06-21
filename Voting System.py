candidates = {}

num_candidates = int(input("Number of candidates: "))

for i in range(num_candidates):
    candidate_name = input(f"Name of candidate {i + 1}: ")
    candidates[candidate_name] = 0
    
voting_age = 18
num_voters = int(input("Number of voters: "))

for i in range(num_voters):
    print(f"Voter {i + 1}, Enter your age: ")
    voter_age = int(input())
    if voter_age < voting_age:
        print(f"Sorry, you are not eligible. You must be at least {voting_age} years old to vote.")
    else:
        print("You are eligible to vote. Enter your vote:")
        for candidate in candidates:
            print(f"{candidate}: {candidates[candidate]} votes")
        voter_choice = input("Enter the name of your chosen candidate: ")

        if voter_choice in candidates:
            candidates[voter_choice] += 1
            print("Thank you for voting!")
        else:
            print("Invalid candidate name. Vote not counted.")
            
winner = max(candidates, key=candidates.get)
print(f"The winner is {winner} with {candidates[winner]} votes.")
