---
dg-publish: true
---
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
- player performances
	- groupby.rolling
	- shift(-1
 - team top 5 players mean(PER, PPG) over the last 40 games
	 - instead of per try crossing all factors
		 - divide by time
 - prev 5 games mean(pace x fga)
	- **Pace** - Pace Factor (available since the 1973-74 season in the NBA); the formula is 48 * (([Tm](https://www.basketball-reference.com/about/glossary.html#team) [Poss](https://www.basketball-reference.com/about/glossary.html#poss) + [Opp](https://www.basketball-reference.com/about/glossary.html#opp_id) [Poss](https://www.basketball-reference.com/about/glossary.html#poss)) / (2 * ([Tm](https://www.basketball-reference.com/about/glossary.html#team) [MP](https://www.basketball-reference.com/about/glossary.html#mp) / 5))). Pace factor is an estimate of the number of possessions per 48 minutes by a team. (Note: 40 minutes is used in the calculation for the WNBA.)
	- **Poss** - Possessions (available since the 1973-74 season in the NBA); the formula for teams is 0.5 * (([Tm](https://www.basketball-reference.com/about/glossary.html#team) [FGA](https://www.basketball-reference.com/about/glossary.html#fga) + 0.4 * [Tm](https://www.basketball-reference.com/about/glossary.html#team) [FTA](https://www.basketball-reference.com/about/glossary.html#fta) - 1.07 * ([Tm](https://www.basketball-reference.com/about/glossary.html#team) [ORB](https://www.basketball-reference.com/about/glossary.html#orb) / ([Tm](https://www.basketball-reference.com/about/glossary.html#team) [ORB](https://www.basketball-reference.com/about/glossary.html#orb) + [Opp](https://www.basketball-reference.com/about/glossary.html#opp_id) [DRB](https://www.basketball-reference.com/about/glossary.html#drb))) * ([Tm](https://www.basketball-reference.com/about/glossary.html#team) [FGA](https://www.basketball-reference.com/about/glossary.html#fga) - [Tm](https://www.basketball-reference.com/about/glossary.html#team) [FG](https://www.basketball-reference.com/about/glossary.html#fg)) + [Tm](https://www.basketball-reference.com/about/glossary.html#team) [TOV](https://www.basketball-reference.com/about/glossary.html#tov)) + ([Opp](https://www.basketball-reference.com/about/glossary.html#opp_id) [FGA](https://www.basketball-reference.com/about/glossary.html#fga) + 0.4 * [Opp](https://www.basketball-reference.com/about/glossary.html#opp_id) [FTA](https://www.basketball-reference.com/about/glossary.html#fta) - 1.07 * ([Opp](https://www.basketball-reference.com/about/glossary.html#opp_id) [ORB](https://www.basketball-reference.com/about/glossary.html#orb) / ([Opp](https://www.basketball-reference.com/about/glossary.html#opp_id) [ORB](https://www.basketball-reference.com/about/glossary.html#orb) + [Tm](https://www.basketball-reference.com/about/glossary.html#team) [DRB](https://www.basketball-reference.com/about/glossary.html#drb))) * ([Opp](https://www.basketball-reference.com/about/glossary.html#opp_id) [FGA](https://www.basketball-reference.com/about/glossary.html#fga) - [Opp](https://www.basketball-reference.com/about/glossary.html#opp_id) [FG](https://www.basketball-reference.com/about/glossary.html#fg)) + [Opp](https://www.basketball-reference.com/about/glossary.html#opp_id) [TOV](https://www.basketball-reference.com/about/glossary.html#tov))). This formula estimates possessions based on both the team's statistics and their opponent's statistics, then averages them to provide a more stable estimate. Please see the article [Calculating Individual Offensive and Defensive Ratings](https://www.basketball-reference.com/about/ratings.html) for more information.
 - point_spread x o/u
 - team four factors
	 - efg%
	 - tov%
	 - orb%
	 - ft/fga
	 - ortg
- uncertainty
	- adjusting for luck
- meta-labeling
	- using bookie predictions (odds)
- fatigue
	- days since last game x nth away game
- exclude data from 2020
- cross (eFG%, TOV%, ORB%, FT/FGA)
- home or away game
- momentum
	- A noticeable pattern that distinguishes the results in Tables [5](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9041568/table/T0005/) and [7](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9041568/table/T0007/) is the reversed relationship between the environmental and technical variables. In Table [7](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9041568/table/T0007/), turnovers become the leading factor, followed by rebounds. This is a very interesting finding: for teams that want to extend their momentum, it is not only about scoring more points directly; less eye-catching moments, such as getting the rebounds and minimizing turnovers, are actually more important.
	- winning streak (-ve for losing streak)
- confidence interval
- % of underdogs that win with odds > x
	- plot 
- risk of ruin
	- https://vegapit.com/article/bet-sizing-using-risk-of-ruin-indicator
	- ((1 – (W – L)) / (1 + (W – L)))U
# Don't use monte carlo
0 https://www.reddit.com/r/statistics/comments/f12eqx/discussion_monte_carlo_simulations_to_simulate/

# Why a model highly correlated to the bookmaker's model is bad
Consider a situation where the bettor’s learned model coincides with the bookmakers model. Then any betting opportunity promising from the viewpoint of an estimated high outcome probability $\hat{p_i}$ = $\bar{p_i}$ is made unfavorable by the odds set lower than $\frac{1}{\bar{p_i}}$ . Therefore, even a highly accurate predictive model is useless as long as it coincides with the bookmaker’s model.

This motivates the objective to learn a predictive model under two criteria of quality: high accuracy on empirical data, and adequately low correlation with the bookmaker’s model.

Unless the bookmaker’s odds are systematically biased, which they are not (Hubacek, 2017), a model considering odds as the only input feature would have no choice but to coincide perfectly with the bookmaker, inevitably doomed to end up with negative returns directly proportional to the margin.

# Bet Sizing
- Kelly criterion for multiple simultaneous bets
https://vegapit.com/article/numerically_solve_kelly_criterion_multiple_simultaneous_bets


# Sorting bet opportunities
- Equal +EV != equal profitability
- CLT: https://www.scribbr.com/statistics/central-limit-theorem/#:~:text=The%20central%20limit%20theorem%20says,the%20mean%20will%20be%20normal.
- Normal Distribution: https://www.probabilitycourse.com/chapter4/4_2_3_normal.php#:~:text=The%20CDF%20of%20the%20standard%20normal%20distribution%20is%20denoted%20by,is%20widely%20used%20in%20probability.

Quant finance: portfolio optimization
- https://towardsdatascience.com/finrl-for-quantitative-finance-tutorial-for-portfolio-allocation-9b417660c7cd

# Neural Network Loss Function
- Should take into account risk of ruin (size of bet vs reward)
# EDA
https://www.youtube.com/watch?v=egTylm6C2is
# Neural Network Betting 
- pace of teams for over/under
https://github.com/charlesmalafosse/sports-betting-customloss/blob/master/notebook/BetSentiment_SportsBetting_CustomLossFunction.ipynb
https://towardsdatascience.com/machine-learning-for-sports-betting-not-a-basic-classification-problem-b42ae4900782

https://medium.com/re-hoop-per-rate/training-a-neural-network-to-fill-out-my-march-madness-bracket-2e5ee562eab1

When exactly can XGBoost get a better result than deep learning?

](https://www.quora.com/When-exactly-can-XGBoost-get-a-better-result-than-deep-learning)

When the features are heterogeneous.

Deep Learning is the state of the art for images, video, audio and natural language processing. In all those tasks the features for each observation are homogeneous in the sense that they have the same scale and unit of measure: pixels in an image, frames in a video, words in text, etc.

When your data is made of heterogeneous columns such as age, weight, number of times the client called, average time of a call, etc then Xgboost is usually better than Deep Learning.

The reason for this is that tree-based methods treat features independently of each other and build rules based on the values for those features. In simpler words a tree-based algorithm will try to answer if a person is going to fill a complain based on things such as “is the time of the call greater than 5 minutes? is the client older than 40?, etc” while a NN would try to do something such as “risk of complain = w1 * age + w2 * time of call”. It can be seen that with heterogeneous columns linearly mixing things that are very different is not an easy task. This explanation is oversimplified but should work to show the point.

PS!: If you find a case where a NN performs better than XGBoost for heterogeneous data please let me know I’m looking for examples.
# Binary Classification Problems
Meta Labeling
 
Binary classification problems present a trade-off between type-I errors (false positives) and type-II errors (false negatives). In general, increasing the true positive rate of a binary classifier will tend to increase its false positive rate. The receiver operating characteristic (ROC) curve of a binary classifier measures the cost of increasing the true positive rate, in terms of accepting higher false positive rates.

## Modular Structure
By decoupling the side prediction from the size prediction, meta labeling enables sophisticated strategy structures.
For instance, consider that the features driving a rally may differ from the features driving a sell-off. In that case, you may want to develop an ML strategy exclusively for long positions, based on the buy recommendations of a primary model, and an ML strategy exclusively for short positions, based on the sell recommendations of an entirely different primary model.

Achieving high accuracy on small bets and low accuracy on large bets will ruin you. As important as identifying good opportunities is to size them properly, so it makes sense to develop an ML algorithm solely focused on getting that critical decision (sizing) right. In my experience, meta labeling ML models can deliver more robust and reliable outcomes than standard labeling models.
![[Pasted image 20230218160314.png]]
## Process
- Train binary classification primary model that has high recall
	- Adjust threshold to increase recall
- Concatenate the predictions to the features from the first model from first model into a new feature set for the secondary model
- Meta labels are used as the target variable in the second model
- Fit the second model
	- The secondary model will reduce false negatives
- Filter predictions 
	- If the primary model predicts a 3 and your secondary model says you have a high probability of the primary model being correct, then the final prediction is a 3 else not a 3


https://hudsonthames.org/meta-labeling-a-toy-example/


# Bet sizing from Predicted Probabilities

For two possible outcomes $x \in \{-1,1\}$, we would like to test the null hypothesis $H_0 : P[x=1] = 1/2$. We compute the test statistic $$z = \frac{P[x=1]-\frac{1}{2}}{\sqrt{P[x=1](1-P[x=1])}}$$
This is derived using z score for standard normal distribution and the standard deviation is estimated using binomial distribution

# Triple Barrier Method Adapted to Bets
- Dynamically function that calculates the rolling threshold based on recent win/rate
	- Low win_rate -> bigger threshold (mimic volatility)
	- Use EMA


When you size positions you can't just simply use the model's confidence. You should look at the distribution of the outcomes to size positions. If most of the outcomes range between 0.4-0.6, it's not really going to improve the position sizing component at all, An easy way to do this, is to use the ECDF of the training set to size the positions. You should also look at outcomes of the average loss and win rates, to determine the threshold to trade. It won't make sense if you have symmetric pay-offs and still trade if the model's confidence is 0.2, leading to a negative EV. You can also use probability calibration to bring the outcomes closer to true probabilities and then size positions

My thesis is that the meta-model makes more sense where the underlying signal is not ML generated and would benefit from a ML layer so this case is actually a good one.
https://www.quantconnect.com/forum/discussion/14706/why-meta-labeling-is-not-a-silver-bullet/p1

https://www.youtube.com/watch?v=hUSJtevWw6M


https://colab.research.google.com/drive/1FmnCJ1CI98khBu88kezLXKqvS7U8Nw_h?usp=sharing#scrollTo=k6s5ZC0eGEbW


# Feature Extraction (Human factor)
- days since last game
- number of games played in the last week
- number of away games
- distance of away game to home game
- confidence/overconfidence?
	- Was the last game an upset
	- % of games against favorites won after an upset
	- % of games against underdogs won after an upset
	- relative victory frequency
- Performance volatility
	- variance of points/min, etc
- team can have high winning rate but also high volatility
	- spreads might be +ev
	- we want to check movl margin^2
- Time of game