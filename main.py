STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests
import datetime
import smtplib



STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


if datetime.datetime.now().weekday() == 6:
    todays_date = datetime.date.today() - datetime.timedelta(days=1)
else:
    todays_date = datetime.date.today()

news_heading=[]
my_email = "vishalXXXX"
to_mail = "vishalXXXX"
password = "XXXX"

stock_parameters = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":"XXXX"
}

news_parameters={
    "q":STOCK_NAME,
    "from":todays_date,
    "sortBy":"popularity&",
    "apiKey": "XXXXX"
}
print(todays_date)

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
data = stock_response.json()["Time Series (Daily)"]
yesterday_date = str(todays_date - datetime.timedelta(days = 1))

yesterday_closing_price = float(data[yesterday_date]["4. close"])

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_date = str(todays_date - datetime.timedelta(days = 2))
day_before_yesterday_closing_price = float(data[day_before_yesterday_date]["4. close"])


#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference_price = yesterday_closing_price - day_before_yesterday_closing_price


#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percentage_difference = (difference_price/yesterday_closing_price)*100


#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

news_response = requests.get("https://newsapi.org/v2/everything", params=news_parameters)
news_data = (news_response.json()["articles"])[:3]
news_heading = [news_data[news]['title'] for news in range(3)]


    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    with smtplib.SMTP("XXX") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_mail,
            msg=f"Subject:Tesla Share Price \n\n{msg.encode('utf-8')}\n{news_heading[0].encode('utf-8')}\n{news_heading[2].encode('utf-8')}",
        )

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 
    if difference_price < 0:
        msg = (f"TSLA: 🔻 {abs(percentage_difference)}%")
    else:
        msg = (f"TSLA: 🔺 {abs(percentage_difference)}%")
    print(msg)
    print(news_heading[0])
    print(news_heading[1])
    print(news_heading[2])


#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

