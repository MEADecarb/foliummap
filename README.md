# Interactive Map with Folium

This project contains a Python script that generates an interactive map using the Folium library. The map is centered over Maryland and includes various layers that display educational facilities, election boundaries, and additional GeoJSON data loaded from Google Drive. Each layer is represented with different markers and pop-ups to provide detailed information about each feature.

## Features

- **Educational Facilities:** Marked with custom icons, these points provide detailed information about each facility when clicked.
- **Election Boundaries:** Outlined areas with pop-ups that show detailed election boundary information, including district names and representative details.
- **HB 550 Areas:** Loaded from a Google Drive path, this layer shows additional GeoJSON data with customized pop-ups.

## Color Palette

A specific color palette is defined for differentiating the layers visually.

## Getting Started

### Prerequisites

You need Python installed on your system along with the following libraries:
- `folium`
- `requests`

You can install these packages using pip:

```bash
pip install folium requests
```

### Running the Script

1. Clone the repository or download the Python script.
2. Ensure you have the required Python packages installed.
3. Run the script:

```bash
python map.py
```

This will generate an interactive map that you can view in a web browser.

## Contributing

Feel free to fork the project and submit pull requests. You can also open an issue for any bugs or feature requests.

## License

This project is open source and available under the [MIT License](LICENSE).

---

**Note:** Make sure to include a `LICENSE` file in your GitHub repository if you reference it in the README. The MIT License is a common choice for open-source projects, but you can choose a different license according to your project's needs.
