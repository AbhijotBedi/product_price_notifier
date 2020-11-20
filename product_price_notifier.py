import bs4
import urllib.request
import smtplib
import time

price_track = []

def check_price():
    #adding url to the amazon product page of a laptop I have been wanting
    url = 'https://www.amazon.in/ASUS-Graphics-Windows-Fortress-FX566LI-HN028T/dp/B08CY63TY8/ref=sr_1_6?crid=50I58R7S4BY6&dchild=1&keywords=asus+a15&qid=1605636272&sprefix=asus+a%2Caps%2C343&sr=8-6'
    
    sauce = urllib.request.urlopen(url).read()
    soup = bs4.BeautifulSoup(sauce, "html.parser")
    
    prices = soup.find(id="priceblock_ourprice").get_text()
    prices = float(prices.replace(",", "").replace("₹", ""))
    price_track.append(prices)
    return prices
    
def send_email(message): 
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login( sender_email , password ) #add the email and password within ".."
    s.sendmail( sender_email , receiver_email, message)
    s.quit()
    
def price_decrease_check(price_track):
    if price_track[-1] < price_track[-2]:
        return True
    else:
        return False
    
count = 1
    
while True:
    current_price = check_price()
    if count > 1:
        flag = price_decrease_check(price_track)
        if flag:
            decrease = price_track[-1] - price_track[-2]
            message = "Your laptop is now {decrease} cheaper."
            send_email(message)
    time.sleep(43000)
    count += 1