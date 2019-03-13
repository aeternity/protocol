
#### initiator ---> node (2019-03-13 11:13:49.147)
```javascript
{
  "action": "deposit",
  "payload": {
    "amount": 2
  }
}
```

#### initiator <--- node (2019-03-13 11:13:49.182)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "tx": "tx_+HIzAaEG3hZD/8OqLoPpLcMc5cfQwNyjR2sUdl6Nry6JJUyBUsKhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AgCGEjCc5UAAoOS8MfHBlgjixRLKCjcyefTuP2/GlRfOlEev4ykJFNXnAgdISyAN"
  },
  "tag": "deposit_tx",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:49.182)
```javascript
{
  "action": "deposit_tx",
  "payload": {
    "tx": "tx_+LwLAfhCuEDQX4m0yBGlnMg/hdBdZ9axAQHoWDZ+lvQ6GPsCsaXZ1fAsU93aKI0WMUFIQNewNmmpWGZiJkIDlGIOzxkrWWIEuHT4cjMBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noCAIYSMJzlQACg5Lwx8cGWCOLFEsoKNzJ59O4/b8aVF86UR6/jKQkU1ecCB3ML4QM="
  }
}
```

#### responder <--- node (2019-03-13 11:13:49.210)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "deposit_created"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:49.210)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "tx": "tx_+HIzAaEG3hZD/8OqLoPpLcMc5cfQwNyjR2sUdl6Nry6JJUyBUsKhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AgCGEjCc5UAAoOS8MfHBlgjixRLKCjcyefTuP2/GlRfOlEev4ykJFNXnAgdISyAN"
  },
  "tag": "deposit_ack",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:13:49.211)
```javascript
{
  "action": "deposit_ack",
  "payload": {
    "tx": "tx_+LwLAfhCuECwc0WOymYdJmnN3w/xYsi2sZYBC5A7/wdPBbpDiaVegXEfaMOrJNaO+q8RfjxE/M4M2RleAHoKuE3T7t+it6UEuHT4cjMBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noCAIYSMJzlQACg5Lwx8cGWCOLFEsoKNzJ59O4/b8aVF86UR6/jKQkU1ecCB0yzf3Q="
  }
}
```

#### responder <--- node (2019-03-13 11:13:49.229)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "tx": "tx_+P4LAfiEuECwc0WOymYdJmnN3w/xYsi2sZYBC5A7/wdPBbpDiaVegXEfaMOrJNaO+q8RfjxE/M4M2RleAHoKuE3T7t+it6UEuEDQX4m0yBGlnMg/hdBdZ9axAQHoWDZ+lvQ6GPsCsaXZ1fAsU93aKI0WMUFIQNewNmmpWGZiJkIDlGIOzxkrWWIEuHT4cjMBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noCAIYSMJzlQACg5Lwx8cGWCOLFEsoKNzJ59O4/b8aVF86UR6/jKQkU1ecCB7iJxJ0="
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:49.244)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "tx": "tx_+P4LAfiEuECwc0WOymYdJmnN3w/xYsi2sZYBC5A7/wdPBbpDiaVegXEfaMOrJNaO+q8RfjxE/M4M2RleAHoKuE3T7t+it6UEuEDQX4m0yBGlnMg/hdBdZ9axAQHoWDZ+lvQ6GPsCsaXZ1fAsU93aKI0WMUFIQNewNmmpWGZiJkIDlGIOzxkrWWIEuHT4cjMBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noCAIYSMJzlQACg5Lwx8cGWCOLFEsoKNzJ59O4/b8aVF86UR6/jKQkU1ecCB7iJxJ0="
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:53.9)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "own_deposit_locked"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:53.12)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "own_deposit_locked"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:53.15)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "deposit_locked"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:53.15)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "deposit_locked"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:53.36)
```javascript
{
  "action": "update",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "state": "tx_+P4LAfiEuECwc0WOymYdJmnN3w/xYsi2sZYBC5A7/wdPBbpDiaVegXEfaMOrJNaO+q8RfjxE/M4M2RleAHoKuE3T7t+it6UEuEDQX4m0yBGlnMg/hdBdZ9axAQHoWDZ+lvQ6GPsCsaXZ1fAsU93aKI0WMUFIQNewNmmpWGZiJkIDlGIOzxkrWWIEuHT4cjMBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noCAIYSMJzlQACg5Lwx8cGWCOLFEsoKNzJ59O4/b8aVF86UR6/jKQkU1ecCB7iJxJ0="
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:53.43)
```javascript
{
  "action": "update",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "state": "tx_+P4LAfiEuECwc0WOymYdJmnN3w/xYsi2sZYBC5A7/wdPBbpDiaVegXEfaMOrJNaO+q8RfjxE/M4M2RleAHoKuE3T7t+it6UEuEDQX4m0yBGlnMg/hdBdZ9axAQHoWDZ+lvQ6GPsCsaXZ1fAsU93aKI0WMUFIQNewNmmpWGZiJkIDlGIOzxkrWWIEuHT4cjMBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noCAIYSMJzlQACg5Lwx8cGWCOLFEsoKNzJ59O4/b8aVF86UR6/jKQkU1ecCB7iJxJ0="
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:13:53.693)
```javascript
{
  "action": "deposit",
  "payload": {
    "amount": 2
  }
}
```

