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

## infinite geometric seriens

**Proposition:** If $|r|<1$, the infinite geometric series
$$
a+ar+ar^2+\cdots
$$
converges to
$$
\frac{a}{r-1}.
$$

Proof: use the limit rules.

## other examples

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

**Proposition:** An eventually repeating decimal converges to a rational number.

## Base $r$ expansions
