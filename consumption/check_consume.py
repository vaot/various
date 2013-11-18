from pyparsing import Word, alphas
import json


class Helper(object):

      @classmethod
      def read_json(self, filename):
          json_file = file(filename, "r")
          json_data = json.load(json_file)
          json_file.close()
          return json_data

class Getter(object):

      @staticmethod
      def options():
          return Helper.read_json("options.json")

      def cars(self, name):
          return self.options()["cars"][name.lower()]

      def cities(self, name):
          return self.options()["cities"][name.lower()]

      def forecast(self, name):
          return self.options()["forecast"][name.lower()]

      def conditions(self, name):
          return self.options()["conditions"][name.lower()]

      def passengers(self):
          return self.options()["passengers"]

      def stops(self):
          return self.options()["stops"]

      def traffic_lights(self):
          return self.options()["traffic_lights"]

class ConsuptionCalculator(Helper, Getter):

      def __init__(self, config_file):
          config_file = super(ConsuptionCalculator, self).read_json(config_file)

          self.car = Getter.cars(self, config_file["Car"] )
          self.weather = Getter.forecast(self, config_file["Forecast"] )
          self.passengers = Getter.passengers(self) * config_file["Passengers"]
          self.stops = Getter.stops(self) * config_file["Stops"]
          self.city = Getter.cities(self, config_file["City"] )
          self.traffic_lights = Getter.traffic_lights(self) * config_file["Traffic Lights"]

# ============================
# ******* HOW THIS WORKS *********
# First, we need to consider that consumption of gas mileage
# depends on driving conditions, according to some research
# gas milage vary by 10 to 15% on driving conditions
# So we are given a formula to calculate the gas mileage, but we need to
# distribute the percentage that varies on drving conditions

# THE DISTRIBUTION BELOW IS OBTAINER BY COMMON SENSE
# AS WE COLLECT MORE DATA WE CAN JUST CHANGE THE VAUES
# =========== Weather : 5%
# =========== Stops : 3% 0.03
# =========== Conditions : 5% 0.05
# =========== Passengers : 3% 0.03

# References :
# http://www.bloomberg.com/news/2013-11-13/-mileage-may-vary-all-too-true-spurs-u-s-to-test-more-cars.html
# http://electronics.howstuffworks.com/gadgets/automotive/gas-mileage-monitor.htm
# http://www.fueleconomy.gov/feg/maintain.shtml
# ==========================

# http://www.fueleconomy.gov/feg/PowerSearch.do?action=noform&path=1&year1=2013&year2=2013&make=Acura&model=ILX&srchtyp=ymm
# http://www.fueleconomy.gov/feg/PowerSearch.do?action=noform&path=1&year1=2013&year2=2013&make=Toyota&model=Corolla&srchtyp=ymm
# http://www.fueleconomy.gov/feg/PowerSearch.do?action=noform&path=1&year1=2013&year2=2013&make=Honda&model=Civic&srchtyp=ymm





