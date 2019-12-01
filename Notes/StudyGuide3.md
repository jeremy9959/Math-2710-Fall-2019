## Final Exam Study Guide

**Overview:** The final exam is two hours long and will cover material from the entire course.  However, it will have some emphasis on material covered since the
second midterm -- roughly 40-50% on the new material and 50% on the earlier material.  *This study guide covers only the new material* and you should use it
together with the first two guides to have the full picture of material to be covered.

### Functions (Chapter 12 of Hammack, not including Sections 12.3 and  12.6)

You should be able to do essentially all of the problems in Sections 12.1-12.2 and 12.4-12.5
of Hammack.

Take special note of:

- Definition of a function as a set of ordered pairs with certain properties (you should know this definition and how to apply it cold).  Cartesian Product of two sets.  Domain, codomain, and range.
Different ways to represent functions (formulas, traditional graphs, circle and arrow pictures, such
as Figures 12.1, 12.2, and 12.3 in Hammack). 

- Definition of *injective* function.  (Know this cold!) Ability to provide examples of
functions that *are* and *are not* injective.  Ability to recognize injectivity from the
various types of pictures of functions. Ability to prove a function is injective,
or disprove it.

- Definition of *surjective* function (know this cold!) Same goals as with injective functions

- Definition of *bijective* function (know this cold!) Same goals again.

From Section 12.2, take special note of problems 1,2,4, 10, 11, 12, 17, 18 as well
as the problems that I assigned from this section.

- Composition of functions.  Properties of composition (such as associativity, Theorem 12.1)
and relationship between injectivity/surjectivity of $f$ and $g$ with injectivity/surjectivity of $g\circ f$ (Theorem 12.2).  Understand and be able to use the key steps in the proofs of Theorems 12.1
and 12.2.

Again, the problems on page 238 are all relevant.

- Inverse functions.  Know the definition of an inverse function (the correct one,
not the one I mangled in class.  I will provide one below.)  Understand and be able to apply the
ideas that relate bijectivity of $f$ to the existence of an inverse for $f$.  **IMPORTANT:**
This is one area where Gilbert and Vanstone is more useful than Hammack, because Hammack's proof of Theorem 12.3 uses the notion of "inverse relation" which I did not discuss.  I will provide
a proof of this theorem as part of this study guide for the sake of consistency.

The problems in Hammack, Section 12.5 are all relevant.
In addition, you should be able to prove:
- that if $f$ has an inverse, then $f$ is bijective; and
- if $f$ is bijective then it has an inverse.
See below.

### Cardinality (Section 14.1 and 14.2)

Know what it means to say that two sets have *the same cardinality*.  Know the definition of *countably infinite* and *uncountable* set.  Pay particular attention:

- to the argument in Theorem 14.2 that shows that the real numbers are NOT countable. 
- to the argument in Figure 14.2 that shows the product of two countably infinite sets is countable
- to the argument in Theorem 14.4 that shows that the rational numbers are countable.

You should be able to produce and explain these arguments.

You should be able to produce other examples of both countable and uncountable sets and
explain why they are countable or not.  For example, make sure you see why Figure 14.1
shows that $(0,\infty)$ and $(0,1)$ have the same cardinality and what's involved in proving this. 

In addition, the problems in 14.1 and 14.2 are relevant. 

## Inverse functions

This section is designed to clarify the relationship between inverse functions and bijectivity.

**Definition:** Let $f:A\to B$ be a function.  An inverse function $f^{-1}$ to $f$ is a
function $f^{-1}:B\to A$ such that $f^{-1}(f(a))=a$ for all $a\in A$ and $f(f^{-1}(b))=b$
for all $b\in B$.

To test your understanding of this definition, prove that if $f^{-1}$ is an inverse function for $f$, then $f$ is an inverse function for $f^{-1}$.

**Theorem:** A function $f:A\to B$ has an inverse function $f^{-1}$ if and only if $f$ is
bijective.

**Proof:** Suppose first that $f$ is bijective.  As a set of ordered pairs in $A\times B$,
we have by definition:
$$
f=\{(x,f(x)):x\in A\}
$$
Let $h=\{(f(x),x):(x,f(x))\in f\}$ be the set of points in $B\times A$ obtained by switching
the entries of each pair in $f$.

**Step 1:** $h$ is in fact a function from $B$ to $A$.  To check this, we need to know that
*every element $b\in B$ occurs as the first element of a pair $(f(x),x)$ exactly one time.*
So first we check that every element of $b\in B$ occurs at least once.  For this, we need to know
that, for every element $b\in B$, there is an $x\in A$ so that $f(x)=b$.  But since
$f$ is bijective, it is surjective, and therefore such an $x$ exists.  Next, we need to know
that there is only *one* pair with first element $b$.  Suppose there were two -- this
would mean that there were $x$ and $y$ in $A$ so that $(f(x),x)$ and $(f(y),y)$ both
have $b$ in the first slot, meaning that $f(x)=b$ and $f(y)=b$.  Since $f$ is injective,
this can only happen if $x=y$.  So there is only one pair with $b$ in the first slot.
That finishes the proof of this direction.  **NOTICE HOW WE USE BOTH INJECTIVITY AND SURJECTIVITY**

**Step 2:** Now we need to check that $h$ is actually $f^{-1}$.  Given $x\in A$,  Let's look at 
$h(f(x))$.  For $f(x)$ we have the pair $(x,f(x))$.  For $h(f(x))$ we need the pair with $f(x)$ in the first slot, but by definition that is $(f(x),x)$.  So $h(f(x))=x$.  Now take $y\in B$.  Then
we need to find the pair in $h$ with $y$ in its first slot.  TO do that, we find $y=f(x)$,
and then the pair is $(y=f(x),x)$.  Therefore $h(y)=x$  and $f(h(y))=f(x)=y$.  So $h$ satisfies
$h(f(x))=x$ and $f(h(y))=y$ for $x\in A$ and $y\in B$, so $h=f^{-1}$.

Now suppose that $f$ has an inverse function $f^{-1}$.  We must show that $f$ is bijective.
Let's first check that $f$ is injective.  Suppose $u,v \in A$ and $f(u)=f(v)$.
Then $f^{-1}(f(u))=f^{-1}(f(v))$ so $u=v$.  Thus $f$ is injective.  Next, we must show
that $f$ is surjective.  For that, choose $b\in B$.  We want to find $x\in A$ so that
$f(x)=b$.  Apply $f^{-1}$ to both sides to get $f^{-1}(f(x))=f^{-1}(b)$.  Let $x=f^{-1}(b)$.
Then $f(x)=f(f^{-1}(b))=b$ so $f$ is surjective, and therefore bijective.

