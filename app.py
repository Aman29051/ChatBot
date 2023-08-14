from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

chat_history = []
def chatbot_response(user_input):
    response = user_input
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["user_input"]
        bot_response = chatbot_response(user_input)

        chat_history.append(("You", user_input))
        chat_history.append(("Bot", bot_response))

        return render_template("index.html", chat_history=chat_history)

    if request.args.get("clear_chat") == "true":
        chat_history.clear()
        return redirect(url_for("index"))

    return render_template("index.html", chat_history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
