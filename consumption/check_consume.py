import json

DOCUMENTATION = r"""============================


******* HOW TO USE IT **********
The current folder contains two JSON files: < config.json > and < options.json >.
From the options files you can see what options are available to choose from.
After choosing the options, specify them in the config file.
As a result, the program will print a report containing data in .TXT and .CSV format.
Experiment with the config file and ensure it contains your needed optons. 
If certain options aren't available, add it to < options.json > and
specify the weights for the newly added option.


******* HOW THIS WORKS *********
First, we need to consider that consumption of gas mileage
depends on driving conditions, according to some research
gas milage vary by 10 to 15% on driving conditions
So we are given a formula to calculate the gas mileage, but we need to
distribute the percentage that varies on drving conditions

THE DISTRIBUTION BELOW IS OBTAINER BY COMMON SENSE
AS WE COLLECT MORE DATA WE CAN JUST CHANGE THE VAUES
=========== Weather : 5%
=========== Stops : 3% 0.03
=========== Conditions : 5% 0.05
=========== Passengers : 3% 0.03

References :
http://www.bloomberg.com/news/2013-11-13/-mileage-may-vary-all-too-true-spurs-u-s-to-test-more-cars.html
http://electronics.howstuffworks.com/gadgets/automotive/gas-mileage-monitor.htm
http://www.fueleconomy.gov/feg/maintain.shtml
==========================

http://www.fueleconomy.gov/feg/PowerSearch.do?action=noform&path=1&year1=2013&year2=2013&make=Acura&model=ILX&srchtyp=ymm
http://www.fueleconomy.gov/feg/PowerSearch.do?action=noform&path=1&year1=2013&year2=2013&make=Toyota&model=Corolla&srchtyp=ymm
http://www.fueleconomy.gov/feg/PowerSearch.do?action=noform&path=1&year1=2013&year2=2013&make=Honda&model=Civic&srchtyp=ymm
"""


# Well, the reason why I didnt define this as function
# member of the classes is that I want to avoid reference to self
# since this will be used pretty often
ADD_WEIGHT_TO_MPG = lambda mpg, weight: mpg - (mpg * weight)

REPORT_HEADER = [
  "City",
  "Total Distance(in Miles)",
  "Gas Gallons Needed",
  "Total Cost(in USD)",
  "Car Name",
  "MPG without D.Conditions",
  "MPG w/ D.Conditions",
  "Forecast",
  "Passengers",
  "Traffic Lights"
]

class Helper(object):

      @classmethod
      def read_json(self, filename):
          json_file = file(filename, "r")
          json_data = json.load(json_file)
          json_file.close()
          return json_data

class Getter(object):

      def options(self):
          return Helper.read_json("options.json")

      def cars(self, name):
          return self.options()["cars"][name.lower()]

      def city_gas_price(self, name):
          return self.options()["cities"][name.lower()][1]

      def city_weight(self, name):
          return self.options()["cities"][name.lower()][0]

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

          self.car_mpg = Getter.cars(self, config_file["Car"] )
          self.car_name = config_file["Car"]
          self.weather_weight = Getter.forecast(self, config_file["Forecast"] )
          self.weather = config_file["Forecast"]
          self.passengers_weight = Getter.passengers(self) * config_file["Passengers"]
          self.passengers = config_file["Passengers"]
          self.stops_weight = Getter.stops(self) * config_file["Stops"]
          self.stops = config_file["Stops"]
          self.city_name = config_file["City"]
          self.city_weight = Getter.city_weight(self, config_file["City"] )
          self.city_gas_price = Getter.city_gas_price(self, config_file["City"] )
          self.traffic_lights_weight = Getter.traffic_lights(self) * config_file["Traffic Lights"]
          self.traffic_lights = config_file["Traffic Lights"]
          self.miles = config_file["Miles"]

      def attributes(self):
          return self.__dict__

      def gallons_needed(self):
          return ( self.miles/self.add_weights_to_car_mpg() )

      def total_cost(self):
          return ( self.gallons_needed() * self.city_gas_price )

      def add_weights_to_car_mpg(self):
          original = self.car_mpg
          # we take a percentage out of the mpg of the car
          # based on all the factors, because it may vary
          # then we subtract, as can be seen it does affect
          # the mpg from 17% to 30% including margin for errors
          weights = self.weights_to_array()
          for weight in weights:
              result = ADD_WEIGHT_TO_MPG(original, weight)
              original = result
          return original

      def report_data(self):
          return map(str, [
              self.city_name,
              self.miles,
              self.gallons_needed(),
              self.total_cost(),
              self.car_name.capitalize(),
              self.car_mpg,
              self.add_weights_to_car_mpg(),
              self.weather.capitalize(),
              self.passengers,
              self.traffic_lights
            ]
          )

      def weights_to_array(self):
          return [
            self.weather_weight,
            self.passengers_weight,
            self.stops_weight,
            self.traffic_lights_weight,
            self.city_weight
          ]

      def populate_report_csv(self):
          new_file = file(FILE_REPORT + ".csv", "w")
          new_report = self.report_data()

          new_file.write("%s \n" % (",".join(REPORT_HEADER)))
          new_file.write("%s \n" % (",".join(new_report)))
          new_file.close
          print 4 * "...New CSV report was just issued..."

      def populate_report_txt(self):
          new_file = file(FILE_REPORT + ".txt", "w")
          new_report = self.map_data_and_header()

          for k,v in new_report.iteritems():
              new_file.write("%s : %s \n" % (k,v))
          new_file.close()
          print 4 * "...New TXT report was just issued..."

      def map_data_and_header(self):
          data = self.report_data()
          return dict(zip(REPORT_HEADER, data))

def main():
    print 5 * "\n"
    new_report = ConsuptionCalculator("config.json")
    new_report.populate_report_csv()
    new_report.populate_report_txt()
    print 5 * "\n"
    print DOCUMENTATION

if __name__ == "__main__":
    FILE_REPORT = raw_input("Please, provide an filename for your report ? (it will be save in this program folder) :")
    main()
