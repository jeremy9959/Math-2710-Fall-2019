% Math 2710
% November 17-21

## Finite and countable sets

**Definition:** For $n\in\mathbb{N}$ (where $\mathbb{N}$ are the natural numbers), we let
$[n]$ denote the set $\{1,2,\ldots, n\}$.  

- Two sets $A$ and $B$ *have the same cardinality* if there is a bijective map $f:A\to B$.

- A set $A$ is finite if there exists an $n$ so that $A$ has the same cardinality as $[n]$. Otherwise,
$A$ is infinite.

- A set $A$ is countable if it is finite or if it has the same cardinality as $\mathbb{N}$.  In the latter
case it is called "countably infinite."

- An infinite set that is not countably infinite is called *uncountable.*

## Some properties of cardinality

**Proposition:** The relation "having the same cardinality" is an equivalence relation.  

**Proof:** First, $A$ has the same cardinality as $A$ because the identity map (which sends $a\in A$ to itself)
is a bijection.  Second, if $A$ and $B$ have the same cardinality, that means there is a bijection
$f:A\to B$.  But then the inverse function $f^{-1}:B\to A$ is a bijection in the other direction, so the relation
is symmetric.  Finally, suppose $A$ has the same cardinality as $B$, and $B$ has the same cardinality as $C$.
Then there is a bijection $f:A\to B$ and $g:B\to C$.  The composition $g\circ f:A\to C$ is again a bijection,
so $A$ and $C$ have the same cardinality.

##  More properties


**Proposition:** An infinite subset $T$ of $\mathbb{N}$ is countably infinite.  

Proof:  We construct a map $\mathbb{N}\to T$. 
Let $f(1)$ be the smallest element of $T$.  For $n>1$, let $T(n)=\{x\in T: x>f(n-1)\}$.
If $T(n)$ is empty, then $T$ is finite, which isn't true;  so by the well-ordering principle
$T(n)$ has a smallest element.  Let $f(n)$ be the smallest element of $T(n)$ for $n\ge 2$.  
$f$ is injective because $f(1)<f(2)<\cdots$.   We will show that $f$ is surjective.  Suppose not.
Then there is a smallest element x of $T$ for which there is no $n$ with $f(n)=x$.  Choose the
largest element of $T$ which is smaller than $x$ and then there is an $m$ with $f(m)=x$.  But then
$x$ is the smallest element of $T(m+1)$ so $f(m+1)=x$, contradicting our choice of $x$.  Thus $f$
is surjective and therefore bijective. 

## more properties

**Proposition:** An infinite subset $T$ of a countably infinite set $S$ is countably infinite.

**Proof:** There is a bijection $f:\mathbb{N}\to S$ since $S$ is countable.  Let $U$ be the subset
of $\mathbf{N}$ consisting of $\{x\in \mathbb{N}: f(x)\in U\}.$  This is an infinite  subset of $\mathbb{N}$
which is therefore countably infinite and in bijection with $U$, so $U$ is countably infinite.


## The product of countable sets

**Proposition:** If $A$ and $B$ are countable, then so is $A\times B$.  

**Proof:** this is the "digaonals" argument.

**Propositon:** If $A_1,\ldots, A_n$ are countable then so is $A_1\times A_2\times\cdots\times A_n$.

**Proof:** By induction.  We know $A_1\times A_2$ is countable. Assume
$A_1\times\cdots\times A_n$ is countable.  Then $A_1\times\cdots\times A_{n+1}$ is countable because it is
$(A_1\times\cdots\times A_n)\times A_{n+1}$.

## the union of countable sets

**Proposition:** If $A$ and $B$ are countable, so is $A\cup B$.  

**Proof:** The union of $A$ and $B$ is a subject of the disjoint union of $A$ and $B$.  Construct
bijections $f$ and $g$ of  $\mathbb{N}$ to each of $A$ and $B$. Define a new function $a$
with $a(2n)=f(n)$ and $a(2n-1)=g(n)$ for $n=1,\ldots$.  Then $a$ is a bijection of $\mathbb{N}$ with
the disjoint union of $A$ and $B$, which is therefore countable, so its subset $A\cup B$ is also countable.

## more properties

**Proposition:** The integers are countable. 

**Proof:** $\mathbb{Z}$ is the union of $0,1,\ldots$ and $-1,-2,\ldots$ each of which is countable.

**Proposition:** The rational numbers are countable..

**Proof:** The set of ordered pairs of integers $(a,b)$ is countable, and the rational numbers is in bijection witha subset of this set.

## Uncountable sets


- The set of infinite   sequences $[a_1,a_2,a_3,\ldots]$ with $a_i\in\mathbb{N}$ is uncountable.
(this is the diagonal argument)

- The real numbers are uncountable.
(diagonal argument)

- The open open infinite interval $(0,\infty)$ has the same cardinality as $\mathbb{R}$.   Use the $\log(x)$ and $\exp(x)$
as bijections.

- If a subset $U$ of $A$ is uncountable, so is $A$.  Proof: Suppose not.  Then $A$ is countable, so $U$ is a subset of a countable set and therefore countable. 

## power sets

**Theorem:** (Cantor)  The power set of a set $A$ has a "larger" cardinality than $A$.

**Proof:** The map $a\to\{a\}$ puts $A$ inside $\mathcal{P}(A)$ so $\mathcal{P}(A)$ is bigger than or equal to $A$ in
cardinality.  Suppose there is a bijection $f:A\to \mathcal{P}(A)$.  Let $U=\{a\in A: a\not\in f(a)\}$.
This is a subset of $A$ so an element of $\mathcal{P}(A)$.    Suppose $f(x)=U$.  Now if $x\in U$, then $x\in f(x)$,
so $x\not\in U$.  But if $x\not\in U$, then $x\not\in f(x)$ so $x\in U$.  Neither is possible, so $U$ cannot
be in the range of $f$, so $f$ is not bijective.








