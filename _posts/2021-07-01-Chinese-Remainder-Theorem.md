---
title: 'Chinese Remainder Theorem'
date: 2021-07-01
permalink: /posts/2021/07/chinese-remainder-theorem/
tags:
  - Competitive Programming
  - Chinese Remainder Theorem
---

\$\$
\\begin{equation}
\\def\\pr{\\text{\\rm pr}}
\\def\\sec{\\text{\\rm sect}}
\\def\\R{\\mathbb{R}}
\\def\\N{\\mathbb{N}}
\\def\\C{\\mathbb{C}}
\\def\\Z{\\mathbb{Z}}
\\def\\H{\\mathcal{H}}
\\def\\beq{\\begin{equation}}
\\def\\endeq{\\end{equation}}
\\def\\lesim{\\lesssim}
\\def\\mc{\\mathcal}
\\def\\h{\\mathcal{H}}
\\newcommand{\\bram}\[1\]{\\begin{bmatrix}#1\\end{bmatrix}}
\\def\\mn{M\^{(n)}}
\\def\\lam{\\lambda}
\\def\\wide{\\widehat}
\\def\\uk{u\^{(k_0)}}
\\def\\uo{u\^{(0)}}
\\def\\pj{P\^{(2)}}
\\def\\pii{P\^{(1)}}
\\def\\pc{P\^{Cone}}
\\def\\tx{\\tilde x}
\\DeclareMathOperator{\\re}{Re}
\\DeclareMathOperator{\\sgn}{sgn}
\\def\\cplus{c\\ci+}
\\def\\cmin{c\\ci-}
\\def\\cplusmin{c\\ci\\pm}
\\def\\chiplus{\\chi\\ci+}
\\def\\chimin{\\chi\\ci-}
\\def\\chiplusmin{\\chi\\ci\\pm}
\\def\\psiplus{\\psi\\ci+}
\\def\\psimin{\\psi\\ci-}
\\def\\psiplusmin{\\psi\\ci\\pm}
\\def\\sigmaplus{\\sigma\\ci+}
\\def\\sigmamin{\\sigma\\ci-}
\\def\\sigmaplusmin{\\sigma\\ci\\pm}
\\def\\bbone{\\mathbbm 1}
\\newcommand{\\dil}{\\text{\\rm Dil}}
\\newcommand{\\spec}{\\operatorname{spec}}
\\newcommand{\\ls}{\\lesssim}
\\newcommand{\\sL}{\\mathscr L}
\\newcommand{\\sJ}{\\mathscr J}
\\newcommand{\\sK}{\\mathscr K}
\\newcommand{\\wh}{\\widehat}
\\newcommand{\\wt}{\\widetilde}
\\newcommand{\\A}{\\mathcal A}
\\newcommand{\\E}{\\mathcal E}
\\newcommand{\\F}{\\mathcal F}
\\newcommand{\\D}{\\mathcal D}
\\newcommand{\\K}{\\mathcal K}
\\newcommand{\\QQ}{\\mathcal Q}
\\newcommand{\\RR}{\\mathcal R}
\\newcommand{\\f}\[2\]{\\frac{#1}{#2}}
\\newcommand{\\term}{c(z,r)F\^\\Psi_r(\\cdot-z)}
\\newcommand{\\norm}\[1\]{ \\left\| #1 \\right\| }
\\newcommand{\\abs}\[1\]{ \\left\| #1 \\right\| }
\\newcommand{\\Norm}\[1\]{ \\left\\\| #1 \\right\\\| }
\\newcommand{\\iff}{\\Leftrightarrow}
\\newcommand{\\set}\[1\]{ \\left\\{ #1 \\right\\} }
\\newcommand{\\Be}{\\begin{equation}}
\\newcommand{\\Ee}{\\end{equation}}
\\newcommand{\\Bm}{\\begin{multline}}
\\newcommand{\\Em}{\\end{multline}}
\\newcommand{\\Bea}{\\begin{eqnarray}}
\\newcommand{\\Eea}{\\end{eqnarray}}
\\newcommand{\\Beas}{\\begin{eqnarray\*}}
\\newcommand{\\Eeas}{\\end{eqnarray\*}}
\\newcommand{\\Benu}{\\begin{enumerate}}
\\newcommand{\\Eenu}{\\end{enumerate}}
\\newcommand{\\Bi}{\\begin{itemize}}
\\newcommand{\\Ei}{\\end{itemize}}
\\def\\conv{\\text{Conv}}
\\def\\tp{\\tilde p}
\\def\\tq{\\tilde q}
\\def\\crit{\\text{\\rm cr}}
\\def\\sparse{\\text{\\rm sp}}
\\def\\dyad{\\text{\\rm dyad}}
\\def\\mart{\\text{dyad}}
\\def\\intslash{\\rlap{\\kern .32em \$\\mspace {.5mu}\\backslash\$ }\\int}
\\def\\qsl{\\rlap{\\kern .32em \$\\mspace {.5mu}\\backslash\$ }\\int\_{Q_x}}
\\def\\Re{\\operatorname{Re\\,}}
\\def\\Im{\\operatorname{Im\\,}}
\\def\\mx
\\def\\mn
\\def\\vth{\\vartheta}
\\def\\rn{\\rr\^{n}}
\\def\\rr{\\mathbb R}
\\def\\Q{\\mathbb Q}
\\def\\N{\\mathbb N}
\\def\\complex{\\mathbb C}
\\def\\emph#1{\\it #1 }
\\def\\diam{\\text{\\rm diam}}
\\def\\osc{\\text{\\rm osc}}
\\def\\ffB{\\mathcal B}
\\def\\seq{\\subseteq}
\\def\\Ga{\\Gamma}
\\def\\ga{\\gamma}
\\def\\Th{\\Theta}
\\def\\prd{\\text{\\it prod}}
\\def\\parab{\\text{\\it parabolic}}
\\def\\eg{\\it e.g. }
\\def\\cf{\\it cf}
\\def\\Rn{\\mathbb R\^n}
\\def\\Rd{\\mathbb R\^d}
\\def\\sgn{\\text{\\rm sign }}
\\def\\rank{\\text{\\rm rank }}
\\def\\corank{\\text{\\rm corank }}
\\def\\coker{\\text{\\rm Coker }}
\\def\\loc{\\text{\\rm loc}}
\\def\\spec{\\text{\\rm spec}}
\\def\\comp{\\text{comp}}
\\def\\Coi{C\^\\infty_0}
\\def\\dist{\\text{\\it dist}}
\\def\\diag{\\text{\\rm diag}}
\\def\\supp{text{\\rm supp}}
\\def\\rad{\\text{\\it rad}}
\\def\\sph{\\text{sph}}
\\def\\Lip{\\text{\\rm Lip}}
\\def\\ev{\\text{\\rm ev}}
\\def\\odd{\\text{\\rm odd}}
\\def\\inn#1#2{\\langle#1,#2\\rangle}
\\def\\biginn#1#2{\\big\\langle#1,#2\\big\\rangle}
\\def\\rta{\\rightarrow}
\\def\\lta{\\leftarrow}
\\def\\noi{\\noindent}
\\def\\lcontr{\\rfloor}
\\newcommand{\\pmtx}\[1\]{\\begin{pmatrix}#1\\end{pmatrix}}
\\def\\meas{\\text{\\rm meas}}
\\def\\card{\\text{\\rm card}}
\\def\\lc{\\lesssim}
\\def\\gc{\\gtrsim}
\\def\\pv{\\text{\\rm p.v.}}
\\def\\a{\\alpha}
\\def\\alp{\\alpha} \\def\\Alp{\\Alpha}
\\def\\bet{\\beta}
\\def\\gam{\\gamma} \\def\\Gam{\\Gamma}
\\def\\del{\\delta} \\def\\Del{\\Delta}
\\def\\eps{\\varepsilon}
\\def\\ep{\\epsilon}
\\def\\zet{\\zeta}
\\def\\tet{\\theta} \\def\\Tet{\\Theta}
\\def\\iot{\\iota}
\\def\\kap{\\kappa}
\\def\\ka{\\kappa}
\\def\\lam{\\lambda} \\def\\Lam{\\Lambda}
\\def\\la{\\lambda} \\def\\La{\\Lambda}
\\def\\sig{\\sigma} \\def\\Sig{\\Sigma}
\\def\\si{\\sigma} \\def\\Si{\\Sigma}
\\def\\vphi{\\varphi}
\\def\\ome{\\omega} \\def\\Ome{\\Omega}
\\def\\om{\\omega}
\\def\\fA{\\mathfrak {A}}
\\def\\fB{\\mathfrak {B}}
\\def\\fC{\\mathfrak {C}}
\\def\\fD{\\mathfrak {D}}
\\def\\fE{\\mathfrak {E}}
\\def\\fF{\\mathfrak {F}}
\\def\\fG{mathfrak {G}}
\\def\\fH{\\mathfrak {H}}
\\def\\fI{\\mathfrak {I}}
\\def\\fJ{\\mathfrak {J}}
\\def\\fK{\\mathfrak {K}}
\\def\\fL{\\mathfrak {L}}
\\def\\fM{\\mathfrak {M}}
\\def\\fN{\\mathfrak {N}}
\\def\\fO{\\mathfrak {O}}
\\def\\fP{\\mathfrak {P}}
\\def\\fQ{\\mathfrak {Q}}
\\def\\fR{\\mathfrak {R}}
\\def\\fS{\\mathfrak {S}}
\\def\\fT{\\mathfrak {T}}
\\def\\fU{\\mathfrak {U}}
\\def\\fV{\\mathfrak {V}}
\\def\\fW{\\mathfrak {W}}
\\def\\fX{\\mathfrak {X}}
\\def\\fY{\\mathfrak {Y}}
\\def\\fZ{\\mathfrak {Z}}
\\def\\fa{\\mathfrak {a}}
\\def\\fb{\\mathfrak {b}}
\\def\\fc{\\mathfrak {c}}
\\def\\fd{\\mathfrak {d}}
\\def\\fe{\\mathfrak {e}}
\\def\\ff{\\mathfrak {f}}
\\def\\fg{\\mathfrak {g}}
\\def\\fh{\\mathfrak {h}}
\\def\\fj{\\mathfrak {j}}
\\def\\fk{\\mathfrak {k}}
\\def\\fl{\\mathfrak {l}}
\\def\\fn{\\mathfrak {n}}
\\def\\fo{\\mathfrak {o}}
\\def\\fq{\\mathfrak {q}}
\\def\\fr{\\mathfrak {r}}
\\def\\fs{\\mathfrak {s}}
\\def\\ft{\\mathfrak {t}}
\\def\\fu{\\mathfrak {u}}
\\def\\fv{\\mathfrak {v}}
\\def\\fw{\\mathfrak {w}}
\\def\\fx{\\mathfrak {x}}
\\def\\fy{\\mathfrak {y}}
\\def\\fz{\\mathfrak {z}}
\\def\\bbA{\\mathbb {A}}
\\def\\bbB{\\mathbb {B}}
\\def\\bbC{\\mathbb {C}}
\\def\\bbD{\\mathbb {D}}
\\def\\bbE{\\mathbb {E}}
\\def\\bbF{\\mathbb {F}}
\\def\\bbG{\\mathbb {G}}
\\def\\bbH{\\mathbb {H}}
\\def\\bbI{\\mathbb {I}}
\\def\\bbJ{\\mathbb {J}}
\\def\\bbK{\\mathbb {K}}
\\def\\bbL{\\mathbb {L}}
\\def\\bbM{\\mathbb {M}}
\\def\\bbN{\\mathbb {N}}
\\def\\bbO{\\mathbb {O}}
\\def\\bbP{\\mathbb {P}}
\\def\\bbQ{\\mathbb {Q}}
\\def\\bbR{\\mathbb {R}}
\\def\\bbS{\\mathbb {S}}
\\def\\bbT{\\mathbb {T}}
\\def\\bbU{\\mathbb {U}}
\\def\\bbV{\\mathbb {V}}
\\def\\bbW{\\mathbb {W}}
\\def\\bbX{\\mathbb {X}}
\\def\\bbY{\\mathbb {Y}}
\\def\\bbZ{\\mathbb {Z}}
\\def\\cA{\\mathcal {A}}
\\def\\cB{\\mathcal {B}}
\\def\\cC{\\mathcal {C}}
\\def\\cD{\\mathcal {D}}
\\def\\cE{\\mathcal {E}}
\\def\\cF{\\mathcal {F}}
\\def\\cG{\\mathcal {G}}
\\def\\cH{\\mathcal {H}}
\\def\\cI{\\mathcal {I}}
\\def\\cJ{\\mathcal {J}}
\\def\\cK{\\mathcal {K}}
\\def\\cL{\\mathcal {L}}
\\def\\cM{\\mathcal {M}}
\\def\\cN{\\mathcal {N}}
\\def\\cO{\\mathcal {O}}
\\def\\cP{\\mathcal {P}}
\\def\\cQ{\\mathcal {Q}}
\\def\\cR{\\mathcal {R}}
\\def\\cS{\\mathcal {S}}
\\def\\cT{\\mathcal {T}}
\\def\\cU{\\mathcal {U}}
\\def\\cV{\\mathcal {V}}
\\def\\cW{\\mathcal {W}}
\\def\\cX{\\mathcal {X}}
\\def\\cY{\\mathcal {Y}}
\\def\\cZ{\\mathcal {Z}}
\\def\\tA{\\widetilde{A}}
\\def\\tB{\\widetilde{B}}
\\def\\tC{\\widetilde{C}}
\\def\\tD{\\widetilde{D}}
\\def\\tE{\\widetilde{E}}
\\def\\tF{\\widetilde{F}}
\\def\\tG{\\widetilde{G}}
\\def\\tH{\\widetilde{H}}
\\def\\tI{\\widetilde{I}}
\\def\\tJ{\\widetilde{J}}
\\def\\tK{\\widetilde{K}}
\\def\\tL{\\widetilde{L}}
\\def\\tM{\\widetilde{M}}
\\def\\tN{\\widetilde{N}}
\\def\\tO{\\widetilde{O}}
\\def\\tP{\\widetilde{P}}
\\def\\tQ{\\widetilde{Q}}
\\def\\tR{\\widetilde{R}}
\\def\\tS{\\widetilde{S}}
\\def\\tT{\\widetilde{T}}
\\def\\tU{\\widetilde{U}}
\\def\\tV{\\widetilde{V}}
\\def\\tW{\\widetilde{W}}
\\def\\tX{\\widetilde{X}}
\\def\\tY{\\widetilde{Y}}
\\def\\tZ{\\widetilde{Z}}
\\def\\tcA{\\widetilde{\\mathcal {A}}}
\\def\\tcB{\\widetilde{\\mathcal {B}}}
\\def\\tcC{\\widetilde{\\mathcal {C}}}
\\def\\tcD{\\widetilde{\\mathcal {D}}}
\\def\\tcE{\\widetilde{\\mathcal {E}}}
\\def\\tcF{\\widetilde{\\mathcal {F}}}
\\def\\tcG{\\widetilde{\\mathcal {G}}}
\\def\\tcH{\\widetilde{\\mathcal {H}}}
\\def\\tcI{\\widetilde{\\mathcal {I}}}
\\def\\tcJ{\\widetilde{\\mathcal {J}}}
\\def\\tcK{\\widetilde{\\mathcal {K}}}
\\def\\tcL{\\widetilde{\\mathcal {L}}}
\\def\\tcM{\\widetilde{\\mathcal {M}}}
\\def\\tcN{\\widetilde{\\mathcal {N}}}
\\def\\tcO{\\widetilde{\\mathcal {O}}}
\\def\\tcP{\\widetilde{\\mathcal {P}}}
\\def\\tcQ{\\widetilde{\\mathcal {Q}}}
\\def\\tcR{\\widetilde{\\mathcal {R}}}
\\def\\tcS{\\widetilde{\\mathcal {S}}}
\\def\\tcT{\\widetilde{\\mathcal {T}}}
\\def\\tcU{\\widetilde{\\mathcal {U}}}
\\def\\tcV{\\widetilde{\\mathcal {V}}}
\\def\\tcW{\\widetilde{\\mathcal {W}}}
\\def\\tcX{\\widetilde{\\mathcal {X}}}
\\def\\tcY{\\widetilde{\\mathcal {Y}}}
\\def\\tcZ{\\widetilde{\\mathcal {Z}}}
\\def\\tfA{\\widetilde{\\mathfrak {A}}}
\\def\\tfB{\\widetilde{\\mathfrak {B}}}
\\def\\tfC{\\widetilde{\\mathfrak {C}}}
\\def\\tfD{\\widetilde{\\mathfrak {D}}}
\\def\\tfE{\\widetilde{\\mathfrak {E}}}
\\def\\tfF{\\widetilde{\\mathfrak {F}}}
\\def\\tfG{\\widetilde{\\mathfrak {G}}}
\\def\\tfH{\\widetilde{\\mathfrak {H}}}
\\def\\tfI{\\widetilde{\\mathfrak {I}}}
\\def\\tfJ{\\widetilde{\\mathfrak {J}}}
\\def\\tfK{\\widetilde{\\mathfrak {K}}}
\\def\\tfL{\\widetilde{\\mathfrak {L}}}
\\def\\tfM{\\widetilde{\\mathfrak {M}}}
\\def\\tfN{\\widetilde{\\mathfrak {N}}}
\\def\\tfO{\\widetilde{\\mathfrak {O}}}
\\def\\tfP{\\widetilde{\\mathfrak {P}}}
\\def\\tfQ{\\widetilde{\\mathfrak {Q}}}
\\def\\tfR{\\widetilde{\\mathfrak {R}}}
\\def\\tfS{\\widetilde{\\mathfrak {S}}}
\\def\\tfT{\\widetilde{\\mathfrak {T}}}
\\def\\tfU{\\widetilde{\\mathfrak {U}}}
\\def\\tfV{\\widetilde{\\mathfrak {V}}}
\\def\\tfW{\\widetilde{\\mathfrak {W}}}
\\def\\tfX{\\widetilde{\\mathfrak {X}}}
\\def\\tfY{\\widetilde{\\mathfrak {Y}}}
\\def\\tfZ{\\widetilde{\\mathfrak {Z}}}
\\def\\Atil{\\widetilde A} \\def\\atil{\\tilde a}
\\def\\Btil{\\widetilde B} \\def\\btil{\\tilde b}
\\def\\Ctil{\\widetilde C} \\def\\ctil{\\tilde c}
\\def\\Dtil{\\widetilde D} \\def\\dtil{\\tilde d}
\\def\\Etil{\\widetilde E} \\def\\etil{\\tilde e}
\\def\\Ftil{\\widetilde F} \\def\\ftil{\\tilde f}
\\def\\Gtil{\\widetilde G} \\def\\gtil{\\tilde g}
\\def\\Htil{\\widetilde H} \\def\\htil{\\tilde h}
\\def\\Itil{\\widetilde I} \\def\\itil{\\tilde i}
\\def\\Jtil{\\widetilde J} \\def\\jtil{\\tilde j}
\\def\\Ktil{\\widetilde K} \\def\\ktil{\\tilde k}
\\def\\Ltil{\\widetilde L} \\def\\ltil{\\tilde l}
\\def\\Mtil{\\widetilde M} \\def\\mtil{\\tilde m}
\\def\\Ntil{\\widetilde N} \\def\\ntil{\\tilde n}
\\def\\Otil{\\widetilde O} \\def\\otil{\\tilde o}
\\def\\Ptil{\\widetilde P} \\def\\ptil{\\tilde p}
\\def\\Qtil{\\widetilde Q} \\def\\qtil{\\tilde q}
\\def\\Rtil{\\widetilde R} \\def\\rtil{\\tilde r}
\\def\\Stil{\\widetilde S} \\def\\stil{\\tilde s}
\\def\\Ttil{\\widetilde T} \\def\\ttil{\\tilde t}
\\def\\Util{\\widetilde U} \\def\\util{\\tilde u}
\\def\\Vtil{\\widetilde V} \\def\\vtil{\\tilde v}
\\def\\Wtil{\\widetilde W} \\def\\wtil{\\tilde w}
\\def\\Xtil{\\widetilde X} \\def\\xtil{\\tilde x}
\\def\\Ytil{\\widetilde Y} \\def\\ytil{\\tilde y}
\\def\\Ztil{\\widetilde Z} \\def\\ztil{\\tilde z}
\\def\\ahat{\\hat a} \\def\\Ahat{\\widehat A}
\\def\\bhat{\\hat b} \\def\\Bhat{\\widehat B}
\\def\\chat{\\hat c} \\def\\Chat{\\widehat C}
\\def\\dhat{\\hat d} \\def\\Dhat{\\widehat D}
\\def\\ehat{\\hat e} \\def\\Ehat{\\widehat E}
\\def\\fhat{\\hat f} \\def\\Fhat{\\widehat F}
\\def\\ghat{\\hat g} \\def\\Ghat{\\widehat G}
\\def\\hhat{\\hat h} \\def\\Hhat{\\widehat H}
\\def\\ihat{\\hat i} \\def\\Ihat{\\widehat I}
\\def\\jhat{\\hat j} \\def\\Jhat{\\widehat J}
\\def\\khat{\\hat k} \\def\\Khat{\\widehat K}
\\def\\lhat{\\hat l} \\def\\Lhat{\\widehat L}
\\def\\mhat{\\hat m} \\def\\Mhat{\\widehat M}
\\def\\nhat{\\hat n} \\def\\Nhat{\\widehat N}
\\def\\ohat{\\hat o} \\def\\Ohat{\\widehat O}
\\def\\phat{\\hat p} \\def\\Phat{\\widehat P}
\\def\\qhat{\\hat q} \\def\\Qhat{\\widehat Q}
\\def\\rhat{\\hat r} \\def\\Rhat{\\widehat R}
\\def\\shat{\\hat s} \\def\\Shat{\\widehat S}
\\def\\that{\\hat t} \\def\\That{\\widehat T}
\\def\\uhat{\\hat u} \\def\\Uhat{\\widehat U}
\\def\\vhat{\\hat v} \\def\\Vhat{\\widehat V}
\\def\\what{\\hat w} \\def\\What{\\widehat W}
\\def\\xhat{\\hat x} \\def\\Xhat{\\widehat X}
\\def\\yhat{\\hat y} \\def\\Yhat{\\widehat Y}
\\def\\zhat{\\hat z} \\def\\Zhat{\\widehat Z}
\\def\\be#1{\\begin{equation}\\label{ #1}}
\\def\\endeq{\\end{equation}}
\\def\\endal{\\end{align}}
\\def\\bas{\\begin{align\*}}
\\def\\eas{\\end{align\*}}
\\def\\bi{\\begin{itemize}}
\\def\\ei{\\end{itemize}}
\\def\\eps{\\varepsilon}
\\def\\textbf#1{\\bf #1}
\\def\\into{\\hookrightarrow}
\\newcommand{\\inf}{\\infty}
\\newcommand{\\os}\[2\]{\\overset{#1}{#2}}
\\newcommand{\\ms}{(X, \\cM, \\mu)}
\\newcommand{\\salg}{\\sig\\text{-algebra}}
\\newcommand{\\ol}\[1\]{\\overline{#1}}
\\newcommand{\\bij}{\\mathrel{\\hookrightarrow\\hspace{-1.8ex}\\to}}
\\newcommand{\\onto}{\\twoheadrightarrow}
\\newcommand{\\id}{\\text{id}}
\\newcommand{\\Stab}{\\text{Stab}}
\\def \\bl {\\backslash}
\\def \\sfin {\\sig\\text{-finite}}
\\def \\mum {\\mu\\text{-measurable}}
\\def \\emps {\\varnothing}
\\newcommand{\\m}\[1\]{\\boldsymbol{#1}}
\\newcommand{\\bs}\[1\]{\\boldsymbol{#1}}
\\newcommand{\\Inf}{\\text{inf}}
\\newcommand{\\wb}\[1\]{\\overline{#1}}
\\newcommand{\\lto}{\\longrightarrow}
\\newcommand{\\todo}\[1\]{\\bf\\color{red}{\[ToDo\]
\\text{#1}}}
\\newcommand{\\char}\[1\]{\\cX\_{#1}}
\\newcommand{\\fp}{f\^+}
\\newcommand{\\fm}{f\^-}
\\newcommand{\\infm}{\\text{inf}}
\\newcommand{\\onorm}\[1\]{\\Norm{#1}\_1}
\\newcommand{\\tnorm}\[1\]{\\Norm{#1}\_2}
\\newcommand{\\infn}\[1\]{\\Norm{#1}\_\\inf}
\\newcommand{\\pnorm}\[1\]{\\Norm{#1}\_p}
\\newcommand{\\End}{\\text{End}}
\\newcommand{\\Ob}{\\text{Ob}}
\\newcommand{\\Hom}{\\text{Hom}}
\\newcommand{\\intall}{\\int\_{-\\inf}\^{\\inf}}
\\newcommand{\\intpmpi}{\\int\_{-\\pi}\^{\\pi}}
\\newcommand{\\div}{\\bigr\|}
\\newcommand{\\when}{\\biggr\|}
\\def \\bsp {\\begin{split}}
\\def \\esp {\\end{split}}
\\def \\bc {\\begin{cases}}
\\def \\ec {\\end{cases}}
\\newcommand{\\sech}{\\text{sech}}
\\newcommand{\\vectk}{\\text{Vect}\_\\text{k}}
\\newcommand{\\top}{\\text{Top}}
\\newcommand{\\grp}{\\text{Grp}}
\\newcommand{\\pathx}{\\text{Paths}\_X}
\\newcommand{\\from}{\\leftarrow}
\\newcommand{\\lfrom}{\\longleftarrow}
\\newcommand{\\tofrom}\[2\]{\\os{\\xrightarrow{#1}}{\\xleftarrow\[#2\]{}}}
\\newcommand{\\sym}{\\text{Sym}}
\\newcommand{\\Set}{\\text{Set}}
\\newcommand{\\zn}{\\Z/n\\Z}
\\newcommand{\\Mor}{\\text{Mor}}
\\newcommand{\\acton}{\\circlearrowright}
\\DeclareMathOperator{\\tr}{Tr}
\\newcommand{\\par}{\\partial}
\\newcommand{\\Fun}{\\text{Fun}}
\\newcommand{\\triv}{\\text{triv}}
\\newcommand{\\zmnz}\[1\]{\\Z/{#1}\\Z}
\\newcommand{\\tl}{\\triangleleft}
\\newcommand{\\paren}\[1\]{\\left({#1}\\right)}
\\newcommand{\\ceil}\[1\]{\\lceil{#1}\\rceil}
\\newcommand{\\floor}\[1\]{\\lfloor{#1}\\rfloor}
\\newcommand{\\mod}{\\textrm{mod}}
\\newcommand{\\ndiv}{\\nmid}
\\end{equation}
\$\$

I recently decided to pick up competitive programming, not only
because I enjoy programming, but also because this is a fail safe for my
academic career. With the tension between China and US rises, any
Chinese research personnel in the US is bound to be persecuted in one
way or another (it already begins with the visa application). It will be
increasingly risky to put all the eggs in one basket. And the recent [Wenhua
Jiang Incident](https://www.universityworldnews.com/post.php?story=20210611084120155){rel="noopener" target="_blank"} further dims the light on the path to tenure in China
for many researchers. So in short, doing competitive programming is an
act of interest (pun intended).

So much gibberish, today we are going to talk about Chinese Remainder
Theorem, which basically says that given a set of coprime integers, and
we know the remainders of an unknown integer modulo those coprime
numbers, then the smallest such unknown number can be uniquely
determined. For a rigorous definition, see [wiki](https://en.wikipedia.org/wiki/Chinese_remainder_theorem){rel="noopener" target="_blank"}.
The proof is quite simply, say the set of coprime numbers are \$n_1, n_2, \\dots, n_k\$, and \$N = \\Pi_i n_i\$. And the aforementioned
remainders are \$r_1, r_2, \\dots,
r_k\$. We only consider integers in the range \$\[1, N\]\$. The key observation is that if
two *different* numbers have the same set of remainders, the
absolute difference between them will be divisible by all \$n_i\$ s, and since the difference is capped
by \$N-1\$, it is zero, contradiction!
Therefore a one-to-one correspondence can be established between each
integer within that range and a set of all possible remainders. Note
that the range of each \$r_i\$ is \$\[0, r_i-1\]\$, so both sides have the same
cardinality.

Now let\'s look at implementation of this theorem in competitive
programming. An example problem is [here](https://atcoder.jp/contests/abc193/tasks/abc193_e){rel="noopener" target="_blank"}. So
the problem is to solve the following set of congruence equations \$\$
x \\equiv a_1 \\pmod{m_1}\\\\
x\\equiv a_2 \\pmod{m_2}
\$\$ which is equivalent to \$\$
x = a_1+n_1 m_1 = a_2+n_2m_2
\$\$ for some integer \$n_1\$ and
\$n_2\$, i.e. \$\$
\\beq
a_2 - a_1 = n_1m_1 - n_2m_2 \\tag{1} \\label{eq:1}
\\end{equation}
\$\$ We can use extended Euclidean algorithm to solve for \$n_i\$ given \$m_i\$ in the following equation \$\$
\\beq
n_1m_1 - n_2m_2 = \\gcd(m_1, m_2) := d \\tag{2}\\label{eq:2}
\\endeq
\$\$ *Detour (please skip at will)*: There is a proof of
existence of an integer solution that I really like about the above
equation. Since we can divide both sides by \$\\gcd(m_1, m_2)\$, we can just deal with the
case \$n_1m_1 - n_2m_2 = 1\$ where
\$m_1\$ and \$m_2\$ are coprime to each other. Now here
is the clever proof: Let \$r\$ be the
smallest positive integer such that \$n_1m_1 -
n_2m_2 = r\$ has an integer solution. And we can express \$m_1\$ as multiple of \$r\$ plus a remainder term, i.e. \$m_1 = q_1r+r_1\$. So the equation becomes
\$\$
n_1m_1 - n_2m_2 = r = (m_1 - r_1)/q_1
\$\$ Some algebra shows that \$(1-q_1n_1)m_1+n_2q_1m_2 = r_1\$, note that
\$r_1\$, as a remainder of division by
\$r\$, is strictly smaller than \$r\$. So there is only one possibility:
\$r_1 = 0\$. So \$m_1\$ is actually a multiple of \$r\$ ! By symmetry, \$m_2\$ is a multiple of \$r\$ as well. However since \$m_1\$ and \$m_2\$ are coprime, \$r \$ can only be 1. Note
that this is effectively a proof of existence since such smallest \$r\$ must exist as everything here is
finite. \$\\blacksquare\$

Now if \$d\\ndiv a_1 - a_2\$, then we
can already claim that the pair of congruent equations have no solution.
If otherwise, we can multiply both sides of \$\\eqref{eq:2}\$ by \$(a_2 - a_1)/d\$ to get \$\\eqref{eq:1}\$. For equation sets that
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

The extended Euler\'s algorithm can be implemented by just two lines
of C++, pretty surprising, isn\'t it? One last thing to note, as there is
a 10\^18 numeric limit in most competitive programming contest, we need
to handle the overflow problem using \$c(a\\pmod{b})\\equiv ca \\pmod{cb}\$ in the
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

That\'s it, happy coding until next time!

###### Reference

\[[Tutorial\] Chinese
Remainder Theorem - Codeforces](https://codeforces.com/blog/entry/61290){rel="noopener" target="_blank"}