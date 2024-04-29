op=0
compraTotal=0
pr=0
orl=0
pv=0
ae=0
tp=0
rp=None
descuento=0
tp=0
print("*****Menu*****\n[1] Pikachu Roll: $4500\n[2] Otaku Roll: $5000\n[3] Pulpo Venenoso Roll: $5200\n[4] Anguila Electrica Roll: $4800\n[5] Pedido Completo")
while op!=5:
    try:
        op=int(input("Escoja una opcion para agregar a su pedido: \n"))
    except ValueError:
        print("El caracter ingresado no es valido")
    else:
        if op==1:
            pr=pr+1
            compraTotal=compraTotal+4500
            tp=tp+1
        elif op==2:
            orl=orl+1
            compraTotal=compraTotal+5000
            tp=tp+1
        elif op==3:
            pv=pv+1
            compraTotal=compraTotal+5200
            tp=tp+1
        elif op==4:
            ae=ae+1
            compraTotal=compraTotal+4800
            tp=tp+1
        elif op==5:
            print("Pedido completado")
        else:
            print("Ingrese una opcion valida. Por favor intente de nuevo.")
        print(f"[1] Pikachu Roll: {pr}\n[2] Otaku Roll: {orl}\n[3] Pulpo Venenoso Roll: {pv}\n[4] Anguila Electrica Roll: {ae}")
try:    
    op1=int(input("¿Posee algun codigo de descuento?:\n[1] Si\n[2] No\n"))
except ValueError:
    print("El caracter ingresado no es valido")
if op1==1:
    while rp != "s":
        codigoDescuento=input("Ingrese su codigo de descuento:\n")
        if codigoDescuento=="soyotaku":
            descuento=10*compraTotal/100
            compraTotald=compraTotal-(10*compraTotal/100)
            print("Codigo valido por descuento de 10%")
            break
        else:
            rp=input("Codigo no valido. Presione [x] para volver a intentarlo o [s] para salir:\n")
elif op1==2:
    compraTotald=compraTotal
print(f"******************************\nTOTAL PRODUCTOS:{tp}\n******************************\nPikachu Roll: {pr}\nOtaku Roll: {orl}\nPulpo Venenoso Roll: {pv}\nAnguila Electrica Roll: {ae}\n******************************\nSubtotal por pagar: {compraTotal}\nDescuento por código: {descuento}\nTOTAL: {compraTotald}")

