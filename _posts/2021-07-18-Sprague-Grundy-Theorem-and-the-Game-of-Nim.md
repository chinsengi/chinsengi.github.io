---
title: 'Sprague-Grundy Theorem and the Game of Nim'
date: 2021-07-18
permalink: /posts/2021/07/sprague-grundy-theorem-and-the-game-of-nim/
tags:
  - Competitive Programming
  - Game Theory
  - Combinatorics
---


Halo, recently I reacquainted myself with the Sprague-Grundy theorem
and would like to introduce the gist of it. I think [Wikipedia](https://en.wikipedia.org/wiki/Sprague%E2%80%93Grundy_theorem){:rel="noopener" target="_blank"}
does a great job explaining the detailed proof, but I would like to fill
in some gaps and provide some intuitions. It is recommended to read
about the rule of the game of nim (and the wiki page if you are
interested in technical details) before reading.

Basically the theorem says that every impartial game is equivalent to
a game of nim with a pile of $n$
stones. The number $n$ is called the
Grundy number of the impartial game. Now there are two things to
explain.

1.  impartial game means that both players of the game have the same set
    of operations given a fixed position of the game. Chess and Go are not
    impartial games, because one player can only move or place pieces that
    have the same color (either black or white).
2.  What does it mean that two games $G$ and $G'$are \"equivalent\"? One may give a
    definition stating that if one game has a winning strategy for the
    player that goes first (or the second player), so does the equivalent
    game and vice versa. However, having this condition is not enough.
    Consider any game that has a winning strategy for the second player.
    Clearly every nim game with non-zero number of stones is equivalent to
    that game, making Grundy number an ill-defined number. Therefore, we
    additionally require that the combined games of $G+H$ and $G'+H$ have winning strategies for the
    same player for any given impartial game $H$.

Now the Sprague-Grundy theorem gives a recursive definition of what
the Grundy number of any given impartial game is: Suppose we can go from
the current position $G_0$ of the
game to $k$ other positions, $\{G_1, G_2, \dots, G_k\}$, and each of
$G_i$ is equivalent to the game of
nim with $n_i$ stones. Then $G_0$ is equivalent to the game of nim with
$n_0$ stones given by $$
n_0 = \text{mex}(n_1, n_2,\dots, n_k)
$$ Here $\text{mex}(A)$ for
some non-negative integer set $A$ is
the smallest non-negative integer that is not in $A$.

This is useful, but not that useful, consider a game of nim consists
of multiple heaps of stones, where i-th heap has $n_i$ stones. How do we determine the
Grundy number and whether we have a winning strategy for the game? If we
still use the recursive definition, we will have $\prod n_i$ states to calculate, which can
be huge. This is where bit xor operation comes to rescue!

In the following we will consider just one quantity: the xor of all
numbers of stones in each heap, i.e. $Q =
\bigoplus n_i$. Let's consider the game bottom-up. Which
position will the losing player face at the end? Obviously, the position
where no stone is left, and $Q = \bigoplus 0
= 0$. It turns out that the winning strategy is to keep leaving
the opponent with a position where $Q =
0$! In order to show that, we have to show two things

1.  If right now $Q = 0$, any valid
    operation will lead to a position where $Q\neq 0$.
2.  If right now $Q\neq 0$, there is
    always a valid operation that can lead to a position where $Q = 0$

The first statement is easy. Consider you are moving the $k$-th heap. Since we have $Q = (\bigoplus_{i\neq k} n_i) \oplus n_k =
0$, i.e. $\bigoplus_{i\neq k} n_i =
n_k$ right now, changing the number of stones in heap $k$ will make $Q$ not equal to 0.

The second statement: First we convert everything into numbers with
base of 2 and fill in zeros so that every $n_i$ has the same length. Consider the
left-most digit of $Q$ that is not 0,
say it is $m$-th digit from the left.
Since $Q$ is 1 at $m$, we can pick $n_k$ such that $n_k$ has 1 at that position. Now since
$\bigoplus_{i\neq k} n_i$ has 0 at
that position, we can set $n_k$ to
$\bigoplus_{i\neq k} n_i$. To see
that this value is strictly smaller than $n_k$, simply note that both have the same
$1$st to $(m-1)$-th digits.

So the winning strategy exists for the first player if we start off
with a non-zero $Q$, and for the
second player if we start off with $Q =
0$. One more thing: how do we show that the Grundy number is
exactly $Q$, instead of any non-zero
number in the case of non-zero $Q$?
This actually follows from the conclusion of the theorem. Let's consider
a simplified case where there are only two heaps. Situations where there
are 3 or more heaps can be reduced by merging two of them at a time.
Following the notation convention in Wikipedia, we denote a single heap
nim game of size $n$ as $\{\*n\}$. We want to show that $\{\*a\}+\{\*b\}\equiv \{\*(a\oplus
b)\}$, i.e. the combined game of two single heap nim games is
equivalent to one single heap nim game in the sense defined in the
theorem. From the theorem we know that 
$$
\{*a\}+\{*b\}\equiv \text{mex}\left(\bigcup_{i = 0}^{a-1}
(\{*i\}+\{*b\})\cup\bigcup_{j =
0}^{b-1}(\{*a\}+\{*j\})\right):=\text{mex}(A)
$$ 
By induction on $a+b$, we
assume that $\{\*i\}+\{\*b\}\equiv
\{\*(i\oplus b)\}$ and the inductive hypothesis holds. To see that the right hand
side is exactly $a\oplus b$, we note
that 

$$
\begin{split}
i\oplus b\oplus a\oplus b &= i\oplus a \neq 0\\
a\oplus j\oplus a\oplus b &= j\oplus b \neq 0\\
i\oplus b\oplus i'\oplus b &= i\oplus i'\\
a\oplus j\oplus a\oplus j' &= j\oplus j'
\end{split}
$$ 

i.e. no element in $A$ is
equal to $a\oplus b$. Moreover, there
are at least $\max(a,b)$ different
elements in $A$. The result follows,
because $a\oplus b \leq \max(a,b)$.
It's left to check the base cases, but they are trivial, so we are done.
$\blacksquare$

Now the Grundy theorem is much more practically useful, since it can
deal with games that have multiple component games efficiently. Remember
that each component game is equivalent to a single heap nim game!

Coding time! [Here](https://atcoder.jp/contests/abc206/tasks/abc206_f){:rel="noopener" target="_blank"} is a
sample problem. Consider the game to be played on interval $[1,100]$, and choosing an interval results
in a position that can be split into two component games. For each
position we can apply the bit xor operation to get the Grundy number.
Applying the mex function to Grundy numbers of all positions gives the
answer.

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
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40</code></pre></td>
<td class="code"><pre><code>#include<bits/stdc++.h>
using namespace std;
#define rep(i,s,n) for(int i = s; i < n; i++)
   
int T; int N; typedef pair<int, int> ii;
vector<ii> intervals;
const int maxn = 105;
int dp[maxn][maxn];

int recur(int st, int end){
    if(st>=end) return dp[st][end] = 0;
 if(dp[st][end]!=-1) return dp[st][end];
    int all[maxn]; memset(all,0,sizeof all);
 for(auto& p : intervals)if(p.first>=st&& p.second<=end){
        int a = recur(st, p.first);
       int b = recur(p.second, end);
     int res = a^b; // merge two component games
        if(res<maxn) all[res] = 1;
   }
    rep(i,0,maxn)if(all[i]==0){ // calculate the mex
     return dp[st][end] = i;
 }
}
    
int main(){
 cin>>T;
    while(T--){
     cin>>N;
        intervals.clear();
     rep(i,0,N) {
           int l,r;cin>>l>>r;
          intervals.push_back({l,r});
        }
        memset(dp, -1, sizeof dp);
        if(recur(1,100)!=0)cout<<"Alice"<<endl;
       else cout<<"Bob"<<endl;
 }
}
    </code></pre></td>
</tr>
</tbody>
</table>
</figure>
