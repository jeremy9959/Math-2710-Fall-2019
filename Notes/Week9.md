% Math 2710
% Oct 28-Nov 1

## More on limit rules

**Proposition:** If $a_n$ converges to $L$ then $ca_n$ converges to $cL$. 

**Definition:** Divergence to infinity: A sequence $a(n)$ diverges to infinity if, for any $B$, there is an
$N$ so that $a(n)>B$ if $n\ge N$.

Remark on calculus trick for ratio of polynomials $P(n)/Q(n)$: look at highest degree terms and if they are the same
degree take ratio of leading coefficients.

Follows from:

- Fact that the sequence $1/n$ converges to $0$.
- Limit rules for sums, products, quotients.

## Series

A *series* is an infinite sum, but it is really a shorthand for a sequence.  The series
$$
a_0+a_1+a_2+\ldots
$$
is a short hand for the sequence of partial sums $(a_0,a_1+a_0,a_2+a_1+a_0,\ldots)$.

A series converges to a limit $L$ means that the sequence of partial sums converges.

Key example is the geometric series $\sum_{n=0}^{\infty} ar^{n}$.

## Geometric series

**Proposition:** Suppose $r\not=1$. The finite geometric series has sum
$$
a+ar+ar^2+ar^3+\cdots+ar^n = a\frac{r^{n+1}-1}{r-1}.
$$

**Proof:** By induction.  If $n=1$ then we get $a+ar=a\frac{r^2-1}{r-1}=ar+r$ as desired.  Suppose true for $n=k$
Then 
$$
a+ar+ar^2+\cdots +ar^{k+1}=a\frac{r^{k+1}-1}{r-1}+ar^{k+1}=a\frac{r^{k+1}+r^{k+1}(r-1)}{r-1}
$$
and 
$$
a\frac{r^{k+1}-1+r^{k+2}-r^{k+1}}{r-1}=a\frac{r^{k+2}-1}{r-1}.
$$

## Infinite geometric seriens

**Proposition:** If $|r|<1$, the infinite geometric series
$$
a+ar+ar^2+\cdots
$$
converges to
$$
\frac{a}{1-r}.
$$

**Proof:**   The partial sums are $s(n)=a\frac{r^{n+1}-1}{r-1}$.  Since $\frac{a}{1-r}$ is a constant
we can write this as 
$$
s(n)=\frac{a}{1-r}(1-r^{n+1}).
$$

Now the sequence $r^{n+1}$ converges to zero when $r<1$ (proof?)  and so $1-r^{n+1}$ converges to $1$ (proof)
and so $s(n)$ converges to $a/(1-r)$.

## Other examples

The harmonic series
$$
1+1/2+1/3+\cdots
$$
does not converge.  For a proof, see problem 33 on page 105 of the Gilbert-Vanstone book where they ask you to show
by induction that, for all $n$, 
$$
1+1/2+1/3+\cdots+1/2^{n}\ge 1+n/2
$$
Therefore the sequence of partial sums diverges (slowly) to infinity.

## Base ten decimals and the geometric series

An infinite decimal is shorthand notation for an infinite series (and thus a sequence).
$$
.a_0a_1a_2\cdots = \sum_{i=0}^{\infty} a_{i}10^{-i}
$$

An eventually repeating decimal is a decimal expansion such that there is an $N$ and a $k$ so that
for all $i\ge N$ we have $a_{i+k}=a_{i}$.  In other words there is a block of $k$ digits $a_N, a_{N+1},\cdots,a_{N+k}$
that repeat over and over.

## Repeating decimals converge to rational numbers

**Proposition:** An eventually repeating decimal converges to a rational number.

**Proof:** First suppose our decimal begins repeating right at the decimal point, so it looks like $a_1 a_2\cdots a_k a_1 a_2\cdots$.
Let $A$ be the integer $a_1a_2\cdots a_k$.  Then the decimal corresponds to the series
$$
\frac{A}{10^{k}}(1+\frac{1}{10^{k}}+\cdots)
$$
This is a geometric series which we know converges to 
$$
\frac{A}{10^{k}}\frac{1}{1-(1/10)^{k}}
$$
which is a rational number.

## Repeating decimals cont'd


If the decimal $x$ has an initial, non repeating part, of length $N$, with digits $a_1 a_2 \ldots a_N$ followed by blocks of $k$ digits
$b_1 b_2\ldots b_k$, we can split out
the leading part and write $x$ as the series:

$$
x=\frac{A}{10^{N}}+\frac{1}{10^{N+k}}(B + B/10^{k} + \cdots)
$$
where $A$ and $B$ are the integers made up of the initial digits and the repeating block respectively.
The second part of this series converges to a rational number by the earlier work, and so the sum is a rational number.

## Base $r$

There was nothing special about base $10$ and the same would be true for repeating "decimals" in any base.

## Every rational has a repeating decimal expansion

For the converse we make an inductive argument.  We are given a fraction $a/b$ and we want to construct a decimal expansion
and prove that it is repeating.  First, we use the division algorithm to write $a=qb+r$ and see that $a/b = q +r/b$.  Now
we proceed as follows.  We multiply $r$ by $10$ and divide again by $b$ using the division algorithm:
$$
10r = q_1b+r_1.
$$

## Repeating decimals continued

This tells us that $r/b = q_1/10+r_1/10b$  Since $r_1<b$, the fraction $r_1/10b$ is less than $1/10$.  Also,
since $r_1<b$, $10r_1<10b$ and so $q_1<10$. Therefore $q_1$ is the first
decimal digit of $r/b$.  Now we repeat the process with $r_1$:
$$
10r_1 = q_2b+r_2
$$
which yields $r_1/b = q_2/10 + r_2/(10b)$ or
$$
r/b=q_1/10+q_2/100+r_2/(100b).
$$
Again, $q_2<10$ and $r_2/100b<1/100$.  

## Repeating decimals continued

Now we proceed by induction.  Suppose we have
$$
r/b = q_1/10+q_2/100+\cdots+q_n/10^{n}+\frac{r_n}{10^{n}b}
$$
with each $q_i<10$ and $r_n<b$ so that $r_n/(10^{n}b)<1/10^{n}$.
Define  $r_{n+1}$ by dividing by $10r_{n}$ by $b$:
$$
10r_{n}=q_{n+1}b+r_{n+1}.
$$
Again, $q_{n+1}<10$ and $r_{n+1}<b$.  Also
$$
r_{n}/b=\frac{q_{n+1}}{10}+\frac{r_{n+1}}{10b}
$$
so
$$
r/b = \frac{q_1}{10}+\frac{q_2}{100}+\cdots+\frac{q_n}{10^n}+\frac{q_{n+1}}{10^{n+1}}+\frac{r_{n+1}}{10^{n+1}b}.
$$

## Finishing up

The key final observation in the proof is that the sequence of remainders $r_{n+1}$ have two important properties:

- First, they are all between $0$ and $b$, and second
- Knowing $r_{n}$ determines $r_{n+1}$. 

These two facts force the sequence of remainders to ultimately repeat, because after considering $b+1$ of them there
have to be two of them which are equal; say $r_{k}=r_{j}$ for some pair $k,j$ with $j>k$.  But then $r_{k+1}=r_{j+1}$,
$r_{k+2}=r_{j+2}$, and so on, and in fact $r_{i+(j-k)}=r_{i}$ for any $i\ge k$.  Thus the sequence of $r$'s, and therefore
the sequence of $q$'s, eventually becomes periodic.

**Other bases:** Notice that there was nothing special about $10$ in the proof above, so rational numbers have periodic expansions
in any base.

