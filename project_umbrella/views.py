# project_umbrella/views/py

from django.http import HttpResponse

def public_home(request):
    """
    A simple view to display a welcome message on the public homepage.
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Project Umbrella</title>
        <style>
            body { font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background-color: #f4f4f9; }
            .container { text-align: center; padding: 40px; background-color: white; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }
            h1 { color: #333; }
            p { color: #555; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Project Umbrella!</h1>
            <p>Your containerized Django application is now running successfully.</p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)