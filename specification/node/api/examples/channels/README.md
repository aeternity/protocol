# Æternity node channel WebSocket API examples

This directory provides a set of examples of state channel's communication via
the WebSocket API. The examples are generated from aeternity node's
integration tests and represent real interaction with the node.

### Different APIs

Currently there is 1 API protocol that is supported:
* JSON-RPC

Legacy protocol was removed.

You can find API specific examples in the corresponding directories.

### Anatomy of an example

Each example pursues a specific use case. Examples are broken down into
sections each one of which describes a single action. Example for a section
would be:

###### responder <--- node (2019-03-13 11:04:47.10)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_open"
    }
  },
  "version": 1
}
```

Each section has an participant, an action, a timestamp and a code snippet. In
the above example the `responder` receives from its node the message.

#### Participants

Channels have two participants: an `initiator` and a `responder`. For clarity
each section has an explicit actor. Each participant has one's own node and
has a WebSocket connection to it. The two nodes open a `noise` protocol
connection between themselves: `initiator`'s node connects to a host and port
that the `responder` provides.

```
+-----------+               +------+
|           |    WebSocket  |      |
| initiator +---------------+ node |
|           |               |      |
+-----------+               +--+---+
                               |
                               |
                               | noise
                               |
                               v
+-----------+               +--+---+
|           |    WebSocket  |      |
| responder +---------------+ node |
|           |               |      |
+-----------+               +------+

```

#### Actions

Actions are either opening a WebSocket connection, receiving a message or
sending a message. All messages are sent and received from one's own node via
the opened WebSocket connection. The node has the responsibility to send
messages to the other participant's node via the noise protocol connection
they persist.

##### Open a WebSocket connection

An opening message includes all the needed parameters and looks like this:

###### initiator opens a WebSocket connection (2019-03-13 11:04:45.887)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3&role=initiator
```

###### Sending and receiving a message 
In the section, right after the participant, there is an arror indicating the
direction of the message:

* `<--- node` means that a message had been received from the node
* `---> node` means that a message had been sent to the node

###### Information log messages
Some WebSocket events represent important milestones regarding the example
logic and those are followed by a special information message that is a
comment of what had just happened. They look like this:

###### responder info
> Received an WebSocket opening request

#### Continuous example

There are two types of examples: that show a full open-close scenario or those
that are built on top of the previous ones'state. The latter are in `./*/continuous/`
and the former are outside it. The continuous ones have one single opening of
the state channel and the following examples are focused on specific actions.
The opening with initial balances is described in
`./*/continuous/init_per_group.md`

