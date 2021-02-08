import subprocess
from sys import platform

if platform == "linux" or platform == "linux2":
    binary = "depthmapXcli_linux64"
elif platform == "darwin":
    binary = "depthmapXcli_macos"
elif platform == "win32":
    binary = "depthmapXcli_win32.exe"
elif platform == "win64":
    binary = "depthmapXcli_win64.exe"
else:
    raise("Couldn't detect operating system.")

def space_syntax_help():
    process = subprocess.Popen(['./'+binary, '-h'], 
                           stdout=subprocess.PIPE,
                           universal_newlines=True)

    while True:
        output = process.stdout.readline()
        print(output.strip())
        # Do something else
        return_code = process.poll()
        if return_code is not None:
            print('RETURN CODE', return_code)
            # Process has finished, read rest of the output 
            for output in process.stdout.readlines():
                print(output.strip())
            break

def gpkg_to_dxf(path_to_gpkg, path_to_dxf, _debug=False):
    print("converting %s to %s..." % (path_to_gpkg, path_to_dxf))
    subprocess.run('ogr2ogr -t_srs "EPSG:2056" -f "DXF" %s %s -dim XY -sql "SELECT geom FROM edges"' % (path_to_dxf, path_to_gpkg), shell=True)

def depthmapX(mode,path_to_input,path_to_output,options=''):
    subprocess.run('./%s -m %s -f %s -o %s %s' % (binary,mode,path_to_input,path_to_output,options), shell=True)

def run_segment_analysis(path_to_dxf, path_to_graph):
    print("importing %s..." % (path_to_dxf))
    # ./depthmapXcli_macos -m IMPORT -f data/lucerne.dxf -o data/lucerne.graph
    depthmapX("IMPORT", path_to_dxf, path_to_graph)
    print("converting %s to segment map..." % (path_to_dxf))
    # ./depthmapXcli_macos -m MAPCONVERT -f data/lucerne.graph -co segment -con segment -o data/lucerne.graph
    depthmapX("MAPCONVERT", path_to_graph, path_to_graph, '-co segment -con segment')
    print("calculating 500m, 1km, 2.5km and 5km angular segment analysis...")
    # ./depthmapXcli_macos -m SEGMENT -st angular -sr 500,1000,2500,5000 -f data/lucerne.graph -o data/lucerne.graph
    #./depthmapXcli_macos -m SEGMENT -st tulip -sr 500,1000,2500,5000 -srt metric -sic -stb 1024 -f data/lucerne.graph -o data/lucerne.graph
    depthmapX("SEGMENT", path_to_graph, path_to_graph, '-st tulip -sr 500,1000,2500,5000 -srt metric -sic -stb 1024')