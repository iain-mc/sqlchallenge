# Challenge Overview/Objective
The objective of this challenge is to build a website which can be used to A) demonstrate an SQL injection attack, B) demonstrate SQL injection attack mitigation techniques (for example, toggle on/off parameterised queries). Imagine the website being used as an educational tool.

The site can be developed using whatever technologies you wish. 

In this repository there is an example site which is vulnerable to SQL injection attacks. It is very basic and does not include any mitigation techniques. Free free to extend this website or create your own. 

# Additional Goals
Can you extend your site to include demonstrations of other common vulnerabilities:

* XSS (Cross Site Scripting)
* CSRF (Cross Site Request Forgery)
* etc.

# Example Site
Clone this repository:

`git clone http://github.com/iain-mc/sqlchallenge`

`cd sqlchallenge`

Install SQLite:

`sudo apt-get install sqlite3`

If you have Python Flask already installed, just run the script:

`python example.py`

If you do not have Python Flask installed, either install it using your preferred method or do the following: 

Install Python Virtualenv:

`sudo apt-get install python virtual-env`

Create and and enter the virutalenv:

`virtualenv venv`

`. venv/bin/activate`

Install Python Flask:

`pip install Flask`

Run the script:

`python example.py`

