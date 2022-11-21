class StepCounter:
    def __init__(self, date):  # Konstruktor _private Variable
        self.__date = date
        self.__step = 0

    def incrementSteps(self):
        self.__step += 1

    def __str__(self):  # string Methode
        return "Am" + self.__date + "bin ich" + str(self.__step) + "Schritte gegangen."


newSc = StepCounter("16.10.2022")  # neues Objekt
for i in range(0, 222):
    newSc.incrementSteps()

print(newSc)  # Ausgabe
