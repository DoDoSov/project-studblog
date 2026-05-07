from src import create_app

# Create the application instance
app = create_app()

if __name__ == "__main__":
    # This part only runs if you do 'python wsgi.py' manually
    app.run(port=5000)