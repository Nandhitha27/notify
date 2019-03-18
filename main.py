import requests
from win10toast import ToastNotifier

url="https://newsapi.org/v2/top-headlines?sources=bbc-news&sortBy=top&apikey=dd43ed381bb646dbadadfcf04cf95d15"


response = requests.get(url).json()
article =response["articles"]
results = []
link= []
for ar in article: 
        results.append(ar["title"]) 
        link.append(ar["url"])  
#for i in range(len(results)): 
          
        # printing all trending news 
    #print(i + 1, results[i], link[i])  
    #print(i + 1, link[i])  




url1="https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=dd43ed381bb646dbadadfcf04cf95d15"

response1 = requests.get(url).json()
article1 =response1["articles"]
results1 = []
link1= []
for ar in article1: 
        results1.append(ar["title"]) 
        link1.append(ar["url"])  
#for i in range(len(results1)): 
          
        # printing all trending news 
    #print(i + 1, results1[i], link1[i])  
    #print(i + 1, link[i])  




url2="https://newsapi.org/v2/top-headlines?sources=business-insider&apiKey=dd43ed381bb646dbadadfcf04cf95d15"

response2 = requests.get(url2).json()
article2 =response2["articles"]
results2 = []
link2= []
for ar in article2: 
        results2.append(ar["title"]) 
        link2.append(ar["url"])  
#for i in range(len(results2)): 
          
        # printing all trending news 
    #print(i + 1, results2[i], link2[i])  
    #print(i + 1, link[i])  

url3 = "https://newsapi.org/v2/top-headlines?sources=cnbc&apiKey=8263b1e62d844870b0477f0d12b96a95"

response3 = requests.get(url3).json()
article3 =response3["articles"]
results3 = []
link3 = []
for ar in article3: 
        results3.append(ar["title"]) 
        link3.append(ar["url"])  
#for i in range(len(results3)): 
          
        # printing all trending news 
    #print(i + 1, results3[i], link3[i])
    #print(i + 1, link[i])  



result0 = results + results1 + results2 + results3
link0 = link + link1 + link2 + link3
#for i in range(len(result0)): 
          
        # printing all trending news 
    #print(i + 1, result0[i], link0[i])  
    #print(i + 1, link[i]) 
keyword = ["Annual Report" , 
    "Arbitrage" , 
    "Averaging Down" ,
    "Bear Market" ,
    "Beta" ,
    "Blue Chip Stocks" ,
    "Bourse" ,
    "Bull Market" ,
    "Broker" ,
    "Bid" ,
    "Close" ,
    "Day Trading" ,
    "Dividend" ,
    "Exchange" ,
    "Execution" ,
    "Haircut" , 
    "High" , 
    "Index" ,
    "Initial Public Offering (IPO)" ,
    "Leverage" ,
    "Low" ,
    "Margin" ,
    "Moving Average" ,
    "Open" ,
    "Order" ,
    "Pink Sheet Stocks" ,
    "Portfolio" ,
    "Quote" ,
    "Rally" ,
    "Sector" ,
    "Share Market" , 
    "Short Selling" ,
    "Spread" ,
    "Stock Symbol" ,
    "Volatility" ,
    "Volume" ,
    "Yield" ,
    "Buy" ,
    "Sell" ,
    "Buy to cover" ,
    "Revenue" ,
    "Profit" ,
    "Loss" ,
    "Earnings per share" , 
    "EPS" ,
    "Price to Earnings ratio" , 
    "P/E ratio" ,
    "Resistance" ,
    "Support" ,
    "Breakout" ,
    "Breakdown" ,
    "Market Valuation" ,
    "Shares outstanding" ,
    "Float" ,
    "Restricted shares" ,
    "Unrestricted Shares" ,
    "Intraday" ,
    "Delivery" ,
    "Ask" ,
    "Bid-Ask spread" ,
    "Limit order" ,
    "Market order" ,
    "Market capitalization" ,
    "Trading volume" ,
    "Liquidity" ,
    "Going low" ,
    "Sensex" ,
    "share" ,
    "Short" ,
    "wars" ,
    "cabinet"
    ]

count=1

for i in range(len(result0)):
    for j in range(len(keyword)):
        if(keyword[j] in result0[i]):
            notifier = ToastNotifier()
        # printing all trending news
            notifier.show_toast(result0[i] , link0[i] , duration=10 , icon_path = "C:\\Users\\nanditha iyer\\Desktop\\notify.ico"  ) 
            #print(count, result0[i], link0[i])
            #count= count + 1 
    #print(i + 1, link[i])