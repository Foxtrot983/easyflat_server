latitude = 27.460465
longitude = 53.884673


example_search = [
    [27.454267, 53.871124], 
    [27.448840, 53.875212], 
    [27.445271, 53.880297], 
    [27.451068, 53.897598], 
    [27.479423, 53.886110],
    [27.475973, 53.871450],
    [27.461169, 53.860400],
    ]
test_index = [27.434109, 53.881380]

la_list = [j[0] for j in example_search]
lo_list = [j[1] for j in example_search]
print(la_list)
print(lo_list)
        
maximum_la = max(la_list)
minimum_la = min(la_list)

maximum_lo = max(lo_list)
minimum_lo = min(lo_list)

print(f"maximum_la: {maximum_la}\n minimum_la: {minimum_la}\n maximum_lo: {maximum_lo}\n minimum_lo: {minimum_lo}")
print(test_index)
#Поиск между макс мин значениями

if (maximum_la>latitude and latitude>minimum_la) and (maximum_lo>longitude and longitude>minimum_lo):
    print(True)

if (((maximum_la>test_index[0]) and (test_index[0]>minimum_la)) and ((maximum_lo>test_index[1]) and (test_index[1]>minimum_lo))):
    print(True)
else: print(False)