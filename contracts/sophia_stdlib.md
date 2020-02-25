<!--
Oh Hi! I see you are editing the stdlib documentation, that's really cool.
I have a request for you – if you are going to update some stuff here please
check if the comments in the sources are up to date as well. You may find them
in the aeternity/aesophia repo in priv/stdlib directory. Also, if the
changes are about the builtin functions (ie. these written in FATE VM,
not in Sophia) please remember to update their entries in
aeternity/protocol repo in contracts/sophia.md file. Thanks!
-->

# Standard library

Sophia language offers standard library that consists of following namespaces:


- [Bits](#Bits)
- [String](#String)
- [Bytes](#Bytes)
- [Int](#Int)
- [Address](#Address)
- [Crypto](#Crypto)
- [Auth](#Auth)
- [Oracle](#Oracle)
- [AENS](#AENS)
- [Contract](#Contract)
- [Call](#Call)
- [Chain](#Chain)
- [List](#List)
- [Option](#Option)
- [Func](#Func)
- [Pair](#Pair)
- [Triple](#Triple)
- [BLS12_381](#BLS12_381)

# Builtin namespaces

They are available without any explicit includes.

## Bits

### none
```
Bits.none : bits
```

A bit field with all bits cleared


### all
```
Bits.all : bits
```

A bit field with all bits set


### set
```
Bits.set(b : bits, i : int) : bits
```

Set bit i


### clear
```
Bits.clear(b : bits, i : int) : bits
```

Clear bit i


### test
```
Bits.test(b : bits, i : int) : bool
```

Check if bit i is set


### sum
```
Bits.sum(b : bits) : int
```

Count the number of set bits


### union
```
Bits.union(a : bits, b : bits) : bits
```

Bitwise disjunction


### intersection
```
Bits.intersection(a : bits, b : bits) : bits
```

Bitwise conjunction


### difference
```
Bits.difference(a : bits, b : bits) : bits
```

Each bit is true if and only if it was 1 in `a` and 0 in `b`


## String

### length
```
String.length(s : string) : int
```

Returns the length of a string


### concat
```
String.concat(s1 : string, s2 : string) : string
```

Concatenates two strings


### sha3
```
String.sha3(s : string) : hash
```

Calculates SHA3 sum of a string


### sha256
```
String.sha256(s : string) : hash
```

Calculates SHA256 sum of a string


### blake2b
```
String.blake2b(s : string) : hash
```

Calculates blake2b of a string

## Bytes

### to_int
```
Bytes.to_int(b : bytes(n)) : int
```

Interprets the byte array as a big endian integer


### to_str
```
Bytes.to_str(b : bytes(n)) : string
```

Returns the hexadecimal representation of the byte array


### concat
```
Bytes.concat : (a : bytes(m), b : bytes(n)) => bytes(m + n)
```

Concatenates two byte arrays


### split
```
Bytes.split(a : bytes(m + n)) : bytes(m) * bytes(n)
```

Splits a byte array at given index


## Int

### to_str
```
Int.to_str : int => string
```

Casts integer to string using decimal representation


## Address

### to_str
```
Address.to_str(a : address) : string
```

Base58Check encoded string


### is_contract
```
Address.is_contract(a : address) : bool
```

Is the address a contract


### is_oracle
```
Address.is_oracle(a : address) : bool
```

Is the address a registered oracle


### is_payable
```
Address.is_payable(a : address) : bool
```

Can the address be spent to


### to_contract
```
Address.to_contract(a : address) : C
```

Cast address to contract type C (where `C` is a contract)


## Crypto

### sha3
```
Crypto.sha3(x : 'a) : hash
```

Hash any object to SHA3


### sha256
```
Crypto.sha256(x : 'a) : hash
```

Hash any object to SHA256


### blake2b
```
Crypto.blake2b(x : 'a) : hash
```

Hash any object to blake2b


### verify_sig
```
Crypto.verify_sig(msg : hash, pubkey : address, sig : signature) : bool
```

Checks if the signature of `msg` was made using private key corresponding to
the `pubkey`

### ecverify_secp256k1
```
Crypto.ecverify_secp256k1(msg : hash, addr : bytes(20), sig : bytes(65)) : bool
```

Verifies a signature for a msg against an Ethereum style address


### ecrecover_secp256k1
```
Crypto.ecrecover_secp256k1(msg : hash, sig : bytes(65)) : option(bytes(20))
```

Recovers the Ethereum style address from a msg hash and respective signature


### verify_sig_secp256k1
```
Crypto.verify_sig_secp256k1(msg : hash, pubkey : bytes(64), sig : bytes(64)) : bool
```
<!-- TODO -->


## Auth

### tx_hash
```
Auth.tx_hash : option(hash)
```

Gets the transaction hash during authentication.


## Oracle

### register
```
Oracle.register(<signature : bytes(64)>, acct : address, qfee : int, ttl : Chain.ttl) : oracle('a, 'b)
```

Registers new oracle answering questions of type `'a` with answers of type `'b`.

* The `acct` is the address of the oracle to register (can be the same as the contract).
* `signature` is a signature proving that the contract is allowed to register the account -
  the account address + the contract address (concatenated as byte arrays) is
  signed with the
  private key of the account, proving you have the private key of the oracle to be. If the
  address is the same as the contract `sign` is ignored and can be left out entirely.
* The `qfee` is the minimum query fee to be paid by a user when asking a question of the oracle.
* The `ttl` is the Time To Live for the oracle, either relative to the current
  height (`RelativeTTL(delta)`) or a fixed height (`FixedTTL(height)`).
* The type `'a` is the type of the question to ask.
* The type `'b` is the type of the oracle answers.

Examples:
```
  Oracle.register(addr0, 25, RelativeTTL(400))
  Oracle.register(addr1, 25, RelativeTTL(500), signature = sign1)
```


### get_question
```
Oracle.get_question(o : oracle('a, 'b), q : oracle_query('a, 'b)) : 'a
```

Checks what was the question of query `q` on oracle `o`


### respond
```
Oracle.respond(<signature : bytes(64)>, o : oracle('a, 'b), q : oracle_query('a, 'b), 'b) : unit
```

Responds to the question `q` on `o`.
Unless the contract address is the same as the oracle address the `signature`
(which is an optional, named argument)
needs to be provided. Proving that we have the private key of the oracle by
signing the oracle query id + contract address


### extend
```
Oracle.extend(<signature : bytes(64)>, o : oracle('a, 'b), ttl : Chain.ttl) : unit
```

Extends TTL of an oracle.
* `signature` is a named argument and thus optional. Must be the same as for `Oracle.register`
* `o` is the oracle being extended
* `ttl` must be `RelativeTTL`. The time to live of `o` will be extended by this value.

### query_fee
```
Oracle.query_fee(o : oracle('a, 'b)) : int
```

Returns the query fee of the oracle


### query
```
Oracle.query(o : oracle('a, 'b), q : 'a, qfee : int, qttl : Chain.ttl, rttl : Chain.ttl) : oracle_query('a, 'b)
```

Asks the oracle a question.
* The `qfee` is the query fee debited to the contract account (`Contract.address`).
* The `qttl` controls the last height at which the oracle can submit a response
  and can be either fixed or relative.
* The `rttl` must be relative and controls how long an answer is kept on the chain.
The call fails if the oracle could expire before an answer.


### get_answer
```
Oracle.get_answer(o : oracle('a, 'b), q : oracle_query('a, 'b)) : option('b)
```

Checks what is the optional query answer


### check
```
Oracle.check(o : oracle('a, 'b)) : bool
```

Returns `true` iff the oracle `o` exists and has correct type


### check_query
```
Oracle.check_query(o : oracle('a, 'b), q : oracle_query('a, 'b)) : bool
```

It returns `true` iff the oracle query exist and has the expected type.


## AENS

The following functionalities are available for interacting with the Aeternity
Naming System (AENS).
If `owner` is equal to `Contract.address` the signature `signature` is
ignored, and can be left out since it is a named argument. Otherwise we need
a signature to prove that we are allowed to do AENS operations on behalf of
`owner`

### resolve
```
AENS.resolve(name : string, key : string) : option('a)
```

Name resolution. Here `name` should be a registered name and `key` one of the attributes
associated with this name (for instance `"account_pubkey"`). The return type
(`'a`) must be resolved at compile time to an atomic type and the value is
type checked against this type at run time.


### preclaim
```
AENS.preclaim(owner : address, commitment_hash : hash, <signature : signature>) : unit
```

The signature should be over `owner address` + `Contract.address`
(concatenated as byte arrays).


### claim
```
AENS.claim(owner : address, name : string, salt : int, name_fee : int, <signature : signature>) : unit
```

The signature should be over `owner address` + `name_hash` + `Contract.address`
using the private key of the `owner` account for signing.


### transfer
```
AENS.transfer(owner : address, new_owner : address, name_hash : hash, <signature : signature>) : unit
```

Transfers name to the new owner.

The signature should be over `owner address` + `name_hash` + `Contract.address`
using the private key of the `owner` account for signing.


### revoke
```
AENS.revoke(owner : address, name_hash : hash, <signature : signature>) : unit
```

Revokes the name to extend the ownership time.

The signature should be over `owner address` + `name_hash` + `Contract.address`
using the private key of the `owner` account for signing.


## Contract

Values related to the current contract

### creator
```
Contract.creator : address
```

Address of the entity that signed the contract creation transaction


### address
```
Contract.address : address
```

Address of the contract account


### balance
```
Contract.balance : int
```

Amount of coins in the contract account


## Call

Values related to the call to the current contract

### origin
```
Call.origin : address
```

The address of the account that signed the call transaction that led to this call.


### caller
```
Call.caller : address
```

The address of the entity (possibly another contract) calling the contract.

### value
```
Call.value : int
```

The amount of coins transferred to the contract in the call.


### gas
```
Call.gas_price : int
```

The gas price of the current call.


### gas
```
Call.gas_left() : int
```

The amount of gas left for the current call.


## Chain

Values and functions related to the chain itself and other entities that live on it.

### balance
```
Chain.balance(a : address) : int
```

The balance of account `a`.


### block_hash
```
Chain.block_hash(h : int) : option(bytes(32))
```

The hash of the block at height `h`.


### block_height
```
Chain.block_height : int"
```

The height of the current block (i.e. the block in which the current call will be included).


### coinbase
```
Chain.coinbase : address
```

The address of the account that mined the current block.


### timestamp
```
Chain.timestamp : int
```

The timestamp of the current block.


### difficulty
```
Chain.difficulty : int
```

The difficulty of the current block.


### gas
```
Chain.gas_limit : int
```

The gas limit of the current block.


# Includable namespaces

These need to be explicitly included (with `.aes` suffix)

## List

This module contains common operations on lists like constructing, querying, traversing etc.

### is_empty
```
List.is_empty(l : list('a)) : bool
```

Returns `true` iff the list is equal to `[]`.


### first
```
List.first(l : list('a)) : option('a)
```

Returns `Some` of the first element of a list or `None` if the list is empty.


### tail
```
List.tail(l : list('a)) : option(list('a))
```

Returns `Some` of a list without its first element or `None` if the list is empty.


### last
```
List.last(l : list('a)) : option('a)
```

Returns `Some` of the last element of a list or `None` if the list is empty.


### find
```
List.find(p : 'a => bool, l : list('a)) : option('a)
```

Finds first element of `l` fulfilling predicate `p` as `Some` or `None` if no such element exists.


### find_indices
```
List.find_indices(p : 'a => bool, l : list('a)) : list(int)
```

Returns list of all indices of elements from `l` that fulfill the predicate `p`.


### nth
```
List.nth(n : int, l : list('a)) : option('a)
```

Gets `n`th element of `l` as `Some` or `None` if `l` is shorter than `n + 1` or `n` is negative.


### get
```
List.get(n : int, l : list('a)) : 'a
```

Gets `n`th element of `l` forcefully, throwing and error if `l` is shorter than `n + 1` or `n` is negative.


### length
```
List.length(l : list('a)) : int
```

Returns length of a list.


### from_to
```
List.from_to(a : int, b : int) : list(int)
```

Creates an ascending sequence of all integer numbers between `a` and `b` (including `a` and `b`).


### from_to_step
```
List.from_to_step(a : int, b : int, step : int) : list(int)
```

Creates an ascending sequence of integer numbers betweeen `a` and `b` jumping by given `step`. Includes `a` and takes `b` only if `(b - a) mod step == 0`. `step` should be bigger than 0.


### replace_at
```
List.replace_at(n : int, e : 'a, l : list('a)) : list('a)
```

Replaces `n`th element of `l` with `e`. Throws an error if `n` is negative or would cause an overflow.


### insert_at
```
List.insert_at(n : int, e : 'a, l : list('a)) : list('a)
```

Inserts `e` into `l` to be on position `n` by shifting following elements further. For instance,
```
insert_at(2, 9, [1,2,3,4])
```
will yield `[1,2,9,3,4]`.


### insert_by
```
List.insert_by(cmp : (('a, 'a) => bool), x : 'a, l : list('a)) : list('a)
```

Assuming that cmp represents `<` comparison, inserts `x` before the first element in the list `l` which is greater than it. For instance,
```
insert_by((a, b) => a < b, 4, [1,2,3,5,6,7])
```
will yield `[1,2,3,4,5,6,7]`


### foldr
```
List.foldr(cons : ('a, 'b) => 'b, nil : 'b, l : list('a)) : 'b
```

Right fold of a list. Assuming `l = [x, y, z]` will return `f(x, f(y, f(z, nil)))`.
Not tail recursive.


### foldl
```
List.foldl(rcons : ('b, 'a) => 'b, acc : 'b, l : list('a)) : 'b
```

Left fold of a list. Assuming `l = [x, y, z]` will return `f(f(f(acc, x), y), z)`.
Tail recursive.

### foreach
```
List.foreach(l : list('a), f : 'a => unit) : unit
```

Evaluates `f` on each element of a list.


### reverse
```
List.reverse(l : list('a)) : list('a)
```

Returns a copy of `l` with reversed order of elements.


### map
```
List.map(f : 'a => 'b, l : list('a)) : list('b)
```

Maps function `f` over a list. For instance
```
map((x) => x == 0, [1, 2, 0, 3, 0])
```
will yield `[false, false, true, false, true]`


### flat_map
```
List.flat_map(f : 'a => list('b), l : list('a)) : list('b)
```

Maps `f` over a list and then flattens it. For instance
```
flat_map((x) => [x, x * 10], [1, 2, 3])
```
will yield `[1, 10, 2, 20, 3, 30]`


### filter
```
List.filter(p : 'a => bool, l : list('a)) : list('a)
```

Filters out elements of `l` that fulfill predicate `p`. For instance
```
filter((x) => x > 0, [-1, 1, -2, 0, 1, 2, -3])
```
will yield `[1, 1, 2]`


### take
```
List.take(n : int, l : list('a)) : list('a)
```

Takes `n` first elements of `l`. Fails if `n` is negative. If `n` is greater than length of a list it will return whole list.


### drop
```
List.drop(n : int, l : list('a)) : list('a)
```

Removes `n` first elements of `l`. Fails if `n` is negative. If `n` is greater than length of a list it will return `[]`.


### take_while
```
List.take_while(p : 'a => bool, l : list('a)) : list('a)
```

Returns longest prefix of `l` in which all elements fulfill `p`.


### drop_while
```
List.drop_while(p : 'a => bool, l : list('a)) : list('a)
```

Removes longest prefix from `l` in which all elements fulfill `p`.


### partition
```
List.partition(p : 'a => bool, l : list('a)) : (list('a) * list('a))
```

Separates elements of `l` that fulfill `p` and these that do not. Elements fulfilling predicate will be in the right list. For instance
```
partition((x) => x > 0, [-1, 1, -2, 0, 1, 2, -3])
```
will yield `([1, 1, 2], [-1, -2, 0, -3])`


### flatten
```
List.flatten(ll : list(list('a))) : list('a)
```

Flattens a list of lists into a one list.


### all
```
List.all(p : 'a => bool, l : list('a)) : bool
```

Checks if all elements of a list fulfill predicate `p`.


### any
```
List.any(p : 'a => bool, l : list('a)) : bool
```

Checks if any element of a list fulfills predicate `p`.


### sum
```
List.sum(l : list(int)) : int
```

Sums elements of a list. Returns 0 if the list is empty.


### product
```
List.product(l : list(int)) : int
```

Multiplies elements of a list. Returns 1 if the list is empty.


### zip_with
```
List.zip_with(f : ('a, 'b) => 'c, l1 : list('a), l2 : list('b)) : list('c)
```

"zips" two lists with a function. n-th element of resulting list will be equal to `f(x1, x2)` where `x1` and `x2` are n-th elements of `l1` and `l2` respectively. Will cut off the tail of the longer list. For instance
```
zip_with((a, b) => a + b, [1,2], [1,2,3])
```
will yield `[2,4]`


### zip
```
List.zip(l1 : list('a), l2 : list('b)) : list('a * 'b)
```

Special case of [zip_with](#zip_with) where the zipping function is `(a, b) => (a, b)`.

### unzip
```
List.unzip(l : list('a * 'b)) : list('a) * list('b)
```

Opposite to the `zip` operation. Takes a list of pairs and returns pair of lists with respective elements on same indices.


### sort
```
List.sort(lesser_cmp : ('a, 'a) => bool, l : list('a)) : list('a)
```

Sorts a list using given comparator. `lesser_cmp(x, y)` should return `true` iff `x < y`. If `lesser_cmp` is not transitive or there exists an element `x` such that `lesser_cmp(x, x)` or there exists a pair of elements `x` and `y` such that `lesser_cmp(x, y) && lesser_cmp(y, x)` then the result is undefined. Currently O(n^2).


### intersperse
```
List.intersperse(delim : 'a, l : list('a)) : list('a)
```

Intersperses elements of `l` with `delim`. Does nothing on empty lists and singletons. For instance
```
intersperse(0, [1, 2, 3, 4])
```
will yield `[1, 0, 2, 0, 3, 0, 4]`


### enumerate
```
List.enumerate(l : list('a)) : list(int * 'a)
```

Equivalent to [zip](#zip) with `[0..length(l)]`, but slightly faster.


## Option

Common operations on `option` types and lists of `option`s.

### is_none
```
Option.is_none(o : option('a)) : bool
```

Returns true iff `o == None`


### is_some
```
Option.is_some(o : option('a)) : bool
```

Returns true iff `o` is not `None`.


### match
```
Option.match(n : 'b, s : 'a => 'b, o : option('a)) : 'b
```

Behaves like pattern matching on `option` using two case functions.


### default
```
Option.default(def : 'a, o : option('a)) : 'a
```

Escapes `option` wrapping by providing default value for `None`.


### force
```
Option.force(o : option('a)) : 'a
```

Forcefully escapes `option` wrapping assuming it is `Some`. Throws error on `None`.


### on_elem
```
Option.on_elem(o : option('a), f : 'a => unit) : unit
```

Evaluates `f` on element under `Some`. Does nothing on `None`.


### map
```
Option.map(f : 'a => 'b, o : option('a)) : option('b)
```

Maps element under `Some`. Leaves `None` unchanged.


### map2
```
Option.map2(f : ('a, 'b) => 'c, o1 : option('a), o2 : option('b)) : option('c)
```

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
```
Option.map3(f : ('a, 'b, 'c) => 'd, o1 : option('a), o2 : option('b), o3 : option('c)) : option('d)
```

Same as [map2](#map2) but with arity 3 function.


### app_over
```
Option.app_over(f : option ('a => 'b), o : option('a)) : option('b)
```

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
```
Option.flat_map(f : 'a => option('b), o : option('a)) : option('b)
```

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
```
Option.to_list(o : option('a)) : list('a)
```

Turns `o` into an empty (if `None`) or singleton (if `Some`) list.


### filter_options
```
Option.filter_options(l : list(option('a))) : list('a)
```

Removes `None`s from list and unpacks all remaining `Some`s. For instance
```
filter_options([Some(1), None, Some(2)])
```
will yield `[1, 2]`.


### seq_options
```
Option.seq_options(l : list (option('a))) : option (list('a))
```

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
```
Option.choose(o1 : option('a), o2 : option('a)) : option('a) 
```

Out of two `option`s choose the one that is `Some`, or `None` if both are `None`s.


### choose_first
```
Option.choose_first(l : list(option('a))) : option('a)
```

Same as [choose](#choose), but chooses from a list insted of two arguments.


## Func

Functional combinators.

### id
```
Func.id(x : 'a) : 'a
```

Identity function. Returns its argument.


### const
```
Func.const(x : 'a) : 'b => 'a = (y) => x
```

Constant function constructor. Given `x` returns a function that returns `x` regardless of its argument.


### flip
```
Func.flip(f : ('a, 'b) => 'c) : ('b, 'a) => 'c
```

Switches order of arguments of arity 2 function.


### comp
```
Func.comp(f : 'b => 'c, g : 'a => 'b) : 'a => 'c
```

Function composition. `comp(f, g)(x) == f(g(x))`.


### pipe
```
Func.pipe(f : 'a => 'b, g : 'b => 'c) : 'a => 'c
```

Flipped function composition. `pipe(f, g)(x) == g(f(x))`.


### rapply
```
Func.rapply(x : 'a, f : 'a => 'b) : 'b
```

Reverse application. `rapply(x, f) == f(x)`.


### recur
```
Func.recur(f : ('arg => 'res, 'arg) => 'res) : 'arg => 'res
```

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
```
Func.iter(n : int, f : 'a => 'a) : 'a => 'a
```

`n`th composition of f with itself, for instance `iter(3, f)` is equivalent to `(x) => f(f(f(x)))`.


### curry
```
Func.curry2(f : ('a, 'b) => 'c) : 'a => ('b => 'c)
Func.curry3(f : ('a, 'b, 'c) => 'd) : 'a => ('b => ('c => 'd))
```

Turns a function that takes n arguments into a curried function that takes 
one argument and returns a function that waits for the rest in the same
manner. For instance `curry2((a, b) => a + b)(1)(2) == 3`.


### uncurry
```
Func.uncurry2(f : 'a => ('b => 'c)) : ('a, 'b) => 'c
Func.uncurry3(f : 'a => ('b => ('c => 'd))) : ('a, 'b, 'c) => 'd
```

Opposite to [curry](#curry).


### tuplify
```
Func.tuplify2(f : ('a, 'b) => 'c) : (('a * 'b)) => 'c
Func.tuplify3(f : ('a, 'b, 'c) => 'd) : 'a * 'b * 'c => 'd
```

Turns a function that takes n arguments into a function that takes an n-tuple.


### untuplify
```
Func.untuplify2(f : 'a * 'b => 'c) : ('a, 'b) => 'c
Func.untuplify3(f : 'a * 'b * 'c => 'd) : ('a, 'b, 'c) => 'd
```

Opposite to [tuplify](#tuplify).


## Pair

Common operations on 2-tuples.

### fst
```
Pair.fst(t : ('a * 'b)) : 'a
```

First element projection.


### snd
```
Pair.snd(t : ('a * 'b)) : 'b
```

Second element projection.


### map1
```
Pair.map1(f : 'a => 'c, t : ('a * 'b)) : ('c * 'b)
```

Applies function over first element.


### map2
```
Pair.map2(f : 'b => 'c, t : ('a * 'b)) : ('a * 'c)
```

Applies function over second element.


### bimap
```
Pair.bimap(f : 'a => 'c, g : 'b => 'd, t : ('a * 'b)) : ('c * 'd)
```

Applies functions over respective elements.


### swap
```
Pair.swap(t : ('a * 'b)) : ('b * 'a)
```

Swaps elements.


## Triple

### fst
```
Triple.fst(t : ('a * 'b * 'c)) : 'a
```

First element projection.


### snd
```
Triple.snd(t : ('a * 'b * 'c)) : 'b
```

Second element projection.


### thd
```
Triple.thd(t : ('a * 'b * 'c)) : 'c
```

Third element projection.


### map1
```
Triple.map1(f : 'a => 'm, t : ('a * 'b * 'c)) : ('m * 'b * 'c)
```

Applies function over first element.


### map2
```
Triple.map2(f : 'b => 'm, t : ('a * 'b * 'c)) : ('a * 'm * 'c)
```

Applies function over second element.


### map3
```
Triple.map3(f : 'c => 'm, t : ('a * 'b * 'c)) : ('a * 'b * 'm)
```

Applies function over third element.


### trimap
```
Triple.trimap(f : 'a => 'x, g : 'b => 'y, h : 'c => 'z, t : ('a * 'b * 'c)) : ('x * 'y * 'z)
```

Applies functions over respective elements.


### swap
```
Triple.swap(t : ('a * 'b * 'c)) : ('c * 'b * 'a)
```

Swaps first and third element.


### rotr
```
Triple.rotr(t : ('a * 'b * 'c)) : ('c * 'a * 'b)
```

Cyclic rotation of the elements to the right.


### rotl
```
Triple.rotl(t : ('a * 'b * 'c)) : ('b * 'c * 'a)
```

Cyclic rotation of the elements to the left.

## BLS12\_381

### Types
- `fp // Built-in (Montgomery) integer representation 32 bytes`
- `fr // Built-in (Montgomery) integer representation 48 bytes`
- `record fp2 = { x1 : fp, x2 : fp }`
- `record g1  = { x : fp, y : fp, z : fp }`
- `record g2  = { x : fp2, y : fp2, z : fp2 }`
- `record gt  = { x1 : fp, x2 : fp, x3 : fp, x4 : fp, x5 : fp, x6 : fp, x7 : fp, x8 : fp, x9 : fp, x10 : fp, x11 : fp, x12 : fp }`

### pairing\_check
```
BLS12_381.pairing_check(xs : list(g1), ys : list(g2)) : bool
```

Pairing check of a list of points, `xs` and `ys` should be of equal length.

### int_to_fr
```
BLS12_381.int_to_fr(x : int) : fr
```

Convert an integer to an `fr` - a 32 bytes internal (Montgomery) integer representation.

### int_to_fp
```
BLS12_381.int_to_fp(x : int) : fp
```

Convert an integer to an `fp` - a 48 bytes internal (Montgomery) integer representation.

### fr_to_int
```
BLS12_381.fr_to_int(x : fr)  : int
```

Convert a `fr` value into an integer.

### fp_to_int
```
BLS12_381.fp_to_int(x : fp)  : int
```

Convert a `fp` value into an integer.

### mk_g1
```
BLS12_381.mk_g1(x : int, y : int, z : int) : g1
```

Construct a `g1` point from three integers.

### mk_g2
```
BLS12_381.mk_g2(x1 : int, x2 : int, y1 : int, y2 : int, z1 : int, z2 : int) : g2
```

Construct a `g2` point from six integers.

### g1_neg
```
BLS12_381.g1_neg(p : g1) : g1
```

Negate a `g1` value.

### g1_norm
```
BLS12_381.g1_norm(p : g1) : g1
```

Normalize a `g1` value.

### g1_valid
```
BLS12_381.g1_valid(p : g1) : bool
```

Check that a `g1` value is a group member.

### g1_is_zero
```
BLS12_381.g1_is_zero(p : g1) : bool
```

Check if a `g1` value corresponds to the zero value of the group.

### g1_add
```
BLS12_381.g1_add(p : g1, q : g1) : g1
```

Add two `g1` values.

### g1_mul
```
BLS12_381.g1_mul(k : fr, p : g1) : g1
```

Scalar multiplication for `g1`.

### g2_neg
```
BLS12_381.g2_neg(p : g2) : g2
```

Negate a `g2` value.

### g2_norm
```
BLS12_381.g2_norm(p : g2) : g2
```

Normalize a `g2` value.

### g2_valid
```
BLS12_381.g2_valid(p : g2) : bool
```

Check that a `g2` value is a group member.

### g2_is_zero
```
BLS12_381.g2_is_zero(p : g2) : bool
```

Check if a `g2` value corresponds to the zero value of the group.

### g2_add
```
BLS12_381.g2_add(p : g2, q : g2) : g2
```

Add two `g2` values.

### g2_mul
```
BLS12_381.g2_mul(k : fr, p : g2) : g2
```

Scalar multiplication for `g2`.

### gt_inv
```
BLS12_381.gt_inv(p : gt) : gt
```

Invert a `gt` value.

### gt_add
```
BLS12_381.gt_add(p : gt, q : gt) : gt
```

Add two `gt` values.

### gt_mul
```
BLS12_381.gt_mul(p : gt, q : gt) : gt
```

Multiply two `gt` values.

### gt_pow
```
BLS12_381.gt_pow(p : gt, k : fr) : gt
```

Calculate exponentiation `p ^ k`.

### gt_is_one
```
BLS12_381.gt_is_one(p : gt) : bool
```

Compare a `gt` value to the unit value of the Gt group.

### pairing
```
BLS12_381.pairing(p : g1, q : g2) : gt
```

Compute the pairing of a `g1` value and a `g2` value.

### miller_loop
```
BLS12_381.miller_loop(p : g1, q : g2) : gt
```

Do the Miller loop stage of pairing for `g1` and `g2`.

### final_exp
```
BLS12_381.final_exp(p : gt) : gt
```

Perform the final exponentiation step of pairing for a `gt` value.
