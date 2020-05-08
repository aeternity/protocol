
#### initiator ---> node
```javascript
{
  "id": -576460752303423485,
  "jsonrpc": "2.0",
  "method": "channels.history.fetch",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
  "id": -576460752303423485,
  "jsonrpc": "2.0",
  "result": [
    {
      "info": {
        "state": "ba_dHhfK1FFTkN3SDRoTGhBRjQ5WEsyM0ZTaDVtWmQ0UWhpV09HVExUYzVRUFYwQkJtbzRQQVVRT2YyZVNnTkFDaU1Samw1eC9OSlh6aEREb3g0MHJ0NzNuWVRyTE40aXNrQ0p2QnJoQTlTeHFNL0VVQUd2TUZnb2pNKzZVVEF1b2lBcHlzYjllWnhFY3hVOFlGTXB2ZzlpWGdjMlYvbnFMTkRZaDRIelVaT2IvUk5tM0pndk90eEc3S3hnbURyaUQrSUV5QWFFQlB4KzBjWWV2cHgrMmR1NGZkNm5mYVQ0dGdDNmkzVDVQMkpzUDdYMVBybkNHUDZvbEltQUFvUUV4SzBWRG81US9VWUprSG95M0pXYkNLamJRaC9XUTNaVUE0UG12Sjd0Zng0WWtZVG5LZ0FBQ0NnQ0dFQVo1MTBnQXdLREZzRi90emRqeHB3ZTgzWlIzS0hzVVBNeDVIaDFYT3VrcVFTZ2pHeEM5M1FId0dsWmyO04cz"
      },
      "tag": "update",
      "time": "2020-05-08T08:47:55.685261Z",
      "type": "report"
    },
    {
      "info": {
        "event": "ba_b3BlbqPd6OU="
      },
      "tag": "info",
      "time": "2020-05-08T08:47:55.684420Z",
      "type": "report"
    },
    {
      "info": {
        "event": "ba_ZnVuZGluZ19sb2NrZWTNLzad"
      },
      "tag": "info",
      "time": "2020-05-08T08:47:55.678490Z",
      "type": "report"
    },
    {
      "info": {
        "channel_id": "ch_CtBFQVXBxEkM9jHH9TPnQNBYpeLquB7yFqTnU2e7sYDycTnkoVWu3wsKcsGCdEWA3DfMfighexGh36",
        "temporary_channel_id": "ch_3h9DLbMKuWgdrTdCgGTtLtaGsXxLuErFm5Nd4hL1ofktLp6Y3nVmgYjNUmTR2sHCYCpzsKkQDgkwb"
      },
      "tag": "funding_locked",
      "time": "2020-05-08T08:47:55.678446Z",
      "type": "receive"
    },
    {
      "info": {
        "channel_id": "ch_CtBFQVXBxEkM9jHH9TPnQNBYpeLquB7yFqTnU2e7sYDycTnkoVWu3wsKcsGCdEWA3DfMfighexGh36",
        "temporary_channel_id": "ch_3h9DLbMKuWgdrTdCgGTtLtaGsXxLuErFm5Nd4hL1ofktLp6Y3nVmgYjNUmTR2sHCYCpzsKkQDgkwb"
      },
      "tag": "funding_locked",
      "time": "2020-05-08T08:47:55.676654Z",
      "type": "send"
    },
    {
      "info": {
        "event": "ba_b3duX2Z1bmRpbmdfbG9ja2VkAieFrg=="
      },
      "tag": "info",
      "time": "2020-05-08T08:47:55.676087Z",
      "type": "report"
    },
    {
      "info": {
        "message": {
          "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
          "from": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc",
          "info": "Hello back",
          "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
        }
      },
      "tag": "message",
      "time": "2020-05-08T08:47:55.623591Z",
      "type": "report"
    },
    {
      "info": {
        "channel_id": "ch_CtBFQVXBxEkM9jHH9TPnQNBYpeLquB7yFqTnU2e7sYDycTnkoVWu3wsKcsGCdEWA3DfMfighexGh36",
        "from": "ak_3e25TU65ND45fF9g47nN7SSyZ8PgSvopFJCq5f7MVkvdo6vGXAArLN5t59F5WtkeGfpyFiNRAtqUH",
        "info": "Hello back",
        "to": "ak_3e25TbYb2Yn73VabAAAQCJG8YzntvhAaFsreeZR7b8E313eBbyVgJWYb8SUQDXVxCcvCEc6HNzE4R"
      },
      "tag": "inband_msg",
      "time": "2020-05-08T08:47:55.623392Z",
      "type": "receive"
    },
    {
      "info": {
        "channel_id": "ch_CtBFQVXBxEkM9jHH9TPnQNBYpeLquB7yFqTnU2e7sYDycTnkoVWu3wsKcsGCdEWA3DfMfighexGh36",
        "from": "ak_3e25TbYb2Yn73VabAAAQCJG8YzntvhAaFsreeZR7b8E313eBbyVgJWYb8SUQDXVxCcvCEc6HNzE4R",
        "info": "Hello",
        "to": "ak_3e25TU65ND45fF9g47nN7SSyZ8PgSvopFJCq5f7MVkvdo6vGXAArLN5t59F5WtkeGfpyFiNRAtqUH"
      },
      "tag": "inband_msg",
      "time": "2020-05-08T08:47:55.617238Z",
      "type": "send"
    },
    {
      "info": {
        "info": "channel_changed",
        "tx": "tx_dHhfK1FFTkN3SDRoTGhBRjQ5WEsyM0ZTaDVtWmQ0UWhpV09HVExUYzVRUFYwQkJtbzRQQVVRT2YyZVNnTkFDaU1Samw1eC9OSlh6aEREb3g0MHJ0NzNuWVRyTE40aXNrQ0p2QnJoQTlTeHFNL0VVQUd2TUZnb2pNKzZVVEF1b2lBcHlzYjllWnhFY3hVOFlGTXB2ZzlpWGdjMlYvbnFMTkRZaDRIelVaT2IvUk5tM0pndk90eEc3S3hnbURyaUQrSUV5QWFFQlB4KzBjWWV2cHgrMmR1NGZkNm5mYVQ0dGdDNmkzVDVQMkpzUDdYMVBybkNHUDZvbEltQUFvUUV4SzBWRG81US9VWUprSG95M0pXYkNLamJRaC9XUTNaVUE0UG12Sjd0Zng0WWtZVG5LZ0FBQ0NnQ0dFQVo1MTBnQXdLREZzRi90emRqeHB3ZTgzWlIzS0hzVVBNeDVIaDFYT3VrcVFTZ2pHeEM5M1FId0dsWmyO04cz",
        "type": "channel_create_tx"
      },
      "tag": "on_chain_tx",
      "time": "2020-05-08T08:47:55.600244Z",
      "type": "report"
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423484,
  "jsonrpc": "2.0",
  "method": "channels.history.fetch",
  "params": {
    "n": 1000
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
  "id": -576460752303423484,
  "jsonrpc": "2.0",
  "result": [
    {
      "info": {
        "state": "ba_dHhfK1FFTkN3SDRoTGhBRjQ5WEsyM0ZTaDVtWmQ0UWhpV09HVExUYzVRUFYwQkJtbzRQQVVRT2YyZVNnTkFDaU1Samw1eC9OSlh6aEREb3g0MHJ0NzNuWVRyTE40aXNrQ0p2QnJoQTlTeHFNL0VVQUd2TUZnb2pNKzZVVEF1b2lBcHlzYjllWnhFY3hVOFlGTXB2ZzlpWGdjMlYvbnFMTkRZaDRIelVaT2IvUk5tM0pndk90eEc3S3hnbURyaUQrSUV5QWFFQlB4KzBjWWV2cHgrMmR1NGZkNm5mYVQ0dGdDNmkzVDVQMkpzUDdYMVBybkNHUDZvbEltQUFvUUV4SzBWRG81US9VWUprSG95M0pXYkNLamJRaC9XUTNaVUE0UG12Sjd0Zng0WWtZVG5LZ0FBQ0NnQ0dFQVo1MTBnQXdLREZzRi90emRqeHB3ZTgzWlIzS0hzVVBNeDVIaDFYT3VrcVFTZ2pHeEM5M1FId0dsWmyO04cz"
      },
      "tag": "update",
      "time": "2020-05-08T08:47:55.685261Z",
      "type": "report"
    },
    {
      "info": {
        "event": "ba_b3BlbqPd6OU="
      },
      "tag": "info",
      "time": "2020-05-08T08:47:55.684420Z",
      "type": "report"
    },
    {
      "info": {
        "event": "ba_ZnVuZGluZ19sb2NrZWTNLzad"
      },
      "tag": "info",
      "time": "2020-05-08T08:47:55.678490Z",
      "type": "report"
    },
    {
      "info": {
        "channel_id": "ch_CtBFQVXBxEkM9jHH9TPnQNBYpeLquB7yFqTnU2e7sYDycTnkoVWu3wsKcsGCdEWA3DfMfighexGh36",
        "temporary_channel_id": "ch_3h9DLbMKuWgdrTdCgGTtLtaGsXxLuErFm5Nd4hL1ofktLp6Y3nVmgYjNUmTR2sHCYCpzsKkQDgkwb"
      },
      "tag": "funding_locked",
      "time": "2020-05-08T08:47:55.678446Z",
      "type": "receive"
    },
    {
      "info": {
        "channel_id": "ch_CtBFQVXBxEkM9jHH9TPnQNBYpeLquB7yFqTnU2e7sYDycTnkoVWu3wsKcsGCdEWA3DfMfighexGh36",
        "temporary_channel_id": "ch_3h9DLbMKuWgdrTdCgGTtLtaGsXxLuErFm5Nd4hL1ofktLp6Y3nVmgYjNUmTR2sHCYCpzsKkQDgkwb"
      },
      "tag": "funding_locked",
      "time": "2020-05-08T08:47:55.676654Z",
      "type": "send"
    },
    {
      "info": {
        "event": "ba_b3duX2Z1bmRpbmdfbG9ja2VkAieFrg=="
      },
      "tag": "info",
      "time": "2020-05-08T08:47:55.676087Z",
      "type": "report"
    },
    {
      "info": {
        "message": {
          "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
          "from": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc",
          "info": "Hello back",
          "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
        }
      },
      "tag": "message",
      "time": "2020-05-08T08:47:55.623591Z",
      "type": "report"
    },
    {
      "info": {
        "channel_id": "ch_CtBFQVXBxEkM9jHH9TPnQNBYpeLquB7yFqTnU2e7sYDycTnkoVWu3wsKcsGCdEWA3DfMfighexGh36",
        "from": "ak_3e25TU65ND45fF9g47nN7SSyZ8PgSvopFJCq5f7MVkvdo6vGXAArLN5t59F5WtkeGfpyFiNRAtqUH",
        "info": "Hello back",
        "to": "ak_3e25TbYb2Yn73VabAAAQCJG8YzntvhAaFsreeZR7b8E313eBbyVgJWYb8SUQDXVxCcvCEc6HNzE4R"
      },
      "tag": "inband_msg",
      "time": "2020-05-08T08:47:55.623392Z",
      "type": "receive"
    },
    {
      "info": {
        "channel_id": "ch_CtBFQVXBxEkM9jHH9TPnQNBYpeLquB7yFqTnU2e7sYDycTnkoVWu3wsKcsGCdEWA3DfMfighexGh36",
        "from": "ak_3e25TbYb2Yn73VabAAAQCJG8YzntvhAaFsreeZR7b8E313eBbyVgJWYb8SUQDXVxCcvCEc6HNzE4R",
        "info": "Hello",
        "to": "ak_3e25TU65ND45fF9g47nN7SSyZ8PgSvopFJCq5f7MVkvdo6vGXAArLN5t59F5WtkeGfpyFiNRAtqUH"
      },
      "tag": "inband_msg",
      "time": "2020-05-08T08:47:55.617238Z",
      "type": "send"
    },
    {
      "info": {
        "info": "channel_changed",
        "tx": "tx_dHhfK1FFTkN3SDRoTGhBRjQ5WEsyM0ZTaDVtWmQ0UWhpV09HVExUYzVRUFYwQkJtbzRQQVVRT2YyZVNnTkFDaU1Samw1eC9OSlh6aEREb3g0MHJ0NzNuWVRyTE40aXNrQ0p2QnJoQTlTeHFNL0VVQUd2TUZnb2pNKzZVVEF1b2lBcHlzYjllWnhFY3hVOFlGTXB2ZzlpWGdjMlYvbnFMTkRZaDRIelVaT2IvUk5tM0pndk90eEc3S3hnbURyaUQrSUV5QWFFQlB4KzBjWWV2cHgrMmR1NGZkNm5mYVQ0dGdDNmkzVDVQMkpzUDdYMVBybkNHUDZvbEltQUFvUUV4SzBWRG81US9VWUprSG95M0pXYkNLamJRaC9XUTNaVUE0UG12Sjd0Zng0WWtZVG5LZ0FBQ0NnQ0dFQVo1MTBnQXdLREZzRi90emRqeHB3ZTgzWlIzS0hzVVBNeDVIaDFYT3VrcVFTZ2pHeEM5M1FId0dsWmyO04cz",
        "type": "channel_create_tx"
      },
      "tag": "on_chain_tx",
      "time": "2020-05-08T08:47:55.600244Z",
      "type": "report"
    },
    {
      "info": {
        "block_hash": "mh_E5WHocVhS4DZZQB9raH3Wjc4D8hmCZYi3ykvCLpZwYPsdnbGKX7J9QQ4vcnHMa13sRzTkn3VsWhNk1",
        "chan_id": "ch_CtBFQVXBxEkM9jHH9TPnQNBYpeLquB7yFqTnU2e7sYDycTnkoVWu3wsKcsGCdEWA3DfMfighexGh36",
        "channel": {
          "channel_amount": 110000000000000,
          "channel_reserve": 2,
          "delegate_ids": [],
          "id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
          "initiator_amount": 70000000000000,
          "initiator_id": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
          "lock_period": 10,
          "locked_until": 0,
          "responder_amount": 40000000000000,
          "responder_id": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc",
          "round": 1,
          "solo_round": 0,
          "state_hash": "st_xbBf7c3Y8acHvN2Udyh7FDzMeR4dVzrpKkEoIxsQvd3eIQz8"
        },
        "tx": "tx_dHhfK1FFTkN3SDRoTGhBRjQ5WEsyM0ZTaDVtWmQ0UWhpV09HVExUYzVRUFYwQkJtbzRQQVVRT2YyZVNnTkFDaU1Samw1eC9OSlh6aEREb3g0MHJ0NzNuWVRyTE40aXNrQ0p2QnJoQTlTeHFNL0VVQUd2TUZnb2pNKzZVVEF1b2lBcHlzYjllWnhFY3hVOFlGTXB2ZzlpWGdjMlYvbnFMTkRZaDRIelVaT2IvUk5tM0pndk90eEc3S3hnbURyaUQrSUV5QWFFQlB4KzBjWWV2cHgrMmR1NGZkNm5mYVQ0dGdDNmkzVDVQMkpzUDdYMVBybkNHUDZvbEltQUFvUUV4SzBWRG81US9VWUprSG95M0pXYkNLamJRaC9XUTNaVUE0UG12Sjd0Zng0WWtZVG5LZ0FBQ0NnQ0dFQVo1MTBnQXdLREZzRi90emRqeHB3ZTgzWlIzS0hzVVBNeDVIaDFYT3VrcVFTZ2pHeEM5M1FId0dsWmyO04cz",
        "tx_hash": "th_Ev325peiKzdCGxY7m1W3CRq7tWwciqpgyMerh7Vatb9RjhKahRmoA1whnpPwLzzSrLEF4ohHnuNZ52"
      },
      "tag": "channel_changed",
      "time": "2020-05-08T08:47:55.598073Z",
      "type": "receive"
    },
    {
      "info": {
        "info": "funding_signed",
        "tx": "tx_dHhfK1FFTkN3SDRoTGhBRjQ5WEsyM0ZTaDVtWmQ0UWhpV09HVExUYzVRUFYwQkJtbzRQQVVRT2YyZVNnTkFDaU1Samw1eC9OSlh6aEREb3g0MHJ0NzNuWVRyTE40aXNrQ0p2QnJoQTlTeHFNL0VVQUd2TUZnb2pNKzZVVEF1b2lBcHlzYjllWnhFY3hVOFlGTXB2ZzlpWGdjMlYvbnFMTkRZaDRIelVaT2IvUk5tM0pndk90eEc3S3hnbURyaUQrSUV5QWFFQlB4KzBjWWV2cHgrMmR1NGZkNm5mYVQ0dGdDNmkzVDVQMkpzUDdYMVBybkNHUDZvbEltQUFvUUV4SzBWRG81US9VWUprSG95M0pXYkNLamJRaC9XUTNaVUE0UG12Sjd0Zng0WWtZVG5LZ0FBQ0NnQ0dFQVo1MTBnQXdLREZzRi90emRqeHB3ZTgzWlIzS0hzVVBNeDVIaDFYT3VrcVFTZ2pHeEM5M1FId0dsWmyO04cz",
        "type": "channel_create_tx"
      },
      "tag": "on_chain_tx",
      "time": "2020-05-08T08:47:55.529633Z",
      "type": "report"
    },
    {
      "info": {
        "event": "ba_ZnVuZGluZ19zaWduZWTjxZfy",
        "fsm_id": "ba_YmFfTVo0SkU5OUxCRVBqRzRvSVRyTnc5OUk2WS9NUnZMamgzTGJVOXJMRllLUzFtRDE2AqccCA=="
      },
      "tag": "info",
      "time": "2020-05-08T08:47:55.528492Z",
      "type": "report"
    },
    {
      "info": {
        "block_hash": "mh_3xrELpC9Dg6PpCwXFfiUrg4tu6BTbFexnLAXeJULcb6WQeuHNBYrdCYMpA7YApx8hYx2mDYzfjJv5",
        "data": {
          "tx": "tx_dHhfK1FFTkN3SDRoTGhBRjQ5WEsyM0ZTaDVtWmQ0UWhpV09HVExUYzVRUFYwQkJtbzRQQVVRT2YyZVNnTkFDaU1Samw1eC9OSlh6aEREb3g0MHJ0NzNuWVRyTE40aXNrQ0p2QnJoQTlTeHFNL0VVQUd2TUZnb2pNKzZVVEF1b2lBcHlzYjllWnhFY3hVOFlGTXB2ZzlpWGdjMlYvbnFMTkRZaDRIelVaT2IvUk5tM0pndk90eEc3S3hnbURyaUQrSUV5QWFFQlB4KzBjWWV2cHgrMmR1NGZkNm5mYVQ0dGdDNmkzVDVQMkpzUDdYMVBybkNHUDZvbEltQUFvUUV4SzBWRG81US9VWUprSG95M0pXYkNLamJRaC9XUTNaVUE0UG12Sjd0Zng0WWtZVG5LZ0FBQ0NnQ0dFQVo1MTBnQXdLREZzRi90emRqeHB3ZTgzWlIzS0hzVVBNeDVIaDFYT3VrcVFTZ2pHeEM5M1FId0dsWmyO04cz"
        },
        "temporary_channel_id": "ch_3h9DLbMKuWgdrTdCgGTtLtaGsXxLuErFm5Nd4hL1ofktLp6Y3nVmgYjNUmTR2sHCYCpzsKkQDgkwb"
      },
      "tag": "funding_signed",
      "time": "2020-05-08T08:47:55.523715Z",
      "type": "receive"
    },
    {
      "info": {
        "block_hash": "mh_3xrELpC9Dg6PpCwXFfiUrg4tu6BTbFexnLAXeJULcb6WQeuHNBYrdCYMpA7YApx8hYx2mDYzfjJv5",
        "data": {
          "tx": "tx_dHhfK01zTEFmaEN1RUFYajFjcmJjVktIbVpsM2hDR0pZNFpNdE56bEE5WFFFR2FqZzhCUkE1L1o1S0EwQUtJeEdPWG5IODBsZk9FTU9qSGpTdTN2ZWRoT3NzM2lLeVFJbThHdUlQNGdUSUJvUUUvSDdSeGg2K25IN1oyN2g5M3FkOXBQaTJBTHFMZFBrL1ltdy90ZlUrdWNJWS9xaVVpWUFDaEFURXJSVU9qbEQ5UmdtUWVqTGNsWnNJcU50Q0g5WkRkbFFEZythOG51MS9IaGlSaE9jcUFBQUlLQUlZUUJublhTQURBb01Xd1grM04yUEduQjd6ZGxIY29leFE4ekhrZUhWYzY2U3BCS0NNYkVMM2RBY3ZzUVZrPazvP2Q=",
          "updates": []
        },
        "temporary_channel_id": "ch_3h9DLbMKuWgdrTdCgGTtLtaGsXxLuErFm5Nd4hL1ofktLp6Y3nVmgYjNUmTR2sHCYCpzsKkQDgkwb"
      },
      "tag": "funding_created",
      "time": "2020-05-08T08:47:55.514613Z",
      "type": "send"
    },
    {
      "info": {
        "tx": "tx_dHhfK01zTEFmaEN1RUFYajFjcmJjVktIbVpsM2hDR0pZNFpNdE56bEE5WFFFR2FqZzhCUkE1L1o1S0EwQUtJeEdPWG5IODBsZk9FTU9qSGpTdTN2ZWRoT3NzM2lLeVFJbThHdUlQNGdUSUJvUUUvSDdSeGg2K25IN1oyN2g5M3FkOXBQaTJBTHFMZFBrL1ltdy90ZlUrdWNJWS9xaVVpWUFDaEFURXJSVU9qbEQ5UmdtUWVqTGNsWnNJcU50Q0g5WkRkbFFEZythOG51MS9IaGlSaE9jcUFBQUlLQUlZUUJublhTQURBb01Xd1grM04yUEduQjd6ZGxIY29leFE4ekhrZUhWYzY2U3BCS0NNYkVMM2RBY3ZzUVZrPazvP2Q=",
        "tx_type": "create_tx"
      },
      "tag": "signed",
      "time": "2020-05-08T08:47:55.514439Z",
      "type": "receive"
    },
    {
      "info": {
        "info": {
          "signed_tx": "encoding_error",
          "updates": []
        },
        "tag": "create_tx",
        "type": "sign"
      },
      "tag": "sign",
      "time": "2020-05-08T08:47:55.496663Z",
      "type": "request"
    },
    {
      "info": {
        "event": "ba_Y2hhbm5lbF9hY2NlcHTTsHqq"
      },
      "tag": "info",
      "time": "2020-05-08T08:47:55.479660Z",
      "type": "report"
    },
    {
      "info": {
        "chain_hash": "ba_YmFfcmlTVTIrQ3R6SXBpc2Q0VFVSVDRlU0w3bG1FTERJSUFCcnFLNzBWVlVzNHhPcjI186+q7Q==",
        "channel_reserve": 2,
        "initiator": "ak_3e25TbYb2Yn73VabAAAQCJG8YzntvhAaFsreeZR7b8E313eBbyVgJWYb8SUQDXVxCcvCEc6HNzE4R",
        "initiator_amount": 70000000000000,
        "minimum_depth": 10,
        "minimum_depth_strategy": "txfee",
        "responder": "ak_3e25TU65ND45fF9g47nN7SSyZ8PgSvopFJCq5f7MVkvdo6vGXAArLN5t59F5WtkeGfpyFiNRAtqUH",
        "responder_amount": 40000000000000,
        "temporary_channel_id": "ch_3h9DLbMKuWgdrTdCgGTtLtaGsXxLuErFm5Nd4hL1ofktLp6Y3nVmgYjNUmTR2sHCYCpzsKkQDgkwb"
      },
      "tag": "channel_accept",
      "time": "2020-05-08T08:47:55.479217Z",
      "type": "receive"
    },
    {
      "info": {
        "chain_hash": "ba_YmFfcmlTVTIrQ3R6SXBpc2Q0VFVSVDRlU0w3bG1FTERJSUFCcnFLNzBWVlVzNHhPcjI186+q7Q==",
        "channel_reserve": 2,
        "initiator": "ak_3e25TbYb2Yn73VabAAAQCJG8YzntvhAaFsreeZR7b8E313eBbyVgJWYb8SUQDXVxCcvCEc6HNzE4R",
        "initiator_amount": 70000000000000,
        "lock_period": 10,
        "push_amount": 1,
        "responder": "ak_3e25TU65ND45fF9g47nN7SSyZ8PgSvopFJCq5f7MVkvdo6vGXAArLN5t59F5WtkeGfpyFiNRAtqUH",
        "responder_amount": 40000000000000,
        "temporary_channel_id": "ch_3h9DLbMKuWgdrTdCgGTtLtaGsXxLuErFm5Nd4hL1ofktLp6Y3nVmgYjNUmTR2sHCYCpzsKkQDgkwb"
      },
      "tag": "channel_open",
      "time": "2020-05-08T08:47:55.473038Z",
      "type": "send"
    },
    {
      "info": {
        "event": "ba_ZnNtX3Vw8DHOTw==",
        "fsm_id": "ba_YmFfTVo0SkU5OUxCRVBqRzRvSVRyTnc5OUk2WS9NUnZMamgzTGJVOXJMRllLUzFtRDE2AqccCA=="
      },
      "tag": "info",
      "time": "2020-05-08T08:47:55.385325Z",
      "type": "report"
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423483,
  "jsonrpc": "2.0",
  "method": "channels.history.fetch",
  "params": {
    "n": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
  "id": -576460752303423483,
  "jsonrpc": "2.0",
  "result": [
    {
      "info": {
        "state": "ba_dHhfK1FFTkN3SDRoTGhBRjQ5WEsyM0ZTaDVtWmQ0UWhpV09HVExUYzVRUFYwQkJtbzRQQVVRT2YyZVNnTkFDaU1Samw1eC9OSlh6aEREb3g0MHJ0NzNuWVRyTE40aXNrQ0p2QnJoQTlTeHFNL0VVQUd2TUZnb2pNKzZVVEF1b2lBcHlzYjllWnhFY3hVOFlGTXB2ZzlpWGdjMlYvbnFMTkRZaDRIelVaT2IvUk5tM0pndk90eEc3S3hnbURyaUQrSUV5QWFFQlB4KzBjWWV2cHgrMmR1NGZkNm5mYVQ0dGdDNmkzVDVQMkpzUDdYMVBybkNHUDZvbEltQUFvUUV4SzBWRG81US9VWUprSG95M0pXYkNLamJRaC9XUTNaVUE0UG12Sjd0Zng0WWtZVG5LZ0FBQ0NnQ0dFQVo1MTBnQXdLREZzRi90emRqeHB3ZTgzWlIzS0hzVVBNeDVIaDFYT3VrcVFTZ2pHeEM5M1FId0dsWmyO04cz"
      },
      "tag": "update",
      "time": "2020-05-08T08:47:55.685261Z",
      "type": "report"
    },
    {
      "info": {
        "event": "ba_b3BlbqPd6OU="
      },
      "tag": "info",
      "time": "2020-05-08T08:47:55.684420Z",
      "type": "report"
    },
    {
      "info": {
        "event": "ba_ZnVuZGluZ19sb2NrZWTNLzad"
      },
      "tag": "info",
      "time": "2020-05-08T08:47:55.678490Z",
      "type": "report"
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423482,
  "jsonrpc": "2.0",
  "method": "channels.history.fetch",
  "params": {
    "n": 1,
    "tag": [
      "update"
    ],
    "type": [
      "rpt"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
  "id": -576460752303423482,
  "jsonrpc": "2.0",
  "result": [
    {
      "info": {
        "state": "ba_dHhfK1FFTkN3SDRoTGhBRjQ5WEsyM0ZTaDVtWmQ0UWhpV09HVExUYzVRUFYwQkJtbzRQQVVRT2YyZVNnTkFDaU1Samw1eC9OSlh6aEREb3g0MHJ0NzNuWVRyTE40aXNrQ0p2QnJoQTlTeHFNL0VVQUd2TUZnb2pNKzZVVEF1b2lBcHlzYjllWnhFY3hVOFlGTXB2ZzlpWGdjMlYvbnFMTkRZaDRIelVaT2IvUk5tM0pndk90eEc3S3hnbURyaUQrSUV5QWFFQlB4KzBjWWV2cHgrMmR1NGZkNm5mYVQ0dGdDNmkzVDVQMkpzUDdYMVBybkNHUDZvbEltQUFvUUV4SzBWRG81US9VWUprSG95M0pXYkNLamJRaC9XUTNaVUE0UG12Sjd0Zng0WWtZVG5LZ0FBQ0NnQ0dFQVo1MTBnQXdLREZzRi90emRqeHB3ZTgzWlIzS0hzVVBNeDVIaDFYT3VrcVFTZ2pHeEM5M1FId0dsWmyO04cz"
      },
      "tag": "update",
      "time": "2020-05-08T08:47:55.685261Z",
      "type": "report"
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423481,
  "jsonrpc": "2.0",
  "method": "channels.history.fetch",
  "params": {
    "n": 1,
    "type": [
      "rcv"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
  "id": -576460752303423481,
  "jsonrpc": "2.0",
  "result": [
    {
      "info": {
        "channel_id": "ch_CtBFQVXBxEkM9jHH9TPnQNBYpeLquB7yFqTnU2e7sYDycTnkoVWu3wsKcsGCdEWA3DfMfighexGh36",
        "temporary_channel_id": "ch_3h9DLbMKuWgdrTdCgGTtLtaGsXxLuErFm5Nd4hL1ofktLp6Y3nVmgYjNUmTR2sHCYCpzsKkQDgkwb"
      },
      "tag": "funding_locked",
      "time": "2020-05-08T08:47:55.678446Z",
      "type": "receive"
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423480,
  "jsonrpc": "2.0",
  "method": "channels.history.fetch",
  "params": {
    "n": 1,
    "type": [
      "snd"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
  "id": -576460752303423480,
  "jsonrpc": "2.0",
  "result": [
    {
      "info": {
        "channel_id": "ch_CtBFQVXBxEkM9jHH9TPnQNBYpeLquB7yFqTnU2e7sYDycTnkoVWu3wsKcsGCdEWA3DfMfighexGh36",
        "temporary_channel_id": "ch_3h9DLbMKuWgdrTdCgGTtLtaGsXxLuErFm5Nd4hL1ofktLp6Y3nVmgYjNUmTR2sHCYCpzsKkQDgkwb"
      },
      "tag": "funding_locked",
      "time": "2020-05-08T08:47:55.676654Z",
      "type": "send"
    }
  ],
  "version": 1
}
```
