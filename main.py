import asyncio
import freewillai
from keras.models import load_model
from web3.middleware import geth_poa_middleware


GNOSIS_TESTNET_RPC = "https://rpc.chiadochain.net"
TESTNET_TOKEN_ADDRESS = "0xc365bc6d5ADd80998FFa68d0Da4925A54C43D0F6"
TESTNET_TASK_RUNNER_ADDRESS = "0x66714d35a0d8C585665AA73279b1828eC049eB26"

GNOSIS_MAINNET_RPC = "https://rpc.gnosischain.com"
MAINNET_TOKEN_ADDRESS = ""        # To deploy
MAINNET_TASK_RUNNER_ADDRESS = ""  # To deploy


# Get freewillai provider of gnosis testnet
gnosis_testnet = freewillai.connect(
    GNOSIS_TESTNET_RPC,
    token_address=TESTNET_TOKEN_ADDRESS,
    task_runner_address=TESTNET_TASK_RUNNER_ADDRESS,
)

# Goerli needs this
gnosis_testnet.add_middleware(geth_poa_middleware, 'POA', layer=0)


# Load model
model = load_model("keras_model_dnn/")

# Get dataset
dataset = "keras_testing_dataset.csv"

# Run on Freewillai
result = asyncio.run(freewillai.run_task(model, dataset, provider=gnosis_testnet))
