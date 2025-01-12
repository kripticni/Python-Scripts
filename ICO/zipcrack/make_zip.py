import zipfile
import os

print(os.getcwd())
with zipfile.ZipFile('protected.zip', 'w') as zipf:
    zipf.setpassword(b'gateway')  # Set the password
    zipf.write("zipcrack.py")

