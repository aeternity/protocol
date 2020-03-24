
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi&keep_running=false&lock_period=10&port=12652&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq&role=initiator
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_I8qttWVQog8iD6ChSzeALV1dAtD5VQlu8kcKJ9DPDBBrqAg/"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi&keep_running=false&lock_period=10&port=12652&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq&role=responder
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_mGesaxe/IsPwzox5V56hV44RK3wd4o1KMvxn/VXPSt36sGk9"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

#### responder <--- node
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

#### responder info
> Received an WebSocket opening request

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_accept"
    }
  },
  "version": 1
}
```

#### initiator info
> Received an WebSocket connection accepted

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAboL6OTMIitlUfHzZ02ulrRUkLninZHINloGk4PSXdA+hj+qJSJgAKEBHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfCGJGE5yoAAAgoAhhAGeddIAMCgVrvVIC0SljE/91zICtADxDJByLzh/kL+GnFlTslFHDoB0AylNA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421946,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBEyrXArbxQpOL9te5jtpdWjTmvjfZmkvCH3x531inYP0WFgA8a57/qqKzWUTUJlmeRkvHF5PUFt+I3zrx/XRUAuIP4gTIBoQG6C+jkzCIrZVHx82dNrpa0VJC54p2RyDZaBpOD0l3QPoY/qiUiYAChAR2sAdtJGgxyZkppx+tt86cnjJddJnDST9nQMM57yCHwhiRhOcqAAAIKAIYQBnnXSADAoFa71SAtEpYxP/dcyArQA8QyQci84f5C/hpxZU7JRRw6AbiTSQY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421946,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "event": "funding_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "fsm_id": "ba_mGesaxe/IsPwzox5V56hV44RK3wd4o1KMvxn/VXPSt36sGk9",
      "signed_tx": "tx_+MsLAfhCuEBEyrXArbxQpOL9te5jtpdWjTmvjfZmkvCH3x531inYP0WFgA8a57/qqKzWUTUJlmeRkvHF5PUFt+I3zrx/XRUAuIP4gTIBoQG6C+jkzCIrZVHx82dNrpa0VJC54p2RyDZaBpOD0l3QPoY/qiUiYAChAR2sAdtJGgxyZkppx+tt86cnjJddJnDST9nQMM57yCHwhiRhOcqAAAIKAIYQBnnXSADAoFa71SAtEpYxP/dcyArQA8QyQci84f5C/hpxZU7JRRw6AbiTSQY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421945,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhARMq1wK28UKTi/bXuY7aXVo05r432ZpLwh98ed9Yp2D9FhYAPGue/6qis1lE1CZZnkZLxxeT1BbfiN868f10VALhAYTnrypn+kT/Ul3vERm9YsveysP//T6XbK/cy2gyoro/wVjrRQ6kzHt861MAft/pJoVBYvgKOFjLI8Hmei3y2AriD+IEyAaEBugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6GP6olImAAoQEdrAHbSRoMcmZKacfrbfOnJ4yXXSZw0k/Z0DDOe8gh8IYkYTnKgAACCgCGEAZ510gAwKBWu9UgLRKWMT/3XMgK0APEMkHIvOH+Qv4acWVOyUUcOgFW0UdA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421945,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhARMq1wK28UKTi/bXuY7aXVo05r432ZpLwh98ed9Yp2D9FhYAPGue/6qis1lE1CZZnkZLxxeT1BbfiN868f10VALhAYTnrypn+kT/Ul3vERm9YsveysP//T6XbK/cy2gyoro/wVjrRQ6kzHt861MAft/pJoVBYvgKOFjLI8Hmei3y2AriD+IEyAaEBugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6GP6olImAAoQEdrAHbSRoMcmZKacfrbfOnJ4yXXSZw0k/Z0DDOe8gh8IYkYTnKgAACCgCGEAZ510gAwKBWu9UgLRKWMT/3XMgK0APEMkHIvOH+Qv4acWVOyUUcOgFW0UdA",
      "type": "channel_create_tx"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_I8qttWVQog8iD6ChSzeALV1dAtD5VQlu8kcKJ9DPDBBrqAg/"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhARMq1wK28UKTi/bXuY7aXVo05r432ZpLwh98ed9Yp2D9FhYAPGue/6qis1lE1CZZnkZLxxeT1BbfiN868f10VALhAYTnrypn+kT/Ul3vERm9YsveysP//T6XbK/cy2gyoro/wVjrRQ6kzHt861MAft/pJoVBYvgKOFjLI8Hmei3y2AriD+IEyAaEBugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6GP6olImAAoQEdrAHbSRoMcmZKacfrbfOnJ4yXXSZw0k/Z0DDOe8gh8IYkYTnKgAACCgCGEAZ510gAwKBWu9UgLRKWMT/3XMgK0APEMkHIvOH+Qv4acWVOyUUcOgFW0UdA",
      "type": "channel_create_tx"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhARMq1wK28UKTi/bXuY7aXVo05r432ZpLwh98ed9Yp2D9FhYAPGue/6qis1lE1CZZnkZLxxeT1BbfiN868f10VALhAYTnrypn+kT/Ul3vERm9YsveysP//T6XbK/cy2gyoro/wVjrRQ6kzHt861MAft/pJoVBYvgKOFjLI8Hmei3y2AriD+IEyAaEBugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6GP6olImAAoQEdrAHbSRoMcmZKacfrbfOnJ4yXXSZw0k/Z0DDOe8gh8IYkYTnKgAACCgCGEAZ510gAwKBWu9UgLRKWMT/3XMgK0APEMkHIvOH+Qv4acWVOyUUcOgFW0UdA",
      "type": "channel_create_tx"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhARMq1wK28UKTi/bXuY7aXVo05r432ZpLwh98ed9Yp2D9FhYAPGue/6qis1lE1CZZnkZLxxeT1BbfiN868f10VALhAYTnrypn+kT/Ul3vERm9YsveysP//T6XbK/cy2gyoro/wVjrRQ6kzHt861MAft/pJoVBYvgKOFjLI8Hmei3y2AriD+IEyAaEBugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6GP6olImAAoQEdrAHbSRoMcmZKacfrbfOnJ4yXXSZw0k/Z0DDOe8gh8IYkYTnKgAACCgCGEAZ510gAwKBWu9UgLRKWMT/3XMgK0APEMkHIvOH+Qv4acWVOyUUcOgFW0UdA",
      "type": "channel_create_tx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello",
    "to": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "message": {
        "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
        "from": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "info": "Hello",
        "to": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
    "to": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "message": {
        "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
        "from": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "info": "Hello back",
        "to": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421944,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421944,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "balance": 69999999999999
    },
    {
      "account": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder info
> Channel is `open` and ready to use

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+QENCwH4hLhARMq1wK28UKTi/bXuY7aXVo05r432ZpLwh98ed9Yp2D9FhYAPGue/6qis1lE1CZZnkZLxxeT1BbfiN868f10VALhAYTnrypn+kT/Ul3vERm9YsveysP//T6XbK/cy2gyoro/wVjrRQ6kzHt861MAft/pJoVBYvgKOFjLI8Hmei3y2AriD+IEyAaEBugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6GP6olImAAoQEdrAHbSRoMcmZKacfrbfOnJ4yXXSZw0k/Z0DDOe8gh8IYkYTnKgAACCgCGEAZ510gAwKBWu9UgLRKWMT/3XMgK0APEMkHIvOH+Qv4acWVOyUUcOgFW0UdA"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+QENCwH4hLhARMq1wK28UKTi/bXuY7aXVo05r432ZpLwh98ed9Yp2D9FhYAPGue/6qis1lE1CZZnkZLxxeT1BbfiN868f10VALhAYTnrypn+kT/Ul3vERm9YsveysP//T6XbK/cy2gyoro/wVjrRQ6kzHt861MAft/pJoVBYvgKOFjLI8Hmei3y2AriD+IEyAaEBugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6GP6olImAAoQEdrAHbSRoMcmZKacfrbfOnJ4yXXSZw0k/Z0DDOe8gh8IYkYTnKgAACCgCGEAZ510gAwKBWu9UgLRKWMT/3XMgK0APEMkHIvOH+Qv4acWVOyUUcOgFW0UdA"
    }
  },
  "version": 1
}
```
