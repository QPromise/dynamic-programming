from xml.dom import minidom
# 生成XML文件方式
# size 为生成xml文件的大小，单位为M
def generateXml(filename,size,quantity):
    impl = minidom.getDOMImplementation()
    # 创建一个xml dom
    # 三个参数分别对应为 ：namespaceURI, qualifiedName, doctype
    doc = impl.createDocument(None, None, None)
    # 创建根元素
    rootElement = doc.createElement('Pythons')
    # 为根元素添加子元素
    for pythonId in range(1):
        # 创建子元素
        childElement = doc.createElement('python')
        # 为子元素添加id属性
        childElement.setAttribute('id', str(pythonId))
        # 将子元素追加到根元素中
        rootElement.appendChild(childElement)
    # 将拼接好的根元素追加到dom对象
        doc.appendChild(rootElement)
    # 打开test.xml文件 准备写入
    for q in range(quantity):
        file = open(filename+str(q)+'.xml', 'w')
        # 根据文件大小，偏移文件读取位置
        file.seek(1024 * 1024 * size)
        # 写入文件
        doc.writexml(file, addindent='  ', newl='\n')
        # 关闭
        file.close()
generateXml('xml_test',500,1)