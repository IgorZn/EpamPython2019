class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f'{self.name} got message:\t {message}')


class Publisher:
    def __init__(self):
        self.subscribers = set()

    def register(self, who):
        self.subscribers.add(who)

    def unregister(self, who):
        self.subscribers.discard(who)

    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


pub = Publisher()

bob = Subscriber('Bob')
alice = Subscriber('Alice')
john = Subscriber('John')

pub.register(bob)
pub.register(alice)
pub.register(john)

pub.dispatch("It's lunchtime!")
pub.unregister(john)
pub.dispatch('Time for dinner!')

# John got message:	 It's lunchtime!
# Bob got message:	 It's lunchtime!
# Alice got message:	 It's lunchtime!
# Bob got message:	 Time for dinner!
# Alice got message:	 Time for dinner!