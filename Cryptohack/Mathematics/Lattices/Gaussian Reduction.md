> Gauss developed his algorithm to find an optimal basis for a two-dimensional lattice given an arbitrary basis. Moreover, the output `v1` of the algorithm is a shortest nonzero vector in `L`, and so solves the SVP.
For the flag, take the two vectors `v = (846835985, 9834798552), u = (87502093, 123094980)` and by applying Gauss's algorithm, find the optimal basis. The flag is the inner product of the new basis vectors.
> 
> 
> **Algorithm for Gaussian Lattice Reduction**
> 
> `Loop`
> 
> `(a) If ||v2|| < ||v1||, swap v1, v2`
> 
> `(b) Compute m = ⌊ v1∙v2 / v1∙v1 ⌉`
> 
> `(c) If m = 0, return v1, v2`
> 
> `(d) v2 = v2 - m*v1`
> 
> `Continue Loop`
>

```
import numpy as np
ar = np.array
v = ar([846835985, 9834798552],dtype='i8')
u = ar([87502093, 123094980],dtype='i8')
v1,v2 = u,v

while 1:
    if np.sqrt(v1.dot(v1)) > np.sqrt(v2.dot(v2)):
        v1, v2 = v2, v1

    m = int(v1.dot(v2)/v1.dot(v1))
    if m == 0:
        print('v1:', v1, ' v2:', v2)
        break
    else:
        v2 = v2 - m*v1

print(v1.dot(v2))
```

`#result
v1: [ 87502093 123094980]  v2: [-4053281223  2941479672]
7410790865146821`