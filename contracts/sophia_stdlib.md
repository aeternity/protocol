# Standard library

Sophia language offers standard library that consists of following namespaces:

- [List.aes](#List)
- [ListInternal.aes](#ListInternal)
- [Option.aes](#Option)
- [Func.aes](#Func)
- [Pair.aes](#Pair)
- [Triple.aes](#Triple)

Each of them can be imported using `include` directive.

## List

This module contains common operations on lists like constructing, querying, traversing etc.

### is_empty
`is_empty(l : list('a)) : bool`

Returns `true` iff the list is equal to `[]`.


### first
`first(l : list('a)) : option('a)`

Returns `Some` of the first element of a list or `None` if the list is empty.


### tail
`tail(l : list('a)) : option(list('a))`

Returns `Some` of a list without its first element or `None` if the list is empty.


### last
`last(l : list('a)) : option('a)`

Returns `Some` of the last element of a list or `None` if the list is empty.


### find
`find(p : 'a => bool, l : list('a)) : option('a)`

Finds first element of `l` fulfilling predicate `p` as `Some` or `None` if no such element exists. 


### find_indices
`find_indices(p : 'a => bool, l : list('a)) : list(int)`

Returns list of all indices of elements from `l` that fulfill the predicate `p`.


### nth
`nth(n : int, l : list('a)) : option('a)`

Gets `n`th element of `l` as `Some` or `None` if `l` is shorter than `n + 1` or `n` is negative.


### get
`get(n : int, l : list('a)) : 'a`

Gets `n`th element of `l` forcefully, throwing and error if `l` is shorter than `n + 1` or `n` is negative.


### length
`length(l : list('a)) : int`

Returns length of a list.


### from_to
`from_to(a : int, b : int) : list(int)`

Creates an ascending sequence of all integer numbers between `a` and `b` (including `a` and `b`).


### from_to_step
`from_to_step(a : int, b : int, step : int) : list(int)`

Creates an ascending sequence of integer numbers betweeen `a` and `b` jumping by given `step`. Includes `a` and takes `b` only if `(b - a) mod step == 0`. `step` should be bigger than 0.


### replace_at
`replace_at(n : int, e : 'a, l : list('a)) : list('a)`

Replaces `n`th element of `l` with `e`. Throws an error if `n` is negative or would cause an overflow.


### insert_at
`insert_at(n : int, e : 'a, l : list('a)) : list('a)`

Inserts `e` into `l` to be on position `n` by shifting following elements further. For instance,
```
insert_at(2, 9, [1,2,3,4])
```
will yield `[1,2,9,3,4]`.


### insert_by
`insert_by(cmp : (('a, 'a) => bool), x : 'a, l : list('a)) : list('a)`

Assuming that cmp represents `<` comparison, inserts `x` before the first element in the list `l` which is greater than it. For instance,
```
insert_by((a, b) => a < b, 4, [1,2,3,5,6,7])
```
will yield `[1,2,3,4,5,6,7]`


### foldr
`foldr(cons : ('a, 'b) => 'b, nil : 'b, l : list('a)) : 'b`

Right fold of a list. Assuming `l = [x, y, z]` will return `f(x, f(y, f(z, nil)))`.
Not tail recursive.


### foldl
`foldl(rcons : ('b, 'a) => 'b, acc : 'b, l : list('a)) : 'b`

Left fold of a list. Assuming `l = [x, y, z]` will return `f(f(f(acc, x), y), z)`.
Tail recursive.

### foreach
`foreach(l : list('a), f : 'a => unit) : unit`

Evaluates `f` on each element of a list.


### reverse
`reverse(l : list('a)) : list('a)`

Returns a copy of `l` with reversed order of elements.


### map
`map(f : 'a => 'b, l : list('a)) : list('b)`

Maps function `f` over a list. For instance
```
map((x) => x == 0, [1, 2, 0, 3, 0])
```
will yield `[false, false, true, false, true]`


### flat_map
`flat_map(f : 'a => list('b), l : list('a)) : list('b)`

Maps `f` over a list and then flattens it. For instance
```
flat_map((x) => [x, x * 10], [1, 2, 3])
```
will yield `[1, 10, 2, 20, 3, 30]`


### filter
`filter(p : 'a => bool, l : list('a)) : list('a)`

Filters out elements of `l` that fulfill predicate `p`. For instance
```
filter((x) => x > 0, [-1, 1, -2, 0, 1, 2, -3])
```
will yield `[1, 1, 2]`


### take
`take(n : int, l : list('a)) : list('a)`

Takes `n` first elements of `l`. Fails if `n` is negative. If `n` is greater than length of a list it will return whole list.


### drop
`drop(n : int, l : list('a)) : list('a)`

Removes `n` first elements of `l`. Fails if `n` is negative. If `n` is greater than length of a list it will return `[]`.


### take_while
`take_while(p : 'a => bool, l : list('a)) : list('a)`

Returns longest prefix of `l` in which all elements fulfill `p`.


### drop_while
`drop_while(p : 'a => bool, l : list('a)) : list('a)`

Removes longest prefix from `l` in which all elements fulfill `p`.


### partition
`partition(p : 'a => bool, l : list('a)) : (list('a) * list('a))`

Separates elements of `l` that fulfill `p` and these that do not. Elements fulfilling predicate will be in the right list. For instance
```
partition((x) => x > 0, [-1, 1, -2, 0, 1, 2, -3])
```
will yield `([1, 1, 2], [-1, -2, 0, -3])`


### flatten
`flatten(ll : list(list('a))) : list('a)`

Flattens a list of lists into a one list.


### all
`all(p : 'a => bool, l : list('a)) : bool`

Checks if all elements of a list fulfill predicate `p`.


### any
`any(p : 'a => bool, l : list('a)) : bool`

Checks if any element of a list fulfills predicate `p`.


### sum
`sum(l : list(int)) : int`

Sums elements of a list. Returns 0 if the list is empty.


### product
`product(l : list(int)) : int`

Multiplies elements of a list. Returns 1 if the list is empty.


### zip_with
`zip_with(f : ('a, 'b) => 'c, l1 : list('a), l2 : list('b)) : list('c)`

"zips" two lists with a function. n-th element of resulting list will be equal to `f(x1, x2)` where `x1` and `x2` are n-th elements of `l1` and `l2` respectively. Will cut off the tail of the longer list. For instance
```
zip_with((a, b) => a + b, [1,2], [1,2,3])
```
will yield `[2,4]`


### zip
`zip(l1 : list('a), l2 : list('b)) : list('a * 'b)`

Special case of [zip_with](#zip_with) where the zipping function is `(a, b) => (a, b)`.

### unzip
`unzip(l : list('a * 'b)) : list('a) * list('b)`

Opposite to the `zip` operation. Takes a list of pairs and returns pair of lists with respective elements on same indices.


### sort
`sort(lesser_cmp : ('a, 'a) => bool, l : list('a)) : list('a)`

Sorts a list using given comparator. `lesser_cmp(x, y)` should return `true` iff `x < y`. If `lesser_cmp` is not transitive or there exists an element `x` such that `lesser_cmp(x, x)` or there exists a pair of elements `x` and `y` such that `lesser_cmp(x, y) && lesser_cmp(y, x)` then the result is undefined. Currently O(n^2).


### intersperse
`intersperse(delim : 'a, l : list('a)) : list('a)`

Intersperses elements of `l` with `delim`. Does nothing on empty lists and singletons. For instance
```
intersperse(0, [1, 2, 3, 4])
```
will yield `[1, 0, 2, 0, 3, 0, 4]`


### enumerate
`enumerate(l : list('a)) : list(int * 'a)`

Equivalent to [zip](#zip) with `[0..length(l)]`, but slightly faster.


## ListInternal

This module is used only to support syntactic sugars for lists. All its features are already included in the [List](#List) namespace. Therefore, it should not be included manually and used explicitly.


## Option

Common operations on `option` types and lists of `option`s.

### is_none
`is_none(o : option('a)) : bool`

Returns true iff `o == None`


### is_some
`is_some(o : option('a)) : bool`

Returns true iff `o` is not `None`.


### match
`match(n : 'b, s : 'a => 'b, o : option('a)) : 'b`

Behaves like pattern matching on `option` using two case functions.


### default
`default(def : 'a, o : option('a)) : 'a`

Escapes `option` wrapping by providing default value for `None`.


### force
`force(o : option('a)) : 'a`

Forcefully escapes `option` wrapping assuming it is `Some`. Throws error on `None`.


### on_elem
`on_elem(o : option('a), f : 'a => unit) : unit`

Evaluates `f` on element under `Some`. Does nothing on `None`.


### map
`map(f : 'a => 'b, o : option('a)) : option('b)`

Maps element under `Some`. Leaves `None` unchanged.


### map2
`map2(f : ('a, 'b) => 'c, o1 : option('a), o2 : option('b)) : option('c)`

Applies arity 2 function over two `option`s' elements. Returns `Some` iff both of `o1` and `o2` were `Some`, or `None` otherwise. For instance
```
map2((a, b) => a + b, Some(1), Some(2))
```
will yield `Some(3)` and
```
map2((a, b) => a + b, Some(1), None)
```
will yield `None`.


### map3
`map3(f : ('a, 'b, 'c) => 'd, o1 : option('a), o2 : option('b), o3 : option('c)) : option('d)`

Same as [map2](#map2) but with arity 3 function.


### app_over
`app_over(f : option ('a => 'b), o : option('a)) : option('b)`

Applies function under `option` over argument under `option`. If either of them is `None` the result will be `None` as well. For instance
```
app_over(Some((x) => x + 1), Some(1))
```
will yield `Some(2)` and
```
app_over(Some((x) => x + 1), None)
```
will yield `None`.


### flat_map
`flat_map(f : 'a => option('b), o : option('a)) : option('b)`

Performs monadic bind on an `option`. Extracts element from `o` (if present) and forms new `option` from it. For instance
```
flat_map((x) => Some(x + 1), Some(1))
```
will yield `Some(2)` and
```
flat_map((x) => Some(x + 1), None)
```
will yield `None`.


### to_list
`to_list(o : option('a)) : list('a)`

Turns `o` into an empty (if `None`) or singleton (if `Some`) list.


### filter_options
`filter_options(l : list(option('a))) : list('a)`

Removes `None`s from list and unpacks all remaining `Some`s. For instance
```
filter_options([Some(1), None, Some(2)])
```
will yield `[1, 2]`.


### seq_options
`seq_options(l : list (option('a))) : option (list('a))`

Tries to unpack all elements of a list from `Some`s. Returns `None` if at least element of `l` is `None`. For instance
```
seq_options([Some(1), Some(2)])
```
will yield `Some([1, 2])`, but
```
seq_options([Some(1), Some(2), None])
```
will yield `None`.


### choose
`choose(o1 : option('a), o2 : option('a)) : option('a) `

Out of two `option`s choose the one that is `Some`, or `None` if both are `None`s.


### choose_first
`choose_first(l : list(option('a))) : option('a)`

Same as [choose](#choose), but chooses from a list insted of two arguments.


## Func

Functional combinators.

### id
`id(x : 'a) : 'a`

Identity function. Returns its argument.


### const
`const(x : 'a) : 'b => 'a = (y) => x`

Constant function constructor. Given `x` returns a function that returns `x` regardless of its argument.


### flip
`flip(f : ('a, 'b) => 'c) : ('b, 'a) => 'c`

Switches order of arguments of arity 2 function.


### comp
`comp(f : 'b => 'c, g : 'a => 'b) : 'a => 'c`

Function composition. `comp(f, g)(x) == f(g(x))`.


### pipe
`pipe(f : 'a => 'b, g : 'b => 'c) : 'a => 'c`

Flipped function composition. `pipe(f, g)(x) == g(f(x))`.


### rapply
`rapply(x : 'a, f : 'a => 'b) : 'b`

Reverse application. `rapply(x, f) == f(x)`.


### recur
`recur(f : ('arg => 'res, 'arg) => 'res) : 'arg => 'res`

The Z combinator. Allows performing local recursion and having anonymous recursive lambdas. To make function `A => B` recursive the user needs to transform it to take two arguments instead – one of type `A => B` which is going to work as a self-reference, and the other one of type `A`  which is the original argument. Therefore, transformed function should have `(A => B, A) => B` signature.

Example usage:
```
let factorial = recur((fac, n) => if(n < 2) 1 else n * fac(n - 1))
```

If the function is going to take more than one argument it will need to be either tuplified or have curried out latter arguments.

Example (factorial with custom step):

```
// tuplified version
let factorial_t(n, step) = 
  let fac(rec, args) =
    let (n, step) = args
    if(n < 2) 1 else n * rec((n - step, step))
  recur(fac)((n, step))
  
// curried version
let factorial_c(n, step) =
  let fac(rec, n) = (step) =>
    if(n < 2) 1 else n * rec(n - 1)(step)
  recur(fac)(n)(step)
```


### iter
`iter(n : int, f : 'a => 'a) : 'a => 'a`

`n`th composition of f with itself, for instance `iter(3, f)` is equivalent to `(x) => f(f(f(x)))`.


### curry2
`curry2(f : ('a, 'b) => 'c) : 'a => ('b => 'c)`

Turns a function that takes two arguments into a curried function that takes one argument and returns a function that waits for the rest. For instance `curry2((a, b) => a + b)(1)(2) == 3`.


### curry3
`curry3(f : ('a, 'b, 'c) => 'd) : 'a => ('b => ('c => 'd))`

Equivalent to [curry2](#curry2), but for 3 arguments.


### uncurry2
`uncurry2(f : 'a => ('b => 'c)) : ('a, 'b) => 'c`

Opposite to [curry2](#curry2).


### uncurry3
`uncurry3(f : 'a => ('b => ('c => 'd))) : ('a, 'b, 'c) => 'd`

Opposite to [curry3](#curry3).


### tuplify2
`tuplify2(f : ('a, 'b) => 'c) : (('a * 'b)) => 'c`

Turns a function that takes two arguments into a function that takes a pair.


### tuplify3
`tuplify3(f : ('a, 'b, 'c) => 'd) : 'a * 'b * 'c => 'd`

Equivalent to [tuplify2](#tuplify2), but for 3 arguments.


### untuplify2
`untuplify2(f : 'a * 'b => 'c) : ('a, 'b) => 'c`

Opposite to [untuplify2](#untuplify2).


### untuplify3
`untuplify3(f : 'a * 'b * 'c => 'd) : ('a, 'b, 'c) => 'd`

Opposite to [untuplify3](#untuplify3).


## Pair

Common operations on 2-tuples.

### fst
`fst(t : ('a * 'b)) : 'a`

First element projection.


### snd
`snd(t : ('a * 'b)) : 'b`

Second element projection.


### map1
`map1(f : 'a => 'c, t : ('a * 'b)) : ('c * 'b)`

Applies function over first element.


### map2
`map2(f : 'b => 'c, t : ('a * 'b)) : ('a * 'c)`

Applies function over second element.


### bimap
`bimap(f : 'a => 'c, g : 'b => 'd, t : ('a * 'b)) : ('c * 'd)`

Applies functions over respective elements.


### swap
`swap(t : ('a * 'b)) : ('b * 'a)`

Swaps elements.


## Triple

### fst
`fst(t : ('a * 'b * 'c)) : 'a`

First element projection.


### snd
`snd(t : ('a * 'b * 'c)) : 'b`

Second element projection.


### thd
`thd(t : ('a * 'b * 'c)) : 'c`

Third element projection.


### map1
`map1(f : 'a => 'm, t : ('a * 'b * 'c)) : ('m * 'b * 'c)`

Applies function over first element.


### map2
`map2(f : 'b => 'm, t : ('a * 'b * 'c)) : ('a * 'm * 'c)`

Applies function over second element.


### map3
`map3(f : 'c => 'm, t : ('a * 'b * 'c)) : ('a * 'b * 'm)`

Applies function over third element.


### trimap
`trimap(f : 'a => 'x, g : 'b => 'y, h : 'c => 'z, t : ('a * 'b * 'c)) : ('x * 'y * 'z)

Applies functions over respective elements.


### swap
`swap(t : ('a * 'b * 'c)) : ('c * 'b * 'a)`

Swaps first and third element.


### rotr
`rotr(t : ('a * 'b * 'c)) : ('c * 'a * 'b)`

Cyclic rotation of the elements to the right.


### rotl
`rotl(t : ('a * 'b * 'c)) : ('b * 'c * 'a)`

Cyclic rotation of the elements to the left.
