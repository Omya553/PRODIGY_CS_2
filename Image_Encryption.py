from PIL import Image
import numpy as np
import random


def encrypt_image(image_path, output_path):
    
    img = Image.open(image_path)
    
    img_array = np.array(img)
    key = random.randint(1, 255)
    encrypted_array = (img_array + key) % 256
    
    encrypted_img = Image.fromarray(np.uint8(encrypted_array))
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")
    print(f"Your encryption key is: {key}")
    return key

def decrypt_image(encrypted_image_path, key, output_path):
   
    encrypted_img = Image.open(encrypted_image_path)
   
    encrypted_array = np.array(encrypted_img)
    
    
    decrypted_array = (encrypted_array - key) % 256
    
   
    decrypted_img = Image.fromarray(np.uint8(decrypted_array))
    
    
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")


def main():
    while True:
       
        choice = input("Do you want to (E)ncrypt or (D)ecrypt an image? Type 'E' or 'D' (or 'exit' to quit): ").lower()

        if choice == 'e':
           
            image_path = input("Enter the path of the image to encrypt: ")
            output_path = input("Enter the path to save the encrypted image: ")
            key = encrypt_image(image_path, output_path)
            print(f"Encryption complete! Keep this key safe to decrypt the image: {key}")
        
        elif choice == 'd':
            
            encrypted_image_path = input("Enter the path of the encrypted image: ")
            try:
                key = int(input("Enter the encryption key: "))
            except ValueError:
                print("Invalid key! Please enter a valid number.")
                continue
            output_path = input("Enter the path to save the decrypted image: ")
            decrypt_image(encrypted_image_path, key, output_path)
            print("Decryption complete!")
        
        elif choice == 'exit':
           
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option! Please choose 'E' for encryption, 'D' for decryption, or 'exit' to quit.")

if __name__ == "__main__":
    main()
