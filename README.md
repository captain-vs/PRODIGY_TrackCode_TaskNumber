#  Q1) Caesar Cipher

### Description
The Caesar Cipher script encrypts and decrypts text using the Caesar Cipher technique. It shifts each letter in the text by a specified number of positions in the alphabet.

### Usage
To encrypt a message:
python caesar_cipher.py encrypt "Your Message Here" 3

To decrypt a message:
python caesar_cipher.py decrypt "Encrypted Message Here" 3

Error Handling
Ensure the shift value is an integer.
Handle non-alphabetical characters appropriately.

# Q2) Keylogger
Description
The keylogger script records and logs keystrokes. It logs the keys pressed and saves them to a file named keylog.txt.

Usage
To run the keylogger:
python keylogger.py

Error Handling
Ensure the script has permission to write to keylog.txt.

Handle exceptions to avoid crashes.

# Q3) Network Packet Analyzer
Description
The network packet analyzer captures and analyzes network packets. It displays relevant information such as source and destination IP addresses, protocols, and payload data.

Usage
To run the packet analyzer:
python network_packet_analyzer.py

Error Handling
Ensure Npcap is installed on Windows.
Handle exceptions related to network permissions and packet capturing.

# Q4) Password Complexity Checker
Description
The password complexity checker assesses the strength of a password based on criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. It provides feedback on the password's strength.

Usage
To check password complexity:
python password_complexity_checker.py

Error Handling
Ensure the script handles different password inputs gracefully.
Provide detailed feedback for missing criteria.

# Q5) Pixel Manipulation for Image Encryption
Description
The pixel manipulation script encrypts and decrypts images by manipulating pixel values. It shifts the pixel values based on a specified key.

Usage
To encrypt an image:
python pixel_manipulation.py encrypt input_image.png encrypted_image.png 42

To decrypt an image:
python pixel_manipulation.py decrypt encrypted_image.png decrypted_image.png 42

Error Handling
Ensure the image file exists and the path is correct.
Handle exceptions related to image processing and file operations.
