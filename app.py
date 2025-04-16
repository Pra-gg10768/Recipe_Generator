from flask import Flask, request, render_template
import openai

openai.api_key = 'sk-k3VGJ5hOH_frNzXZxePFyQBMYHihSZYZC-Z_WCJWmpT3BlbkFJvjJEILBK0WlRD1lkppU7rJDfms5xZ-aUrQHqEj2qoA'  # Replace with your OpenAI API key

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def generate_recipe():
    recipe = ""
    if request.method == "POST":
        ingredients = request.form["ingredients"]
        if ingredients:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful recipe assistant."},
                    {"role": "user", "content": f"Create a unique recipe using the following ingredients in pointwise manner: {ingredients}."}
                ],
                max_tokens=300
            )
            recipe = response.choices[0].message['content'].strip()
    return render_template("index.html", recipe=recipe)

if __name__ == "__main__":
    app.run(debug=True)
