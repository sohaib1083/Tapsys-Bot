from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_merchant(phone):
    conn = sqlite3.connect('tapsys.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM merchants WHERE phone = ?", (phone,))
    merchant = cursor.fetchone()
    conn.close()
    return merchant

@app.route('/lookup', methods=['GET'])
def lookup():
    phone = request.args.get('phone')
    merchant = get_merchant(phone)
    if merchant:
        return jsonify({"id": merchant[0], "salutation": merchant[2], "name": merchant[3], "gender": merchant[4]})
    return jsonify({"error": "Merchant not found"}), 404

if __name__ == "__main__":
    app.run(port=5000)
