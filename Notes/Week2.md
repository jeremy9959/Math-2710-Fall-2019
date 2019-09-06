% Math 2710
% Sep 2-6

# Some catch-up from prior classes

## Two notes

**Definitions**

Although I never said this explicitly, a **definition** is an 'if and only if' statment. When I write:

*Definition:* An integer $x$ is "5-ish" if there is an integer $n$ so that $x=5n$

I am actually saying that "$x$ is 5-ish IF AND ONLY IF there is an integer $n$ so that $x=5n$.  

**Negation of implication**

The easiest way to express NOT (A implies B) is as (A and NOT B).  Check the truth tables.


# 1.4 Variable statements and quantifiers

## First examples 

**Compare the following three statements**

- *Helen* is a UConn student who has watched every minute of Game of Thrones.
- *There is a UConn student* who has watched every minute of Game of Thrones.
- *Every UConn student*  has watched every minute of Game of Thrones.

**All make assertions about the set $U$ of UConn students**

- The first asserts that a *particular*  named element of $U$ has a certain property (...has watched every minute of GoT)
- The second asserts that *There exists* an element of $U$ with that property. 
- The third asserts that *Every* element of $U$ has that property.



## Universal quantifier (For all, for every, for each)

A statement that includes a universal quantifier makes a claim about ALL objects of a particular type.

- For all $x$ in the real numbers, $(x^2-1)=(x+1)(x-1)$. 
- Every declared democratic presidential candidate will appear in the next official television debate.
- Each midterm exam in this course counts as 25\% of your final grade.

**Symbolic Form**

- For all $X$, $P(X)$
- $\forall x$, $P(X)$.

## Existential quantifier (There is, there exists, for some)

- There is a real number $y$ so that $y^2=11$.
- There exists a car for sale in the United States that gets 50 mpg.
- There are some dogs that you should be afraid of.

**Symbolic Form**

- There exists $X$ such that $P(X)$ 
- $\exists x$ such that $P(x)$.

## Relation between universal and existential quantifiers

To show that the statement *Every UConn student has watched every minute of Game of Thrones* is FALSE, you must produce
an example of a UConn student who has NOT watched every minute.  So the negation of this claim is:

**Some UConn student has not watched every minute of Game of Thrones** 
or 
**There is a UConn student who has not watched every minute of Game of Thrones**

To show that the statement *There is a UConn student who has watched every minute of Game of Thrones* is FALSE, you must show
that:
**No student has watched every minute of Game of Thrones**
or
**All students at UConn have NOT watched every minute of Game of Thrones.**

**Symbolic Form (page 11 of the text)**

 - NOT($\forall x, P(x)$) $\leftrightarrow$ $\exists x, \mathrm{NOT\ } P(x)$
 - NOT($\exists x, P(x)$) $\leftrightarrow$ $\forall x, \mathrm{NOT\ } P(x)$

## Examples

The statement $(S\cap T)\subset U$  is the statement that

$\forall x, ((x\in S) and (x\in T)) \implies x\in U$

Write the negation of this statement in a simple form.

## Second order statements 

Second order statements have two quantifiers.

- For all $x$, there exists $y$, so that.... 
- There exists $x$, so that for all $y$, ...

**For all $x$, there exists $y$.**

- For every even integer $x$, there exists an integer $y$ so that $x=2y$.
- For every real positive number $x$, there exists a real number $y$ so that $x=y^2$.
- For every real $\epsilon>0$, there exists a real $\delta>0$ so that if $|x|<\delta$ then $x^2<\epsilon$.

**There exists $y$, so that for all $x$**

- There exists an integer $x$ so that, for all integers $y$, $xy=0$.

## An example

**Definition:** Given two integers $n$ and $d$, we say that 

-*$n$ is divisible by $d$* 

or 

-*$n$ is a multiple of $d$*

or 

-*$d$ divides $n$* 

if there exists an integer $m$ so that $n=dm$. 

## Divisibility examples

