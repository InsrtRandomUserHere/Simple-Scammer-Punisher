import requests
import threading

# functions.py    Uncomment to use fake email and password generator
#import functions

iterations = 0  # To keep track of how many we've sent
thread_amt = 1  # How many threads to use


def send_post():
    url = "https://linkhere.com/"  # Scammer's request url
    
    global iterations
    while True:
        iterations += 1
        payload_data = {} 
        
        """
        Template for email and password only parameters
        
        email = functions.create_fake_email()
        password = functions.create_password()
        payload_data = {
            "email": email,
            "password": password
        }
        """
        
        # Send data
        requests.post(url=url, data=payload_data)
        
        #  To print out what you have sent. Example below is for email and password only
        #print(f"{iterations} - Email: {email} Password: {password}")


if __name__ == "__main__":
    # Setting threads
    threads = []
    for i in range(thread_amt):
        t = threading.Thread(target=send_post)
        t.daemon = True
        threads.append(t)

    # Starting threads
    for i in range(thread_amt):
        threads[i].start()

    for i in range(thread_amt):
        threads[i].join()
