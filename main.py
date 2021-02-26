#Recall in our Dictionaries Lecture, we created a program that converts USD to other currencies.

#Now, let's create a more advanced version of it, that lets the user enter both an amount of money, the type of currency they're entering, and the type of currency you'd like it converted to.

#Your options are: USD, EUR, GBP, INR, XBT, AUD, MXN

#Here is a table of conversion values:
#1 USD = 00.83 Eur
#1 USD =	.74 GBP
#1 USD = 73.13 INR
#1 USD =	00.01 XBT
#1 Eur = 01.61 AUD
#1 Eur = 25.90 MXN

#Make dictionaries for each currency. You could probably make a dictionary of dictionaries, but I will try that later

currencyDict = {"USD" : {"Eur" : 00.83, 
"GBP" : 00.74, 
"INR" : 73.13, 
"XBT" : 00.01}, 
"EUR" : {"AUD" : 01.61, "MXN" : 25.90}
}

#print(currencyDict)
userCurrency = input("Enter the currency you would like to convert from: USD or Eur: ")
#print(convertToList)


print(currencyDict[userCurrency])
#print(currencyList)
convertTo = input("Enter the currency you would like to convert to: ")
#currencyAmount = float(input("Enter how much currency you would like to convert: "))

#for currency in currencyDict:
#  print(currency)
#  for subcurrency in currencyDict[currency]:
#    print(currency, subcurrency)
#convertedAmount = currencyAmount * currencyDict[userCurrency][convertTo]
#print(f"You will get {convertedAmount} of {convertTo} from {userCurrency}")

#print(currencyDict[userCurrency][convertTo])
