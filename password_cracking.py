import math
import time

def calculate_bruteforce_time():
    # Password complexity math
    charset_size = 0
    has_upper = True
    has_lower = True
    has_digits = True
    has_symbols = False
    
    # Arithmetic to calculate total combinations
    if has_lower:
        charset_size += 26
    if has_upper:
        charset_size += 26
    if has_digits:
        charset_size += 10
    if has_symbols:
        charset_size += 32
    
    password_length = 8
    total_combinations = charset_size ** password_length  # Exponentiation!
    
    # Cracking speed (hashes/second)
    cracks_per_second = 100_000_000_000  # 100 billion/sec (modern GPU cluster)
    
    seconds_to_crack = total_combinations / cracks_per_second
    years_to_crack = seconds_to_crack / (365 * 24 * 3600)
    
    print(f"Total combinations: {total_combinations:,}")
    print(f"Time to crack: {years_to_crack:.2f} years")
    
    return years_to_crack

calculate_bruteforce_time()
