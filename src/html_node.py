from functools import reduce

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_string = ''
        if self.props == None:
         return props_string
        for i in self.props:
            props_string += f' {i}="{self.props[i]}"'
        return props_string
    
    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            if (
                self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props
                ):
                return True
        return False

    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})' 
    
#

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Invalid HTML: no value")
        if self.tag == None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'

#

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        # print('TAG:', self.tag)
        # print('CHILDREN:', self.children)
        if self.tag == None:
            # print('VALUE ERROR')
            raise ValueError("Invalid HTML: no tag")
        if self.children == None or self.children == []:
            # print('VALUE ERROR')
            raise ValueError("Invalid HTML: no children")
        accumulation = reduce(lambda accumulated_result, node: accumulated_result + f'{node.to_html()}', self.children, '')
        result = f'<{self.tag}{self.props_to_html()}>{accumulation}</{self.tag}>'
        # print('RESULT:', result)
        return result
    
    def __repr__(self):
        return f'ParentNode({self.tag}, CHILDREN: {self.children}, {self.props})'
    
#

