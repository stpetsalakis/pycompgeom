import math
from predicates import *

class Point2(object):
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	@classmethod
	def from_point2(cls, point2):
		return cls(point2.x, point2.y)
		
	@classmethod
	def from_tuple(cls, tup):
		return cls(tup[0], tup[1])
		
	@property
	def coordinates(self):
		return self.x, self.y
		
	def __repr__(self):
		return "Point2(%s,%s)" % (self.x, self.y)
		
	def __eq__(self, other):
		if not other:
			return False
		else:
			return (self.x, self.y) == (other.x, other.y)
		
	def __ne__(self, other):
		if not other:
			return True
		else:
			return (self.x, self.y) != (other.x, other.y)
	
	def __lt__(self, other):
		return (self.x, self.y) < (other.x, other.y)
	
	def __gt__(self, other):
		return (self.x, self.y) > (other.x, other.y)
	
	def __le__(self, other):
		return (self.x, self.y) <= (other.x, other.y)
	
	def __ge__(self, other):
		return (self.x, self.y) >= (other.x, other.y)
	
	def __getitem__(self, index):
		return (self.x, self.y)[index]
		
	def __setitem__(self, index, value):
		temp = [self.x, self.y]
		temp[index] = value
		self.x, self.y = temp
		
	def __iter__(self):
		yield self.x
		yield self.y	
	
	def __repr__(self):
		return "Point2(%s, %s)" % (self.x, self.y)
		
	def distance_to(self, other):
		return math.hypot(self.x - other.x, self.y - other.y)

class Segment2(object):
	
	def __init__(self, start, end):
		self.start = start
		self.end = end
		
	@classmethod
	def from_segment2(cls, segment2):
		return cls(segment2.start, segment2.end)
				
	def __repr__(self):
		return "Segment2(%s, %s)" % (self.start, self.end)
		
	def __eq__(self, other):
		return self.start==other.start and self.end==other.end
		
	def intersectsProperly(self, other):
		a, b = self.start, self.end
		c, d = other.start, other.end
		return intersectProperly(a, b, c, d)
		
	def length(self):
		return self.start.distance_to(self.end)
		
class Polygon2(object):
	def __init__(self, vertices=[]):
		""" Here vertices is a list of Point2s or tuples
		"""
		self.__edges = []
		if vertices:
			self.vertices = vertices
			
	def __getitem__(self, index):
		return self.__vertices[index % len(self)]
		
	def __len__(self):
		return len(self.__vertices)
		
	def index(self, item):
		return self.__vertices.index(item)
			
	@property
	def vertices(self):
		for vertex in self.__vertices:
			yield vertex
	@vertices.setter
	def vertices(self, vertices):
		self.__vertices = [Point2.from_point2(x) for x in vertices]
		self.__edges = []
		lastvertex = None
		c = self.__vertices[0]
		for v in self.__vertices[1:]:
			s = Segment2(c, v)
			self.__edges.append(s)
			c = v
			lastvertex = v
		if lastvertex:
			# Close the polygon boundary
			self.__edges.append(Segment2(v, self.__vertices[0]))

	@property
	def edges(self):
		for edge in self.__edges:
			yield edge
	
	def bounding_box(self):
		minx,miny=WINSIZE
		maxx=maxy=0
		for v in self.vertices:
			if v.x < minx:
				minx=v.x
			if v.x > maxx:
				maxx=v.x
			if v.y < miny:
				miny=v.y
			if v.y > maxy:
				maxy=v.y
		return minx, maxy, maxx-minx, maxy-miny
	
	def isClockwiseOriented(self):
		if len(self) > 3:
			p = self.__vertices[0]
			q = self.__vertices[1]
			r = self.__vertices[2]
			return cw(p, q, r)
		return False
		
	def isConvex(self):
		for vertex in self.vertices:
			previousVertex = self[self.index(vertex)-1]
			nextVertex = self[self.index(vertex)+1]
			if cw(previousVertex, vertex, nextVertex):
				return False
		return True
