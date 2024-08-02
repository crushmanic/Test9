import secrets

def generate_csrf_token():    
# Generate a random URL-safe text string
    csrf_token = secrets.token_urlsafe(32)   
    return csrf_token
# Generate and print a CSRF token
csrf_token = generate_csrf_token()
print(csrf_token)
