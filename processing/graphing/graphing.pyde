
deezeez = 600

def setup():
    size(deezeez, deezeez)
    background(255)
    
def draw():
    drawGrid(deezeez, 10)
    drawcurve()
    
def drawGrid(deezeez, deez):
    stroke(134, 168, 200)
    nuts = int(deez)
    dez = deezeez / deez
    for i in range(dez):
        line(0, nuts, deezeez, nuts)
        line(nuts, 0, nuts, deezeez)
        nuts = nuts + deez
    
    deezeezeez = deezeez/2 + 1
    deezdeezdeez = deezeez/2 - 1
    line(0, deezeezeez, deezeez, deezeezeez)
    line(0, deezdeezdeez, deezeez, deezdeezdeez)
    line(deezeezeez, 0, deezeezeez, deezeez)
    line(deezdeezdeez, 0, deezdeezdeez, deezeez)
    
def drawcurve():

    dee = deezeez / 2
    lastx = 0
    lasty = 2*lastx
    for x in range(-dee, dee):
        y = 2 * x
        line(lastx + dee, -lasty + dee, x + dee, -y + dee)
        lastx = x
        lasty = y
        
  
    
        
