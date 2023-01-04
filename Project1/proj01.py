###########################################################################
#    Computer project 01
#
#    Ask for input
#    Convert to meters, furlongs, miles, feet, and time to walk
#    Round and then print the results with message showing calculated units
###########################################################################

#These statements store the input data and convert it into floats
rods_str = input('Input rods: ')
rods_float = float(rods_str)

#These variables store the conversions after converting
m = rods_float*5.0292
furlongs = rods_float/40
mi = m/1609.34
ft = m/0.3048
time = mi*(60/(3.1))

#The below print statements round the calculated numbers and then display them
print('You input', rods_float, 'rods.\n')
print('Conversions')
print('Meters:', round(m,3))
print('Feet: ', round(ft,3))
print('Miles:', round(mi,3))
print('Furlongs:', round(furlongs,3))
print('Minutes to walk', rods_float , 'rods:', (round(time,3)))