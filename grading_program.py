from replit import clear

students_scores = {
    "bakary": 84,
    "saliou": 92,
    "olivier": 73,
}

students_grades = {}
for student in students_scores:
    if 91 <= students_scores[student] <= 100:
        students_grades[student] = "Outstanding"
    elif 81 <= students_scores[student] <= 90:
        students_grades[student] = "Exceeds expectation"
    elif 71 <= students_scores[student] <= 80:
        students_grades[student] = "Acceptable"
#print(students_grades)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
    return highest_bid


bids = {}
add_other = True
while add_other:
    name = input("What is your name?: ")
    bid = int(input("What is you bid?: "))
    bids[name] = bid
    should_continue = input("do you want to continue?: ")
    if should_continue == "no":
        add_other = False
    elif should_continue == "yes":
        clear()

print("the higher score is: ", str(find_highest_bidder(bids)))