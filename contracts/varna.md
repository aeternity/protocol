[back](./contracts.md)
# The Varna Language

The high level language "Varna" (Sanskrit for type) is somewhat
similar to Bitcoins Script language.  Varna contracts do not contain
any loops and the gas cost for a call is bounded at compile
time. Thanks to Æternity's many first order objects the languages is
still very powerful.

This is still very much work in progress and the language has not yet been finalised. All that currently exists is the scanner and parser.

Example:

```
 function buy_tokens(value: aeons) : void
     var amount : integer = (value / oracle("GameTokenPrice", "price"))
     if owner.tokens."GameTokens" > amount then
        caller.tokens."GameTokens" += amount
        owner.tokens."GameTokens" -= amount
        owner.balance += value
     end
 end

```

The High Level Machine (HLM) is a very simple virtual machine.  The
Varna contract is evaluated directly by the node verification code.

A BNF describing the Varna syntax:

```
# A comment

contractdef ::= 'contract' name [ statedef ] { functiondef } 'end'

statedef ::= 'state' [ fieldlist ] 'end'

functiondef ::= { funcscope } name '(' [ pars ] ')' typedef block 'end'

funcscope ::= private | public | stateful

pars ::= parameter { ',' parameter }

parameter ::= name typedef

block ::= { localdef } { stat { ';' } } [ reststat ]

localdef ::= 'var' name typedef '=' exp

retstat ::= 'return' [ exp ]

stat ::= varname '=' exp |
         functioncall |
         'if' exp 'then' block { 'elseif' exp 'then' block }
             [ 'else block ] 'end'

functioncall ::= funcname '(' [ args ] ') [ callmod ]

args ::= exp { ',' exp }

# Call modifier.

callmod ::=  'with' modlist 'end'

modlist ::= name '=' exp |
            modlist ',' name '=' exp

explist ::= exp {',' exp}

exp ::= null |
        boolean |
        number |
        string |
        varname |
        functioncall |
        exp binop exp |
        unop exp |
        '(' exp ')'

varname ::= name |
            name '.' varname |          # Record field name
            varname '[' exp ']'         # Dynamic field name

funcname ::= name |
             name '.' name              # Call another contract

typedef ::= [ ':' type ]

type ::= 'boolean' | 'integer' | 'string' |
         'address' | 'tokenaddress' | 'void'

fieldlist ::= field { ',' field } [ fieldlist ]

field ::= name typedef '=' exp

binop ::= '+' | '-' | '*' | '/' |
          '>' | '<=' | '>' | '>=' | '==' | '!=' |
          and | or

unop ::= '-' | not

```

# The Varna_01 ABI
TODO: Describe the Varna ABI
