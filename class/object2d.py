DEFINE_2D = False
if DEFINE_2D:
   class Object2D(object):
      def __init__(self, name, vector, data, shape=square): 
         self.name = name
         self.vector = vector
         self.data = data
         self.shape = shape

      @staticmethod
      def static(self) -> object: ...

      def render(self): ... 

else:
   DEFINE_2D