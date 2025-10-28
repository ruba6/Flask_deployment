import os
from flask import Flask, render_template, request, url_for, redirect ,send_file, send_from_directory,abort
from email.mime.text import MIMEText 
import smtplib 
from email.message import EmailMessage 

app=Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html', title="rubadarshini_portfolio_home")

@app.route('/download_cv')
def download_cv():
    try:
        directory = os.path.join(app.root_path, 'static', 'resume')
        filename = 'L RUBADARSHINI_Resume_2025_Dev.pdf'
        return send_from_directory(directory, filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)

@app.route('/')
def home():
    return render_template('index.html', title="Portfolio")


@app.route('/about')
def about():
    return render_template('about.html', title="About")



if __name__ == "__main__":
    app.run(debug=True)

