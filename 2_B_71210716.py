nrsi = int(input("Masukkan besar RSI: "))
nmacd= str(input("Masukkan kondisi MACD: "))


if (nrsi >= 70) and (nmacd == "death-cross"):
    print("RSI lebih dari sama dengan 70 dan MACD Death-cross, saatnya Jual")

elif (nrsi <= 30) and (nmacd == "golden-cross"):
    print("RSI kurang dari sama dengan 30 dan MACD Golden-cross, saatnya Beli")

elif (nrsi >= 70) and (nmacd == "golden-cross"):
    print("RSI lebih dari sama dengan 70 dan MACD Golden-cross, Tunggu MACD sampai death-cross")

elif (nrsi <= 30) and (nmacd == "death-cross"):
    print("RSI kurang dari sama dengan 30 dan MACD Death-cross, Tunggu MACD sampai Golden-cross")

elif (nrsi > 30 and nrsi <70) and (nmacd == "golden-cross" or nmacd == "death-cross"):
    print("RSI berada di area 31-69, Bukan saatnya membeli maupun menjual")
else:
    print("Perhatikan data yang anda input !!!")
