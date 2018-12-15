a=raw_input("Get the person 1 choice:")
b=raw_input("Get the person 2 choice:")
if ( a is "rock" and b is "rock"):
    print "Game Tie"
elif ( a == "rock" and b == "scissors"):
    print "Rock will win the game"
elif ( a == "rock" and b == "paper"):
    print "Paper will wrap the rock"
elif ( a== "scissors" and b == "rock"):
     print "Rock will win the game"
elif (a == "scissors" and b =="paper"):
    print "Scissors will cut the paper"
elif (a == "scissors" and b =="scissors"):
    print "Game Tie"
elif ( a == "paper" and b== "rock"):
    print "Paper will wrap the rock"
elif (a== "paper" and b =="scissors"):
    print "scissors will cut the paper"
elif ( a=="paper" and b=="paper"):
    print "Game tie"