#### responder <--- node (2019-03-13 11:13:53.716)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "tx": "tx_+HIzAaEG3hZD/8OqLoPpLcMc5cfQwNyjR2sUdl6Nry6JJUyBUsKhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAgCGEjCc5UAAoADf6a1QrkT2vHtQiVJwBpbYZ51IXlgBekXHdUgYqHkjAwKBHDNh"
  },
  "tag": "deposit_tx",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:13:53.718)
```javascript
{
  "action": "deposit_tx",
  "payload": {
    "tx": "tx_+LwLAfhCuEA1Gsp/FCQKu4qnZr8eFAF/PE469qrRh5w1gsvBfvQTJgJVCrEs+St8lL744KGPyK8D2MpWw0k+9hIY1Le9RnMCuHT4cjMBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFysCAIYSMJzlQACgAN/prVCuRPa8e1CJUnAGlthnnUheWAF6Rcd1SBioeSMDAka8Zl4="
  }
}
```

#### initiator <--- node (2019-03-13 11:13:53.746)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "deposit_created"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:53.747)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "tx": "tx_+HIzAaEG3hZD/8OqLoPpLcMc5cfQwNyjR2sUdl6Nry6JJUyBUsKhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAgCGEjCc5UAAoADf6a1QrkT2vHtQiVJwBpbYZ51IXlgBekXHdUgYqHkjAwKBHDNh"
  },
  "tag": "deposit_ack",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:53.748)
```javascript
{
  "action": "deposit_ack",
  "payload": {
    "tx": "tx_+LwLAfhCuEDVAn1sUByPIEEgFsMvhnvafGgPzSIuVMdZGsMrOq1YtNreNz0nSHkG1QBqoYJI/nHo0hUawIBuNo3nTc/3FiMFuHT4cjMBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFysCAIYSMJzlQACgAN/prVCuRPa8e1CJUnAGlthnnUheWAF6Rcd1SBioeSMDAoJef1Y="
  }
}
```

#### initiator <--- node (2019-03-13 11:13:53.768)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "tx": "tx_+P4LAfiEuEA1Gsp/FCQKu4qnZr8eFAF/PE469qrRh5w1gsvBfvQTJgJVCrEs+St8lL744KGPyK8D2MpWw0k+9hIY1Le9RnMCuEDVAn1sUByPIEEgFsMvhnvafGgPzSIuVMdZGsMrOq1YtNreNz0nSHkG1QBqoYJI/nHo0hUawIBuNo3nTc/3FiMFuHT4cjMBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFysCAIYSMJzlQACgAN/prVCuRPa8e1CJUnAGlthnnUheWAF6Rcd1SBioeSMDAmLe5B8="
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:53.785)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "tx": "tx_+P4LAfiEuEA1Gsp/FCQKu4qnZr8eFAF/PE469qrRh5w1gsvBfvQTJgJVCrEs+St8lL744KGPyK8D2MpWw0k+9hIY1Le9RnMCuEDVAn1sUByPIEEgFsMvhnvafGgPzSIuVMdZGsMrOq1YtNreNz0nSHkG1QBqoYJI/nHo0hUawIBuNo3nTc/3FiMFuHT4cjMBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFysCAIYSMJzlQACgAN/prVCuRPa8e1CJUnAGlthnnUheWAF6Rcd1SBioeSMDAmLe5B8="
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:57.942)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "own_deposit_locked"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:57.942)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "own_deposit_locked"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:57.947)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "deposit_locked"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:57.949)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "deposit_locked"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:57.971)
```javascript
{
  "action": "update",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "state": "tx_+P4LAfiEuEA1Gsp/FCQKu4qnZr8eFAF/PE469qrRh5w1gsvBfvQTJgJVCrEs+St8lL744KGPyK8D2MpWw0k+9hIY1Le9RnMCuEDVAn1sUByPIEEgFsMvhnvafGgPzSIuVMdZGsMrOq1YtNreNz0nSHkG1QBqoYJI/nHo0hUawIBuNo3nTc/3FiMFuHT4cjMBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFysCAIYSMJzlQACgAN/prVCuRPa8e1CJUnAGlthnnUheWAF6Rcd1SBioeSMDAmLe5B8="
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:57.979)
```javascript
{
  "action": "update",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "state": "tx_+P4LAfiEuEA1Gsp/FCQKu4qnZr8eFAF/PE469qrRh5w1gsvBfvQTJgJVCrEs+St8lL744KGPyK8D2MpWw0k+9hIY1Le9RnMCuEDVAn1sUByPIEEgFsMvhnvafGgPzSIuVMdZGsMrOq1YtNreNz0nSHkG1QBqoYJI/nHo0hUawIBuNo3nTc/3FiMFuHT4cjMBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFysCAIYSMJzlQACgAN/prVCuRPa8e1CJUnAGlthnnUheWAF6Rcd1SBioeSMDAmLe5B8="
  },
  "version": 1
}
```
