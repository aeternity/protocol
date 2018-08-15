[back](./contracts.md)
## The Sophia Language
An Æternity BlockChain Language
The Sophia is a language in the ML family. It is strongly typed and has
restricted mutable state.

Sophia is customized for smart contracts, which can be published
to a blockchain (the Æternity BlockChain). Thus some features of conventional
languages, such as floating point arithmetic, are not present in Sophia, and
some blockchain specific primitives, constructions and types have been added.

## Language Features
### Contracts

Sophia does not have modules. Instead sophia has static
contracts. Contracts are similar to classes in object oriented
languages and support local state and inheritance. More specifically:

- A contract implementation, or simply a contract, is the code for a
  smart contract and consists of a list of types and functions that
  may or may not have a definition. A contract where all types and
  functions are defined is called a concrete contract. Only concrete
  contracts can be instantiated. (Used in a create contract transaction.)

- A contract can be abstract where no types or functions have definitions. Example:

```javascript
// An abstract contract
contract VotingType =
  public stateful function vote : string => unit
```

- A contract instance is an entity living on the block chain (or in a state channel). Each
instance is associated with a particular contract implementation (at
least from the view of high-level language; the low-level details of
how to store and check API information on the chain is still to be
worked out).
- A contract may define a type state encapsulating its local
  state. The state must be initialised when instantiating a
  contract. This is done by the init function which can take arbitrary
  arguments and is called on contract instance creation.
- Contracts have a public API, comprising the functions and types
  annotated with the public keyword. These can be used from outside
  the contract. Functions and types with no annotation (or internal)
  are part of the internal API and can be used by contracts inheriting
  (see below) the given contract. Functions and types annotated with
  private can only be used locally.
- Contracts can inherit one (or more?) other contract(s). In this case
  the public functions (and types) of the inherited contract are
  included in the public API and internal functions are included in
  the internal API of the current contract. The state of the contract
  contains the states of all inherited contracts as well as the local
  state. However, the state of an inherited contract cannot be
  accessed other than through internal functions defined by that
  contract.
- Open question: should we allow overriding defined functions? I would
  suggest no, but there might be compelling use cases that I'm
  missing.

*NOTE: Contract inheritance is not yet implemented.*

### Mutable state

Sophia does not have arbitrary mutable state, but only a limited form of
state associated with each contract instance.

- Each contract defines a type `state` encapsulating its mutable state.
- The initial state of a contract is computed by the contract's `init`
  function. The `init` function is *pure* and returns the initial state as its
  return value. At contract creation time, the `init` function is executed and
  its result is stored as the contract state.
- The value of the state is accessible from inside the contract
  through an implicitly bound variable `state`.
- State updates are performed by calling a function `put : state => unit`.
- Aside from the `put` function (and similar functions for transactions
  and events), the language is purely functional.
- Functions modifying the state need to be annotated with the `stateful` keyword.

To make it convenient to update parts of a deeply nested state Sophia
provides special syntax for map/record updates.  Open
question: we likely want to make it possible to have immutable state
(parameters). Keep separate from mutable state or annotate certain
fields as immutable?

### Types
Sophia has the following types:

| Type       | Description                     | Example
| ---------- | ------------------------------- | -------:
| uint       | A 256 bit integer               | ```42```
| int        | A 256 bit 2-complement integer  | ```-1```
| address    | A 256 bit number given as a hex | ```ff00```
| bool       | A Boolean                       | ```true```
| string     | An array of bytes               | ```"Foo"```
| list       | A homogeneous immutable singly linked list. | ```[1, 2, 3]```
| tuple      | An ordered heterogeneous array   | ```(42, "Foo", true)```
| record     | An immutable key value store with fixed key names and typed values | ``` record balance = { owner: address, value: uint } ```
| map        | An immutable key value store with dynamic mapping of keys of one type to values of one type | ```type accounts = map(string, address)```
| option('a) | An optional value either None or Some('a) | ```Some(42)```
| state        | A record of blockstate key, value pairs  |
| transactions | An append only list of blockchain transactions |
| events       | An append only list of blockchain events (or log entries) |
| signature    | A signature. |
| oracle('a, 'b)       | And oracle answering questions of type 'a with answers of type 'b |  ```Oracle.register(acct, sign, qfee, ttl)```
| oracle_query('a, 'b) | A specific oracle query |  ```Oracle.query(o, q, qfee, qttl, rttl)```


