
# Edge Extraction
- Where does the edge come from to use in our kelly bet criterion?
	- Or maybe we don't use kelly bet criterion and instead let the policy figure it out
	- We allow each bet to be a maximum of x% 
	- Perhaps a ML model predicts the the outcome of a match
		- Calculate confidence score of prediction
		- Unlikely that we will be able to out-predict a sportsbook


# RL Model 
# Environment
Imagine each bet as a roadblock which we navigate through
At each step we only consider the action for the next bet

## States
- Account balance
- Importance of match
	- Playoff eligibility
	- Playoff match
- Home game
	- Was it a long flight with little to no rest?
- Well rested
	- Days since last game
- Uncertainty factor
	- Win against underdog percentage in last x games
	- Stand-ins/Injuries present

# Action Space
Kelly Criterion Bet


# Policy: Stochastic