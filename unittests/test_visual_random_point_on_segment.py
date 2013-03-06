import sys
sys.path.append('..')
from pycompgeom.generators import *
from pycompgeom.visuals import *
from pycompgeom.events import *

while True:
	s = VSegment2()
	VPoint2(random_point_on_segment(s))
	
