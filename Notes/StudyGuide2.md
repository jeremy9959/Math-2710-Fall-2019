## Math 2710 Second Exam Study Guide

**Note:** This guide is offered without warranty.

The second exam will cover the following topics.

- Chapter 3 omitting 3.6 and 3.7 but including:

	- Section 3.1 Congruence
   - Section 3.3 Equivalence Relations
   - Section 3.4 Modular Arithmetic, in particular Fermat's Little Theorem (3.42)
   - Section 3.5 Congruence Equations, in particular The Linear Congruence Theorem (3.54)

- Chapter 4, all topics.

- Sequences and Series
  
  - Definitions of convergence of a sequence to a limit
  - Proofs of convergence and divergence in particular cases
  - Sums of convergent sequences converge; constant multiples of convergent sequences converge
  - Geometric Series (finite and infinite): definition, proof of convergence
  
- Decimal Expansions of Rational Numbers (Section 4 of Chapter 5)
  
  - Relationship between repeating expansions and geometric series
  - Convergence of eventually repeating decimal expansions to rational numbers
  - Proof that rational numbers have eventually repeating decimal expansions

### Key topics from Chapter Three

- Definition of congruence and ways in which it acts like equality (Prop 3.11, 3.12).  Example: Prove that if $a\equiv a'\pmod{m}$
and $b\equiv b'\pmod{m}$ then $ab\equiv a'b'\pmod{m}$.
- Division of congruences (When you can cancel x from both sides in a congruence $ax\equiv bx\pmod{m}$ and proof of why or why not)
(Proposition 3.13) 
- Calculation modulo $m$ (see for Example 3.15).  Examples: Prove that no perfect square is of the form $3n+2$ for some $n$; 
find the ones digit of $3^{2019}$.
- Equivalence relations:  Definition of an equivalence relation (reflexivity, symmetry, transitivity); proof that congruence
is an equivalence relation -- for example, prove that if $a\equiv b\pmod{m}$ and $b\equiv c\pmod{m}$ then $a\equiv c\pmod{m}$. 
Definition of an *equivalence class.*  **Example:** Suppose the relation on people is "currently live in the same town";  explain
that this is an equivalence relation; what are the equivalence classes?  **Example:** Say $x\sim y$ if $x^2=y^2$; is this
an equivalence relation?  What are the equivalence classes?
- Modular Arithmetic.  **Example:** Solve the congruence $13x=53\pmod{11}$.   **Example:** Prove that if $\mathrm{gcd}(a,m)=1$ then
$ax\equiv b\pmod{m}$ has a solutions.  **Example:** Prove that if $ax\equiv b\pmod{m}$ has a solution $x$ then $\mathrm{gcd}(a,m)$ divides
$d$.  **Example:** Explain the relationship between the theorem on solving congruences (3.54) and the Theorem from chapter 2 on
Linear Diophantine Equations. **Example:** Suppose $p$ is a prime, 
and $a$ is an integer not divisible by $p$.  Prove that if $ai\equiv aj\pmod{p}$ then $i\equiv j\pmod{p}$. Use this to prove
that the set of congruence classes $\{[a],[2a],[3a],\ldots,[(p-1)a]\}$ modulo $p$ is the same as the set $\{[1],[2],\ldots,[p-1]\}$.
(this is a key step in the proof of Fermat's little theorem).  **Example:** Prove Fermat's little theorem.
- Congruence Equations. See problems 32-41 on page 83 of Gilbert and Vanstone.  Also look at problems 98-104.

#### Key Topics from Chapter 4

Sample problems on induction from Gilbert and Vanstone -- see for example: 11-18, 29, 31, 33, 37, 43, 45, 47, 53, 56, 65-67, 74, 76.

- Prove that the binomial coefficient $\binom{n}{r}$ counts the number of $r$ element subsets of an $n$ element set.

- Prove that the sum of a finite geometric series $a+ar+ar^2+\cdots+ar^{n}$ is $a\frac{r^{n+1}-1}{r-1}$.

- (Optional) Define a function recursively by setting $f(0)=0$, $f(1)=1$, and $f(n)=af(n-1)+bf(n-2)$ for constants $a$ and $b$.
Let 
$$
u(x)=\sum \frac{f(n)}{n!}x^{n}.
$$

Prove that $u(x)$ is a solution to the linear second order differential equation
$$
\frac{d^2u}{dx^2}-a\frac{du}{dx}-bu.
$$

Let $t^2-at-b=0$ be the characteristic polynomial of this differential equation and let $r_0$ and $r_1$ be its roots.
Assume for simplicity that these roots are distinct (so that $a^2-4b\not=0$.)  By expressing $u(x)$ as a linear combination
of $\exp(r_0x)$ and $\exp(r_1x)$, derive a formula for $f(n)$ involving $r_0$ and $r_1$.

#### Sequences and series

- See the problems in Hammack in the section on sequences, esp. Problems 1-6, 8, 9, 10, 13.  In particular You should be able to state
**verbatim** the definition of convergence of a sequence and prove directly that simple sequences converge to stated limits.
**Example:** Prove that $n/(3n+2)$ converges to $1/3$ without using any tricks from Calculus.

- See the problems in Hammack in the section on series, esp. problem 1. 

#### Decimal expansions

Prove that an eventually repeating decimal expansion (or base r expansion) converges to a rational number.
Prove that a rational number has an eventually repeating decimal (or base r) expansion.

See: Gilbert and Vanstone, Chapter 5, Problems 23-32, 37, 41,  42, 44, 
