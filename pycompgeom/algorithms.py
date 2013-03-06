from primitives import *
from predicates import *
import random

def jarvis(points):
	r0 = min(points)
	hull = [r0]
	r = r0
	while True:
		u = random.choice(points)
		for t in points:
			if cw(r, u, t) or collinear(r, u, t) and between(r, t, u):
				u = t
		if u == r0: break
		else:
			r = u
			points.remove(r)
			hull.append(r)
	return hull

def find_bridge(poly1, poly2, upper=True):
	max1, min2 = max(poly1.vertices), min(poly2.vertices)
	i, j = poly1.index(max_p1), poly2.index(min_p2)
	
	bridge_found = False
	while not bridge_found:
		if upper:
			if not ccw(poly1[i], poly1[i+1], poly2[j]):
				i += 1; i_changed = True
			else: i_changed = False
			if not cw(poly2[j], poly2[j-1], poly1[i]):
				j -= 1; j_changed = True
			else: j_changed = False
		else:
			if not cw(poly1[i], poly1[i-1], poly2[j]):
				i -= 1; i_changed = True
			else: i_changed = False
			if not ccw(poly2[j], poly2[j+1], poly1[i]):
				j -= 1; j_changed = True
			else: j_changed = False
		bridge_found = not i_changed and not j_changed
	
	return Segment2(poly1[i], poly2[j])

def andrew(points):
	upper = []
	lower = []
	for point in sorted(points):
		while len(upper) > 1 and ccwon(upper[-2], upper[-1], point):
			upper.pop()
		while len(lower) > 1 and cwon(lower[-2], lower[-1], point):
			lower.pop()
		upper.append(point)
		lower.append(point)
	hull = lower[:-1]+ [x for x in reversed(upper[1:])]
	return hull
