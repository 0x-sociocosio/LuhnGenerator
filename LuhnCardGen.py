import random

# === Advertencia ética ===
print("=" * 60)
print("⚠️  ADVERTENCIA: Este programa es solo para fines educativos.")
print("El uso indebido de esta herramienta puede ser ilegal.")
print("OpenAI ni el autor se responsabilizan por usos maliciosos.")
print("=" * 60 + "\n")

# === Lista de BINs predefinidos ===
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

# === Funciones base ===

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_sum = sum(digits[-1::-2])
    even_sum = sum([d*2 if d*2 < 10 else d*2 - 9 for d in digits[-2::-2]])
    return (odd_sum + even_sum) % 10

def calculate_check_digit(card_number):
    checksum = luhn_checksum(int(card_number) * 10)
    return 0 if checksum == 0 else 10 - checksum

def detect_card_type(bin_number):
    if bin_number.startswith("4"):
        return "Visa"
    elif bin_number.startswith("5"):
        return "Mastercard"
    elif bin_number.startswith("3"):
        return "Amex"
    elif bin_number.startswith("6"):
        return "Discover"
    elif bin_number.startswith("35"):
        return "JCB"
    else:
        return "Desconocida"

def generate_expiry():
    month = str(random.randint(1, 12)).zfill(2)
    year = str(random.randint(26, 30))
    return f"{month}/{year}"

def generate_cvv(card_type):
    if card_type == "Amex":
        return str(random.randint(1000, 9999))
    else:
        return str(random.randint(100, 999))

def generate_card(bin_number, card_type):
    if card_type == "Amex":
        length = 15
    else:
        length = 16

    body_length = length - len(bin_number) - 1
    body = ''.join(str(random.randint(0, 9)) for _ in range(body_length))
    partial_number = bin_number + body
    check_digit = calculate_check_digit(partial_number)
    full_card = partial_number + str(check_digit)

    expiry = generate_expiry()
    cvv = generate_cvv(card_type)

    return {
        "tarjeta": full_card,
        "tipo": card_type,
        "vencimiento": expiry,
        "cvv": cvv
    }

# === Programa principal ===

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
        description = "Personalizado"
    elif 1 <= choice <= len(bins):
        bin_selected = list(bins.keys())[choice - 1]
        description = bins[bin_selected]
    else:
        print("Opción fuera de rango.")
        return

    card_type = detect_card_type(bin_selected)

    try:
        cantidad = int(input("¿Cuántas tarjetas deseas generar?: ").strip())
        if cantidad < 1 or cantidad > 100:
            raise ValueError
    except ValueError:
        print("Por favor ingresa una cantidad válida entre 1 y 100.")
        return

    print(f"\n🎴 Generando {cantidad} tarjeta(s) con BIN {bin_selected} ({description})...\n")

    for i in range(cantidad):
        data = generate_card(bin_selected, card_type)
        print(f"#{i+1}: {data['tarjeta']} | Tipo: {data['tipo']} | Vence: {data['vencimiento']} | CVV: {data['cvv']}")

if __name__ == "__main__":
    main()

