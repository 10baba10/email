# email

As default, the code sends the email through gmail.
The code needs access to your gmail account to be able to send the password.
To benefit from this code you need to; from your gmail account generate an App Password.
Below will be instructions on how to do this (you can also watch tutorials or search on google).

In your Google Account settings, under "Security," find the "App passwords" section.
Choose "Select app" and select "Mail" from the dropdown.
Choose your device (you can select "Other (Custom name)" if you want).
Click "Generate."
A generated app password will be displayed. This is the password your Python bot will use to authenticate.


To send the email with another server, you will need to change the host and port in the python code.
If access is needed to your account through an App generated password - you can follow the instruction above (for gmail) as reference - if not successful, easy solution can be found with google.
