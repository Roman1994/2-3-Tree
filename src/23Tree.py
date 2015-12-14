from pdb        import set_trace
from nodeModule import Node



class T23 :


  def __init__(self) :
    """ создание пустого дерева """
    self.root = Node()


  def insert(self, newKey) :
    """
       1. Спуск вниз по дереву в поисках подходящего листа
       2. Если лист заполнен - разделить
       3. Иначе, просто вставить новый ключ
                                           """
    current = self.root
    # спуск вниз по дереву до листа #
    while current.isntLeaf :
      index = current.length-1
      current = current.children[current.searchChild(index,
                                                     newKey)]
    print(current)
    current.insertKey(newKey)
    if current.length > Node.order-1 :
      self.splitNode(current)


  def splitNode(self, node) :
    """
       1. Разбить вершину:
         1.1 В новую вершину перейдет наибольший ключ
         1.2 В старой останется наименьший
         1.3 Медиана будет вставлена в предка
         (медиана служит разделителем между двумя новыми вершинами)
                                                                   """
    parent = node.parent
    if node != self.root :
      # cоздание новой вершины #
      newNode = Node(parent)
      median = Node.order//2
      # передача медианы родителю #
      medianKey = node.keys[median]
      parent.insertKey(medianKey)
      # Связывание родителя с двумя новыми вершинами #
      # Переданная медиана служит разделителем       #
      # значит вершина с меньшими ключами имеет тот  #
      # же индекс что и вставленая медиана           #
      # а новая вершина - индекс+1.                  #
      index = parent.getKeyIndex(medianKey)
      parent.insertChild(index, node)
      parent.insertChild(index+1, newNode)
      # Распределение ключей между новыми вершинами #
      self.__separateKeys(node, median, newNode)
      # Распределение детей между новыми вершинами    #
      self.__separateChildren(node, newNode)
      # если родитель переполнен, то продолжить разделение #
      if parent.length > Node.order-1 :
        self.splitNode(parent)
    # разделение корня происходит отдельно #
    else :
      self.splitRoot(node)

  def splitRoot(self, oldRoot) :
    """
       1. Cоздать новый корень (обновить self.root)
       2. Переместить в него медианый ключ
       3. Создать брата старому корню
       4. Связать новый корень, и 2 новые вершины между собой
       5. Распределить между старым корнем и его братом
       ключи и детей
       6. ??????
       7. Profit
                """
    newRoot   = Node()
    self.root = newRoot

    median    = Node.order//2
    medianKey = oldRoot.keys[median]
    newRoot.insertKey(medianKey)

    oldRootBro        = Node()

    oldRoot.parent    = newRoot
    oldRootBro.parent = newRoot
    index = newRoot.getKeyIndex(medianKey)
    newRoot.children[index] = oldRoot
    newRoot.children[index+1] = oldRootBro

    self.__separateKeys(oldRoot, median, oldRootBro)
    self.__separateChildren(oldRoot,
                            oldRootBro)

  def __separateKeys(self, oldNode, median, newNode) :
    keysLessMedian    = oldNode.keys[:median]
    keysGreaterMedian = oldNode.keys[median+1:]
    oldNode.keys = keysLessMedian + \
                   [None for i in range(Node.order-1 - \
                                        len(keysLessMedian))]
    newNode.keys = keysGreaterMedian + \
                   [None for i in range(Node.order-1 - \
                                        len(keysGreaterMedian))]

  def __separateChildren(self, oldNode, newNode) :
    middle                = len(oldNode.children)//2
    childrenLessMedian    = oldNode.children[:middle]
    childrenGreaterMedian = oldNode.children[middle:]
    oldNode.children = childrenLessMedian + \
                       [None for i in range(Node.order - \
                                            len(childrenLessMedian))]
    newNode.children = childrenGreaterMedian + \
                       [None for i in range(Node.order - \
                                            len(childrenGreaterMedian))]


  def delete(self, key) :
    """
       1. Если ключ находится в узле и узел являтся листом,
       то удалить ключ
       2. Если ключ находится в узле и узел являтся внутреним:
         2.1. Если дочерний по отнешению к текущему узлу узел
         предшествует ключу и содержит не менее median ключей,
         то найти предшественника удаляемого ключа, в поддереве,
         корнем которого являтся тот дочерний узел.
         Заменить удаляемый ключ его предшественником.
         2.2. Если дочерний узел предшествующий ключу имеет
         менеее median ключей, тогда рассмотреть дочерний
         узел следующий за ключом. Найти ключ, который будет
         следующим за удаляемым ключом в поддереве корнем которого
         будет тот узел.
         Удалить следующий ключ и заменить им удаляемый.
         2.3. Иначе, если и предшествующий и последующий узлы заполнены
         менее чем median ключами. Внести удаляемый + ключи из 
         узла последующего за удаляемым
    """


  def preorder(self, subtree) :
    if subtree :
      print(repr((subtree.keys, subtree.parent)), end='\n')
      self.preorder(subtree.children[0])
      self.preorder(subtree.children[1])
      self.preorder(subtree.children[2])
