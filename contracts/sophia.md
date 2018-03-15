[back](./contracts.md)
## The Sophia Language
An AEternity BlockChain Language
The Sophia is a language in the ML family. It is strongly typed and has
restricted mutable state.

Sophia is customized for smart contracts, which can be published
to a blockchain (the AEternity BlockChain). Thus some features of conventional
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

### Mutable state

Sophia does not have arbitrary mutable state, but only a limited form of
state associated with each contract instance.

- Each contract defines a state type encapsulating its mutable state.
- The value of the state is accessible from inside the contract
  through an implicitly bound variable `state`.
- State updates are performed by calling a function `put : state => unit`
  (possibly with a better name).
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

| Type    | Description                     | Example
| ------- | ------------------------------- | -------:
| uint    | A 256 bit integer               | ```42```
| int     | A 256 bit 2-complement integer  | ```-1```
| address | A 256 bit number given as a hex | ```ff00```
| bool    | A Boolean                       | ```true```
| string  | An array of bytes               | ```"Foo"```
| list    | A homogeneous immutable singly linked list. | ```[1, 2, 3]```
| tuple   | An ordered heterogeneous array   | ```(42, "Foo", true)```
| record  | An immutable key value store with fixed key names and typed values | ``` type balance = { owner: address, value: uint } ```
| map     | An immutable key value store with dynamic mapping of keys of one type to values of one type | ```type accounts = map(string, address)```
| state   | A record of blockstate key, value pairs  |
| transactions | An append only list of blockchain transactions |
| events   | An append only list of blockchain events (or log entries) |

#### Types not in Sophia
- Arrays
- References
- Objects

### Algebraic data types

Sophia supports algebraic data types (variant types) and pattern matching. Data
types can be recursive and are declared by giving a list of constructors with
their respective arguments. For instance, the following defines a type of
binary trees parameterised over the element type:

```ocaml
type tree('a) = Tip | Bin(tree('a), 'a, tree('a))
```

Elements of data types can be pattern matched against, using the `switch` construct:

```ocaml
function root(t : tree('a)) : option('a) =
  switch(t)
    Tip => None
    Bin(_, v, _) => Some(v)
```

### Builtins

#### Events

Sophia contracts log structured messages to an event log in the resulting
blockchain transaction. To use events a contract must declare a type `event`,
and events are then logged using the `event` function:

```
event(e : event) : ()
```

#### Transactions
Sophia can generate blockchain transactions.
```
transaction(tx : transaction) : ()
```
The transaction type defines the transactions that can be created:
```
type spend_tx = {recipient : address, amount : uint}
type transaction = SpendTx(spend_tx)
                 | ...
```

#### Contract primitives

The block-chain environment available to a contract is defined by three record types
`call`, `self` and `chain`:

```
type call  = {caller : address,
              value  : uint,
              ...}
type self  = {creator : address,
              address : address,
              balance : uint,
              ...}
type chain = {height    : uint,
              timestamp : uint,
              ...}
```
A contract has access to variables of the same names, so that

- `call.caller` is the address of the entity (possibly another contract)
  calling the contract.
- `call.value` is the amount of coins transferred to the contract in the call
- `self.creator` is the address of the entity that signed the contract creation
  transaction
- `self.address` is the address of the contract account
- `self.balance` is the amount of coins currently in the contract account
- `chain.height` is the height of the current block (i.e. the block in which the current call will be included)
- `chain.timestamp` is the timestamp of the current block

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
internal let mod private public rec stateful switch true type
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

```ocaml
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
       | 'type' Id ['(' TVar* ')'] ['=' TypeDef]
       | Modifier* 'function' Id ':' Type
       | Modifier* 'function' Id Args [':' Type] '=' Block(Stmt)

Modifier ::= 'stateful' | 'public' | 'private' | 'internal'

Args ::= '(' Sep(Arg, ',') ')'
Arg  ::= Id [':' Type]
```

Contract declarations must appear at the top-level.

For example,
```ocaml
contract Test =
  type t = int
  public function add (x : t, y : t) = x + y
```

There are three forms of type declarations: type aliases, record type definitions and data type definitions:

