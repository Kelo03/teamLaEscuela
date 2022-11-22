class Carro:
    def __init__(self,request):
        self.request=request
        self.session=request.session
        carro = self.session.get("carro")
        if not carro:
            carro= self.session["carro"]={}
        self.carro=carro

    def agregar(self,juego):
        if(str(juego.id)not in self.carro.keys()):
            self.carro[juego.id]={
                "juego_id":juego.id,
                "nombre":juego.nombre,
                "categoria":juego.categoria,
                "precio":str(juego.precio),
                "cantidad":1,
                "imagen":juego.imagenSmall.url
            }
            self.guardar_carro() 
        else:
            for key ,valor in self.carro.items():
                if key==str(juego.id):
                    print("el producto ya se encuentra en el carrito")
                    break
            self.guardar_carro() 
        
    

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True
    
    #def borrar_juego(self,juego):
     #   if (str(juego.id) in self.carro.keys()):
      #      del self.carro[juego.id]
       #     self.guardar_carro()
    def borrar_juego(self,juego):
        juego.id=str(juego.id)
        if juego.id in self.carro:
            del self.carro[juego.id]
        self.guardar_carro()
        

    def restar(self,juego):
        for key ,valor in self.carro.items():
                if key==str(juego.id):
                    valor["cantidad"]=valor["cantidad"]-1
                    if valor["cantidad"]<1:
                        self.borrar_juego(juego)
                    break
        self.guardar_carro() 

        



    def vaciar_carro(self):
        self.session['carro']={}
        self.session.modified=True