# blackjack-q-learning
Q learning (Reinforcement learning) with blackjack. Model is still in testing 🚧

I used the player's hand, one of the dealer's cards, the current card count (ooh sneaky), and the number cards that have been dealt so far as the parameters. In order to use the qTable though, I had to squishify 4 of these into just 1 with 4 for loops ... and ended up with an insanely big q table... It's just a first attempt so that shall do for now :) and on hindsight maybe q table was not the best approach. 

Currently in the process of squishifying the q table further by introducing true count (rounded to 3sf?) to remove the need for 2 other features. If this works, I'll see you in Vegas🎰
