% Math 2710
% Nov 11-15

## Functions


**Definition:** A function $f:A\to B$ is a subset $f\subset A\times B$ with the property that for every $a\in A$
there is exactly one $b$ in $B$ so that $(a,b)\in f$.  We write $f:A\to B$ to mean that $f$ is a function with domain $A$ and co-domain $B$.

Compare this with the definition of a function as a "rule."  The associated "rule" says: to compute $f(a)$,
find the (uniquely determined) pair $(a,b)$ in $f$, and then set $f(a)=b$.  

In some sense this definition replaces the notion of a function with its graph.  

## Domain, co-Domain, Range

$A$ is called the **DOMAIN** of $f$ and $B$ is called the **CO-DOMAIN.**

The **range** of $f$ is the subset of $b$ that occur in a pair $(a,b)\in f$.  

A function can be drawn as a graph or as a "mapping" between two sets (see figure 12.3 in Hammack).

## Examples 

Consider problem 1 from Hammack.  $A=\{0,1,2,3,4\}$ and $B=\{2,3,5,6\}$.  Then $f=\{(0,3),(1,3),(2,4), (3,2), (4,2)\}$
Verify that $f$ is a function and then find its range.

Is the subset of pairs of integers $(x,y)$ where $3x+y=4$ a function from $\mathbf{Z}$ to $\mathbf{Z}$?

## Terminology: injective and surjective

**Definition:** A function is *injective* if it has the property that $f(a)\not=f(b)$ implies $a\not=b$. (or $f(a)=f(b)$ implies $a=b$).
A function is *surjective* if for every $b\in B$ there is an $a$ with $(a,b)\in f$.  A function is *bijective* if it is both injective and surjective.

- *Injective* is also called "one-to-one."  *Surjective* is also called "onto."

- Surjectivity depends on the codomain (you can shrink the codomain to make the function surjective).

## Some examples

- $f:\mathbb{Z}\to\mathbb{Z}$ given by $f(n,m)=2n-4m$.  

- $f:\mathbb{Q}-\{2\}\to\mathbb{Q}-\{5\}$ given by $f(x)=(5x+1)/(x-2)$ is bijective.

- Consider maps from $\{0,1,2\}$ to $\{0,1,2\}$.  how many are there?  How many are injective? How many surjective? How many bijective?

- The function  $f:\mathbb{Z}_m\to \mathbb{Z}_m$ given by $f(x)=ax$ is bijective if $\mathrm{gcd}(a,m)=1$.  

## Composition of functions

**Definition:** Suppose that $f:A\to B$ is a function and $g:B\to C$ is a function.  The *composition* $g\circ f$ is a function from $A\to C$
defined by $(g\circ f)(a)=g(f(a))$.  

This makes sense because $f(a)\in B$ and $g:B\to C$.  

**Examples:** 

- $f:\mathbf{R}\to\mathbf{R}$ given by $f(x)=x^2$, and $g:\mathbf{R}\to\mathbf{R}$ with $g(x)=\sin(x)$.  What are $f\circ g$ and $g\circ f$?

- $A=\{0,1,2,3\}$, $B=\{1,2,3,4\}$, $C=\{1,3,5,6\}$.   $f=\{(0,1),(1,2), (2,3),(3,3)\}$ in $A\times B$.  $g=\{(1,3), (2,3),(3,3),4,3)\}$ in $B\times C$. 
What is the composition?

## Properties of composition

**Theorem:** Composition of functions is associative.

**Theorem:** If $f:A\to B$ and $g:B\to C$ are injective then $g\circ f$ is injective.  Similarly if $f$ and $g$ are surjective then $g\circ f$ is surjective.
And if both are bijective, so is the composition.

