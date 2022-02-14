# trip.py contains the class and the behaviors of a trip
class Trip:
    def __init__(self, title, budget=0):
        self.title = title
        self.budget = budget
        self.destinations = list()

    def addDestination(self, place):
        self.destinations.append(place)

    def printDestinations(self):
        print(self.destinations)

    def __repr__(self):
        return'[Trip:%s, %s]' % (self.title, self.budget)


class BussinessTrip(Trip):
    def __init__(self, title, budget, company):
        Trip.__init__(self, title, budget)
        self.company = company

    def getCompany(self):
        company = input('Enter Company Name: ')
        print(company)
        self.company = company

    def __repr__(self):
        if self.company != None:

            return'[Trip:%s, %s, %s]' % (self.title, self.budget, self.company)
        else:
            return Trip.__repr__(self)


class MonthlyTrips:
    def __init__(self, *args):
        self.members = list(args)

    def addMembers(self, trip):
        self.memebers.append(trip)

    def showAll(self):
        for trip in self.members:
            print(trip)


if __name__ == '__main__':
    # self-test code

    thai = Trip('Thailand', 10000)
    rio = Trip('Rio de Janeiro')
    print(rio.title, rio.budget)
    print(thai.title, thai.budget)
    rio.destinations.append("Lapa")
    rio.addDestination("Barra")
    print(rio.destinations)
    print(rio)
    thai.printDestinations()
    print(thai)
    paris = BussinessTrip('Paris', 5000, 'GM')
    turkey = BussinessTrip('Turkey', 400, 'MS')
    paris.getCompany()
    print(paris)
    print('--- All ---')
    # for obj in (paris, thai, rio, turkey):
    #     print(obj)

    peru = Trip("Peru")
    london = Trip("London", 300)

    january = MonthlyTrips(rio, thai, turkey)
    february = MonthlyTrips(paris, peru, london)

    january.showAll()
    february.showAll()
