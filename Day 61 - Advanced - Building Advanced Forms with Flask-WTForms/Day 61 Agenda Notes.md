Day 61 Goals: Building Advanced Forms

Yesterday we saw how we could make HTML forms work with our Flask server and get hold of the data that a user enters into the form. Today, we're going to improve on that, we're going to build forms using a Flask extension called Flask-WTF. It has a number of benefits over the simple HTML Form. e.g.

Easy Form Validation - Makes sure the user is entering data in the required format in all the required fields. e.g. checking that the user's email entry has a "@" and a "." at the end. All without having to write your own validation code.

Less Code - If you have a number of forms in your website, using WTForm can dramatically reduce the amount of code you have to write (or copy & paste).

Built in CSRF Protection - CSRF stands for Cross Site Request Forgery, it's an attack that can be made on website forms which forces your users to do unintended actions (e.g. transfer money to a stranger) or compromise your website's security if it's an admin.

Flask developers will usually choose Flask-WTF to create forms in their websites. However, in the wild, you might also see projects that are built with HTML Forms. So it's important to understand how both of them work.

Secrets

By the end of today, we will build a website that holds some secrets. Only with the right username and password can you access the page with our secrets.

