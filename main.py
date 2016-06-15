# main.py -- put your code here!



from pyb import UART
from micropyGPS import MicropyGPS
from pyb import LED





# Setting up UART
# This example uses UART 2 with RX on pin X4
# Baudrate is 9600bps, with the standard 8 bits, 1 stop bit, no parity


uart = UART(2, 9600)


# Initiate

my_gps = MicropyGPS()


# Reads 100 sentences and reports how many were parsed and if any failed the CRC check
sentence_count = 0
while True:
    if uart.any():
        led = LED(3)
        led.on()
        stat = my_gps.update(chr(uart.readchar()))
        
        if stat:
            print(stat)
            print('Latitude:', my_gps.latitude_string())
            print('Longitude:', my_gps.longitude_string())
            print('Speed:', my_gps.speed_string('kph'), 'or', my_gps.speed_string('mph'), 'or', my_gps.speed_string('knot'))
            print('Date (Short M/D/Y Format):', my_gps.date_string('s_mdy'))
            print('# of Satellites in View:', my_gps.satellites_in_view)
            data_valid = my_gps.satellite_data_updated()
            
            
            file = open('GPS_Log.txt', 'ab')
            
            
            file.write('Latitude: ')
            file.write(my_gps.latitude_string())
            file.write(' , \n')
            file.write('Longitude: ')
            file.write(my_gps.longitude_string())
            file.write(' , \n')
            file.write( my_gps.speed_string('knot'))
            file.write(' , \n')
            file.flush()
            

            stat = None
            sentence_count += 1



    if sentence_count == 100:
        led.off()
        file.close
        break;




print('Sentences Found:', my_gps.clean_sentences)
print('Sentences Parsed:', my_gps.parsed_sentences)
print('CRC_Fails:', my_gps.crc_fails)





