import json
import sys

def load_old_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def save_new_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def transform_json_to_geojson(old_json):
    new_json = {
        'name': old_json['name'],
        'color': old_json['color'],
        'type': 'FeatureCollection',
        'features': []
    }

    for feature in old_json['data']:

        new_feature = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [feature['lat'], feature['long']],
            },
            'properties': {
                'radius': feature['radius'],
                'intensity': feature['intensity'],
            },
        }
        new_json['features'].append(new_feature)

    return new_json

if __name__ == '__main__':
    inpt = sys.argv[1]

    old_json = load_old_json('./data/' + inpt)
    new_json = transform_json_to_geojson(old_json)
    save_new_json('./data/geo_'+ inpt, new_json)