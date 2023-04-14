"""
    This code is made for running the "get_contours" function outside of the Grasshopper3D
    environment using the rpc module from the compas framework.
    This code is meant to be copy pasted inside a ghPython component.
    Inputs : "
            path : The file path of the image to process.
            read : A boolean to run the code. 
 
    Outputs : 
            points : lists of points from compas geometry 

"""


from compas.rpc import Proxy
import os
from scriptcontext import sticky
from compas.geometry import Polyline, Transformation, Scale, Frame, Vector, Polygon
import Rhino.Geometry as rg
from ghpythonlib.treehelpers import list_to_tree

#Define a unique id before using sticky
points_key = 'pts_{}'.format(str(ghenv.Component.InstanceGuid))

#Avoid the component to run into an error
if points_key not in sticky:
    sticky[points_key] = None

#Running "Contours_By_Color" python file and save the result inside sticky
if read:
    canvas = ghenv.Component.OnPingDocument()
    folder_path =  os.path.abspath(os.path.dirname(canvas.FilePath))
    with Proxy('contours by color', path = folder_path) as cbc:
        sticky[points_key] = cbc.get_contours(path)

#Output for Artist to convert compas geometry into rhino geometry
pts = sticky[points_key]
points = [Polyline(points=p) for p in pts]


 
