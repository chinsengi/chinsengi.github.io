---
title: 'Sprague-Grundy Theorem and the Game of Nim'
date: 2021-07-18
permalink: /posts/2021/07/sprague-grundy-theorem-and-the-game-of-nim/
tags:
  - Competitive Programming
  - Game Theory
  - Combinatorics
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

Halo, recently I reacquainted myself with the Sprague-Grundy theorem
and would like to introduce the gist of it. I think [Wikipedia](https://en.wikipedia.org/wiki/Sprague%E2%80%93Grundy_theorem){rel="noopener" target="_blank"}
does a great job explaining the detailed proof, but I would like to fill
in some gaps and provide some intuitions. It is recommended to read
about the rule of the game of nim (and the wiki page if you are
interested in technical details) before reading.

Basically the theorem says that every impartial game is equivalent to
a game of nim with a pile of \$n\$
stones. The number \$n\$ is called the
Grundy number of the impartial game. Now there are two things to
explain.

1.  impartial game means that both players of the game have the same set
    of operations given a fixed position of the game. Chess and Go are not
    impartial games, because one player can only move or place pieces that
    have the same color (either black or white).
2.  What does it mean that two games \$G\$ and \$G\'\$are \"equivalent\"? One may give a
    definition stating that if one game has a winning strategy for the
    player that goes first (or the second player), so does the equivalent
    game and vice versa. However, having this condition is not enough.
    Consider any game that has a winning strategy for the second player.
    Clearly every nim game with non-zero number of stones is equivalent to
    that game, making Grundy number an ill-defined number. Therefore, we
    additionally require that the combined games of \$G+H\$ and \$G\'+H\$ have winning strategies for the
    same player for any given impartial game \$H\$.

Now the Sprague-Grundy theorem gives a recursive definition of what
the Grundy number of any given impartial game is: Suppose we can go from
the current position \$G_0\$ of the
game to \$k\$ other positions, \$\\set{G_1, G_2, \\dots, G_k}\$, and each of
\$G_i\$ is equivalent to the game of
nim with \$n_i\$ stones. Then \$G_0\$ is equivalent to the game of nim with
\$n_0\$ stones given by \$\$
n_0 = \\text{mex}(n_1, n_2,\\dots, n_k)
\$\$ Here \$\\text{mex}(A)\$ for
some non-negative integer set \$A\$ is
the smallest non-negative integer that is not in \$A\$.

This is useful, but not that useful, consider a game of nim consists
of multiple heaps of stones, where i-th heap has \$n_i\$ stones. How do we determine the
Grundy number and whether we have a winning strategy for the game? If we
still use the recursive definition, we will have \$\\prod n_i\$ states to calculate, which can
be huge. This is where bit xor operation comes to rescue!

In the following we will consider just one quantity: the xor of all
numbers of stones in each heap, i.e. \$Q =
\\bigoplus n_i\$. Let\'s consider the game bottom-up. Which
position will the losing player face at the end? Obviously, the position
where no stone is left, and \$Q = \\bigoplus 0
= 0\$. It turns out that the winning strategy is to keep leaving
the opponent with a position where \$Q =
0\$! In order to show that, we have to show two things

1.  If right now \$Q = 0\$, any valid
    operation will lead to a position where \$Q\\neq 0\$.
2.  If right now \$Q\\neq 0\$, there is
    always a valid operation that can lead to a position where \$Q = 0\$

The first statement is easy. Consider you are moving the \$k\$-th heap. Since we have \$Q = (\\bigoplus\_{i\\neq k} n_i) \\oplus n_k =
0\$, i.e. \$\\bigoplus\_{i\\neq k} n_i =
n_k\$ right now, changing the number of stones in heap \$k\$ will make \$Q\$ not equal to 0.

The second statement: First we convert everything into numbers with
base of 2 and fill in zeros so that every \$n_i\$ has the same length. Consider the
left-most digit of \$Q\$ that is not 0,
say it is \$m\$-th digit from the left.
Since \$Q\$ is 1 at \$m\$, we can pick \$n_k\$ such that \$n_k\$ has 1 at that position. Now since
\$\\bigoplus\_{i\\neq k} n_i\$ has 0 at
that position, we can set \$n_k\$ to
\$\\bigoplus\_{i\\neq k} n_i\$. To see
that this value is strictly smaller than \$n_k\$, simply note that both have the same
\$1\$st to \$(m-1)\$-th digits.

So the winning strategy exists for the first player if we start off
with a non-zero \$Q\$, and for the
second player if we start off with \$Q =
0\$. One more thing: how do we show that the Grundy number is
exactly \$Q\$, instead of any non-zero
number in the case of non-zero \$Q\$?
This actually follows from the conclusion of the theorem. Let\'s consider
a simplified case where there are only two heaps. Situations where there
are 3 or more heaps can be reduced by merging two of them at a time.
Following the notation convention in Wikipedia, we denote a single heap
nim game of size \$n\$ as \$\\set{\*n}\$. We want to show that \$\\set{\*a}+\\set{\*b}\\equiv \\set{\*(a\\oplus
b)}\$, i.e. the combined game of two single heap nim games is
equivalent to one single heap nim game in the sense defined in the
theorem. From the theorem we know that \$\$
\\set{\*a}+\\set{\*b}\\equiv \\text{mex}\\left(\\bigcup\_{i = 0}\^{a-1}
(\\set{\*i}+\\set{\*b})\\cup\\bigcup\_{j =
0}\^{b-1}(\\set{\*a}+\\set{\*j})\\right):=\\text{mex}(A)
\$\$ By induction on \$a+b\$, we
assume that \$\\set{\*i}+\\set{\*b}\\equiv
\\set{\*(i\\oplus b)}\$ and \$+ \$ holds. To see that the right hand
side is exactly \$a\\oplus b\$, we note
that \$\$
\\bsp
i\\oplus b\\oplus a\\oplus b &= i\\oplus a \\neq 0\\\\
a\\oplus j\\oplus a\\oplus b &= j\\oplus b \\neq 0\\\\
i\\oplus b\\oplus i\'\\oplus b &= i\\oplus i\'\\\\
a\\oplus j\\oplus a\\oplus j\' &= j\\oplus j\'
\\esp
\$\$ i.e. no element in \$A\$ is
equal to \$a\\oplus b\$. Moreover, there
are at least \$\\max(a,b)\$ different
elements in \$A\$. The result follows,
because \$a\\oplus b \\leq \\max(a,b)\$.
It\'s left to check the base cases, but they are trivial, so we are done.
\$\\blacksquare\$

Now the Grundy theorem is much more practically useful, since it can
deal with games that have multiple component games efficiently. Remember
that each component game is equivalent to a single heap nim game!

Coding time! [Here](https://atcoder.jp/contests/abc206/tasks/abc206_f){rel="noopener" target="_blank"} is a
sample problem. Consider the game to be played on interval \$\[1,100\]\$, and choosing an interval results
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