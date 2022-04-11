# Pre-made quotes list and function that returns a random quote
import random as ran


class Quotes:
    def __init__(self):
        self.quoteslist = ["You are loved.", "Call your mom.", "You are beautiful", "You can get through any problem.",
                           "You are awesome.", "Yo mama, you looking good asl today",
                           "If it makes you feel better, Thaddeaus is "
                           "uglier than you."]

    def giveRandomQuote(self):
        num = ran.randrange(0, len(self.quoteslist))
        quote = self.quoteslist[num]
        return quote

    def addQuote(self, quote):
        self.quoteslist.append(quote)
        print("Quote successfully added.")

    def listQuotes(self):
        num = 0
        for i in self.quoteslist:
            print(str(num) + ". " + i)
            num += 1
        print()

    def giveQuoteTot(self):
        return len(self.quoteslist)

    def delQuote(self, index):
        if index > len(self.quoteslist):
            print("Error. Index larger than quote list size.")
        else:
            del self.quoteslist[index]
            print("Successfully deleted quote.")
