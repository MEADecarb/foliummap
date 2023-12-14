import folium
import json
import requests

# Define a color palette
color_palette = ["#2C557E", "#fdda25", "#B7DCDF", "#000000"]  # Fixed color format

# Create a base map centered over Maryland
m = folium.Map(location=[39.0458, -76.6413], zoom_start=5)

# Custom marker function for school points
def create_school_marker(feature, map_obj):
    coordinates = feature['geometry']['coordinates']
    lat, lon = coordinates[1], coordinates[0]
    icon = folium.Icon(icon='graduation-cap', prefix='fa', color='red')
    popup_info = '<br>'.join([f'{key}: {value}' for key, value in feature['properties'].items()])
    popup = folium.Popup(popup_info, max_width=300)
    folium.Marker(
        location=[lat, lon],
        icon=icon,
        popup=popup
    ).add_to(map_obj)

# Function to add GeoJSON from a URL to a feature group with custom color and pop-up
def add_geojson_from_url(geojson_url, name, color, map_obj):
    feature_group = folium.FeatureGroup(name=name)
    style_function = lambda x: {'fillColor': color, 'color': color}
    response = requests.get(geojson_url)
    geojson_data = response.json()

    if name == "Education Facilities":
        for feature in geojson_data['features']:
            create_school_marker(feature, map_obj)
    else:
        geojson_layer = folium.GeoJson(
            geojson_data,
            style_function=style_function
        )

        if name == "Election Boundaries":
            fields = ['DISTRICT', 'State_Senator', 'State_Representative_1', 'State_Representative_2', 'State_Representative_3', 'State_Senator_Party', 'State_Representative_1_Party', 'State_Representative_2_Party', 'State_Representative_3_Party', 'StateSenator_MDManualURL', 'StateRepresentative1MDManualURL', 'StateRepresentative2MDManualURL', 'StateRepresentative3MDManualURL']
            aliases = ['District', 'State Senator', 'State Rep. 1', 'State Rep. 2', 'State Rep. 3', 'Senator Party', 'Rep. 1 Party', 'Rep. 2 Party', 'Rep. 3 Party', 'Senator URL', 'Rep. 1 URL', 'Rep. 2 URL', 'Rep. 3 URL']
            geojson_layer.add_child(folium.GeoJsonPopup(fields=fields, aliases=aliases, labels=True, localize=True))
        else:
            all_fields = list(geojson_data['features'][0]['properties'].keys())
            geojson_layer.add_child(folium.GeoJsonPopup(fields=all_fields, labels=True))

        geojson_layer.add_to(feature_group)

    feature_group.add_to(map_obj)

# Add each GeoJSON source as a separate feature group with a color, label, and pop-up
github_geojson_sources = [
    ("https://geodata.md.gov/imap/rest/services/Education/MD_EducationFacilities/FeatureServer/5/query?outFields=*&where=1%3D1&f=geojson", "Education Facilities"),
    ("https://geodata.md.gov/imap/rest/services/Boundaries/MD_ElectionBoundaries/FeatureServer/1/query?outFields=*&where=1%3D1&f=geojson", "Election Boundaries")
]

for i, (url, name) in enumerate(github_geojson_sources):
    color = color_palette[i % len(color_palette)]
    add_geojson_from_url(url, name, color, m)

# Load and add the GeoJSON data from Google Drive as another feature group with pop-up
google_drive_path = '/content/drive/MyDrive/Folium/censusOB.geojson'
color_for_drive_data = color_palette[-1]

drive_feature_group = folium.FeatureGroup(name="HB 550 Areas")
with open(google_drive_path, "r") as geojson_file:
    geojson_data = json.load(geojson_file)
    all_fields_drive = list(geojson_data['features'][0]['properties'].keys())
    folium.GeoJson(
        geojson_data,
        style_function=lambda x: {'fillColor': color_for_drive_data, 'color': color_for_drive_data},
        popup=folium.GeoJsonPopup(fields=all_fields_drive, labels=True)
    ).add_to(drive_feature_group)

drive_feature_group.add_to(m)

# Add Layer Control to toggle feature groups
folium.LayerControl().add_to(m)

# Display the map
m
