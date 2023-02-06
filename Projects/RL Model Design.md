
# Edge Extraction
- Where does the edge come from to use in our kelly bet criterion?
	- Or maybe we don't use kelly bet criterion and instead let the policy figure it out
	- We allow each bet to be a maximum of x% 
	- Perhaps a ML model predicts the the outcome of a match
		- Calculate confidence score of prediction
		- Unlikely that we will be able to out-predict a sportsbook


- Overall team performance is not important
- team elo + whether top 2 star player are playing or not
	- use sum(player rating)
	- use variance player rating
- Probability of underdog winning in a bo1 is much higher than in a bo3
	- especially for spreads
	- there is an edge if we can hardcap the probability of a team winning
		- ex: underdog predicted with 10% chance winning
		- But realistically 
		- calculate underdog winning ratio for underdogs with odds > 3
			- cap probability based on this
			- we should also consider the total player rating difference
	- Now with an edge, we can use kelly criterion
- We are essentially looking for which lines look "sketchy", not which lines are priced correctly
	- this leads us to betting more favourably on mispriced underdogs
	- rarely is betting on the massive favorite profitable


- How much edge does a team really have if the given odds are 1.3 vs 1.8
	- when the odds are too close, 1.4 vs 1.6, we should avoid since this is essentially a coin flip without much edge

- Trends are meaningless without context
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
	- Days since last game (is this match a back to back)
- Uncertainty factor
	- Win against underdog percentage in last x games
	- Stand-ins/Injuries present

# Action Space
Kelly Criterion Bet


# Policy: Stochastic