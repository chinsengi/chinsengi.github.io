---
title: 'Chinese Remainder Theorem'
date: 2021-07-01
permalink: /posts/2021/07/chinese-remainder-theorem/
tags:
  - Competitive Programming
  - Chinese Remainder Theorem
---


I recently decided to pick up competitive programming, not only
because I enjoy programming, but also because this is a fail safe for my
academic career. With the tension between China and US rises, any
Chinese research personnel in the US is bound to be persecuted in one
way or another (it already begins with the visa application). It will be
increasingly risky to put all the eggs in one basket. And the recent [Wenhua
Jiang Incident](https://www.universityworldnews.com/post.php?story=20210611084120155){:rel="noopener" target="_blank"} further dims the light on the path to tenure in China
for many researchers. So in short, doing competitive programming is an
act of interest (pun intended).

So much gibberish, today we are going to talk about Chinese Remainder
Theorem, which basically says that given a set of coprime integers, and
we know the remainders of an unknown integer modulo those coprime
numbers, then the smallest such unknown number can be uniquely
determined. For a rigorous definition, see [wiki](https://en.wikipedia.org/wiki/Chinese_remainder_theorem){:rel="noopener" target="_blank"}.
The proof is quite simply, say the set of coprime numbers are $n_1, n_2, \dots, n_k$, and $N = \Pi_i n_i$. And the aforementioned
remainders are $r_1, r_2, \dots,
r_k$. We only consider integers in the range $[1, N]$. The key observation is that if
two *different* numbers have the same set of remainders, the
absolute difference between them will be divisible by all $n_i$ s, and since the difference is capped
by $N-1$, it is zero, contradiction!
Therefore a one-to-one correspondence can be established between each
integer within that range and a set of all possible remainders. Note
that the range of each $r_i$ is $[0, r_i-1]$, so both sides have the same
cardinality.

Now let's look at implementation of this theorem in competitive
programming. An example problem is [here](https://atcoder.jp/contests/abc193/tasks/abc193_e){:rel="noopener" target="_blank"}. So
the problem is to solve the following set of congruence equations $$
x \equiv a_1 \pmod{m_1}\\
x\equiv a_2 \pmod{m_2}
$$ which is equivalent to $$
x = a_1+n_1 m_1 = a_2+n_2m_2
$$ for some integer $n_1$ and
$n_2$, i.e. $$
\begin{equation}
a_2 - a_1 = n_1m_1 - n_2m_2 \tag{1} \label{eq:1}
\end{equation}
$$ We can use extended Euclidean algorithm to solve for $n_i$ given $m_i$ in the following equation $$
\begin{equation}
n_1m_1 - n_2m_2 = \gcd(m_1, m_2) := d \tag{2}\label{eq:2}
\end{equation}
$$ *Detour (please skip at will)*: There is a proof of
existence of an integer solution that I really like about the above
equation. Since we can divide both sides by $\gcd(m_1, m_2)$, we can just deal with the
case $n_1m_1 - n_2m_2 = 1$ where
$m_1$ and $m_2$ are coprime to each other. Now here
is the clever proof: Let $r$ be the
smallest positive integer such that $n_1m_1 -
n_2m_2 = r$ has an integer solution. And we can express $m_1$ as multiple of $r$ plus a remainder term, i.e. $m_1 = q_1r+r_1$. So the equation becomes
$$
n_1m_1 - n_2m_2 = r = (m_1 - r_1)/q_1
$$ Some algebra shows that $(1-q_1n_1)m_1+n_2q_1m_2 = r_1$, note that
$r_1$, as a remainder of division by
$r$, is strictly smaller than $r$. So there is only one possibility:
$r_1 = 0$. So $m_1$ is actually a multiple of $r$ ! By symmetry, $m_2$ is a multiple of $r$ as well. However since $m_1$ and $m_2$ are coprime, $r $ can only be 1. Note
that this is effectively a proof of existence since such smallest $r$ must exist as everything here is
finite. $\blacksquare$

Now if $d\nmid a_1 - a_2$, then we
can already claim that the pair of congruent equations have no solution.
If otherwise, we can multiply both sides of $\eqref{eq:2}$ by $(a_2 - a_1)/d$ to get $\eqref{eq:1}$. For equation sets that
contain 3 or more equations, we can process and merge two of them at a
time

Coding time!

<figure class="highlight c++">
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td class="gutter"><pre><code>1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19</code></pre></td>
<td class="code"><pre><code>typedef long long ll;
//extended euler's algorithm
void gcd(ll a, ll b, ll& d, ll& x, ll& y){
   if(!b){d  = a; x = 1; y = 0;}
   else {gcd(b, a%b, d, y, x); y -= (a/b)*x;}
}

ll china(int n, ll* a, ll* m){
  ll d,y,x = 0;
    rep(i,0,n-1){
      gcd(m[i],m[i+1],d,x,y);
        if((a[i+1] - a[i])%d!=0) return -1;
        a[i+1] = a[i]+((x*((a[i+1] - a[i])/d))%(m[i+1]/d))*m[i];
     m[i+1] = m[i]*(m[i+1]/d);
        a[i+1] = a[i+1]%m[i+1];
  }
    ll M = m[n-1];
   return (a[n-1]+M)%M;
}</code></pre></td>
</tr>
</tbody>
</table>
</figure>

The extended Euler's algorithm can be implemented by just two lines
of C++, pretty surprising, isn't it? One last thing to note, as there is
a 10\^18 numeric limit in most competitive programming contest, we need
to handle the overflow problem using $c(a\pmod{b})\equiv ca \pmod{cb}$ in the
following line of code

<figure class="highlight c++">
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td class="gutter"><pre><code>1</code></pre></td>
<td class="code"><pre><code>a[i+1] = a[i]+((x*((a[i+1] - a[i])/d))%(m[i+1]/d))*m[i];</code></pre></td>
</tr>
</tbody>
</table>
</figure>

That's it, happy coding until next time!

###### Reference

[[Tutorial] Chinese
Remainder Theorem - Codeforces](https://codeforces.com/blog/entry/61290){:rel="noopener" target="_blank"}
