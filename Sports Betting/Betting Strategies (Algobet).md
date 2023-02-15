Generally if you are looking to bet the favorite, take them early. If you are looking to bet the underdog, take them later. For the most part, wherever the public is betting on will be where the line moves.


TRENDS ARE MEANINGLESS (without context). The main reason I say this is that the 2013 Golden State Warriors is not the same team as the 2017 one, teams, lines, players are all different and Vegas definitely accounts for that.



https://unabated.com/articles/eliminate-these-five-sharp-betting-tells-from-your-game


Another thing is that once we move away from 50/50 wagers there is a lot less historical examples, so the margin of error increases. My method takes all this into account, and those differences are not small: I did not have a profitable model before I took all kinds of detail such as this into account


https://harbourfronts.com/system-lowest-risk-ruin/#:~:text=We%20can%20see%20from%20the,systems%20are%20in%20this%20category.
- risk of ruin is high if we bet on low odd games or on high odd games 
- practically, we want 50/50 games

We need to find which range of bets is the most profitable


https://vegapit.com/article/numerically_solve_kelly_criterion_multiple_simultaneous_bets


only bet on home in the 50/50 games

bet on underdog games where underdog is at home


In a gambling situation where the odds are against you, your best strategy is usually to make as few bets large as possible, in order to increase the variance in the outcome. The more/smaller bets you make, the closer your fraction of wins is going to be to the probability of winning on any one bet.



- team consistency statistic is important
	- will they play good against underdogs?
	- recent performance is important
	- should take into account winning margin

When do you bet on underdogs?
- high o/u (> 220)
- odds have to have difference of at least 0.2
- small spread (< 5)

How should we identify a low spread high o/u?


When do you bet on favorites?
- high consistency statistic over last 3 games (past week)
- low variance (high spread, high o/u)

When would you skip a bet?
- low spread, low o/u or high o/u
- Evenly matched games with equal odds
	- Games will have low spread, even odds, 
	- No edge here



# Forget about Predicting Match Winner
A really common failure model in trading/investing is focusing on things that don't matter much because you think you could do better, so you think you should. But stuff gets complicated real fast whatever you do, so you have to be pretty ruthless about focusing on the things that actually matter and keeping everything else as simple as possible imo. Zen is in getting really good at the 20% that matters and letting the nerds waste their energy arguing about the 80% that does not. - Robotjames

# Buy cheap sell rich
- Where do we expect cheaper 
- We are limited to buying and don't have opportunities to sell

# Mean reversion?

# Unpredictable Randomness is a defining feature of financial market returns
- Another source of variance in trade returns is being wrong about edge

# Bet Sizing
- Some form of historical volatility to determine risk size
- Wins Above Seeding”, that measures both how well a team resists being upset and how good a team is at upsetting higher seeds.

# Volatility forecast?
- point spread
- o/u spread
- odds difference
- we want to find out probability of upset


# MDP 
https://github.com/llSourcell/sports_betting_with_reinforcement_learning/blob/master/value_iteration_for_sports.py
p(home_team_win) = bookie odds - vig/2
- can possibly use a supervised machine learning model with features
	- (leave roster changes to bookie, they will be reflected in the odds)
	- point spread
	- ou spread
	- team consistency
	- bookie odds

What if this probability is not optimal. We don't use it as the true probability of a team winning
## State
- better's capital

## Actions
- Bet amount (stake)
- a = {0,...,threshold}

## Reward
- The reward is zero on all transitions except those on which the sport better reach is his goal when it is +1
- what is a reward function?
# Neural Networks (custom loss function)
https://towardsdatascience.com/machine-learning-for-sports-betting-not-a-basic-classification-problem-b42ae4900782
# Model Performance
- What if we skip some matches?
# Feature Engineering
 - using social engagement to determine edge?
 - Team resilience
	 - Ability to come back from a deficit
	 - requires exact history of points scored
	 - https://onlinelibrary.wiley.com/doi/10.1111/sms.14295

# Bet Sizing
- Kelly criterion for multiple simultaneous bets
https://vegapit.com/article/numerically_solve_kelly_criterion_multiple_simultaneous_bets


# Sorting bet opportunities
- Equal +EV != equal profitability
- CLT: https://www.scribbr.com/statistics/central-limit-theorem/#:~:text=The%20central%20limit%20theorem%20says,the%20mean%20will%20be%20normal.
- Normal Distribution: https://www.probabilitycourse.com/chapter4/4_2_3_normal.php#:~:text=The%20CDF%20of%20the%20standard%20normal%20distribution%20is%20denoted%20by,is%20widely%20used%20in%20probability.

Quant finance: portfolio optimization
- https://towardsdatascience.com/finrl-for-quantitative-finance-tutorial-for-portfolio-allocation-9b417660c7cd