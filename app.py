from flask import Flask, render_template_string

app = Flask(__name__)

HTML_CONTENT = """
<!DOCTYPE html>
<html>
<head>
    <title>K8s Status Page</title>
    <style>
        body { font-family: sans-serif; background: #eceff1; display: flex; justify-content: center; padding-top: 50px; }
        .container { background: white; padding: 40px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; margin: 0; }
        p { color: #7f8c8d; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Pipeline Status: Online</h1>
        <p>Integrated with Jenkins & Kubernetes</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_CONTENT)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8090)
