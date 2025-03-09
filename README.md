<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Setup Instructions</title>
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f8f9fa;
            color: #333;
            margin: 40px;
            padding: 20px;
        }
        .container {
            max-width: 700px;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        h2 {
            color: #007bff;
        }
        code {
            background: #f4f4f4;
            padding: 5px 10px;
            border-radius: 5px;
            font-family: monospace;
            display: inline-block;
        }
        .code-block {
            background: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            font-family: monospace;
            display: block;
            overflow-x: auto;
        }
        a {
            color: #007bff;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

    <div class="container">
        <h2>Setup Instructions</h2>
        <p>To get started, first obtain an <strong>API_KEY</strong> from <a href="https://console.groq.com/keys" target="_blank">Groq API Keys</a>.</p>
        
        <p>Then, update your <code>.env</code> file with the API key:</p>
        <pre class="code-block">GROQ_API_KEY=your_api_key_here</pre>

        <h3>Step 1: Install Dependencies</h3>
        <p>Run the following command to install required dependencies:</p>
        <pre class="code-block">pip install -r requirements.txt</pre>

        <h3>Step 2: Run the Streamlit App</h3>
        <p>Use the command below to start your Streamlit application:</p>
        <pre class="code-block">streamlit run main.py</pre>
    </div>

</body>
</html>
