from flask import Flask, jsonify, request
import unicodedata
import re
import random


app = Flask(__name__)


def treatment(text):
    text = unicodedata.normalize("NFD", text)
    text = "".join(i for i in text if unicodedata.category(i) != "Mn")
    return text.lower()


def has_word(word, text):
    return re.search(rf"\b{re.escape(word)}\b", text)


def json_construction(text, success=True, status=200):
    return jsonify({"success": success, "menssage": text}), status


@app.route('/')
def main():
    return ""


@app.route('/menssage')
def menssage():

    msg = request.args.get("msg", type=str)

    if not msg or not msg.strip():
        return json_construction(
            "ERROR - PARAMETER ?msg= IS NOT FOUND OR MENSSAGE NOT EXIST",
            success=False,
            status=400
        )

    msg_treated = treatment(msg)

    if has_word("pensao", msg_treated):
        return json_construction("Silencio Profundo")

    if has_word("pix", msg_treated):
        pix_amount = random.randint(25, 40)
        return json_construction(f"{pix_amount} reais ta bom?")

    return json_construction("Joia")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
