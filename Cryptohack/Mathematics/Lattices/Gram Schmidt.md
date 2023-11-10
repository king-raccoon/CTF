> Given a basis `v1, v2, ..., vn ∈ V` for a vector space, the Gram-Schmidt algorithm calculates an orthogonal basis `u1, u2, ..., un ∈ V`.
> 
> 
> To test your code, let's grab the flag. Given the following basis vectors: `v1 = (4,1,3,-1), v2 = (2,1,-3,4), v3 = (1,0,-2,7), v4 = (6, 2, 9, -5),`
> 
> use the Gram-Schmidt algorithm to calculate an orthogonal basis. The flag is the float value of the second component of `u4` to 5 significant figures.
> 
> **Algorithm for Gram-Schmidt**
> 
> `u1 = v1`
> 
> `Loop i = 2,3...,n`
> 
> `Compute μij = vi ∙ uj / ||uj||^2, 1 ≤ j < i.`
> 
> `Set ui = vi - μij * uj(Sum over j for 1 ≤ j < i)`
> 
> `End Loop`
>

계산기를 돌린다

[Gram-Schmidt-calculator](https://www.emathhelp.net/en/calculators/linear-algebra/gram-schmidt-calculator/)

<img width="648" alt="스크린샷 2023-10-02 오후 4 56 26" src="https://github.com/king-raccoon/king-raccoon/assets/78426205/8d21803c-8d37-4d66-9eb6-56da2ebf11fe">
