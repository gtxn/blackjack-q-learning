# blackjack-q-learning
This is an exploration of Q learning (Reinforcement learning) with the example of blackjack. Currently the model is very simple and only allows players to 'hit' once. However, the good news is that the percentage win is approximately 38-40%, which beats randomly hitting (30-33%) and hitting only if the score is below 16 (30-33%)

I used the player's hand, one of the dealer's cards, the true card count (ooh sneaky) to construct a q table and iterated about 500000 times.

In the (hopefully) not so distant future I'll get this to work better at least nearer to 50%. Then, I'll see you in Vegas🎰
