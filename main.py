import time
import pandas as pd
import plotly.express as px

refresh = True

while refresh:
    url_latlong = "http://api.open-notify.org/iss-now.json"
    url_info = "http://api.open-notify.org/astros.json"

    position_data = pd.read_json(url_latlong)
    info_data = pd.read_json(url_info)

    print('On Board Crew :-\n')
    for i in info_data['people']:
        print('Name : ' + i['name'], '\tCraft : ' + i['craft'])

    position_data['latitude'] = position_data.loc['latitude', 'iss_position']
    position_data['longitude'] = position_data.loc['longitude', 'iss_position']
    position_data.reset_index(inplace=True)

    position_data.drop(columns=['index', 'iss_position', 'message'], index=1, inplace=True)

    print("\nMap View :-")
    fig = px.scatter_geo(position_data,
                         lat='latitude',
                         lon='longitude')
    fig.show()

    print('latitude  : ', position_data['latitude'][0])
    print('longitude : ', position_data['longitude'][0])

    time.sleep(10)
    try:
        value = input("Do you want to refresh yes or no : ")
        if value[0].upper() == 'Y':
            print("\n")
            continue
        else:
            break
    except:
        print("Enter only yes or no ! /n Default : yes")
        refresh = True
