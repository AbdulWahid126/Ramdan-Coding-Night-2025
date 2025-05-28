from fastapi import FastAPI
import random

app = FastAPI()

# we will build teo simple get endpoints
# 1) side-hustles
# 2) money-quotes

side_hustles = [
    "Freelancing - Start offering your skills online!",
    "Dropshiping - Sell without handleing inventory!",
    "Stock Market - Invest and watch your money grow!",
    "Affiliate Marketing - Earn by promoting product!",
    "Crypto Trading - Buy and sell digital assets!",
    "Online Courses - Share your knowledge and earn!",
    "Print-on-Demand - Coll cuctom-designed Products!",
    "Blogging - Create content and earn through ads and sponsorships!",
    "Youtube Chennel - Monetize vedios throgh ads and sponsorships!",
    "Social Media Management - Mange account from brands and influencers!",
    "App Development - Create mobile or web application for buinesses!"
]

money_quotes = [
    "Too many people spend money they haven't earned, to buy things they don't want, to impress people they don't like. — Will Rogers",
    "An investment in knowledge pays the best interest. — Benjamin Franklin",
    "Do not save what is left after spending, but spend what is left after saving. — Warren Buffett",
    "Money is a terrible master but an excellent servant. — P.T. Barnum",
    "Formal education will make you a living; self-education will make you a fortune. — Jim Rohn",
    "Time is more valuable than money. You can get more money, but you cannot get more time. — Jim Rohn",
    "The stock market is filled with individuals who know the price of everything, but the value of nothing. — Philip Fisher",
    "The lack of money is the root of all evil. — Mark Twain",
    "It’s not your salary that makes you rich, it’s your spending habits. — Charles A. Jaffe",
    "Money often costs too much. — Ralph Waldo Emerson"
]

@app.get("/side_hustles")
def get_side_hustles():
    """Return a random side hustles idea"""
    return {"side_hustles": random.choice(side_hustles)}

@app.get("/money_quotes")
def get_money_quotes():
    """Return a random maoney quotes"""
    return {"money_quotes": random.choice(money_quotes)}



# Build by ABDULWAHID