% Math 2710
% Aug 26-28

# Course Info
## Key links

- [Syllabus](https://learn.uconn.edu/bbcswebdav/courses/M1198-MATH-2710-001.002/syllabus.pdf)
- Tests
- [Homework](https://learn.uconn.edu/bbcswebdav/courses/M1198-MATH-2710-001.002/Homework.html)
- [Piazza](https://piazza.com/uconn/fall2019/m1198math2710001002)

## Grading

- Two midterms (25 points) tentatively Sep 30 and Nov 5.  
  - Notify me by Sep 20
if you need an alternate date for the first exam because of Rosh Hashanah.
- Final Exam (40 points)
- Homework (8 points)
- Piazza participation (2 points)

##  Homework

- daily assignments
- periodically collected and graded with short lead time
- assorted short quizzes or other assignments from time to time


# 1.1 What is this course about?

## Mathematics as a discipline

This course is about

- *how mathematics is done* 
- *how mathematics is communicated*.

The actual mathematics we will learn in this course is less important than the approach

## A very simple example

**Assertion:** The sum of two even numbers is an even number.

Goal: find a mathematical proof of this fact. 

## Mathematical Proof
A *mathematical proof* of this assertion is an argument that starts from known facts
and definitions and establishes the the truth of the assertion using the tools of logic. 

A proof in *formal logic* starts from explicit hypotheses or axioms and applies the rules of deductive logic
to reach a conclusion.  Proofs of even simple facts in formal logic are extremely long and mostly not readable
by humans.  

In principle, a mathematical proof contains enough information to produce a formal logical proof. 

## Good Mathematical Proofs
A good mathematical proof is 

- *rigorous*, meaning it gives a complete logical argument,
- *informative*, meaning  that it provides enough information to explain why the assertion is true
-  *efficient*, meaning that it is as short as possible while still being rigorous and informative.

## Example, continued

To construct a proof of this assertion, we need:

- to know exactly what the terms mean (what is an even integer?)
- to establish in our own minds that the assertion IS true, and figure out why
- communicate our understanding of why the assertion is true rigorously and efficiently.

## Discussion

- Define *even number*.
- Explain why the assertion about even numbers is true, as rigorously and efficiently as you can.

## Key Vocabulary

::: {.columns}

::: {.column width="50%"}

* theorem
* lemma
* proposition
* corollary
* example
* algorithm
* definition
* proof
:::
::: {.column width="50%"}
* statement
* proposition
* converse
* contrapositive
* conditional statement
:::
:::

::: notes

Section 1.2 starts here, Wed Aug 28.

:::

# 1.2 Logic



## Statements

A statement is a sentence that is either **True** or **False**

Compound statements are built up using logical operators **AND**, **OR**, **NOT**, and others.

The truth of a compound statement depends on the individual statements and the properties of the
operators.

## AND, OR, NOT

::: {.columns}

::: {.column width="33%"}


| P  | Q |  **AND**|
|:---|:---|:---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |



:::

::: {.column width="33%"}

|P | Q | **OR** |
|:---|:---|:---|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |


:::

::: {.column width="33%"}


| P | **NOT** |
|:--|:--------|
| T | F       |
| F | T       |
:::

:::

## Implications/Conditionals

::: {.columns}

::: {.column width="50%"}

| P | Q | $\implies$ |
|---|---|------------|
| T | T | T          |
| T | F | F          |
| F | T | T          |
| F | F | T           |

:::

::: {.column width="50%"}

| P | Q | $\Longleftrightarrow$ |
|---|---|-----------------------|
| T | T | T                     |
| T | F | F                     |
| F | T | F                     |
| F | F | T                     |

:::

:::

## Discussion

- $P$ and $Q$ are equivalent means $P\Longleftrightarrow Q$ or "$P$ if and only if $Q$".
- Show: $P \implies Q$ is equivalent to ($Q$ OR NOT $P$).
- Exclusive OR is the operator that is TRUE when one of two statements is True, but not both. Express it in terms of AND, OR, and NOT.
- If my basement is wet, then it is either very rainy or a pipe has broken. Express this using the various operators and test its truth under different conditions.


::: notes

Section 1.3 starts here, Friday Aug. 30

# 1.3 Sets

## Sets

We rely on a "naive" notion of set, meaning a collection of objects. For example:

- the set of integers
- the set of words in the English language
- the set of people in the world
- the empty set

## Subsets

We can construct sets by selecting elements of another set, yielding a *subset* of the original set.

## Explicit specification
$A=\{1,3,5,8,9\}$, a subset of the integers.

## Selection by a property
Suppose $P$ is the set of people. Then
$$\{p\in P: \textrm{$p$ is a legal resident of Chicago}\}$$
is shorthand for the set consisting of people $p$ for which the statement "$p$ is a legal resident of Chicago" is True.

## Set operations

If $A$ and $B$ are both subsets of some huge (and usually unmentioned) set $U$, then:

- $A=B$ means that $A$ and $B$ have the same elements.
- $A\subset B$ means that every element of $A$ is also an element of $B$.

## More set operations

- $A\cup B$, the union of $A$ and $B$, is $\{x\in U : x \in A \mathrm{\ OR\ } x\in B\}$
- $A\cap B$, the intersection of $A$ and $B$, is $\{x \in U : x \in A \mathrm{\ AND\ } x\in B\}$
- $A\times B$, the product of $A$ and $B$, is the set of all ordered pairs $(x,y)$ where $x\in A$ and $y\in B$.

## Discussion

Suppose $A$ and $B$ are two sets contained in some big set $U$. Prove the following; truth tables may be helpful.

- $A=B$ if and only if $A\subset B$ and $B\subset A$.  
- $((A\cap B) = A)$ implies $A\subset B$.



