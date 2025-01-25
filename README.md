<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calorie Tracker - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f9;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background: white;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        h1, h2, h3 {
            color: #333;
        }
        h1 {
            text-align: center;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        ul li {
            margin: 5px 0;
            padding-left: 1.5rem;
            position: relative;
        }
        ul li:before {
            content: '🔥';
            position: absolute;
            left: 0;
        }
        code {
            background: #eef;
            padding: 2px 4px;
            border-radius: 4px;
            font-size: 0.95rem;
        }
        a {
            color: #007BFF;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🍎 Calorie Tracker</h1>
        <p>A powerful and intuitive web application to help you log meals, calculate calories, and monitor your nutritional goals. 🥗💪</p>

        <h2>✨ Features</h2>
        <ul>
            <li><b>User Authentication</b>: Secure login and logout functionality 🔐</li>
            <li><b>Food Logging</b>: Add food items with details like carbs, proteins, fats, and calories 🥘</li>
            <li><b>Calorie Calculations</b>: Automatic computation of nutritional values 📊</li>
            <li><b>Progress Tracking</b>: Visualize your daily calorie intake with charts 📈</li>
            <li><b>Responsive Design</b>: Clean and user-friendly interface 🌟</li>
        </ul>

        <h2>🎯 Business Requirements</h2>
        <ul>
            <li><b>Core Purpose:</b> Enable users to monitor daily calorie intake and maintain a healthy diet 🥗</li>
            <li><b>Primary Features:</b> User authentication, meal logging, calorie calculations, and progress tracking</li>
            <li><b>Technology Stack:</b> Django (Python), SQLite, HTML, CSS, Bootstrap</li>
            <li><b>Deployment:</b> Designed for cloud platforms like Render or Heroku 🌐</li>
        </ul>

        <h2>📂 Project Structure</h2>
        <pre>
calorietracker/
├── manage.py                # Django's entry point
├── mysite/                  # Django project folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── myapp/                   # Main app folder
│   ├── models.py
│   ├── views.py
│   ├── templates/
├── requirements.txt         # Python dependencies
├── Procfile                 # For deployment
        </pre>

        <h2>🚀 Setup Instructions</h2>
        <ol>
            <li>Clone the repository:
                <pre><code>git clone https://github.com/your-repo/calorie-tracker.git</code></pre>
            </li>
            <li>Navigate to the project folder:
                <pre><code>cd calorie-tracker</code></pre>
            </li>
            <li>Create and activate a virtual environment:
                <pre>
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
.\venv\Scripts\activate
                </pre>
            </li>
            <li>Install dependencies:
                <pre><code>pip install -r requirements.txt</code></pre>
            </li>
            <li>Run migrations:
                <pre><code>python manage.py migrate</code></pre>
            </li>
            <li>Start the development server:
                <pre><code>python manage.py runserver</code></pre>
            </li>
            <li>Visit <a href="http://127.0.0.1:8000/" target="_blank">http://127.0.0.1:8000/</a> in your browser 🌐</li>
        </ol>

        <h2>📊 Limitations</h2>
        <ul>
            <li>Uses SQLite, which is suitable for development but not production.</li>
            <li>Deployment challenges encountered on Render (optional note).</li>
        </ul>

        <h2>🎨 Future Improvements</h2>
        <ul>
            <li>Add a feature to set daily calorie goals 🎯</li>
            <li>Integrate third-party APIs for nutritional data 🛠️</li>
            <li>Enhance deployment setup for easier hosting 🚀</li>
        </ul>

        <p style="text-align: center;">Made with ❤️ by Mohammed Zakeer</p>
    </div>
</body>
</html>
