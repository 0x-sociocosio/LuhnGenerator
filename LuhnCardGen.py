import random

def luhn_checksum(card_number):
    """Calcula el dígito verificador de Luhn para un número sin el último dígito"""
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
    checksum = luhn_checksum(int(card_number) * 10)  # Append a 0 to calculate
    return 0 if checksum == 0 else 10 - checksum

def generate_card(bin_number):
    # Validar longitud del BIN
    if len(bin_number) not in [4, 6]:
        raise ValueError("El BIN debe tener 4 o 6 dígitos")
    
    # Completar el número con dígitos aleatorios hasta tener 15 dígitos
    length_to_generate = 15 - len(bin_number)
    card_number = bin_number + ''.join(str(random.randint(0, 9)) for _ in range(length_to_generate))
    
    # Calcular dígito verificador
    check_digit = calculate_check_digit(card_number)
    
    # Tarjeta completa
    full_card = card_number + str(check_digit)
    return full_card

def main():
    bin_number = input("Ingrese el BIN (4 o 6 dígitos): ").strip()
    
    if not bin_number.isdigit() or len(bin_number) not in [4, 6]:
        print("Error: El BIN debe contener solo números y tener 4 o 6 dígitos.")
        return
    
    card = generate_card(bin_number)
    print(f"Tarjeta generada válida según Luhn: {card}")

if __name__ == "__main__":
    main()