```c
TypeDef    ::= TypeAlias | RecordType | DataType
TypeAlias  ::= Type
RecordType ::= '{' Sep(FieldType, ',') '}'
DataType   ::= Sep1(ConDecl, '|')

FieldType  ::= Id ':' Type
ConDecl    ::= Con ['(' Sep1(Type, ',') ')']
```

For example,
```ocaml
type point('a) = {x : 'a, y : 'a}
type shape('a) = Circle(point('a), 'a) | Rect(point('a), point('a))
type int_shape = shape(int)
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
```ocaml
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

```ocaml
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

### Operator precendences

In order of highest to lowest precedence.

| Operators | Associativity
| --- | ---
| `!` `bnot` | right
| `*` `/` `mod` `band` | left
| `-` (unary) | right
| `+` `-` `bor` `bxor` `bsl` `bsr` | left
| `::` `++` | right
| `<` `>` `=<` `>=` `==` `!=` | non
| `&&` | right
| `\|\|` | right

## Examples

```ocaml
/*
 *  A simple crowd funding example.
 *  Not production code (do not use)!
 */
contract FundMe =

  type state = { contributions : map(address, uint),
                 total         : uint,
                 beneficiary   : address,
                 deadline      : uint,
                 goal          : uint }

  private function require(b : bool, err : string) =
    if(!b) abort(err)

  public function init(beneficiary, deadline, goal) : state =
    { contributions = Map.empty,
      beneficiary   = beneficiary,
      deadline      = deadline,
      total         = 0,
      goal          = goal }

  // -- API --

  // Contribute to the project
  public stateful function contribute() =
    require(chain.height < state.deadline, "Deadline has passed")
    let amount =
      switch(Map.lookup(call.caller, state.contributions))
        None    => call.amount
        Some(n) => n + call.amount
    put(state{ contributions[call.caller] = amount,
               total = state.total + call.amount })

  // Withdraw funds after the deadline.
  public stateful function withdraw() =
    require(chain.height >= deadline, "Cannot withdraw before deadline")
    if(call.caller == state.beneficiary)
      withdraw_beneficiary()
    elif(is_contributor(call.caller))
      withdraw_contributor()
    else
      abort("Not a contributor or beneficiary")

  // -- Private functions --

  private function is_contributor(addr) =
    Map.member(addr, state.contributions)

  private stateful function withdraw_beneficiary() =
    require(state.total >= state.goal, "Project was not funded")
    transaction(SpendTx({recipient = state.beneficiary,
                         amount    = state.total }))
    put(state{ beneficiary = #0 })

  private stateful function withdraw_contributor() =
    require(state.total < state.goal, "Project was funded")
    let to = call.caller
    transaction(SpendTx({recipient = to,
                         amount    = state.contributions[to]}))
    put(state{ contributions[to] = 0 })
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

## ABI

The calldata contains a tuple with function name and argument. E.g. ("main", (1,2,3))
The compiler will generate entry coad to
load the calldata to memory and then create a pattern matching switch on the function name
and call the function with the second element as the argument.
e.g.
```
 CALLDATALOAD
 MLOAD
```

```
 case Data of
  ("main", arg) : main(arg)

```
Data is laid out in memory as follows:

Data of types uint, address, and bool are encoded as a big endian 256-bit word (32 bytes).

Data of other types are encoded as a pointer to the position of their place in the calldata.

String arguments are encoded with a 32 byte length (number of bytes) and as few 256-bit words
as needed padded on the right with 0.

A list is a series of cons cells each cell two 256-bit words, where the first word is data
encoded in the same way as arguments and the second argument is either an address or
nil (encoded as a 256-bit word with all bits = 1).

A tuple of size N is encoded in the same way as N arguments (functions
arguments are in reality a tuple).

Records are encoded as tuples.

Maps are encoded as a list of tuples, (key, value). ***This is subject to change***

Return values are encoded in the same way as arguments.

The contract code start by getting the calldata):

```
PUSH1 0       ;; MLOAD Address 0
DUP           ;; Used for CALLDATACOPY address 0
CALLDATASIZE
CALLDATACOPY
MLOAD

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

