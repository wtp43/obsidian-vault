---
title:  "Sorting Betting Opportunities"
tags:
- stats
created: 2023-02-11
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```


# Sorting Betting Opportunities
Let’s imagine 2 bets with same profit expectation: One with 60% probability of success at 2.0 odds, and the other with 40% probability at 3.0 odds. Which one of these two seems more attractive to take? Well, intuitively, the first one as its profit probability is the highest.

Conclusion: expectation alone seems incomplete to asses the quality of bets.

We need take each bet a very large number of times to study the distribution of the cumulated profit/loss


# Normal Distribution + Central Limit Theorem (CLT)

CLT: The more simulations we make, the more our cumulated profit/loss tends to be Normally distributed.

Let $X_n$ = sum of n independent unit bets.
For $n$ large enough:

$$X_n \sim N(\mu_n, \sigma^2_n)$$ $$E(X_n) = \mu_n = n(pq-1)$$


# Source
https://vegapit.com/article/formula-sorting-betting-opportunities