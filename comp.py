from graphics import *

WIDTH, HEIGHT = 1000, 800
centerPoint = Point(WIDTH / 2, HEIGHT / 2)
currentpage = 'main'
lastpage = 'main'
items = []
restaurants = [['Yell\'s Burgers', [['Burger', 15], ['Cheese Burger', 20], ['Chicken Sandwich', 11], ['Lemonade', 2]]],
			   ['Hooters', [['Wings', 10], ['Red Bull', 4], ['Boneless Wings', 11], ['French Fries', 5], ['Boneless Pizza', 420.69]]],
			   ['Chick-Fil-A', [['Fried Chicken Tenders', 8], ['Spicy Chicken Sandwich', 10], ['Chicken Nuggets', 7], ['Sweet Tea', 3]]]]

def inItems(item):
	out = -1
	for i in range(len(items)):
		if items[i][0] == item[0] and items[i][1][0] == item[1][0]: out = i
	return out

def main(win):
	global lastpage, currentpage, restaurants
	lastpage = 'main'
	main = Rectangle(Point(25, 55), Point(55, 85))
	mainText = Text(Point(40, 70), 'Main')
	cart = Rectangle(Point(145, 55), Point(175, 85))
	cartText = Text(Point(160, 70), 'Cart')
	quit = Rectangle(Point(85, 116), Point(115, 146))
	quitText = Text(Point(100, 131), 'Quit')

	title = Text(Point(WIDTH / 2, 100), 'Restaurants')
	title.setSize(36)
	title.setStyle('bold italic')
	title.setFace('helvetica')

	c = 200
	rs = []
	for r in restaurants:
		b = Rectangle(Point(WIDTH / 2 - 100, c - 15), Point(WIDTH / 2 + 100, c + 15))
		rs.append(b)
		b.draw(win)

		t = Text(Point(WIDTH / 2, c), r[0])
		t.setSize(20)
		t.draw(win)
		c += 100

	main.draw(win)
	mainText.draw(win)
	quit.draw(win)
	quitText.draw(win)
	cart.draw(win)
	cartText.draw(win)
	title.draw(win)

	clickPoint = win.getMouse()
	if clickPoint is None:
		pass
	elif inside(clickPoint, main):
		currentpage = 'main'
	elif inside(clickPoint, cart):
		currentpage = 'cart'
	elif inside(clickPoint, quit):
		currentpage = 'none'
	for i in range(len(rs)):
		if inside(clickPoint, rs[i]):
			currentpage = 'res' + str(i)

def cart(win):
	global lastpage, currentpage, items
	lastpage = 'cart'
	main = Rectangle(Point(25, 55), Point(55, 85))
	mainText = Text(Point(40, 70), 'Main')
	cart = Rectangle(Point(145, 55), Point(175, 85))
	cartText = Text(Point(160, 70), 'Cart')
	quit = Rectangle(Point(85, 116), Point(115, 146))
	quitText = Text(Point(100, 131), 'Quit')

	title = Text(Point(WIDTH / 2, 100), 'Cart')
	title.setSize(36)
	title.setStyle('bold italic')
	title.setFace('helvetica')

	tot = 0
	c = 200
	for item in items:
		t1 = Text(Point(WIDTH / 2, c - 25), 'Restaurant: ' + item[0])
		t1.setSize(25)
		t1.draw(win)

		t2 = Text(Point(WIDTH / 2, c), item[1][0] + '\t${:.2f}'.format(item[1][1]))
		t2.setSize(25)
		t2.draw(win)

		t3 = Text(Point(WIDTH / 2, c + 25), 'Quantity: ' + str(item[2]))
		t3.setSize(25)
		t3.draw(win)

		c += 100
		tot += (item[1][1] * item[2])

	totText = Text(Point(WIDTH / 2, HEIGHT - 100), 'Total: ' + '${:.2f}'.format(tot))
	totText.setSize(25)

	main.draw(win)
	mainText.draw(win)
	quit.draw(win)
	quitText.draw(win)
	cart.draw(win)
	cartText.draw(win)
	title.draw(win)
	totText.draw(win)

	clickPoint = win.getMouse()
	if clickPoint is None:
		pass
	elif inside(clickPoint, main):
		currentpage = 'main'
	elif inside(clickPoint, cart):
		currentpage = 'cart'
	elif inside(clickPoint, quit):
		currentpage = 'none'

def res(win, resNum):
	global lastpage, currentpage, restaurants, items
	lastpage = 'res' + str(resNum)
	main = Rectangle(Point(25, 55), Point(55, 85))
	mainText = Text(Point(40, 70), 'Main')
	cart = Rectangle(Point(145, 55), Point(175, 85))
	cartText = Text(Point(160, 70), 'Cart')
	quit = Rectangle(Point(85, 116), Point(115, 146))
	quitText = Text(Point(100, 131), 'Quit')

	title = Text(Point(WIDTH / 2, 100), restaurants[resNum][0])
	title.setSize(36)
	title.setStyle('bold italic')
	title.setFace('helvetica')

	c = 200
	adds = []
	adds2 = []
	for item in restaurants[resNum][1]:
		t1 = Text(Point(WIDTH / 2, c), item[0])
		t1.setSize(25)
		t1.draw(win)

		t2 = Text(Point(WIDTH / 2, c + 25), '${:.2f}'.format(item[1]))
		t2.setSize(20)
		t2.draw(win)

		b = Rectangle(Point(WIDTH / 2 + 150, c - 15), Point(WIDTH / 2 + 250, c + 15))
		bText = Text(Point(WIDTH / 2 + 200, c), 'Add to Cart')
		bText.setSize(15)
		b.draw(win)
		bText.draw(win)
		adds.append(b)

		i = inItems([restaurants[resNum][0], item])
		q = Text(Point(WIDTH / 2 + 350, c), 'Quantity: ' + ('0' if i == -1 else str(items[i][2])))
		q.setSize(25)
		q.draw(win)
		adds2.append(q)
		c += 100

	main.draw(win)
	mainText.draw(win)
	quit.draw(win)
	quitText.draw(win)
	cart.draw(win)
	cartText.draw(win)
	title.draw(win)

	clickPoint = win.getMouse()
	if clickPoint is None:
		pass
	elif inside(clickPoint, main):
		currentpage = 'main'
	elif inside(clickPoint, cart):
		currentpage = 'cart'
	elif inside(clickPoint, quit):
		currentpage = 'none'
	for i in range(len(adds)):
		adds2[i].undraw()
		if inside(clickPoint, adds[i]):
			x, y = restaurants[resNum][0], restaurants[resNum][1][i]
			t = inItems([x, y])
			if t != -1:
				items[t][2] += 1
			else:
				items.append([x, y, 1])

def clear(win):
	for item in win.items[:]:
		item.undraw()
	win.update()

def inside(point, rectangle):
	ll = rectangle.getP1()
	ur = rectangle.getP2()
	return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

win = GraphWin('Menu', WIDTH, HEIGHT)
while True:
	if lastpage != currentpage: clear(win)
	if currentpage == 'main': main(win)
	elif currentpage == 'cart': cart(win)
	elif currentpage[:3] == 'res': res(win, int(currentpage[3:]))
	elif currentpage == 'none': break
	win.update()

win.close()