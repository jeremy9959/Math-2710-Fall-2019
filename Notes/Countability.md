# Countability Examples

## Eventually zero sequences

**Proposition:** Let $S$ be the set of *eventually zero* sequences of non-negative integers $a_1,a_2,\ldots$;
eventually zero means that for each sequence $s$ there is an $N$ so that $a_i=0$ for $i\ge N$.  (Informally,
the sequence can have anything at the beginning but eventually it becomes $0,0,0,\ldots$.) Then $S$ is countable.

This is interesting because we know on the one hand that, for any $k$, the set of 
$k$-tuples of non-negative integers $(a_1,\ldots, a_k)$ is countable because it is a finite product of countable
sets; and we know that the set of *all* sequences of non-negative integers $(a_1,a_2,\ldots)$ is uncountable by
the diagonalization argument.  So $S$ is a kind of intermediate case, but it turns out to be countable as well.

**Proof:** First, let $\mathbb{W}$ be the set of non-negative integers and let $A(n)$ be 
$$
A(n)=\overbrace{W\times W\times W\times \cdots\times W}^{(n-1)}\times \mathbb{N}
$$
For each $n$, $A(n)$ is countable because it is a finite cartesian product of countable sets.  For each $n>0$
let 
$$
f_{n}:\mathbb{N}\to A(n)
$$
be a bijection, and let $f_0$ send $0$ to the zero sequence.

Now, let $S(n)\subset S$ be the subset of sequences whose last non-zero entry is in position $n$ (and let $S(0)$ be the zero sequence).
Now each element of $S$ belongs to exactly one $S(n)$ -- just choose the $n$ corresponding to the last non-zero entry in the sequence,
or zero if the sequence is all zero. It suffices to prove that $S^{*}$, which is $S$ with the zero sequence deleted, is countable.

To construct a bijection from $\mathbb{N}\to S^*$, first construct a bijection $h:\mathbb{N}\times\mathbb{N}\to S^{*}$
by sending $(x,y)$ to $f_x(y)$.  This is a bijection, since every $s\in S$ belongs to exactly one
$S(n)$ and $f_n:\mathbb{N}\to S(n)$ is bijective by construction. 

Finally, since $\mathbb{N}\times\mathbb{N}$ is countable, $S^*$, and also $S$, is countable.
