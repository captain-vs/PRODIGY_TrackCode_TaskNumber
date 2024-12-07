from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    # Open the image
    image = Image.open(image_path)
    image_array = np.array(image, dtype=np.uint8)  # Ensure array is of type uint8

    # Apply encryption (modifying pixel values)
    encrypted_array = (image_array.astype(np.uint16) + key) % 256  # Convert to uint16 to avoid overflow, then back to uint8
    encrypted_array = encrypted_array.astype(np.uint8)

    # Save the encrypted image
    encrypted_image = Image.fromarray(encrypted_array)
    encrypted_image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    # Open the encrypted image
    image = Image.open(image_path)
    image_array = np.array(image, dtype=np.uint8)  # Ensure array is of type uint8

    # Apply decryption (reversing the modification)
    decrypted_array = (image_array.astype(np.uint16) - key) % 256  # Convert to uint16 to avoid underflow, then back to uint8
    decrypted_array = decrypted_array.astype(np.uint8)

    # Save the decrypted image
    decrypted_image = Image.fromarray(decrypted_array)
    decrypted_image.save(output_path)
    print(f"Decrypted image saved to {output_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Encrypt and decrypt images using pixel manipulation.')
    parser.add_argument('mode', choices=['encrypt', 'decrypt'], help='Mode: "encrypt" or "decrypt"')
    parser.add_argument('image_path', help='Path to the input image')
    parser.add_argument('output_path', help='Path to save the output image')
    parser.add_argument('key', type=int, help='Encryption/Decryption key')

    args = parser.parse_args()

    if args.mode == 'encrypt':
        encrypt_image(args.image_path, args.output_path, args.key)
    elif args.mode == 'decrypt':
        decrypt_image(args.image_path, args.output_path, args.key)

