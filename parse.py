import json
import csv

# read in the 'encounters.csv' csv file and parse the data
def parse_encounters(encounters_file):
    # open the encounters file
    with open(encounters_file, 'r') as encounters_csv:
        # create a csv reader object
        reader = csv.reader(encounters_csv)
        # skip the header row
        next(reader)
        # initialize an empty list to store the data
        encounters = []
        # loop over the rows in the csv file
        for row in reader:
            # parse the data from each row
            encounter = {
                'Encounter': row[0],
                'Castle': row[1],
                'C. of Dead': row[2],
                'Dock': row[3],
                'Field': row[4],
                'North': row[5],
                'Sea': row[6],
                'Southern': row[7],
                'Trades': row[8],
            }
            # append the encounter to the list
            encounters.append(encounter)
        # return the list of encounters
        return encounters

def str_to_range(str_range):
    if str_range == 'pass':
       return
    if '-' in str_range:
         str_range = str_range.split('-')
         range = [int(str_range[0]), int(str_range[1])]
    else:
         range = [int(str_range), int(str_range)]
    if range[1] == 0:
        range[1] = 100
    if range[0] == 0:
       range[0] = 100
    return range

def build_encounter_data(encounter, index):
   str_range = encounter[index]
   # if there is a - split the range
   range = str_to_range(str_range)
   if not range:
       return
   print(f'range {str_range} -> [{range[0]}, {range[1]}]')
   return { 'range': range,  'text': encounter['Encounter']}

def build_table(encounters, location):
    location_encounters = []
    for encounter in encounters:
        data = build_encounter_data(encounter, location)
        if data:
            location_encounters.append(data)
    return {
        'title': f'{location}  Encounters',
        'formula': '1d100',
        'entries': location_encounters,
    }


def build_encounters():
    encounters = parse_encounters('encounters.csv')
    locations = [
                'Castle',
                'C. of Dead',
                'Dock',
                'Field',
                'North',
                'Sea',
                'Southern',
                'Trades',
            ]
    for location in locations:
        location_data = build_table(encounters, location)
        # dump table data to a json encounters_file
        with open(f'tables/{location}-encounters.json', 'w') as encounters_file:
            json.dump(location_data, encounters_file)

def build_factions():
    # read in the 'factions.csv' csv file and parse the data
    with open('factions.csv', 'r') as factions_csv:
        # create a csv reader object
        reader = csv.reader(factions_csv)
        # skip the header row
        next(reader)
        # initialize an empty list to store the data
        factions = []
        for row in reader:
            faction = {
                    'range': row[0],
                    'text': row[1]
                    }
            factions.append(faction)
    for faction in factions:
        faction['range'] = str_to_range(faction['range'])

    for faction in factions:
        print(f'faction {faction["range"]} -> {faction["text"]}')

    with open(f'tables/factions.json', 'w') as encounters_file:
        json.dump({
            'title': 'Factions',
            'formula': '1d100',
            'entries': factions,
            }, encounters_file)

def build_table(name, formula='1d100'):
    # read in the 'factions.csv' csv file and parse the data
    with open(f'{name}.csv', 'r') as data_csv:
        # create a csv reader object
        reader = csv.reader(data_csv, delimiter="|")
        # skip the header row
        next(reader)
        # initialize an empty list to store the data
        entries = []
        for row in reader:
            element = {
                    'range': row[0],
                    'text': row[1]
                    }
            entries.append(element)
    for element in entries:
        element['range'] = str_to_range(element['range'])

    for element in entries:
        print(f'{name} {element["range"]} -> {element["text"]}')

    with open(f'tables/{name}.json', 'w') as encounters_file:
        json.dump({
            'title': f'{name.capitalize().replace("_", " ")}',
            'formula': formula,
            'entries': entries,
            }, encounters_file)



def main():
   build_table('autumn_weather', '1d20')
   build_table('spring_weather', '1d20')
   build_table('summer_weather', '1d20')
   build_table('winter_weather', '1d20')


if __name__ == "__main__":
    main()
