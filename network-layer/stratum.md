# Stratum

This document describes a protocol, that allows a group of miners to connect
to a server, which coordinates the distribution of work packages among
miners.

The initial protocol was written for Bitcoin and contains several pieces that
need adjustment in order to be usable with æternity.

Pool operators looking to implement this specification should note, that the
usage of the Bitcoin-NG protocol changes the dynamics of the mining game.
With Bitcoin-NG pools will end up authoring the microblocks containing
transactions while the miners try to find keyblocks, which are used for
leader election.
This procedure puts both more power into the hands of pool operators while
also adding more burden. This burden comes in the form of increased book
keeping complexity—the full revenue of one epoch can only be computed after
the fact—and an increase in computational resources required for signing
microblocks.


## Specification


### Conventions

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to
be interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).

The stratum protocol mostly adheres to the [JSON RPC 2.0](https://www.jsonrpc.org/specification) specification.

This specification derives from works by [slushpool](https://slushpool.com/help/manual/stratum-protocol),
[zcash](https://github.com/str4d/zips/blob/77-zip-stratum/drafts/str4d-stratum/draft1.rst)
and [nicehash](https://github.com/nicehash/Specifications/blob/master/EthereumStratum_NiceHash_v1.0.0.txt).


### Overview

Communication happens over a bidirectional channel with messages encoded as
JSON with `LF` delimiter—in this document written as `\n`.

Since requests can be handled out of order, each request in a session SHOULD
have an unique `id`. In order to be able to match request and response,
responses MUST have the same `id` as their matching request. Notifications
sent by the server or calls that do not trigger any response MAY have an `id` of
`null`.

For further details on the members of request and response objects consult the
[JSON RPC 2.0 specification](https://www.jsonrpc.org/specification).


### Protocol flow example

The following shows what a session might look like from subscription to
submitting a solution.

```
Client                                Server
  |                                     |
  | --------- mining.subscribe -------> |
  | --------- mining.authorize -------> |
  | <-------- mining.set_target ------- |
  |                                     |----
  | <---------- mining.notify --------- |<--/
  |                                     |
  | ---------- mining.submit ---------> |
```


### Methods

- [mining.configure](#mining-configure)
- [mining.subscribe](#mining-subscribe)
- [mining.authorize](#mining-authorize)
- [mining.notify](#mining-notify)
- [mining.set_target](#mining-set_target)
- [mining.submit](#mining-submit)
- [client.reconnect](#client-reconnect)


### Errors

Whenever an RPC call triggers an error, the response MUST include an `error`
field which maps to a **list** of the following values:

- [ `code` : `int` ]
- [ `message` : `string` ]
- [ `data` : `object` ]

```
{"id": 10, "result": null, "error": [21, "Job not found", null]}
```

Errors SHOULD be identified by their `code` and programs SHOULD do error
handling based on the `code` and not the `message`.
Available error codes, in addition to the codes defined in the [JSON RPC 2.0]() specification, are:

- `20` - Other/Unknown
- `21` - Job not found (=stale)
- `22` - Duplicate share
- `23` - Low difficulty share
- `24` - Unauthorized worker
- `25` - Not subscribed

The `message` field SHOULD be a concise description of the error for human
consumption.

Implementors MAY choose to include an optional `data` object with additional
information relevant to the error.


### mining.configure

In order to allow easier upgrades in the future, a client MAY send a
configuration as its initial messages to the server, specifying possible
extensions it supports.
The specific mechanism is described by [slushpool here](https://github.com/slushpool/stratumprotocol/blob/master/stratum-extensions.mediawiki)

A client MAY choose to skip this message, which a server SHOULD interpret as the
client adhering to the protocol as described in this document, without any
further extensions.

This method call will only be executed by clients.


### mining.subscribe

In order to initiate or resume a session with the server, a client needs to
call the subscribe method.

This method call will only be executed by clients.


#### Request:

```
{"id": 1, "method": "mining.subscribe", "params": ["MyMiner/1.0.0", null, "my.pool.com", 1234]}\n
```


- [ `id` : `int` ]: request id
- [ `method` : `string` ]: RPC method name
- [ `params` : (`string`, `string`, `string`, `int`) ]: list of method
  parameters
	1. MUST be name and version of mining software in the given format or empty
	   string
	2. MUST be session id received during a previous session or `null` if a new
	   session should be initiated by the server
	3. MUST be the host the client is trying to connect to or `null`
	4. MUST be the port on the given host the client is trying to connect to or
     `null`

Please see the [zcash stratum specification](https://github.com/str4d/zips/blob/77-zip-stratum/drafts/str4d-stratum/draft1.rst#rationale)
for a reason as to why `subscribe` includes a host and port.


#### Response

```
{ "id": 1, "result": ["ed70df83","080000"], "error": null }\n
```

- [ `id` : `int` ]: request id
- [ `result` : (`string`, `string`) ]:
	- MUST be `null` if an error occurred or otherwise
		1. If the server supports session resumption, then this SHOULD be a unique
       session id, `null` otherwise
		2. The last bytes of the 8 byte nonce, hex encoded
- [ `error` : (`int`, `string`, `object`) ]

This nonce sent by the server is usually referred to as the extranonce, i.e.
`nonce = minernonce || extranonce`. The server MAY freely choose the length of
the extranonce and clients SHOULD NOT expect it to be always of the same length.
`extranonce` and `minernonce` MUST be 8 bytes long together.

The nonce is in little-endian form.

The server SHOULD assign disjoint subspaces of the 8 byte nonce space to miners,
avoiding the problem of multiple miners working on the same problem.


### mining.authorize

Before a client can submit solutions to a server it MUST authorize at least one worker.

This method call will only be executed by clients.


#### Request

```
{"id": 2, "method": "mining.authorize", "params": ["WORKER_NAME", "WORKER_PASSWORD"]}\n
```

- [ `id` : `int` ]: request id
- [ `method` : `string` ]: RPC method name
- [ `params` : (`string`, `string`) ]: list of method parameters
	1. The worker name
	2. The worker password


#### Response

```
{"id": 2, "result": true, "error": null}\n
```

- [ `id` : `int` ]: request id
- [ `result` : `bool` ]: authorization success
	- MUST be `true` if successful
	- MUST be `null` if an error occurred
- [ `error` : (`int`, `string`, `object`) ]
	- MUST be `null` if `result` is `true`
	- If authorization failed then it MUST contain error object with the
	  appropriate error id and description


### mining.set_target

The target difficulty for a block can change and a server needs to be able to
notify clients of that.

This method call will only be executed by the server.


#### Request

```
{"id": null, "method": "mining.set_target", "params": ["FFFF000000000000000000000000000000000000000000000000000000000000"]}\n
```

- [ `id` : `int` ]: request id
- [ `method` : `string` ]: RPC method name
- [ `params` : (`string`) ]: list of method parameters
	1. The the 256bit big-endian target, which MUST be hex encoded.

Any subsequent jobs started by a client after receiving this update MUST
honor the new target and servers MUST reject submission above this target.

For jobs started before this update, a server MAY accept submissions if they are
below the previous target.

Please consult the document describing the consensus and proof-of-work
algorithms for details on the target.


#### Response

There is no explicit response for this call.


### mining.notify

The notify call is used to supply a worker with new work packages.

This method call will only be executed by the server.


#### Request

```
{"id": null, "method": "mining.notify", "params": ["d70fd222", "abad8f99f3918bf903c6a909d9bbc0fdfa5a2f4b9cb1196175ec825c6610126c", true ]}\n
```

- [ `id` : `int` ]: request id
- [ `method` : `string` ]: RPC method name
- [ `params` : (`string`, `int`, `string`, `bool`) ]: list of method parameters
	1. Job ID
	2. Block version
	3. Header hash
	4. A boolean indicating whether the miners job queue should be emptied or not

In order to keep the protocol flexible and anticipate changes in both the
structure of blocks and proof of work scheme, the block version should be
considered as a switch for the subsequent parameters.

The following is valid for block version (***TODO:*** insert genesis block version).

In its current iteration, all that is needed as input for the proof of work
puzzle solver is a hash of the block header plus a nonce, as described in the
consensus document.
Thus a client only requires the header hash from the server.


#### Response

There is no explicit response for this call.


### mining.submit

With this method a worker can submit solutions for the mining puzzle.
This method call will only be executed by clients.


#### Request

```
{"id": 4, "method": "mining.submit", "params": ["WORKER_NAME", "d70fd222", "98b6ac44d2", ""]}\n
```

- [ `id` : `int` ]: request id
- [ `method` : `string` ]: RPC method name
- [ `params` : (`string`, `string`, `string`, `solution`) ]: list of method
  parameters
	1. Worker name, mostly for statistics
	2. Job ID
	3. Miner nonce in hex format
	4. Proof of work puzzle solution

As with `mining.notify` all parameters after the job ID should be understood as
being conditional on the block version sent along in `mining.notify`.

The miner nonce MUST be `8 - len(extra_nonce)` bytes long and be little endian,
in order for the server to produce a correct 8 bytes nonce when concatenating
the extra and miner nonce.

A `solution` in our current instantiation of cuckoo cycle is a list of 42 32bit
integers. The solution MUST be formatted according to the rules specified in the
consensus document.


#### Response

```
{"id": 4, "result": true, "error": null}\n
```

- [ `id` : `int` ]: request id
- [ `result`: `bool` ]: submission accepted
	- MUST be `true` if accepted
	- MUST be `null` if an error occurred
- [ `error` : (`int`, `string`, `object`) ]
	- MUST be `null` if `result` is `true`
	- If submission failed then it MUST contain error object with the
	  appropriate error id and description


### client.reconnect

If a pool operator wants to have their clients reconnect to the same or a
different host they use this call.

This method call will only be executed by the server.


#### Request

```
{"id": null, "method": "client.reconnect", "params": [("my.pool.com", 1234, 23)]} \n
```


- [ `id` : `int` ]: request id
- [ `method` : `string` ]: RPC method name
- [ `params`: (`string`, `int`, `int`) ]: list of method parameters
	1. MUST be the new host name or `null` if the name is the same
	2. MUST be the new port name or `null` if the port is the same
	3. MUST be a positive integer wait time in seconds that the client should wait

The `params` list MAY be empty, which signals that the client SHOULD reconnect
to the same host and port immediately.


#### Response

There is no explicit response for this call.
