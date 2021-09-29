from lxml import etree

# 创建根节点
map = etree.Element("map")
map.set('version', '1.0.1')

# 创建主题节点
root: etree.ElementBase = etree.Element("node")
root.set('TEXT', '安徒生')
map.append(root)

# 创建主题的子节点（1级节点）
node1: etree.ElementBase = etree.Element("node")
node1.set('TEXT', '节点1')
root.append(node1)

# 创建主题的子节点（1级节点）
node2: etree.ElementBase = etree.Element("node")
node2.set('TEXT', '节点2')
root.append(node2)

# 创建子节点的子节点（2级节点）
node1child1: etree.ElementBase = etree.Element("node")
node1child1.set('TEXT', '节点1的子节点1')
node1.append(node1child1)

# 创建子节点的子节点（2级节点）
node1child2: etree.ElementBase = etree.Element("node")
node1child2.set('TEXT', '节点1的子节点2')
node1.append(node1child2)

# 转换成 str，方便导出
map_bytes = etree.tostring(map, pretty_print=True)

with open('mymind.xml', 'w+b') as fp:
    fp.write(map_bytes)

# 导出到 .mm 格式的文件中
with open('mymind.mm', 'w+b') as fp:
    fp.write(map_bytes)
