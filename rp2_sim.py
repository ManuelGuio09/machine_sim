def asm_pio(*args, **kwargs): 
    def decorador(programa):
        def compilador():
            print("Parámetros", kwargs) 
            programa()
            return None
        return compilador
    return decorador

"""
La función asm_pio cumple con una funcion de decorardor para la placa de rasperry; esta funcion recibe
los parametros *args y **kwargs los cuales son comunmente usados para la creacion de decoradores como lo
es este caso debido a que estos dos parametros se usan principalmente en la deficion de la funcion donde el
numero de parametros de entrada es variable. En el caso de los kwargs tiene una funcion importante ya que estos
pueden ir asociados con un nombre a una entrada de una funcion determinada. Por otra parte imprime los parametros
kwargs, ejecuta el probrama que recibe y por ultimo retorna el compilador y el decorador asociado al programa

"""
def decorador_instr(fun_inst):
    def decoracion_instr(self,*args, **kwargs):
        fun_inst(self,*args, **kwargs)
        return None 
    return decoracion_instr

"""
La funcion decorador_instr recibe los mismos parametros con la finalidad de guardarlos en la funcion nombrada como
decoracion_instr, la cual es retornada al final de la funcion con los parametros inicializados. 

"""

pins='pins'

class PIO():
    OUT_LOW='PIO.OUT_LOW'
    
"""
La class PIO define a OUT_LOW con el valor de PIO.OUT_LOW como el parametro de inicializacion del programa 
"""

class StateMachine:
  def __init__(self, id_, program, freq=125000000, **kwargs):
        global sm_iniciandose,fsms
        sm_iniciandose=self
        #print('StateMachine.__init__',id_, program, freq, kwargs)
        self.lista_instr=[]
        program()
        print('Fueron leidas',len(self.lista_instr), 'instrucciones')
        sm_iniciandose=None
        fsms[id_]=self
        pass
"""
La class StateMachine esta compuesta por la funcion __init__ la cual inicializa los parametros dados (id, program, freq), para posteriormente definir las variables globales sm_iniciandose
y fsms. Con el fin de leer la lista de instrucciones que sean ingresadas a la SM, en el caso del valor self hace referencia a la funcion que llamo a la clase StateMachine. A partir de esto
el programa sabrá a que lugar SM se deben enviar los datos. 

"""
        
  def active(self, x=None):
    '''Esta rutina simula exclusivamnte esa FSM. Sería interesante crear simulación en parlelo con otras FSM'''
    if x==1:
        print('Está pendiente de realizar la simulacón')
        
"""
Define a la funcion active como activacion dentro de la maquina de estados para definir si la SM esta encendida o apagada a partir del valor de x 
"""

fsms=[None]*8
"""
Para el caso de la rasperry la cual contiene 8 maquinas de estado, inicializa una lista de 8 espacios los cuales estan vacios.

"""

sm_iniciandose=None    


class nop:
    @decorador_instr
    def __init__(self,*args, **kwargs):
        global sm_iniciandose
        print(self.__class__.__name__)#,'nop.__init__',args,kwargs)
        sm_iniciandose.lista_instr.append(self)

        pass
"""
Para el decorador creado, se le definen los parametros de inicializacion a partir de los argumentos, con el fin de conectar la funcion ya definida
anteriormente. Posteriormente a esto las variables que entran a la clase nop se inicializaran posteriormente a partir de la herencia de la clase nop 
"""
     
    def __getitem__(self,name):
        #print('nop.__getattr__',name)
        pass
""" Unicamente recibe la variable nombre, junto a la funcion"""        
class set(nop):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        pass
""" Inicializa las variables dadas a partir de heredar los valores de la clase nop"""   
class wrap_target(nop):
    def __init__(self,*args, **kwargs):
         super().__init__(*args, **kwargs)
         pass 
""" Al igual que la anterior a partir de la clase nop hereda los valores para ser inicializados """  
class wrap(nop):
    def __init__(self,*args, **kwargs):
         super().__init__(*args, **kwargs)
         pass
""" Para la clase wrap hereda los parametros de la clase nop para inicializar los valores de nop"""

         
         
