import numpy as np

def create_random_dimension_cube():
    # Dimensiones aleatorias para cada lado del cubo
    x_length = np.random.uniform(1, 5)  # Longitud en la dirección x
    y_length = np.random.uniform(1, 5)  # Longitud en la dirección y
    z_length = np.random.uniform(1, 5)  # Longitud en la dirección z

    # Nombre del archivo de salida
    filename = "random_cube.vtu"

    # Abrir el archivo para escribir
    with open(filename, 'w') as f:
        # Escribir el encabezado del archivo VTK
        f.write('<?xml version="1.0"?>\n')
        f.write('<VTKFile type="UnstructuredGrid" version="0.1" byte_order="LittleEndian">\n')
        f.write('  <UnstructuredGrid>\n')
        f.write('    <Piece NumberOfPoints="8" NumberOfCells="12">\n')

        # Coordenadas de los puntos del cubo
        f.write('      <Points>\n')
        f.write('        <DataArray type="Float32" NumberOfComponents="3" format="ascii">\n')
        f.write(f'          0 0 0   {x_length} 0 0   {x_length} {y_length} 0   0 {y_length} 0   0 0 {z_length}   {x_length} 0 {z_length}   {x_length} {y_length} {z_length}   0 {y_length} {z_length}\n')  # Vértices del cubo
        f.write('        </DataArray>\n')
        f.write('      </Points>\n')

        # Celdas (12 triángulos)
        f.write('      <Cells>\n')
        f.write('        <DataArray type="Int32" Name="connectivity" format="ascii">\n')
        # Cada cara del cubo dividida en 2 triángulos
        f.write('          0 1 2   0 2 3   4 5 6   4 6 7   0 4 7   0 7 3   1 5 6   1 6 2   0 1 5   0 5 4   2 3 7   2 7 6\n')
        f.write('        </DataArray>\n')
        f.write('        <DataArray type="Int32" Name="offsets" format="ascii">\n')
        f.write('          3 6 9 12 15 18 21 24 27 30 33 36\n')  # Offset en la lista de conectividad
        f.write('        </DataArray>\n')
        f.write('        <DataArray type="UInt8" Name="types" format="ascii">\n')
        f.write('          5 5 5 5 5 5 5 5 5 5 5 5\n')  # Código VTK para triángulos
        f.write('        </DataArray>\n')
        f.write('      </Cells>\n')

        f.write('    </Piece>\n')
        f.write('  </UnstructuredGrid>\n')
        f.write('</VTKFile>\n')

# Llamada a la función para crear el archivo VTK
create_random_dimension_cube()
