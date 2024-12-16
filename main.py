# Чтение кошельков для сравнения из файла provided_wallets.txt
with open('provided_wallets.txt', 'r') as file:
    provided_wallets = file.read().splitlines()

# Чтение кошельков из файла wallets.txt
with open('wallets.txt', 'r') as file:
    file_wallets = file.read().splitlines()

# Сравнение кошельков
matching_wallets = set(provided_wallets).intersection(file_wallets)
non_matching_wallets = set(file_wallets).difference(provided_wallets)

# Вывод результатов
print("Совпадающие кошельки(eligble wallets):")
for wallet in matching_wallets:
    print(wallet)

print("\nНесовпадающие кошельки(not eligble wallets):")
for wallet in non_matching_wallets:
    print(wallet)
