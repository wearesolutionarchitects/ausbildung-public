print("Bitte geben Sie eine"
      " Temperatur in Celsius ein:")
TemperaturInCelsius = float(input())

TemperaturInFahrenheit = TemperaturInCelsius \
                         * 9 / 5 + 32

print(TemperaturInCelsius, "Grad Celsius entsprechen",
      TemperaturInFahrenheit, "Grad Fahrenheit")
