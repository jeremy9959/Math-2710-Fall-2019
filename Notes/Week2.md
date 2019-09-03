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
