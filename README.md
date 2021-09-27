# blackjack-q-learning
This is an exploration of Q learning (Reinforcement learning) with the example of blackjack. Currently the model is very simple and only allows players to 'hit' once. However, the good news is that the percentage win is approximately 38-40%, which beats randomly hitting (30-33%) and hitting only if the score is below 16 (30-33%)

I used the player's hand, one of the dealer's cards, the true card count (ooh sneaky) to construct a q table and iterated about 500000 times.

A win occurs only when the score of the player is higher than the casino. In the event that the scores are the same, the dealer wins. In the event that both the player and casino busts, the dealer wins. When both the dealer and casino blackjack, the dealer also wins.

In the (hopefully) not so distant future I'll get this to work better! Then I'll see you in Vegas ;D 🎰
