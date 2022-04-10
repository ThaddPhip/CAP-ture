# Pre-made quotes list and function that returns a random quote
import random as ran

quoteslist = ["You are loved.", "Call your mom.", "You are beautiful", "You can get through any problem.",
              "You are awesome.", "Yo mama, you looking good asl today", "If it makes you feel better, Thaddeaus is "
                                                                         "uglier than you."]


def giveRandomQuote():
    num = ran.randrange(0, len(quoteslist))
    print(quoteslist[num])
