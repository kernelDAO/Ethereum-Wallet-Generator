from eth_account import Account

def generate_wallets(count):
    wallets = []
    for _ in range(count):
        acct = Account.create()
        address = acct.address
        private_key = acct.key.hex()
        wallets.append(f"{address}:{private_key}")
    
    with open("wallets.txt", "w") as f:
        for wallet in wallets:
            f.write(wallet + "\n")
    print(f"[🟢] {count} wallets successfully generated and saved to wallets.txt.")


if __name__ == "__main__":
    try:
        print("--- Ethereum Wallet Generator ---\nmade by t.me/kerneldrops\n")
        num = int(input("Enter number of wallets to be generated: "))
        generate_wallets(num)
    except ValueError as e:
        print(f"[🔴] {e}")
    except Exception as ex:
        print(f"[🔴] Что-то пошло не так: {ex}")