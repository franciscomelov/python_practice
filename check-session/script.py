import requests

# Replace with your Netflix account credentials
email = 'faany4591@gmail.com'
password = 'melovalle'

# Send a request to the Netflix login page
print("sending request")
login_url = 'https://www.netflix.com/login'
session = requests.Session()
response = session.get(login_url)

# Check if you're already logged in
if 'Sign Out' in response.text:
    print('You are already logged in.')
else:
    # Log in to Netflix
    data = {'email': email, 'password': password}
    response = session.post(login_url, data=data)

    print("Response")
    print(response.text)

    # Check if login was successful
    if 'Sign Out' in response.text:
        print('Login successful.')
    else:
        print('Login failed.')
    
    # Log out of Netflix
    session.get('https://www.netflix.com/logout')
    print('Logged out.')