### Algebraic data types

Sophia supports algebraic data types (variant types) and pattern matching. Data
types can be recursive and are declared by giving a list of constructors with
their respective arguments. For instance, the following defines a type of
binary trees parameterised over the element type:

```
datatype tree('a) = Tip | Bin(tree('a), 'a, tree('a))
```

Elements of data types can be pattern matched against, using the `switch` construct:

```
function root(t : tree('a)) : option('a) =
  switch(t)
    Tip => None
    Bin(_, v, _) => Some(v)
```

*NOTE: Recursive data types are not yet implemented*

### Lists

A Sophia list is a dynamically sized, homogenous, immutable, singly
linked list. A list is constructed with the syntax `[1, 2, 3]`. The
elements of a list can be any of datatype so for example we can have
the following lists:

```
[1, 33, 2, 666]
[(1, "aaa"), (10, "jjj"), (666, "the beast")]
[{ [1] = "aaa", [10] = "jjj"}, { [5] = "eee", [666] = "the beast"}]
```

New elements can be prepended to the front of a list with the `::`
operator. So `42 :: [1, 2, 3]` returns the list `[42, 1, 2, 3]`. The
concatenation operator `++` appends its second argument to its first
and returns the resulting list. So concatenating two lists
`[1, 22, 33] ++ [10, 18, 55]` returns the list `[1, 22, 33, 10, 18, 55]`.

### Maps and records

A Sophia record type is given by a fixed set of fields with associated,
possibly different, types. For instance
```
  record account = { name    : string,
                     balance : int,
                     history : list(transaction) }
```

Maps, on the other hand, can contain an arbitrary number of key-value bindings,
but of a fixed type. The type of maps with keys of type `'k` and values of type
`'v` is written `map('k, 'v)`. Key types are restricted to atomic types (`int`,
`address`, `bool`, and `string`).

#### Constructing maps and records

A value of record type is constructed by giving a value for each of the fields.
For the example above,
```
  function new_account(name) =
    {name = name, balance = 0, history = []}
```
Maps are constructed similarly, with keys enclosed in square brackets
```
  function example_map() : map(string, int) =
    {["key1"] = 1, ["key2"] = 2}
```
The empty map is written `{}`.

#### Accessing values

Record fields access is written `r.f` and map lookup `m[k]`. For instance,
```
  function get_balance(a : address, accounts : map(address, account)) =
    accounts[a].balance
```
Looking up a non-existing key in a map results in the contract failing. See
`Map.member` and `Map.lookup` below for safe lookups.

#### Updating a value

Record field updates are written `r{f = v}`. This creates a new record value
which is the same as `r`, but with the value of the field `f` replaced by `v`.
Similarly, `m{[k] = v}` constructs a map with the same values as `m` except
that `k` maps to `v`. It makes no difference if `m` has a mapping for `k` or
not.

It is possible to give a name to the old value of a field or mapping in an
update: instead of `acc{ balance = acc.balance + 100 }` it is possible to write
`acc{ balance @ b = b + 100 }`, binding `b` to `acc.balance`. When giving a
name to a map value (`m{ [k] @ x = v }`), the corresponding key must be present
in the map or the contract will fail.

Updates can be nested:
```
function clear_history(a : address, accounts : map(address, account)) : map(address, account) =
  accounts{ [a].history = [] }
```
This is equivalent to `accounts{ [a] @ acc = acc{ history = [] } }` and thus
requires `a` to be present in the accounts map.


#### Builtin functions on maps

The following builtin functions are defined on maps:

```
  Map.lookup(k : 'k, m : map('k, 'v)) : option('v)
  Map.member(k : 'k, m : map('k, 'v)) : bool
  Map.delete(k : 'k, m : map('k, 'v)) : map('k, 'v)
  Map.size(m : map('k, 'v)) : int
  Map.to_list(m : map('k, 'v)) : list(('k, 'v))
  Map.from_list(m : list(('k, 'v))) : map('k, 'v)
```

### Builtins

#### Account interface

To spend tokens from the contract account to the account "to" you call the raw_spend function.

```
raw_spend(to : address, amount : integer)
```

#### Oracle interface
You can attach an oracle to the current contract and you can interact with oracles
through the Oracle interface.

