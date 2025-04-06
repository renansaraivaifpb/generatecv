from flask import Flask, request, Response, render_template
from langchain_pipeline import process_resume

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/answer", methods=["POST"])
def answer():
    data = request.get_json()
    resume = data.get("message")

    result = process_resume(resume)



    final_output = f"""

    {resume}

---


### Curriculum Vitae Translated into English:

{result["English_Resume"]}

---

### Improved Resume:

{result["Resume_improved"]}

---

### Technical Skills:

{result["Resume_final"]}
"""

    def stream():
        for line in final_output.splitlines(keepends=True):
            yield line

    return Response(stream(), mimetype='text/plain')

if __name__ == "__main__":
    app.run(debug=True)
