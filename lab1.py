import requests  # εισαγωγή της βιβλιοθήκης

def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break

url = input("Give url:\t") # προσδιορισμός του url
print(url)

#with requests.get(url) as response:  # το αντικείμενο response
    #html = response.text
    #more(html)

if not url.startswith('https://'):
    url = 'https://' + url

 
with requests.get(url) as response:
    for key in response.headers:
        print(f"{key}, []{response.headers[key]}")

    print(f"Server: {response.headers.get('Server')}")

    print(f"Has cookies: {'Set-Cookie' in response.headers}")

    for cookie in response.cookies:
        print(f"Name: {cookie.name}, Expires:{datetime}")