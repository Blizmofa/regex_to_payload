import rstr
import random
import string

patterns = [
    r"[A-Za-z]{5}\d{2}",      # Five letters followed by two digits
    r"\w{3}-\d{4}",           # Three word characters, a dash, and four digits
    r"[A-Z]{3}\d[A-Z]\d{2}",  # Three uppercase letters, one digit, one uppercase letter, and two digits
    r"\d{3}-[A-Za-z]{2}",     # Three digits, a dash, and two letters (upper or lower case)
    r"\+1-\(\d{3}\)-\d{3}-\d{4}",  # US phone number format with country code
    r"-?\d{1,3}\.\d{1,6},\s?-?\d{1,3}\.\d{1,6}", # Map Coordinates
    r"https?://(www\.)?[a-zA-Z0-9\-]+\.[a-z]{2,}(/[a-zA-Z0-9\-]*)?" # URL
]


# Function to add random noise around a generated pattern
def add_noise(text, noise_length=5):
    noise_prefix = ''.join(random.choices(string.ascii_letters + string.digits, k=noise_length))
    noise_suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=noise_length))
    return f"{noise_prefix} {text} {noise_suffix}"

# Generate and print random strings for each pattern with added noise
for pattern in patterns:
    print(f"Pattern: {pattern}")
    for _ in range(3):  # Generate three examples for each pattern
        # Generate the string based on the regex pattern
        generated_string = rstr.xeger(pattern)
        # Add noise around the generated string
        noisy_string = add_noise(generated_string)
        print("  ", noisy_string)
    print()