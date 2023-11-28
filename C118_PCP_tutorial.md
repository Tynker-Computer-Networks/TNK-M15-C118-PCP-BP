Send Secret Santas emails.
=====================================


In this activity, you will set up the SMTP server to send secret Santa assignments with the wishlist.




<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10946319/118_proj_op.gif" width = "480" height = "320">




Follow the given steps to complete this activity:
1. Send Secret Santas emails.


* Open the file `app.py`.


* Setup and connect with SMTP server .


    ```sh
    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    ```
* Start TLS server to securely send the emails.

    ```sh
    smtp_server.starttls()
    ```


* Login by passing email and password in `login()` function of SMTP server.


    ```
    smtp_server.login(sender_email, password)
    ```


* Write a friendly letter with the Secret Santa assignment and wishlist in a Subject and msg_body variables respectively.
    ```sh
    subject = "Your Secret Santa Assignment"
    msg_body = f"Hello {recipient_name},\n\nYour Secret Santa assignment is: {assigned_to}\n\nWishlist: {wishlist}"


    ```


* Receive the emails in template format.
	```sh
    message = MIMEMultipart()
    ```


* Write down the sender's and recipient's addresses on the magical envelope.
	```sh
    message["From"] = sender_email
    message["To"] = recipient_email
    ```


       
*  Make the letter as an attachment by defining the format.
	```sh
    message.attach(MIMEText(msg_body, "plain"))
    ```
   
* Send the Email to each Santa's Mailbox.
	```sh
    smtp_server.sendmail(sender_email, recipient_email, message.as_string())
	```




* Close and lock the magical mailbox after sending the wishes..
	```sh
    smtp_server.quit()
	```




* Print the text message as `“Email sent successfully.”`.
	```sh
    print("Email Sent", "Email sent successfully!")
	```


* Save and run the code to check the output.





