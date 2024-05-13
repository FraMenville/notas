import click
import chorizo
import jason_manager


@click.group()  #comando para crear una serie de comandos 
def comandos(): #variable definida de pasar
    pass

@click.command() #todo este bloque es para calcular la prueba corta
@click.option("--nota", prompt="ingrese la nota de la prueba corta",type=float,help="el prompt llama el valor a colocar en la prueba corta")
def prueba_corta(nota): #esto se conecta a la variable definida en chorizo.py
    resultado = chorizo.pruebacorta(nota)
    print(resultado)

@click.command() #todo este bloque es para calcular la prueba parcial
@click.option("--parcial", prompt="ingrese la nota de la prueba parcial",type=float,help="el prompt llama el valor a colocar en la prueba parcial")
def prueba_parcial(parcial): #esto se conecta a la variable definida en chorizo.py
    resultado = chorizo.pruebaparcial(parcial)
    print(resultado)

@click.command()
@click.option("--corte", prompt="nota del corte 1")
def leer_corte(corte):
    notas = jason_manager.read_json()
    contador = leer_corte - 1
    print(notas[contador])
    #print(type(notas))
    print(notas[1])

    #if notas["corte"]==corte:
    #    print(notas)

comandos.add_command(prueba_corta) #serie de comandos para que funcione correctamente
comandos.add_command(prueba_parcial)
comandos.add_command(leer_corte)

if __name__=="__main__": #llama a un bucle con "comandos", la serie de comandos definidos anteriormente
    comandos()

