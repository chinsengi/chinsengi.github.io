---
title: '如何求解 $\dot{x} = x+f(t)$'
date: 2021-09-29
permalink: /posts/2021/09/diffeqsolve/
tags:
  - math
  - differential equation
---


最近在看Dayan和Abbott的[*Theoretical
Neuroscience*](https://mitpress.mit.edu/books/theoretical-neuroscience){:rel="noopener" target="_blank"}。虽然是数学系学生但是由于太浪，分析代数几何都学了个遍，感觉哪科都没学好，于是后遗症就是像傅里叶变换这种极为重要的东西竟然不是很熟。
于是我决定先把书后面的数学Appendix先光速过一遍，以免在读正文的时候尴尬卡壳。在附录讲微分方程的部分有一个方程：
$$
\begin{equation}
C\frac{dV}{dt} = \frac{E-V}{R} + I_e
\end{equation}
$$ 这是比较容易求解的，令$W =
-V+E+RI_e$, 我们有 $$
\begin{equation}
RC(-W)' = W
\end{equation}
$$ 愉快地分离变量就能得到$W =
C'\exp(-t/\tau)$. 把$V(0)$ 这个初始条件代进去就有$C' = W(0) = -V(0)+E+RI_e$。
我们就能得到书上列出的解 $$
\begin{equation}
V(t) = V\_\inf +(V(0)- V\_\inf) \exp(-t/\tau)
\end{equation}
$$

[]{#more}

其中$V\_\inf = E+RI_e$, $\tau =
RC$。接下来作者又假设了另外一种情况， 这种情况下$I_e$ 随时间振荡： $I_e = I\cos(\omega t)$.
这下就有点难办，不过没关系，把我们的意大利炮拉上来: 对于方程 $\dot{x} = a(t)x+b(t)$, 我们有解 $$
\begin{equation}
x(t) = \exp\left(\int_0^t a(s)\,ds\right)x(0)+\int_0^t
\exp\left(\int_s^t a(r)\,dr\right)b(s)\,ds
\end{equation}\label{eq:1}\tag{1}
$$ 这个方程是这样解的， 两边同乘$\mu(t) = \exp(-\int_0^t a(s) ds)$
(别问我为啥是这个，问就是exponential的derivative可以把指数拿下来然后用链式法则，就硬凑)。这样方程就变成了
$$
\begin{equation}
\begin{split}
\mu(t)\dot{x} - \mu(t)a(t)x&= b(t)\mu(t)\\
\left(\mu(t)x\right)' &= b(t)\mu(t)\\
\mu(t)x &=\int_0^t b(r)\mu(r)dr+C\\
\end{split}
\end{equation}
$$

把$t = 0$带进去, 发现$C = x(0)$, 把$\mu(t)$
移到另一边，我们就得到了之前那个解$\eqref{eq:1}$。直接把答案代到方程里面验算当然也可以证明，但那就是明目张胆的作弊了。而且应该会用到[Leibniz
integral rule](https://en.wikipedia.org/wiki/Leibniz_integral_rule){:rel="noopener" target="_blank"}。接下来我们，开炮！我们把$V$当成$x$, $a(t) =
-1/\tau$, $b(t) = E/\tau+I\cos(\omega
t)/C$, 所以解就是 $$
\begin{equation}
V(t) = e^{-t/\tau}V(0)+\int_0^t e^{-(t-s)/\tau}b(s)ds
\end{equation}
$$

可能大家读到这里都忘了我们是在解一本书里面的方程，书上是这么说的,
\"once an initial transient has decayed to zero, we find\" $$
\begin{equation}
V(t) = E+\frac{RI\cos(wt- \phi)}{ \sqrt{1+\omega^2 \tau^2} }
\end{equation}
$$ 其中$\tan(\phi) =
\omega\tau$。啊这。。。我刚开始看的时候是懵逼的，啥是transient?
后来才知道可能这是电子工程里面的术语。
Transient的意思不是短暂的么，这里就是指在$t\to \inf$时趋于0的项，
可以想象成时间长了后散逸掉的能量。我们相当于要求下面这个东西 $$
\lim\_{t\to\inf} \int_0^t e^{-(t-s)/\tau}b(s)ds
$$ 这里的极限不是分析意义上的，只是表示去掉$t\to \inf$时为0的项。东凑凑西算算，
最后发现还是把余弦化成复数形式会比较好： $$
\begin{equation}
\cos(\omega t) = \frac{\exp(iwt)+\exp(-iwt)}{2}
\end{equation}
$$

目的当然是好积分， 并不清楚作者是如何算的 $$
\begin{split}
\int_0^te^{-(t-s)/\tau}(E/\tau+I\cos(\omega s)/C)ds &= A(t)+B(t)+C(t)\\
A(t)&=\frac{E}{\tau}\int_0^t e^{-(t-s)/\tau}ds\\
B(t)&= \frac{I}{2C}\int_0^t\exp(iws-(t-s)/\tau)ds\\
C(t)&= \frac{I}{2C}\int_0^t\exp(-iws-(t-s)/\tau)ds
\end{split}
$$ 简单的积分: $$
\begin{split}
A(t) &= E(1-e^{-t/\tau})\\
B(t) &= \frac{I\tau}{2C(iw\tau +1)}(\exp(iwt) - \exp(-t/\tau))\\
C(t) &= \frac{I\tau}{2C(-iw\tau +1)}(\exp(-iwt) - \exp(-t/\tau))\\
\end{split}
$$ 求个"极限" $$
\begin{split}
\lim\_{t\to\inf} A(t) &= E\\
\lim\_{t\to\inf} B(t) &=\frac{I\tau}{2C(iw\tau +1)}\exp(iwt)\\
\lim\_{t\to \inf}C(t) &= \frac{I\tau}{2C(-iw\tau +1)}\exp(-iwt)\\
\end{split}
$$ 别忘了$\tau = RC$,
于是我们有 $$
V(t) = E+\frac{RI\left[\exp(iwt)(-iw\tau+1)+\exp(-iwt)(iw\tau+1)\right]}{2(
1+\omega^2 \tau^2)}
$$ 把指数再展开成三角函数 $$
V(t) = E+\frac{RI(\cos(w\tau)+w\tau \sin(w\tau) )}{1+w^2\tau^2}
$$
诶和书上的答案不一样，gg。小丑竟是我自己。其实是这样，观察分子和 $$
\cos(\alpha-\beta) = \cos(\alpha)\cos(\beta)+\sin(\alpha)\sin(\beta)
$$ 的相似性， 我们希望 $$
\begin{split}
\cos(\phi) = 1\\
\sin(\phi) = w\tau
\end{split}
$$ 这不可能，平方和要是1，于是上下同除$1/\sqrt{1+w^2\tau^2}$即可。 $$
\begin{split}
\cos(\phi) = 1/\sqrt{1+w^2\tau^2}\\
\sin(\phi) = w\tau/\sqrt{1+w^2\tau^2}
\end{split}
$$ $\tan(\phi) =
w\tau$自然成立。到此我们终于得到了这个书上没有过程的结论。。。

后记：打这篇文章主要是想体验一下在博客里面写有大量公式的文章的体验。
有macro确实爽。不过打latex得不断切换中英输入法很麻烦，下次用英语写得了。
