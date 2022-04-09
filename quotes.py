import random as ran

quoteslist = ["You are loved.", "Call your mom.", "You are beautiful", "You can get through any problem.",
              "You are awesome.", "Yo mama you looking good asl today"]


def giveRandomQuote():
    num = ran.randrange(0, 5)
    print(quoteslist[num])


def main():
    giveRandomQuote()


if __name__ == "__main__":
    main()
