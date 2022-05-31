import json
import sys

def load_old_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def save_new_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)

def transform_json_to_geojson(old_json):
    new_json = {
        'name': old_json['name'],
        'color': old_json['color'],
        'type': 'FeatureCollection',
        'features': []
    }

    counter = 0
    for feature in old_json['data']:
        # limit to 3000 features
        # if counter > 3000:
        #     break

        new_feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [feature['long'], feature['lat']],
            },
            'properties': {
                'radius': feature['radius'],
                'intensity': feature['intensity'],
            },
        }

        new_json['features'].append(new_feature)
        counter += 1

    return new_json

if __name__ == '__main__':
    inpt = sys.argv[1]
    
    filename = inpt.split('/')[-1]

    old_json = load_old_json(inpt)
    new_json = transform_json_to_geojson(old_json)
    save_new_json('./geo_jsons/geo_'+ filename, new_json)