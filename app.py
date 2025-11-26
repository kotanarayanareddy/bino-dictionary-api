from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

EXTERNAL_API = "https://api.dictionaryapi.dev/api/v2/entries/en/"

@app.route("/")
def home():
    return {"message": "Bino Dictionary API is running"}

@app.route("/search", methods=["GET"])
def search_word():
    word = request.args.get("word")
    if not word:
        return jsonify({"error": "Word parameter is required"}), 400

    response = requests.get(EXTERNAL_API + word)

    if response.status_code != 200:
        return jsonify({"error": "Word not found"}), 404

    data = response.json()[0]  # Take only the first result
    result = {
        "word": data.get("word"),
        "partOfSpeech": data["meanings"][0]["partOfSpeech"] if data.get("meanings") else "",
        "definition": data["meanings"][0]["definitions"][0]["definition"] if data.get("meanings") else "",
        "phonetic": data.get("phonetic", ""),
        "source": data.get("sourceUrls")[0] if data.get("sourceUrls") else ""
    }
    return jsonify(result)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

