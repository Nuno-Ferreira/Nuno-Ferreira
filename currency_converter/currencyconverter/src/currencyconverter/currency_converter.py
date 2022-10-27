import requests

payload = {}
headers= {
  "apikey": "BpvfOLSPhMzoOTHaB8kx075dBhrXsMjr"
}

#code-----------------------------------------------------
def main():
  currency_to_convert_to = str(input('Which currency would you like to convert to?:')) #might need to change this to 0 since I will be assign it another value in the app program
  currency_to_convert_from = str(input('Which currency would you like to convert from?:'))
  amount_to_convert = int(input('How much would you like to convert?:'))

  url = 'https://api.apilayer.com/exchangerates_data/convert?to=' + str(currency_to_convert_to) + '&from=' + str(currency_to_convert_from) + '&amount=' + str(amount_to_convert)

  response = requests.request("GET", url, headers=headers, data = payload) #this will request the data from the API and do the conversion for us

  status_code = response.status_code #still need to figure out if this is necessary 
  result = response.json() #this puts the information in a dictionary 

  print(result['result']) #we use this to get the value of the dictionary that we know has the conversion done

main()

#response------------------------------------------------
"""
{
  "date": "2022-10-12",
  "info": {
    "rate": 0.874417,
    "timestamp": 1665611823
  },
  "query": {
    "amount": 5,
    "from": "EUR",
    "to": "GBP"
  },
  "result": 4.372085,
  "success": true
}
"""