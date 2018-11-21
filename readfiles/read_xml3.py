from xml.dom import minidom

dom = minidom.parse('info.xml')

root = dom.documentElement

provinces = dom.getElementsByTagName('province')

citys = dom.getElementsByTagName('city')

p2 = provinces[1].firstChild.data
print(p2)

c1 = citys[0].firstChild.data
print(c1)

c2 = citys[2].firstChild.data
print(c2)

# firstChild属性返回被选节点的第一个子节点。data表示获取该节点的数据，它和WebDriver中提供的text方法类似。






