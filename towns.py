import cv2

def avg(couple):
	return sum(couple)/2

CHARS = " `'~.,:;i1tfLCG0"

towns = cv2.imread("towns.png", cv2.CV_LOAD_IMAGE_GRAYSCALE)
#towns = cv2.resize(towns, (100,100))

row_pairs = [towns[it:it+2] for it in range(0, len(towns), 2)]
row_tuples = [zip(row[0], row[1]) for row in row_pairs]
rows = [map(lambda (tup): avg(tup), row) for row in row_tuples]

newim = []
for row in rows:
	new = []
	for pix in row:
		new.append(CHARS[pix/15])
	newim.append(new)


for row in newim:
	print("".join(row))
