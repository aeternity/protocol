
#### initiator ---> node (2019-03-13 11:13:59.983)
```javascript
{
  "action": "withdraw",
  "payload": {
    "amount": 2
  }
}
```

#### initiator <--- node (2019-03-13 11:14:00.43)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "tx": "tx_+HI0AaEG3hZD/8OqLoPpLcMc5cfQwNyjR2sUdl6Nry6JJUyBUsKhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AgCGEjCc5UAAoOYOjzVcFes6ShmrqmbqfuH+VF/KioEqDn9E3t3CQxWZBAg77YD2"
  },
  "tag": "withdraw_tx",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:14:00.44)
```javascript
{
  "action": "withdraw_tx",
  "payload": {
    "tx": "tx_+LwLAfhCuECOQhinCK+2ncJr1Ydr+fodgJpD016O6VfDo2e0tuQAOgpmr+nDnY7NWtKCR9kLV4LGfgaq+W6mKFWkZ2twxLcDuHT4cjQBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noCAIYSMJzlQACg5g6PNVwV6zpKGauqZup+4f5UX8qKgSoOf0Te3cJDFZkECIbym5I="
  }
}
```

#### responder <--- node (2019-03-13 11:14:00.99)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "withdraw_created"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:14:00.102)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "tx": "tx_+HI0AaEG3hZD/8OqLoPpLcMc5cfQwNyjR2sUdl6Nry6JJUyBUsKhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AgCGEjCc5UAAoOYOjzVcFes6ShmrqmbqfuH+VF/KioEqDn9E3t3CQxWZBAg77YD2"
  },
  "tag": "withdraw_ack",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:14:00.103)
```javascript
{
  "action": "withdraw_ack",
  "payload": {
    "tx": "tx_+LwLAfhCuEDZjgiAKDp0H84yEu53IP4bKaHZyT+d9CYIh37lHmrkxMWQzqR+XwXK7rcx54Wd8IL4kdv+3k8UEkd8aHV/JUUHuHT4cjQBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noCAIYSMJzlQACg5g6PNVwV6zpKGauqZup+4f5UX8qKgSoOf0Te3cJDFZkECDZHyok="
  }
}
```

#### responder <--- node (2019-03-13 11:14:00.133)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "tx": "tx_+P4LAfiEuECOQhinCK+2ncJr1Ydr+fodgJpD016O6VfDo2e0tuQAOgpmr+nDnY7NWtKCR9kLV4LGfgaq+W6mKFWkZ2twxLcDuEDZjgiAKDp0H84yEu53IP4bKaHZyT+d9CYIh37lHmrkxMWQzqR+XwXK7rcx54Wd8IL4kdv+3k8UEkd8aHV/JUUHuHT4cjQBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noCAIYSMJzlQACg5g6PNVwV6zpKGauqZup+4f5UX8qKgSoOf0Te3cJDFZkECP6TRsc="
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:14:00.139)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "tx": "tx_+P4LAfiEuECOQhinCK+2ncJr1Ydr+fodgJpD016O6VfDo2e0tuQAOgpmr+nDnY7NWtKCR9kLV4LGfgaq+W6mKFWkZ2twxLcDuEDZjgiAKDp0H84yEu53IP4bKaHZyT+d9CYIh37lHmrkxMWQzqR+XwXK7rcx54Wd8IL4kdv+3k8UEkd8aHV/JUUHuHT4cjQBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noCAIYSMJzlQACg5g6PNVwV6zpKGauqZup+4f5UX8qKgSoOf0Te3cJDFZkECP6TRsc="
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:14:03.966)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "own_withdraw_locked"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:14:03.976)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "own_withdraw_locked"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:14:03.977)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "withdraw_locked"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:14:03.981)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "withdraw_locked"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:14:03.997)
```javascript
{
  "action": "update",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "state": "tx_+P4LAfiEuECOQhinCK+2ncJr1Ydr+fodgJpD016O6VfDo2e0tuQAOgpmr+nDnY7NWtKCR9kLV4LGfgaq+W6mKFWkZ2twxLcDuEDZjgiAKDp0H84yEu53IP4bKaHZyT+d9CYIh37lHmrkxMWQzqR+XwXK7rcx54Wd8IL4kdv+3k8UEkd8aHV/JUUHuHT4cjQBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noCAIYSMJzlQACg5g6PNVwV6zpKGauqZup+4f5UX8qKgSoOf0Te3cJDFZkECP6TRsc="
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:14:03.998)
```javascript
{
  "action": "update",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "state": "tx_+P4LAfiEuECOQhinCK+2ncJr1Ydr+fodgJpD016O6VfDo2e0tuQAOgpmr+nDnY7NWtKCR9kLV4LGfgaq+W6mKFWkZ2twxLcDuEDZjgiAKDp0H84yEu53IP4bKaHZyT+d9CYIh37lHmrkxMWQzqR+XwXK7rcx54Wd8IL4kdv+3k8UEkd8aHV/JUUHuHT4cjQBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noCAIYSMJzlQACg5g6PNVwV6zpKGauqZup+4f5UX8qKgSoOf0Te3cJDFZkECP6TRsc="
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:14:04.501)
```javascript
{
  "action": "withdraw",
  "payload": {
    "amount": 2
  }
}
```

