from soil import moisture, sample

def main():
    moisture = sample()
    days = 0
    while  moisture > 25:
        moisture = sample()
        days += 1
        print(f'Day {days}: Moisture is {moisture}%')
    print("time to water")

main()
