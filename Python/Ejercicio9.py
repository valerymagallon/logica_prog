#IMPORTAR LIBRERÍAs
import math
import locale
locale.setlocale(locale.LC_MONETARY, 'es_MX.UFT-8')

# ENTRADA DE DATOS



mes = str(input("Ingrese el mes: "))
días_laborables = float(input("Ingrese los días laborables: "))
pago_por_día = float(input("Ingrese el pago por día: "))

# PROCESO (Cálculos y Operaciones Matemáticas y/o Lógicas)

pago_bruto = días_laborables * pago_por_día
iva_trasladado = pago_bruto * 0.16
subtotal = pago_bruto + iva_trasladado
iva_retenido = (2/3) * iva_trasladado
isr_retenido = pago_bruto * 0.10
pago_neto = subtotal - iva_retenido - isr_retenido

# SALIDA DE DATOS 

print(f"Mes= " + str(mes))
print(f"EL pago bruto es de: {locale.currency(pago_bruto)}")
print(f"El IVA trasladado es de: {locale.currency(iva_trasladado)}")
print(f"El subtotal es de: {locale.currency(subtotal)}")
print(f"El IVA retenido es de: {locale.currency(iva_retenido)}")
print(f"El ISR retenido es de: {locale.currency(isr_retenido)}")
print(f"El pago neto es de: {locale.currency(pago_neto)}")