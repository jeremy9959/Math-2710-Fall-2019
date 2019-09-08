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
- Homework + participation (including Piazza)  (10 points)

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

A great deal of reasoning is about *conditional statments*.  

- If I get a vaccine for flu today, then I will not get the flu this year.
- If there is a recession in the next six months, President Trump will not be re-elected.
- If the nucleotide at a certain genomic position is switched from A to T, the affected individual will have a certain
genetic disease.

The truth of an implication depends on the Truth/Falsehood of BOTH components.  But if the first
clause is FALSE, the statement is TRUE.  So the interesting cases are when the first clause is TRUE.

**For discussion:**  Compare how other disciplines think about implications such as those above with how
mathematicians do.  Which of the statements above might be susceptible to proof in "real life"?

## Truth Tables for conditionals


| P | Q | $\implies$ |
|---|---|:------------:|
| T | T | T          |
| T | F | F          |
| F | T | T          |
| F | F | T           |


## Alternate formulations

- P implies Q
- If P, then Q
- Q if P
- P only if Q
- P suffices for Q, or is sufficient for Q
- Q is necessary for P.


## Equivalence

The claim that two statements are *equivalent* is the claim that they are either both True or both False.

- P is equivalent to Q
- P if and only if Q
- P is necessary and sufficient for Q.

| P | Q | $\Longleftrightarrow$ |
|---|---|:-----------------------:|
| T | T | T                     |
| T | F | F                     |
| F | T | F                     |
| F | F | T                     |


## Example Computation

(X and (Y or Z)) $\Longleftrightarrow$ ((X and Y) or (X and Z))



| X   | Y | Z | Y or Z | X and (Y or Z) | X and Y | X and Z | ((X and Y) or (X and Z)) |
|-----|---|---|:------:|:--------------:|:-------:|:-------:|:------------------------:|
| T   | T | T | T      | T              | T       | T       | T                        |
| T   | T | F | T      | T              | T       | F       | T                        |
| T   | F | T | T      | T              | F       | T       | T                        |
| T   | F | F | F      | F              | F       | F       | F                        |
| F   | T | T | T      | F              | F       | F       | F                         |
| ... |   |   |        |                |         |         |                          |

(X and (Y or Z)) have the same truth values as ((X and Y) or (X and Z)) and so the statements are
equivalent.

## Discussion

- Give some examples (in English) of statements where P implies Q (meaning P implies Q is TRUE), 
but Q does not imply P.
- Give some examples of statements that are equivalent.
- Are their statements P and Q so that neither P implies Q nor Q implies P are True?
- $P$ and $Q$ are equivalent means $P\Longleftrightarrow Q$ or "$P$ if and only if $Q$".
- Show: $P \implies Q$ is equivalent to ($Q$ OR NOT $P$).
- Exclusive OR is the operator that is TRUE when one of two statements is True, but not both. Express it in terms of AND, OR, and NOT.
- If my basement is wet, then it is either very rainy or a pipe has broken. Express this using the various operators and test its truth under different conditions.


## Problems Originally posted to piazza

**Definition:** An integer x is 5-ish if there is an integer y so that x=5y.

1. Write the definition for a number that is NOT 5-ish.
2.  Is 37 a 5-ish number?  How do you know?

**Definition:** An integer x is "purple" if there is a integer y so that x=5y+1.

Which of the following statements are true?

1. If x is purple, then x is not 5-ish.
2. If x is 5-ish, then x is not purple.
3. There is a number z that is neither purple nor 5-ish.

# 1.3 Sets

## Sets

We rely on a "naive" notion of set, meaning a collection of objects. For example:

- the set of integers
- the set of words in the English language
- the set of people in the world
- the empty set

For a discussion of why this is naive, see [Russell's paradox](https://www.scientificamerican.com/article/what-is-russells-paradox/).

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

- $A\subset B$ means that every element of $A$ is also an element of $B$ or $x\in A \implies x\in B$.
- $A=B$ means that $A$ and $B$ have the same elements, or $x\in A \Longleftrightarrow x\in B$.

## More set operations

- $A\cup B$, the union of $A$ and $B$, is $\{x\in U : x \in A \mathrm{\ OR\ } x\in B\}$.
- $A\cap B$, the intersection of $A$ and $B$, is $\{x \in U : x \in A \mathrm{\ AND\ } x\in B\}$.
- $A\times B$, the product of $A$ and $B$, is the set of all ordered pairs $(x,y)$ where $x\in A$ and $y\in B$.

## Discussion 1

Suppose $A$ and $B$ are two sets contained in some big set $U$. Prove the following by a truth table:

- $((A\cap B) = A)$ implies $A\subset B$.

Hint: Start with the statements $X=(x\in A)$ and $Y=(x\in B)$.  Then $A\subset B$ is $X\implies Y$.
Express the left hand side similarly and work out the truth table.

## Discussion 2

What is the truth table associated to the proposition about any three sets $A, B, C$:

$$
A\cup (B\cap C) = (A\cup B)\cap (A\cup C)
$$

Is the proposition true?

