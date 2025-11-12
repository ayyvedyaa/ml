from scipy.stats import norm

# PDF (Probability Density Function)
d_norm = norm.pdf(2.3, loc=5, scale=2.51)
print("dnorm (norm):", d_norm)

# CDF (Cumulative Distribution Function)
p_norm = norm.cdf(5.3, loc=5, scale=2.51)
print("pnorm (norm):", p_norm)
