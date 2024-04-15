def create_paraview_square():
    # Nombre del archivo de salida
    filename = "square.vtu"
    
    # Abrir el archivo para escribir
    with open(filename, 'w') as f:
        # Escribir el encabezado del archivo VTK
        f.write('<?xml version="1.0"?>\n')
        f.write('<VTKFile type="UnstructuredGrid" version="0.1" byte_order="LittleEndian">\n')
        f.write('  <UnstructuredGrid>\n')
        f.write('    <Piece NumberOfPoints="4" NumberOfCells="2">\n')
        
        # Coordenadas de los puntos del cuadrado
        f.write('      <Points>\n')
        f.write('        <DataArray type="Float32" NumberOfComponents="3" format="ascii">\n')
        f.write('          0 0 0   1 0 0   1 1 0   0 1 0\n')  # Vértices del cuadrado
        f.write('        </DataArray>\n')
        f.write('      </Points>\n')
        
        # Celdas (dos triángulos)
        f.write('      <Cells>\n')
        f.write('        <DataArray type="Int32" Name="connectivity" format="ascii">\n')
        f.write('          0 1 2   0 2 3\n')  # Dos triángulos
        f.write('        </DataArray>\n')
        f.write('        <DataArray type="Int32" Name="offsets" format="ascii">\n')
        f.write('          3 6\n')  # Offset en la lista de conectividad
        f.write('        </DataArray>\n')
        f.write('        <DataArray type="UInt8" Name="types" format="ascii">\n')
        f.write('          5 5\n')  # Código VTK para triángulos
        f.write('        </DataArray>\n')
        f.write('      </Cells>\n')
        
        f.write('    </Piece>\n')
        f.write('  </UnstructuredGrid>\n')
        f.write('</VTKFile>\n')

# Llamada a la función para crear el archivo VTK
create_paraview_square()