For a full description of how Oracle works see [Oracles](/oracles/oracles.md#oracles)

An Oracle operator will use the functions:
* `Oracle.register`
* `Oracle.get_question`
* `Oracle.respond`
* `Oracle.extend`

An Oracle user will use the functions:
* `Oracle.query_fee`
* `Oracle.query`
* `Oracle.get_answer`

##### Oracle register

To register a new oracle answering questions of type `'a` with answers of type `'b`,
call `Oracle.register`:
```
Oracle.register(acct : address
                sign : signature,   // Signed account address
                qfee : int,
                ttl  : int) : oracle('a, 'b)
```

* The `acct` is the address of the oracle to register (can be the same as the contract).
* The `sign` is a signature of the address to register proving you have the private key
  of the oracle, or the integer 0 when address is the same as the contract.
* The `qfee` is the minimum query fee to be paid by a user when asking a question of the oracle.
* The `ttl` is the Time To Live in relative block height for the oracle.
* The type `'a` is the type of the question to ask.
* The type `'b` is the type of the oracle answers.

##### Oracle extend

To extend the TTL of an oracle, call `Oracle.extend`:
```
Oracle.extend(o    : oracle('a, 'b),
              sign : signature,   // Signed oracle address
              ttl  : int) : ()
```

##### Oracle get_question

To check what the question of a query is, use the `Oracle.get_question` function:
```
Oracle.get_question(o : oracle('a, 'b), q : oracle_query('a, 'b)) : 'a
```

##### Oracle respond

To respond to an oracle question, use the `Oracle.respond` function:
```
Oracle.respond(o    : oracle('a, 'b),
               q    : oracle_query('a, 'b),
               sign : signature,
               r    : 'b)
```

##### Oracle query

To ask an oracle a question, use the `Oracle.query` function:
```
Oracle.query(o    : oracle('a, 'b),
             q    : 'a,
             qfee : int,
             qttl : int,
             rttl : int) : oracle_query('a, 'b)
```

* The `qfee` is the query fee debited to the contract account (`Contract.address`).

##### Oracle query_fee

To ask the oracle what the query fee is, use the `Oracle.query_fee` function:
```
Oracle.query_fee(o : oracle('a, 'b)) : int
```

##### Oracle get_answer

To ask the oracle what the optional query answer is, use the `Oracle.get_answer` function:
```
Oracle.get_answer(o : oracle('a, 'b), q : oracle_query('a, 'b)) : option('b)
```

##### Example

Example for an oracle answering questions of type `string` with answers of type `int`:
```
contract Oracles =

  function registerOracle(acct : address,
                          sign : signature,   // Signed account address
                          qfee : int,
                          ttl  : int) : oracle(string, int) =
     Oracle.register(acct, sign, qfee, ttl)

  function queryFee(o : oracle(string, int)) : int =
    Oracle.query_fee(o)

  // Do not use in production!
  function unsafeCreateQuery(o    : oracle(string, int),
                       q    : string,
                       qfee  : int,
                       qttl : int,
                       rttl : int) : oracle_query(string, int) =
    Oracle.query(o, q, qfee, qttl, rttl)

  function extendOracle(o    : oracle(string, int),
                        sign : signature,   // Signed oracle address
                        ttl  : int) : () =
    Oracle.extend(o, sign, ttl)

  function respond(o    : oracle(string, int),
                   q    : oracle_query(string, int),
                   sign : signature,
                   r    : int) =
    Oracle.respond(o, q, sign, r)

  function getQuestion(o : oracle(string, int),
                       q : oracle_query(string, int)) : string =
    Oracle.get_question(o, q)

  function hasAnswer(o : oracle(string, int),
                     q : oracle_query(string, int)) =
    switch(Oracle.get_answer(o, q))
      None    => false
      Some(_) => true

  function getAnswer(o : oracle(string, int),
                     q : oracle_query(string, int)) : option(int) =
    Oracle.get_answer(o, q)
```

#### AENS interface

The following primitives are available for interacting with the Aeternity
Naming System (AENS):

- Name resolution
  ```
  AENS.resolve(name : string, key : string) : option('a)
  ```
  Here `name` should be a registered name and `key` one of the attributes
  associated with this name (for instance `"account_pubkey"`). The return type
  (`'a`) must be resolved at compile time to an atomic type and the value is
  type checked against this type at run time.
- AENS transactions
  ```
  AENS.preclaim(owner : address, commitment_hash : hash, sig : signature) : ()
  AENS.claim   (owner : address, name : string, salt : int, sig : signature) : ()
  AENS.transfer(owner : address, new_owner : address, name_hash : hash, sig : signature) : ()
  AENS.revoke  (owner : address, name_hash : hash, sig : signature) : ()
  ```
  If `owner` is different from `Contract.address`, `sig` should be a signature
  of the other arguments by the private key of the `owner` account.
  (*TODO: make precise*, *TODO: not implemented*)


#### Events

Sophia contracts log structured messages to an event log in the resulting
blockchain transaction. To use events a contract must declare a type `event`,
and events are then logged using the `event` function:

```
event(e : event) : ()
```

*NOTE: Events are not yet implemented*

#### Transactions
Sophia can generate blockchain transactions.
```
transaction(tx : transaction) : ()
```
The transaction type defines the transactions that can be created:
```
record   spend_tx = {recipient : address, amount : uint}
datatype transaction = SpendTx(spend_tx)
                     | ...
```

*NOTE: Transaction types are not yet implemented. For now spend transactions
can be issued using the builtin function*

```
  raw_spend : (address, int) => ()
```

#### Contract primitives

The block-chain environment available to a contract is defined in three name spaces
`Contract`, `Call`, and `Chain`:

- `Contract.creator` is the address of the entity that signed the contract creation
  transaction.
- `Contract.address` is the address of the contract account.
- `Contract.balance` is the amount of coins currently in the contract account.
  Equivalent to `Chain.get_balance(Contract.address)`.
- `Call.origin` is the address of the account that signed the call transaction that led to this call.
- `Call.caller` is the address of the entity (possibly another contract)
  calling the contract.
- `Call.value` is the amount of coins transferred to the contract in the call.
- `Call.gas_price` is the gas price of the current call.
- `Call.gas_left` is the amount of gas left for the current call.
- `Chain.get_balance(a : address)` returns the balance of account `a`.
- `Chain.block_hash(h)` returns the hash of the block at height `h`.
- `Chain.block_height` is the height of the current block (i.e. the block in which the current call will be included).
- `Chain.coinbase` is the address of the account that mined the current block.
- `Chain.timestamp` is the timestamp of the current block.
- `Chain.difficulty` is the difficulty of the current block.
- `Chain.gas_limit` is the gas limit of the current block.

### Exceptions

Contracts can fail with an (uncatchable) exception using the function

```
abort(reason : string) : 'a
```

## Syntax

### Lexical syntax

#### Comments

Single line comments start with `//` and block comments are enclosed in `/*`
and `*/` and can be nested.

#### Keywords

```
and band bnot bor bsl bsr bxor contract elif else false function if import
internal let mod private public rec stateful switch true type record datatype
```

#### Tokens

- `Id = [a-z_][A-Za-z0-9_']*` identifiers start with a lower case letter.
- `Con = [A-Z][A-Za-z0-9_']*` constructors start with an upper case letter.
- `QId = (Con\.)+Id` qualified identifiers (e.g. `Map.member`)
- `QCon = (Con\.)+Con` qualified constructor
- `TVar = 'Id` type variable (e.g `'a`, `'b`)
- `Int = [0-9]+|0x[0-9A-Fa-f]+` integer literal
- `Hash = #[0-9A-Fa-f]+` hash literal
- `String` string literal enclosed in `"` with escape character `\`
- `Char` character literal enclosed in `'` with escape character `\`

### Layout blocks

Sophia uses Python-style layout rules to group declarations and statements. A
layout block with more than one element must start on a separate line and be
indented more than the currently enclosing layout block. Blocks with a single
element can be written on the same line as the previous token.

Each element of the block must share the same indentation and no part of an
element may be indented less than the indentation of the block. For instance

```
contract Layout =
  function foo() = 0  // no layout
  function bar() =    // layout block starts on next line
    let x = foo()     // indented more than 2 spaces
    x
     + 1              // the '+' is indented more than the 'x'
```

### Notation

In describing the syntax below, we use the following conventions:
- Upper-case identifiers denote non-terminals (like `Expr`) or terminals with
  some associated value (like `Id`).
- Keywords and symbols are enclosed in single quotes: `'let'` or `'='`.
- Choices are separated by vertical bars: `|`.
- Optional elements are enclosed in `[` square brackets `]`.
- `(` Parentheses `)` are used for grouping.
- Zero or more repetitions are denoted by a postfix `*`, and one or more
  repetitions by a `+`.
- `Block(X)` denotes a layout block of `X`s.
- `Sep(X, S)` is short for `[X (S X)*]`, i.e. a possibly empty sequence of `X`s
  separated by `S`s.
- `Sep1(X, S)` is short for `X (S X)*`, i.e. same as `Sep`, but must not be empty.


### Declarations

A Sophia file consists of a sequence of *declarations* in a layout block.

```c
File ::= Block(Decl)
Decl ::= 'contract' Con '=' Block(Decl)
       | 'type'     Id ['(' TVar* ')'] ['=' TypeAlias]
       | 'record'   Id ['(' TVar* ')'] '=' RecordType
       | 'datatype' Id ['(' TVar* ')'] '=' DataType
       | Modifier* 'function' Id ':' Type
       | Modifier* 'function' Id Args [':' Type] '=' Block(Stmt)

Modifier ::= 'stateful' | 'public' | 'private' | 'internal'

Args ::= '(' Sep(Arg, ',') ')'
Arg  ::= Id [':' Type]
```

Contract declarations must appear at the top-level.

For example,
```
contract Test =
  type t = int
  public function add (x : t, y : t) = x + y
```

There are three forms of type declarations: type aliases (declared with the
`type` keyword), record type definitions (`record`) and data type definitions
(`datatype`):

```c
TypeAlias  ::= Type
RecordType ::= '{' Sep(FieldType, ',') '}'
DataType   ::= Sep1(ConDecl, '|')

FieldType  ::= Id ':' Type
ConDecl    ::= Con ['(' Sep1(Type, ',') ')']
```

For example,
```
record   point('a) = {x : 'a, y : 'a}
datatype shape('a) = Circle(point('a), 'a) | Rect(point('a), point('a))
type     int_shape = shape(int)
```

### Types

```c
Type ::= Domain '=>' Type             // Function type
       | Type '(' Sep(Type, ',') ')'  // Type application
       | '(' Type ')'                 // Parens
       | Id | QId | TVar

Domain ::= Type                       // Single argument
         | '(' Sep(Type, ',') ')'     // Multiple arguments
```

The function type arrow associates to the right.

Example,
```
'a => list('a) => (int, list('a))
```

### Statements

Function bodies are blocks of *statements*, where a statement is one of the following

```c
Stmt ::= 'switch' '(' Expr ')' Block(Case)
       | 'if' '(' Expr ')' Block(Stmt)
       | 'elif' '(' Expr ')' Block(Stmt)
       | 'else' Block(Stmt)
       | 'let' LetDef
       | 'let' 'rec' Sep1(LetDef, 'and')  // (Mutually) recursive binding
       | Expr

LetDef ::= Id [Args] [':' Type] '=' Block(Stmt)

Case    ::= Pattern '=>' Block(Stmt)
Pattern ::= Expr
```

`if` statements can be followed by zero or more `elif` statements and an optional final `else` statement. For example,

```
let x : int = 4
switch(f(x))
  None => 0
  Some(y) =>
    if(y > 10)
      "too big"
    elif(y < 3)
      "too small"
    else
      "just right"
```

### Expressions

```c
Expr ::= '(' Args ')' '=>' Block(Stmt)      // Anonymous function    (x) => x + 1
       | 'if' '(' Expr ')' Expr 'else' Expr // If expression         if(x < y) y else x
       | Expr ':' Type                      // Type annotation       5 : uint
       | Expr BinOp Expr                    // Binary operator       x + y
       | UnOp Expr                          // Unary operator        ! b
       | Expr '(' Sep(Expr, ',') ')'        // Application           f(x, y)
       | Expr '.' Id                        // Projection            state.x
       | Expr '[' Expr ']'                  // Map lookup            map[key]
       | Expr '{' Sep(FieldUpdate, ',') '}' // Record or map update  r{ fld[key].x = y }
       | '[' Sep(Expr, ',') ']'             // List                  [1, 2, 3]
       | '{' Sep(FieldUpdate, ',') '}'      // Record or map value   {x = 0, y = 1}, {[key] = val}
       | '(' Expr ')'                       // Parens                (1 + 2) * 3
       | Id | Con | QId | QCon              // Identifiers           x, None, Map.member, AELib.Token
       | Int | Hash | String | Char         // Literals              123, 0xff, #00abc123, "foo", '%'

FieldUpdate ::= Path '=' Expr
Path ::= Id                 // Record field
       | '[' Expr ']'       // Map key
       | Path '.' Id        // Nested record field
       | Path '[' Expr ']'  // Nested map key

BinOp ::= '||' | '&&' | '<' | '>' | '=<' | '>=' | '==' | '!='
        | '::' | '++' | '+' | '-' | '*' | '/' | 'mod'
        | 'bor' | 'bxor' | 'band' | 'bsr' | bsl'
UnOp  ::= '-' | '!' | 'bnot'
```

### Operators types

| Operators | Type
| --- | ---
| `-` `+` `*` `/` `mod` | arithmetic operators
| `bnot` `band` `bor` `bxor` `bsl` `bsr` | bitwise operators
| `!` `&&` `\|\|` | logical operators
| `==` `!=` `<` `>` `=<` `>=` | comparison operators
| `::` `++` | list operators

### Operator precendences

In order of highest to lowest precedence.

| Operators | Associativity
| --- | ---
| `!` `bnot` | right
| `*` `/` `mod` `band` | left
| `-` (unary) | right
| `+` `-` `bor` `bxor` `bsl` `bsr` | left
| `::` `++` | right
| `<` `>` `=<` `>=` `==` `!=` | none
| `&&` | right
| `\|\|` | right

## Examples

```
/*
 * A simple crowd-funding example
 */
contract FundMe =

  record spend_args = { recipient : address,
                        amount    : int }

  record state = { contributions : map(address, int),
                   total         : int,
                   beneficiary   : address,
                   deadline      : int,
                   goal          : int }

  private function abort(err : string) =
    switch(0) 1 => ()

  private function require(b : bool, err : string) =
    if(!b) abort(err)

  private function spend(args : spend_args) =
    raw_spend(args.recipient, args.amount)

  public function init(beneficiary, deadline, goal) : state =
    { contributions = {},
      beneficiary   = beneficiary,
      deadline      = deadline,
      total         = 0,
      goal          = goal }

  private function is_contributor(addr) =
    Map.member(addr, state.contributions)

  public stateful function contribute() =
    if(Chain.block_height >= state.deadline)
      spend({ recipient = Call.caller, amount = Call.value }) // Refund money
      false
    else
      let amount =
        switch(Map.lookup(Call.caller, state.contributions))
          None    => Call.value
          Some(n) => n + Call.value
      put(state{ contributions[Call.caller] = amount,
                 total @ tot = tot + Call.value })
      true

  public stateful function withdraw() =
    if(Chain.block_height < state.deadline)
      abort("Cannot withdraw before deadline")
    if(Call.caller == state.beneficiary)
      withdraw_beneficiary()
    elif(is_contributor(Call.caller))
      withdraw_contributor()
    else
      abort("Not a contributor or beneficiary")

  private stateful function withdraw_beneficiary() =
    require(state.total >= state.goal, "Project was not funded")
    spend({recipient = state.beneficiary,
           amount    = Contract.balance })
    put(state{ beneficiary = #0 })

  private stateful function withdraw_contributor() =
    if(state.total >= state.goal)
      abort("Project was funded")
    let to = Call.caller
    spend({recipient = to,
           amount    = state.contributions[to]})
    put(state{ contributions @ c = Map.delete(to, c) })
```

## The lifetime of a contract

# Killing a contract

There is no selfdestruct instruction in the aevm as in the Ethereum
Virtual Machine instead there is a disable transaction which the
creator of a contract can issue. When a contract is disabled no new
contract can call the old contract.

When a contract is posted to the chain all references to other
contracts are checked and a reference counter in each contract is
increased. You can only post a contract to the chain if all the
contracts referred to are enabled.

When a contract is disabled all other contracts it refer to get their
reference count decreased.

If a contract is disabled and its reference count is zero a miner can
choose to garbage collect the contract.

The reference count of a contract is handled as the account balance
and kept in the state tree of the miner and the merkle hash is
included in the state hash in each block just as with balances.

The transaction for creating a contract has an extra fee called
deposit which has to be an even number. The disable transaction is
free but the miner and the creator get half of the deposit fee each at
contract disable thus encouraging creators to disable their contracts
and miners to pick disable transactions.

## The Sophia_01 ABI

The calldata contains a tuple with function name and argument, e.g. `("main", (1,2,3))`.
The compiler will generate entry code to
load the calldata to memory and then create a pattern matching switch on the function name
and call the function with the second element as the argument:


```
CALLDATASIZE
PUSH1 0
PUSH1 32
CALLDATACOPY  ;; Copy all calldata into address 32 (addr 0 is the state pointer)
```

followed by

```
 switch(CallData)
  ("fun1", arg) => fun1(arg)
  ("fun2", arg) => fun2(arg)
  ...
```

The above could also be implemented as a search tree looking at one
byte at the time of the function hash if that produces smaller
code. The compiler could also choose to truncate the hash to the
shortest unique prefix and shift the incoming hash down. E.g if there
are only three functions in the contract and their hashes starts with
0xA, 0xB nd 0xC respectively.

(Given that the contract invocation checks that the function call is to a valid address/hash before calling AEVM.)

The shortest unique suffix could also be used, and the hash could be ANDed with the suffix length instead.

Then each exported function starts with an exported entry point where it executes
code to fetch the arguments to memory.

### Data memory layout

Data communicated between a contract and the outside world is encoded as binary
block in the VM memory. This includes calldata, contract state, and return
values. The contract is responsible for converting between such binaries and
Sophia values.

Data is encoded in memory as follows:

- Unboxed types (`int`, `address`, and `bool`) are encoded as a single big
  endian 256-bit word (32 bytes).

- Boxed types are encoded as a pointer into a following binary. This binary is encoded as follows:
  - Unboxed types are encoded as a single word.
  - Strings are encoded with a 32 byte length (number of bytes), followed by as few 256-bit words
    as needed padded on the right with 0.
  - Tuples are encoded with one word per component (stored left-to-right) where
    each word is either an unboxed value or a pointer.
  - Lists are encoded by an unboxed -1 word for the empty list and an encoded
    pair of the head and the tail for a cons cell.
  - Records are encoded as a tuple of field values.
  - Maps are encoded as a list of key-value pairs. ***This is subject to change***
  - The order of values is unspecified. For instance, in the encoding of a pair
    of boxed values, the three cells (first component, second component, and
    pair cell) can appear in any order in the encoded binary.
  - The option type is encoded as -1 for `None` and as a singleton tuple `{v}` for `Some(v)`.
  - Values of datatypes are encoded as tuples where the first component is a
    constructor tag (starting with 0 for the first constructor), and the
    following components are the constructor arguments. For instance, for
    ```
      datatype zeroOrTwo = Zero | Two(int, int)
    ```
    `Zero` is encoded as a singleton tuple `{0}` and `Two(a, b)` as the triple `{1, a, b}`.
  - Type representations are encoded as tuples as follows:
    - `word`: `{0}`  (any unboxed type)
    - `string`: `{1}`
    - `list(t)`: `{2, encode(t)}`
    - `tuple(ts)`: `{3, encode(ts)}`, where `ts : list(typerep)`
    - `option(t)`: `{4, encode(t)}`
    - `datatype(cs)`: `{5, encode(cs)}`, where `cs : list(list(typerep))`
      are the type representations for the constructor arguments
- Pointers are relative, with the address of the first word of the data being
  the *base address*. For calldata, the base address is 32 and for return
  values and contract state the base address is 0.



#### Example

A valid encoding of the value `("main", (1, 2, 3))` with base address 32 (`0x20`) would be
```
Word       0       1       2       3       4       5       6       7
Addr    0x20    0x40    0x60    0x80    0xA0    0xC0    0xE0   0x100
Value   0x40    0x80    0xC0       4    "main"     1       2       3
```
(where `"main"` is the 32 byte word obtained by right padding the string
`"main"` with zeroes.)

### Contract state

Before a contract call is executed the current state of the contract is loaded
into memory encoded as described above. A pointer to the encoded state is stored at
address 0. The Sophia compiler generates code to unpack the encoded state and
update the state pointer with a pointer to decoded value. Before returning the
contract should encode the updated state and point the state pointer to the
encoded data. If the call did not update the state the contract can set the
state pointer to 0.

### Local function calls

A local function call pushes the return address then the arguments.
The callee pops the arguments and local variables then swaps the
return address and the return value on the stack and jumps to
the return value leaving only the return value on the stack.

Call id(x):

```
            PUSHx RetAddress
            DUP2              ; Get argument
            PUSHx CalleeAdr
            JUMP

:RetAddress JUMPDEST          ; SP(0) contains ret address.
```

Return:

```
            SWAP1            ; Swap retvalue with first arg (only one arg in this fun)
            POP              ; Drop the argument
            SWAP1            ; Swap retval and retaddress
            JUMP             ; return to the caller

```

