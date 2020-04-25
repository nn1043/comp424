import csv
import json
from alpha_vantage.timeseries import TimeSeries


def user_interface():
    menu_list = {
        "MENU": print_menu, "ORGANIZE": organize_data
        }
    print("Please choose an operation:")
    print("MENU")
    run_program = True
    while run_program is True:
        user_response = input("Input: ")
        if user_response.upper() in menu_list:
            if type(menu_list[user_response.upper()]) is list:
                for to_do in menu_list[user_response.upper()]:
                    to_do()
            else:
                menu_list[user_response.upper()]()
        elif user_response.upper() in ["EXIT", "QUIT"]:
            print("Goodbye.")
            run_program = False
        else:
            print("Not a valid command.")

# not really used
def print_menu():
    print("Make data usable: ORGANIZE")


# calls the alpha vantage API
def call_api():
    #JA5HX8HI54MWP72A
    key = "JA5HX8HI54MWP72A"
    ts = TimeSeries(key)
    tqqq, meta = ts.get_intraday(symbol='TQQQ', interval='1min', outputsize='full')
    #print(tqqq["2020-03-05 15:00:00"])

# saves information from API call to a csv file, isn't currently callable
def save_information():
    with open('2020-03-05.csv', 'w') as f:
        for key in tqqq.keys():
            f.write("%s,%s\n"%(key,tqqq[key]))
    print("Done.")

# example JSON outputs
    """
'2020-03-04 13:15:00': {
    '1. open': '85.8400',
    '2. high': '85.9099',
    '3. low': '85.6100',
    '4. close': '85.9099',
    '5. volume': '295540'}}



2020-02-28 10:27:00,{'1. open': '70.5200', '2. high': '70.8691', '3. low': '69.9600', '4. close': '69.9700', '5. volume': '107302'}

2020-02-28 10:27:00
{'1. open': '70.5200'
'2. high': '70.8691'
'3. low': '69.9600'
'4. close': '69.9700'
'5. volume': '107302'}

    """
# everything below is attempting to clean up the JSON, does not function
# as intended
def organize_data():
    timestamps = []
    opens = []
    highs = []
    lows = []
    closes = []
    volumes = []

    learning = open("2020-03-05.csv", "r")
    for line in learning.readlines():
            reading = line.split(",")
            for data in reading:
                if reading.index(data) == 0:   # timestamp
                    temp_slice = data[11:19]
                    timestamps.append(temp_slice)

            #    temp_time = data.split()
            #    for i in temp_time:
            #        if temp_time(i) == 1:
            #            timestamps.append(i)
                if reading.index(data) == 1:    # open
                    temp_slice = data[4:12]
                    #temp = temp_slice[0:7]
                    opens.append(temp_slice)
                if reading.index(data) == 2:    # high
                    temp_slice = data[4:12]
                    temp = temp_slice[0:7]
                    highs.append(temp)
                if reading.index(data) == 3:    # low
                    temp_slice = data[3:11]
                    temp = temp_slice[0:7]
                    lows.append(temp)
                if reading.index(data) == 4:    # close
                    temp_slice = data[5:13]
                    temp = temp_slice[0:7]
                    closes.append(temp)
                if reading.index(data) == 5:    # volume
                    temp_slice = data[6:14]
                    temp = temp_slice[0:7]
                    volumes.append(temp)
    learning.close()
    print(timestamps)
    print(opens)
    # I DONT KNOW WHY BUT IM GOING TO NEED TO SPLIT EVERY PIECE LIKE TIMESTAMPS IS

    # convert to string
    #input = json.dumps(dataset)

    # load to dict
    # my_dict = json.loads(input)

    dataset = {}
    x = 0
    for i in range(len(timestamps)):
        dataset[timestamps[x]] = [
            timestamps[x], opens[x], highs[x], lows[x], closes[x], volumes[x]
            ]
        x = x + 1

    input = json.dumps(dataset)
    with open('dataset.csv', 'w') as f:
        f.write(input)
    f.close()


user_interface()









# empty space
