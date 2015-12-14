class Node :


  order = 3


  def __init__(self, parent=None) :
    """ создание пустой вершины """
    self.keys     = [None for i in range(Node.order-1)]
    self.children = [None for i in range(Node.order)]
    self.parent   = parent


  @property
  def isntLeaf(self) :
    """
       вернет True, если есть хоть один не None
       элемент, иначе - False
                             """
    return any(self.children)
  @property
  def isLeaf(self) :
    return all(self.children)

  @property
  def length(self) :
    """ вернет количество не None элементов """
    return len(self.keys) - (self.keys).count(None)

  @property
  def childrenLength(self) :
    return len(self.children) - (self.children).count(None)

  def getKeyIndex(self, key) :
    return (self.keys).index(key)


  def searchChild(self, index, newKey) :
    if index == 0 and newKey < self.keys[index] :
      return 0
    elif newKey < self.keys[index] :
      return self.searchChild(index-1, newKey)
    else :
      return index+1


  def insertKey(self, newKey) :
    if self.length == 0 :
      # вставить в начало списка #
      self.keys[0] = newKey
    else :
      # если новый ключ меньше первого #
      if newKey <= self.keys[0] :
        (self.keys).insert(0, newKey)
        if self.keys[len(self.keys)-1] == None :
          (self.keys).pop()
      # если новый ключ больше последнего #
      elif newKey >= self.keys[self.length-1] :
        # если узел незаполнен #
        if self.length < Node.order-1 :
          self.keys[(self.keys).index(None)] = newKey
        # если узел заполнен #
        else :
          (self.keys).append(newKey)
      else :
        # найти первое значение, которое будет больше вставляемого #
        # вставить новый ключ перед ним                            #
        i = 0
        while newKey < self.keys[i] :
          i += 1
        (self.keys).insert(i+1, newKey)

  def insertChild(self, index, child) :
    self.children = self.children[:index] + [child] + self.children[index+1:]
    if len(self.children) > Node.order and \
       self.children[len(self.children)-1] == None :
      (self.children).pop()