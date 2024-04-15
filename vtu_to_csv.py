import xml.etree.ElementTree as ET
import csv

def parse_vtu_file(vtu_filename):
    """ Parse the VTU file and extract vertices and connectivity data. """
    tree = ET.parse(vtu_filename)
    root = tree.getroot()
    
    points_data = root.find('.//Points/DataArray').text
    connectivity_data = root.find('.//Cells/DataArray[@Name="connectivity"]').text
    
    # Process vertices
    vertices = [tuple(map(float, point.split())) for point in points_data.split()]
    
    # Process connectivity
    connectivity = [tuple(map(int, conn.split())) for conn in connectivity_data.split()]
    
    return vertices, connectivity

def write_to_csv(csv_filename, vertices, connectivity):
    """ Write the extracted data to a CSV file. """
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Type', 'Vertices', 'Connectivity'])
        writer.writerow(['Cube', '; '.join(map(str, vertices)), '; '.join(map(str, connectivity))])

def main():
    vtu_filename = 'random_cube.vtu'  # Replace with your actual file path
    csv_filename = 'output.csv'
    
    vertices, connectivity = parse_vtu_file(vtu_filename)
    write_to_csv(csv_filename, vertices, connectivity)
    
    print("Vertices:", vertices)
    print("Connectivity:", connectivity)

if __name__ == "__main__":
    main()
