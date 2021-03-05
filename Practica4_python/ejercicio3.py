dias_por_mes = [28,30,31]

print("Selecciona un mes: \n"
      "\n1. enero\n"
      "2. febrero\n"
      "3. marzo\n"
      "4. abril\n"
      "5. mayo\n"
      "6. junio\n"
      "7. julio\n"
      "8. agosto\n"
      "9. septiembre\n"
      "10. octubre\n"
      "11. noviembre\n"
      "12. diciembre\n"
      )
select = int(input("ingresa el numero correspondiente a un mes: \n"))

if select != 4 and select != 6 and select != 9 and select != 11:
  if not select == 2:
    print("\nEste mes tiene 31 dias.")
  else:
    print("Este mes tiene 28 dias excepto en los años bisiestos que tienen 29")
else:
  print("Este es tiene 30 dias.")