A. Let $X=\{ n\in \mathbb{Z}: 3|n \}$ and let $Y=\{n\in \mathbb{Z}: 5|n\}$.  Show that
$X\cap Y=\{n\in \mathbb{Z}: 15|n\}$.

B. Let $X=\{n \in \mathbb{Z}: 6|n\}$ and let $Y=\{n \in \mathbb{Z}: 4|n\}$.  Show that
$X\cap Y$ is not equal to $W=\{n\in\mathbb{Z}: 24|z\}$.

# Section 1.5: Proofs

## Main ingredients

Remember that a mathematical proof is a careful explanation of the logical reasons for the truth of a proposition.
Good proofs are:

-*rigorous*, meaning that they present a completely, logically correct argument
-*informative*, meaning that they convey the reasoning behind the truth of the proposition being proved
-*efficient*, meaning that they are as short as possible while still being rigorous and informative.


## Things to try

Faced with a proposition to be provided:

- Make sure you understand the definitions of all the terms in the statement
- Carefully review the logical structure of the proposition so you know what you need to establish.
- If it's not clear how to proceed, consider some special cases or examples.  Review carefully what you know already.  We will see more approaches later.
- Finding a proof of a proposition can be hard. It can take many people working for centuries.  For example, the [Clay Millenium problems](https://www.claymath.org/millennium-problems) are a series of propositions to be proved (or disproved); successfully solving one of these problems brings a $1M dollar prize as well as world-wide fame.

## Examples 1: Direct Implication

**Proposition:** Let $S$ and $T$ be sets.  Prove that if $S \cap T=S$ then $S\subset T$.

Analysis: This is a direct implication $P\implies Q$.

- $P$ is the statement $S \cap T=S$.
- $Q$ is the statement $S \subset T$.

$S\cap T = S$ means that $x\in S \mathrm{\ and\ }x\in T$ if and only if $x\in S$.

$S\subset T$ means that $(x\in S)\implies (x\in T)$.

Look at the truth tables and compare with paragraph on page 14.

## Examples 2: If and only if

**Proposition:** $S \cap T = S\cup T$ if and only if $S=T$.

- $P$ is the statement $x\in (S\cap T) \Leftrightarrow x\in (S \cup T)$.
- $Q$ is the statement $x\in S \Leftrightarrow x\in T$.

Look at truth tables and compare with paragraph on page 14.

## Examples 3: Contrapositive

**Proposition:** If $x$ is a real number such that $x^3+7x^2<9$ then $x<1.1$.

- $P$ is the statement $x^3+7x^2<9$
- $Q$ is the statement $x<1.1$.

$P\implies Q$ is equivalent to $~Q \implies ~P$.

Must show: $x\ge 1.1$ implies $x^3+7x^2\ge 9$.

## Example 4: Contradiction.

**Proposition:** There is no largest integer.

Suppose that this statement $P$ is false.  Then there is a largest integer; call it $n$.  Since $n$ is the largest integer, $n+1$ must be less than or equal to $n$.
Therefore $n+1\le n$ or $1\le 0$.  This is false.

Let $Q$ be the statement "There is no largest integer."  Let $P$ be the statement $1\le 0$. 

Then we have shown that $~Q \implies P$.  Since $P$ is false, this implication can only be true if $~Q$ is false, so $Q$ is true.

This is called *PROOF BY CONTRADICTION.*

## Example 5: Compound implications

**Proposition:** If $x$ is a real number, then $(x-a)(x-b)=0$ if and only if either $x=a$ or $x=b$.

Here $P$ is $(x-a)(x-b)=0$.
The conclusion is of the form $Q \mathrm{\ or\ } R$ where  $Q$ is $x=a$ and $R$ is $x=b$.

One approach: $P\implies (Q\mathrm{\ or\ } R)$ is equivalent to $P\mathrm{\ and\ }~R\implies Q$.
So $(x-a)(x-b)=0$ and $x\not=a$ means we can divide by $x-a$ to get $x=b$.

In the other direction, try each possibility.

## Discussion Problems

Selected problems from 55-61 on page 21 and 65-70 on page 22 of the book.
