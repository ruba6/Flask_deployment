import os
from flask import Flask, render_template, request, url_for, redirect ,send_file, send_from_directory,abort
from email.mime.text import MIMEText 
import smtplib 
from email.message import EmailMessage 

app=Flask(__name__,template_folder='templates')

@app.route("/") 
def index(): 
   return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/project')
def project():
    return render_template("project.html") 

@app.route('/contact')
def contact():
   return render_template("contact.html")

@app.route('/sendemail', methods=['POST'])
def send_email():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form.get('name')
        subject = request.form.get('subject')
        email = request.form.get('email')
        message = request.form.get('message')

        your_email = "rubaloganathan6@gmail.com"
        your_password = "2002-07-18"

        msg = EmailMessage()
        msg.set_content(f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}")
        msg['Subject'] = subject
        msg['From'] = your_email
        msg['To'] = your_email

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(your_email,your_password)
                server.send_message(msg)
                print("Email sent!")
        except Exception as e:
            print(f"Failed to send email: {e}")

        return redirect(url_for('thank_you'))

    # Handle case where method is not POST (optional)
    return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return "Thank you! Your message has been sent."


@app.route('/download_cv')
def download_cv():
    try:
        # Define the directory where your CV is stored
        directory = "static folder"
        filename = "LResume.pdf"
        
        # Send the file from the specified directory
        return send_from_directory(directory, filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)

#if __name__ == "__main__":
 #   app.run(debug=True)