---
title: 'Limit of Binomial Distribution'
date: 2021-06-19
permalink: /posts/2021/06/limit-of-binomial-distribution/
tags:
  - math
  - Poisson
---


In computational neuroscience, Poisson distribution is very important
in that spike trains are usually modeled as a Poisson process. This
article demonstrates that the Poisson distribution can be obtained as a
limit of Binomial Distribution.

Consider a time interval $[0,T]$
in which spikes occur. Let's assume that $k$ spikes occur within that interval. Now
we divide the interval into $n$ bins,
and within each time bin, a spike occurs with probability $p$. Note that we only allow one spike per
bin. So the probability of having $k$
spikes within $[0,T]$ is $$
P(k) = {n\choose k}p^k(1-p)^{n-k}
$$ Now this is the probability mass function of binomial
distribution. If we take the limit of $n\to
\inf$, we quickly find that the result is zero. This is because
it is upper-bounded by $n^k (1-p)^n$
times a constant. It suffices to show that $n\alpha^n\to 0$ as $n\to \inf$, where $0\<\alpha\<1$. Simply note that $n\alpha^{n-1}$ is the derivative of $\alpha^n$ which goes to 0 as $n$ goes to infinity. So we can always
choose large enough $n$ such that any
finite difference of $\alpha^n$ around
$\alpha$ is below any small $\varepsilon$, QED.

The question now is how do we take the limit in a proper sense so
that the result is the probability mass function of Poisson
distribution. We introduce a new concept called the firing rate $r$, which indicates how often the neuron
fires with the time interval $[0,T]$.
Here is the key insight: as $n$
grows, each time bin gets smaller and smaller, so the probability of a
spike occurring $p$ is also
increasingly smaller. More specifically, they are related by $\lambda:=rT = np$.

Now here is the mathematical show: 
$$
\begin{split}
\lim_{\lambda = np,\ n\to \inf}P(k) &= \lim_{rT = np,\ n\to
\inf}\frac{n!}{k!(n-k)!}(\lambda/n)^k(1-\lambda/n)^{n-k}\\
&=\lim_{\lambda = np,\ n\to
\inf}\frac{n!}{k!(n-k)!}(\lambda/n)^k(1-\lambda/n)^{-k}((1-\lambda/n)^{-n/\lambda})^{-\lambda}\\
&=\lim_{\lambda = np,\ n\to
\inf}\frac{n!}{k!(n-k)!}\frac{\lambda^k}{(n-\lambda)^k}\exp(-\lambda)\\
&=\frac{\lambda^k}{k!}\exp(-\lambda)
\end{split}
$$

In the intermediate step we use the definition of Euler's
number $e$, and we arrive at the
probability mass function of Poisson Distribution. We are done, have a
nice day :)