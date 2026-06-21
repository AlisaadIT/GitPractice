import random
import string

def generate_strong_password(length=16):
   
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password


if __name__ == "__main__":
    print("--- أداة توليد كلمات المرور المعقدة ---")
    secure_pass = generate_strong_password(16)
    print(f"تم توليد الرمز بنجاح: {secure_pass}")