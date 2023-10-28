```python
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "admin": generate_password_hash("admin_password"),
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

def generate_key():
    key = Fernet.generate_key()
    return key

def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

@app.route('/encrypt', methods=['POST'])
@auth.login_required
def encrypt_data():
    data = request.get_json()
    key = generate_key()
    encrypted_data = encrypt_message(data['message'], key)
    return jsonify({'key': key.decode(), 'encrypted_data': encrypted_data.decode()}), 200

@app.route('/decrypt', methods=['POST'])
@auth.login_required
def decrypt_data():
    data = request.get_json()
    decrypted_data = decrypt_message(data['encrypted_data'].encode(), data['key'].encode())
    return jsonify({'decrypted_data': decrypted_data}), 200

if __name__ == '__main__':
    app.run(debug=True)
```