[back](./contracts.md)
# Sophia explained

The [Sophia](./sophia.md) language is described in [The Sophia
Language](./sophia.md). However, some concepts could need a more in depth
description and some accompanying examples to be easier to grasp. We aim to
collect such in-depth explanations on this page.

## Table of Contents
- [Events](#events)

## Events

The implementation of [Events](./sophia.md#events) is largely inspired by
[events in
Solidity/Ethereum](https://solidity.readthedocs.io/en/v0.4.24/contracts.html#events).
But instead of defining multiple `event` structs in Sophia *one* instance of
the `event` data type is defined - with one type constructor per event we want
to emit. For example the following definition makes it possible to emit two
different events `TheFirstEvent` and `AnotherEvent`.

```
  datatype event =
      TheFirstEvent(indexed int)
    | AnotherEvent(indexed address, string)
```

An event may have 0-3 fixed width (32 bytes) fields (sometimes refered to as
`indexed`), these fields should have a Sophia type that is represented as one
32-byte word at the VM level (for example int, bool, short byte arrays, bits,
and addresses). An event may also have an additional non-indexed field, this
field should be of type `string`. (Note: the `indexed` keyword was previously
mandatory, but is not anymore; since there are no non-indexed word arguments)
Events are emitted by using the `Chain.event` function. The following function
will emit one Event of each kind in the example.

```
  public function emit_events() : () =
    Chain.event(TheFirstEvent(42))
    Chain.event(AnotherEvent(Contract.address, "This is not indexed"))
```

### Accessing events

The events are stored in the [contract call
object](../serializations.md#contract-call) and can be accessed by looking up
the transaction in which they were emitted. If we assume that `emit_events`,
from our example, was called in a transaction with transaction hash
`th_a5239bd8e3...` we can access it from the HTTP API
`/v2/transactions/th_a5239bd8e3.../info`:

```
#{<<"caller_id">> => <<"ak_XSnUeXPB8UncW8d5R9xoov8x5iTnA8NrURdqLGn9PnyAXYY78">>,
  <<"caller_nonce">> => 4,
  <<"contract_id">> => <<"ct_2pvLLjPfjqRMSX91BgDRK8gLzeJD4qaQtNF5F6GdWKamCCnZc">>,
  <<"gas_price">> => 1000000000,
  <<"gas_used">> => 3274,
  <<"height">> => 7,
  <<"log">> =>
      [#{<<"address">> => <<"ct_2pvLLjPfjqRMSX91BgDRK8gLzeJD4qaQtNF5F6GdWKamCCnZc">>,
         <<"data">> => <<"cb_Xfbg4g==">>,
         <<"topics">> => [25381774165057387707802602748622431964055296361151037811644748771109370239835,
                          42]},
       #{<<"address">> => <<"ct_2pvLLjPfjqRMSX91BgDRK8gLzeJD4qaQtNF5F6GdWKamCCnZc">>,
         <<"data">> => <<"cb_VGhpcyBpcyBub3QgaW5kZXhlZK+w140=">>,
         <<"topics">> => [101640830366340000167918459210098337687948756568954742276612796897811614700269,
                          1875564187002476023854543820981509249331367502514562901623081521315128929137]}],
  <<"return_type">> => <<"ok">>,
  <<"return_value">> => <<"cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAArMtts">>}
```

First look at the `data` field. For the first event it is `<<"cb_Xfbg4g==">>`
which decodes to `<<>>`, i.e. no data (and that is expected since the event did
not have any extra data.). For the second event we see
`<<"cb_VGhpcyBpcyBub3QgaW5kZXhlZK+w140=">>` which decodes to `<<"This is not
indexed">>`. For the `topics` field we see that there is actually two values
per event. The events only contain one value each, but there is *one extra
implicit topic* added per event. This additional value is the Blake2b hash
of the event constructor name, i.e. `Blake2b("TheFirstEvent")` and
`Blake2b("AnotherEvent")` respectively:

```
(aeternity_ct@localhost)1> aec_hash:blake2b_256_hash(<<"TheFirstEvent">>).
<<56,29,147,56,123,224,214,195,32,234,189,161,114,143,4,
  86,229,198,194,243,62,145,21,48,213,185,208,190,17,...>>
(aeternity_ct@localhost)2> <<25381774165057387707802602748622431964055296361151037811644748771109370239835:256>>.
<<56,29,147,56,123,224,214,195,32,234,189,161,114,143,4,
  86,229,198,194,243,62,145,21,48,213,185,208,190,17,...>>
```

The implicit value goes first in the `topics` array. The topics are (currently,
this might change in the future) presented as 256-bit unsigned integers - i.e.
`1875564187002476023854543820981509249331367502514562901623081521315128929137`
in the second event in the example corresponds to `<<"ct_2pvLLjPfjq...">>`. A
boolean argument would come out as `0` (= false) or `1` (= true).

### Argument order

It is only possible to have one (1) `string` parameter in the event, but it can
be placed in any position (and its value will end up in the `data` field), i.e.
```
AnotherEvent(string, indexed address)

...

Chain.event(AnotherEvent("This is not indexed", Contract.address))
```
would yield exactly the same result in the example above!

### Event indexing

Finally it has to be pointed out that there is no *indexing* going on in the
Aeternity node itself. One could imagine this being part of a middleware
service, with a subscribe/notify interface or applications could be scraping
the chain by other means.
