class Observable:
    def __init__(self):
        self.observers = []

    def register(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def unregister_all(self):
        if self.observers:
            del self.observers[:]

    def update_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)


class Observer:
    def update(self, *args, **kwargs):
        pass


class AmericanStockMarket(Observer):
    def update(self, *args, **kwargs):
        print("American stock market received: {0}\n{1}".format(args, kwargs))


class EuropeanStockMarket(Observer):
    def update(self, *args, **kwargs):
        print("European stock market received: {0}\n{1}".format(args, kwargs))


# >>> from observer import observable, Americanstockmarket, Europeanstockmarket
# >>> really_big_company = observable()
# >>> american_observer = Americanstockmarket()
# >>> really_big_company.register(american_observer)
# >>> european_observer = Europeanstockmarket()
# >>> really_big_company.register(european_observer)
# >>> really_big_company.update_observers('important_update, msg='CEO unexpectedly resigns')
# American stock market received: ('important_update',) cmsg': 'CEO unexpectedly resigns'}
# European stock market received: ('important_update',) rmsg': 'CEO unexpectedly resigns'}