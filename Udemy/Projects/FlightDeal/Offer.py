# Day 39 - 100 Days of Code

from pprint import pprint
import requests_cache
from datetime import datetime, timedelta

from Func import Task
from Data import FlightData
from Search import FlightSearch
from Notify import FlightNotifs

print(f'\n---- Flight ^ Deals ----\n')

requests_cache.install_cache(
    'flight_cache',
    urls_expire_after = {
        '*.sheety.co*': requests_cache.DO_NOT_CACHE,
        '*': 3600,
    }
) # Conserve requests | Preserve free tier

task = Task()
sheety_data = task.get_destination_data()
# pprint(sheety_data)
customer_data = task.get_customer_emails()
customer_email_list = [row['whatIsThyEmail?'] for row in customer_data]

tomorrow = datetime.now() + timedelta(days=1)
six_months_after = datetime.now() + timedelta(days=(6 * 30))

search = FlightSearch()
notify = FlightNotifs()

ORIGIN_CITY_IATA = 'IATA_code'

for destination in sheety_data:
    pprint(f"Flights to {destination['city']}....")
    flights = search.check_flights(ORIGIN_CITY_IATA, destination['iataCode'], from_time=tomorrow, to_time=six_months_after, is_direct=True)
    # pprint(flights)

    cheapest_flight = FlightData.find_cheapest_flight(flights, return_date=six_months_after.strftime('%Y-%m-%d'))
    pprint(f"{destination['city']} : ISO_code {cheapest_flight.price}")

    if cheapest_flight.price == 'N/A':
        pprint(f"No direct flight found to {destination['city']}!")
        stopover_flights = search.check_flights(ORIGIN_CITY_IATA, destination['iataCode'], from_time=tomorrow, to_time=six_months_after, is_direct=False)
        
        cheapest_flight = FlightData.find_cheapest_flight(stopover_flights, return_date=six_months_after.strftime('%Y-%m-%d'))
        print(f'Cheapest indirect flight price : ISO_code {cheapest_flight.price}')
        
    if cheapest_flight.price != 'N/A' and cheapest_flight.price < destination['lowestPrice']:
        if cheapest_flight.stops == 0:
            message = f'Low price alert! Only ISO_code {cheapest_flight.price} to fly direct from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, on {cheapest_flight.out_date} until {cheapest_flight.return_date} !!'
    
        else:
            message = f'Low price alert! Only ISO_code {cheapest_flight.price} to fly from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, on {cheapest_flight.out_date} until {cheapest_flight.return_date} !!'
        
        print(f'Check email. Lower price flight found to {destination['city']}!')
        task.update_least_price(destination['id'], cheapest_flight.price)
        
        notify.send_sms(message_body=message)
        notify.send_whatsapp(message_body=message)
        
        notify.send_emails(email_list=customer_email_list, email_body=message)