#### responder <--- node (2019-03-13 11:14:04.526)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "tx": "tx_+HI0AaEG3hZD/8OqLoPpLcMc5cfQwNyjR2sUdl6Nry6JJUyBUsKhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAgCGEjCc5UAAoBVQItrXeXi1NNVLrFNRky7mqhur6CrV3Ihp6ANYAJVSBQMLv5DQ"
  },
  "tag": "withdraw_tx",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:14:04.529)
```javascript
{
  "action": "withdraw_tx",
  "payload": {
    "tx": "tx_+LwLAfhCuEAm1YwhmDE5ZbXeimNq8NHkdDKfRN0tlAt58kYfdjc6oJxsy200NxFpRPhShOb7PSrW7I7AWTYl5blWuGou7xcGuHT4cjQBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFysCAIYSMJzlQACgFVAi2td5eLU01UusU1GTLuaqG6voKtXciGnoA1gAlVIFA1AT3fk="
  }
}
```

#### initiator <--- node (2019-03-13 11:14:04.563)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "withdraw_created"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:14:04.565)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "tx": "tx_+HI0AaEG3hZD/8OqLoPpLcMc5cfQwNyjR2sUdl6Nry6JJUyBUsKhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAgCGEjCc5UAAoBVQItrXeXi1NNVLrFNRky7mqhur6CrV3Ihp6ANYAJVSBQMLv5DQ"
  },
  "tag": "withdraw_ack",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:14:04.565)
```javascript
{
  "action": "withdraw_ack",
  "payload": {
    "tx": "tx_+LwLAfhCuEBhkdw/EE02rQqOs6DNS1RRFw7yROL+jfD54f2cNrObMnKYlNZubKj9sfwU7VgvWrtXFuT8uSJZCUwlyh6tyeYBuHT4cjQBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFysCAIYSMJzlQACgFVAi2td5eLU01UusU1GTLuaqG6voKtXciGnoA1gAlVIFA1Yl1w8="
  }
}
```

#### initiator <--- node (2019-03-13 11:14:04.586)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "tx": "tx_+P4LAfiEuEAm1YwhmDE5ZbXeimNq8NHkdDKfRN0tlAt58kYfdjc6oJxsy200NxFpRPhShOb7PSrW7I7AWTYl5blWuGou7xcGuEBhkdw/EE02rQqOs6DNS1RRFw7yROL+jfD54f2cNrObMnKYlNZubKj9sfwU7VgvWrtXFuT8uSJZCUwlyh6tyeYBuHT4cjQBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFysCAIYSMJzlQACgFVAi2td5eLU01UusU1GTLuaqG6voKtXciGnoA1gAlVIFA1BOd4g="
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:14:04.616)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "tx": "tx_+P4LAfiEuEAm1YwhmDE5ZbXeimNq8NHkdDKfRN0tlAt58kYfdjc6oJxsy200NxFpRPhShOb7PSrW7I7AWTYl5blWuGou7xcGuEBhkdw/EE02rQqOs6DNS1RRFw7yROL+jfD54f2cNrObMnKYlNZubKj9sfwU7VgvWrtXFuT8uSJZCUwlyh6tyeYBuHT4cjQBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFysCAIYSMJzlQACgFVAi2td5eLU01UusU1GTLuaqG6voKtXciGnoA1gAlVIFA1BOd4g="
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:14:08.411)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "own_withdraw_locked"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:14:08.421)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "own_withdraw_locked"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:14:08.421)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "withdraw_locked"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:14:08.422)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "withdraw_locked"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:14:08.431)
```javascript
{
  "action": "update",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "state": "tx_+P4LAfiEuEAm1YwhmDE5ZbXeimNq8NHkdDKfRN0tlAt58kYfdjc6oJxsy200NxFpRPhShOb7PSrW7I7AWTYl5blWuGou7xcGuEBhkdw/EE02rQqOs6DNS1RRFw7yROL+jfD54f2cNrObMnKYlNZubKj9sfwU7VgvWrtXFuT8uSJZCUwlyh6tyeYBuHT4cjQBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFysCAIYSMJzlQACgFVAi2td5eLU01UusU1GTLuaqG6voKtXciGnoA1gAlVIFA1BOd4g="
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:14:08.445)
```javascript
{
  "action": "update",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "state": "tx_+P4LAfiEuEAm1YwhmDE5ZbXeimNq8NHkdDKfRN0tlAt58kYfdjc6oJxsy200NxFpRPhShOb7PSrW7I7AWTYl5blWuGou7xcGuEBhkdw/EE02rQqOs6DNS1RRFw7yROL+jfD54f2cNrObMnKYlNZubKj9sfwU7VgvWrtXFuT8uSJZCUwlyh6tyeYBuHT4cjQBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwqEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFysCAIYSMJzlQACgFVAi2td5eLU01UusU1GTLuaqG6voKtXciGnoA1gAlVIFA1BOd4g="
  },
  "version": 1
}
```
