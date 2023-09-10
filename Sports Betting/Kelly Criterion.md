---
dg-publish: true
title:  "Kelly Criterion"
tags:
created: 2023-02-05
---

>[!summary]+ Contents
>```toc
style: number
min_depth:1
max_depth:6 
>```


# Kelly Criterion Gambling Formula
Where losing the bet involves losing the entire wager, the Kelly bet is:
$$f^* = p - \frac{q}{b} = p - \frac{1-p}{b}$$
where:
- $f^*$ is the fraction of the current bankroll to wager
- $p$ is the probability of a win
- $q$ is the probability of a loss ($q=1-p$)
- $b$ is the proportion of the bet gained with a win
	- Ex: If betting $10 with decimal odds = 3. (Returned $30, with profit = $20), then $b =20/10=2$

Thus, 
- Higher $b$ and $p$ results in higher bet fraction

If the gambler has zero edge, i.e. if $b=\frac{q}{p}$, then the criterion recommends for the gambler to bet nothing.

# Kelly Criterion Investment Formula
A more general form that allows for partial losses:
$$f^* = \frac{p}{a}-\frac{q}{b}$$
where: 
- $p$ is the probability that the investment increases in value
- $q$ is the probability that the investment decreases in value
- $a$ is the fraction that is lost in a negative outcome
- $b$ is the fraction that is gained in a positive outcome

Note that the Kelly criterion is valid only for known outcome probabilities, which is not the case with investments.This formula can result in Kelly fractions higher than 1. In this case, it is theoretically advantageous to use [leverage](https://en.wikipedia.org/wiki/Leverage_(finance) "Leverage (finance)") to purchase additional securities on [margin](https://en.wikipedia.org/wiki/Margin_(finance) "Margin (finance)").

Source: https://en.wikipedia.org/wiki/Kelly_criterion
# Implementation

```python
def decimal_odds_to_implied(dec_odds):
	return 1/dec_odds


def kelly_criterion_size(odds):
	
	return p - (1-p)/b

	return bet_size
```

