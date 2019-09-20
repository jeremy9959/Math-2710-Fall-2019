## The gcd as the smallest positive linear combination

**Theorem:** Let $a$ and $b$ be integers with $b\not=0$.  Then the greatest common divisor of $a$ and $b$ is the smallest
positive value $ax+by$ as $x$ and $y$ run through all integers.

**Proof:** Let $d$ be the smallest positive value of $ax+by$.  Such a value exists by the Well Ordering Principle.  We show that
$d=\mathrm{gcd}(a,b)$.  

- First, suppose that $s$ is a common divisor of $a$ and $b$.  Then $s|(ax+by)$ by Proposition 2.1(ii), so $s|d$. Therefore $d\ge s$
by Proposition 2.1(iv).  So $d$ is greater than or equal to every common divisor of $a$ and $b$.

- Second we show that $d|a$.  Apply the division algorithm to write $a=qd+r$ with $0\le r<d$.  Multiply the equation $ax+by=d$ by $q$
to obtain
$$
qax+qby=qd=a-r
$$
so 
$$
r=a(1-qx)+b(-qy).
$$
Since $r$ is of the form $ax'+by'$ for integers $x'$ and $y'$, and $r<d$, we know that $r$ cannot be positive.  Therefore $r=0$,
so $d|a$.

- A similar argument shows that $d|b$.

- Since $d$ is a common divisor of $a$ and $b$, and is greater than or equal to any other common divisor, we conclude that $d=\mathrm{gcd}(a,b)$.


## The relationship between lcm and gcd

**Theorem:** $\mathrm{lcm}(a,b)\mathrm{gcd}(a,b)=ab$.

**Proof:** First, notice that $\mathrm{gcd}(a,b)$ divides $ab$ because in fact it divides each of $a$ and $b$.  Let
$T$ be any common multiple of $a$ and $b$, that is, any integer such that $a|T$ and $b|T$.  Find $x$ and $y$
so that
$$
ax+by=\mathrm{gcd}(a,b)
$$
and multiply this equation by $T$:
$$
Tax+Tby=\mathrm{gcd}(a,b)T.
$$
Now notice that $ab|aT$ because $a$ divides $a$ and $b$ divides $T$; and also $ab$ divides $bT$ for the same sort of reason.
Therefore we can factor $ab$ out of $Tax+Tby=abU$ and obtain
$$
abU=\mathrm{gcd}(a,b)T.
$$
Finally we have
$$
T=\frac{ab}{\mathrm{gcd}(a,b)}U.
$$
In other words, $T$ isa multiple of $ab/\mathrm{gcd}(a,b)$.  This shows that any common multiple of $a$ and $b$ is a multiple of
$M=ab/\mathrm{gcd}(a,b)$, and is therefore greater than or equal to $M$.  Putting this together we see that $M$ is a common multiple
that is smaller than or equal to any other common multiple, and it is therefore $\mathrm{lcm}(a,b)$. 
