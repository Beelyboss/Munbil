# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from mail_handler import configure_mail, send_verification_email
from verification_codes import generate_verification_code, store_verification_code, get_verification_code, remove_verification_code

app = Flask(__name__)
CORS(app)
configure_mail(app)

if __name__ == '__main__':
    app.run(debug=True)