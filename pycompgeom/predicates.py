def area2(p, q, r):
	return (r.y-p.y) * (q.x-p.x) - (q.y-p.y) * (r.x-p.x)

def ccw(p, q, r):
	return area2(p, q, r) > 0
	
def ccwon(p, q, r):
	return area2(p, q, r) >= 0
	
def cw(p, q, r):
	return area2(p, q, r) < 0
	
def cwon(p, q, r):
	return area2(p, q, r) <= 0
	
def collinear(p, q, r):
	return area2(p, q, r) == 0
	
def between(p, q, r):
	if not collinear(p, q, r):
		return False
	if p.x != q.x:
		return p.x <= r.x <= q.x or p.x >= r.x >= q.x
	else:
		return p.y <= r.y <= q.y or p.y >= r.y >= q.y
