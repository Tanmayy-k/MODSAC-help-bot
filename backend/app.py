from flask import Flask, request, jsonify
from flask_cors import CORS
from knowledge_graph import load_knowledge_graph
import difflib

app = Flask(__name__)
CORS(app)

G = load_knowledge_graph('faq_data.csv')

@app.route("/ask", methods=["POST"])
def ask():
    user_query = request.json.get("query", "")
    questions = [n for n in G.nodes if G.nodes[n].get("type") == "question"]
    match = difflib.get_close_matches(user_query, questions, n=1, cutoff=0.4)
    if match:
        answer = list(G.successors(match[0]))[0]
        return jsonify({"answer": answer})
    else:
        return jsonify({"answer": "Sorry, I couldn’t find an answer."})

if __name__ == "_main_":
    app.run(debug=True)
    