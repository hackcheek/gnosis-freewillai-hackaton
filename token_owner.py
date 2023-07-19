import argparse

from freewillai.contract import TokenContract
from freewillai.common import Provider
from freewillai.exceptions import UserRequirement
from freewillai.utils import get_account, load_global_env


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mint', type=int)
    parser.add_argument('-b', '--burn', type=int)
    parser.add_argument('-w', '--wait', action=argparse.BooleanOptionalAction)
    parser.add_argument('-o', '--to', type=str)
    parser.add_argument('-n', '--network', type=str)
    parser.add_argument('-p', '--private-key', type=str)
    parser.add_argument('-e', '--env-file', type=str)

    args = parser.parse_args()

    assert args.network

    if not args.private_key:
        # Load environ variables 
        env_filename = args.env_file or ".env"
        loaded = load_global_env(env_filename)
        if not loaded:
            raise UserRequirement(
                f"Please declare the following environment variables in {env_filename}\n"
                "  > PRIVATE_KEY\n",
            )

    # Get user and Make sure that the user is the owner
    account = get_account()
    
    # Just one option
    assert args.mint or args.burn
    assert not (args.mint and args.burn)
    
    if args.network.startswith("http"):
        provider = Provider(args.network)
    else:
        provider = Provider.by_network_name(args.network).build()
    token = TokenContract(account, provider=provider)
    try: 
        tx_hash = token.initialize()
        token.wait_for_transaction(tx_hash)
    except: ...

    if args.mint and not args.to:
        raise UserRequirement("Please especify which is the address to mint") 

    if args.burn and not args.to:
        raise UserRequirement("Please especify which is the address to burn") 

    if args.mint and args.to:
        tx_hash = token.mint(args.to, args.mint)
        
    if args.burn and args.to:
        tx_hash = token.burn(args.to, args.mint)

    if args.wait:
        token.wait_for_transaction(tx_hash)
        balance = token.get_balance_of(args.to)
        print(f"[*] Address: {args.to} has {balance} fwai")


if __name__ == "__main__":
    cli()
