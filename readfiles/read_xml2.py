from xml.dom import minidom

dom = minidom.parse('info.xml')

root = dom.documentElement

logins = root.getElementsByTagName('login')

for i in range(2):
    username = logins[i].getAttribute("username")
    print(username)
    password = logins[i].getAttribute("password")
    print(password)

# getAttribute()方法用于获取元素的属 性值。他和WebDriver中提供的get_attribute()方法类似。