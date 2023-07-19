# gnosis-freewillai-hackaton


## Step by Step

### Add to metamask (https://docs.gnosischain.com/about/networks/chiado)
### Get xDAI and GNO (https://gnosisfaucet.com/)


### Deploy contracts (mainnet gnosischain.com, testnet chiadochain.net)
```bash
forge create contracts/FreeWillAIToken.sol:FreeWillAI \
    --rpc-url https://rpc.chiadochain.net \
    --private-key [metamask-private-key]

forge create contracts/TaskRunner.sol:TaskRunner \
    --rpc-url https://rpc.chiadochain.net \
    --private-key [metamask-private-key]
    --constructor-args [token-address]

```
### export addresses as environ variables
```bash
export FREEWILLAI_TOKEN_ADDRESS=0x...
export FREEWILLAI_TASK_RUNNER_ADDRESS=0x...
```

### Install FreeWillAI from source
```bash
git clone git@github.com:FreeWillAI/freewilliai.git _freewilliai
cd _freewilliai
python setup.py install
cd ..
cp -r _freewilliai/freewillai _freewilliai/scripts .
```

### Mint FWAI to nodes and the user (Do not use the same metamask account for nodes and user)
```bash
# Repeat this with user, node1 and node2 addresses
python -m token_owner -n https://rpc.chiadochain.net --mint 200 --to [user-address]
python -m token_owner -n https://rpc.chiadochain.net --mint 200 --to [node1-address]
python -m token_owner -n https://rpc.chiadochain.net --mint 200 --to [node2-address]
```

### Run nodes
```bash
python -m freewilliai.node -s 200 
```

### Declare contract addresses in main.py and run the code
```bash
python main.py
```
