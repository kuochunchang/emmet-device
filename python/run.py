import time

INPUT_GOIO = [10]
OUTPUT_GOIO = [20]

current_data = {}


def get_dht11():
    print("DHT11")


# initial current data
for i in INPUT_GOIO:
    current_data[i] = 100
    print(i, ": ", current_data[i])

for o in OUTPUT_GOIO:
    current_data[o] = 200
    print(o, ": ", current_data[o])


while True:
    time.sleep(1)

    for key, value in current_data.items():
        print("%s: %s" % (key, value))
        get_dht11()
