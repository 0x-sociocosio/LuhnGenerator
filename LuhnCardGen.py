import random

# Lista de BINs preestablecidos
bins = {
    "400005": "Visa - JPMorgan Chase (EE. UU.)",
    "520082": "Mastercard - Bank of America (EE. UU.)",
    "453242": "Visa - Wells Fargo (EE. UU.)",
    "601100": "Discover - Discover Bank (EE. UU.)",
    "371449": "American Express - American Express (EE. UU.)",
    "414709": "Visa - Citibank (EE. UU.)",
    "530072": "Mastercard - Capital One (EE. UU.)",
    "542418": "Mastercard - HSBC (Reino Unido)",
    "411111": "Visa - Bank of America (EE. UU.)",
    "400551": "Visa - Barclays Bank (Reino Unido)",
    "510510": "Mastercard - JPMorgan Chase (EE. UU.)",
    "345678": "American Express - American Express (EE. UU.)",
    "448407": "Visa - Banco Santander (España)",
    "524293": "Mastercard - BBVA (España)",
    "404159": "Visa - Banamex (México)",
    "520416": "Mastercard - Scotiabank (México)",
    "415231": "Visa - Banco de Bogotá (Colombia)",
    "530054": "Mastercard - Banco do Brasil (Brasil)",
    "402365": "Visa - Itaú Unibanco (Brasil)",
    "356600": "JCB - Sumitomo Mitsui (Japón)"
}

# Algoritmo de Luhn
def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_sum = sum(digits[-1::-2])
    even_sum = 0
    for d in digits[-2::-2]:
        doubled = d * 2
        even_sum += doubled if doubled < 10 else doubled - 9
    return (odd_sum + even_sum) % 10

def calculate_check_digit(card_number):
    checksum = luhn_checksum(int(card_number) * 10)
    return 0 if checksum == 0 else 10 - checksum

def generate_card(bin_number):
    length_to_generate = 15 - len(bin_number)
    card_number = bin_number + ''.join(str(random.randint(0, 9)) for _ in range(length_to_generate))
    check_digit = calculate_check_digit(card_number)
    return card_number + str(check_digit)

def main():
    print("==== Lista de BINs preestablecidos ====\n")
    for i, (bin_code, description) in enumerate(bins.items(), 1):
        print(f"{i}. {bin_code} - {description}")

    print("\n0. Ingresar un BIN personalizado")

    try:
        choice = int(input("\nSeleccione una opción: ").strip())
    except ValueError:
        print("Opción inválida.")
        return

    if choice == 0:
        custom_bin = input("Ingrese su BIN personalizado (4 o 6 dígitos): ").strip()
        if not custom_bin.isdigit() or len(custom_bin) not in [4, 6]:
            print("Error: El BIN debe contener solo números y tener 4 o 6 dígitos.")
            return
        bin_selected = custom_bin
    elif 1 <= choice <= len(bins):
        bin_selected = list(bins.keys())[choice - 1]
        print(f"Seleccionaste: {bin_selected} - {bins[bin_selected]}")
    else:
        print("Opción fuera de rango.")
        return

    card = generate_card(bin_selected)
    print(f"\n *Tarjeta generada válida según Luhn: {card}")

if __name__ == "__main__":
    main()

