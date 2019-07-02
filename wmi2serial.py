import wmi
import serial
import sys

# print(len(sys.argv))

if len(sys.argv) < 3:
    print('-' * 50)
    print('Usage:')
    print('-' * 50)
    print('> python wmi2serial.py COM9 9600')
    print('-' * 50)
    print('Onde:')
    print('-' * 50)
    print('COM9 = sua porta serial')
    print('9600 = velocidade desejada para a comunicacao')
    print('-' * 50)
    exit()

string_serial = ""

# CPU Load
c = wmi.WMI()
for s in c.Win32_Processor():
    #print(s)
    string_serial += "cpu_load=" + str(s.LoadPercentage)

# CPU Temperature
c = wmi.WMI(namespace=r'root\WMI')
wql = "SELECT * FROM MSAcpi_ThermalZoneTemperature"
for s in c.query(wql):
    #print(s) # divide by 10 and subtract 273.15 to get celsius
    temp_kelvin = s.CurrentTemperature
    temp_celsius = (temp_kelvin / 10) - 273.15
    string_serial += "&temp_celsius=%0.2f" % temp_celsius

# System Information
# c = wmi.WMI(namespace=r'root\WMI')
# wql = "select * from MS_SystemInformation"
# for s in c.query(wql):
#   print(s) 

# HDD used size
c = wmi.WMI ()
for disk in c.Win32_LogicalDisk(DriveType=3):
    hdd_used = ((int(disk.Size) - int(disk.FreeSpace)) / 1024 / 1024 / 1024)
    #print(disk.Caption, "%d GB used" % hdd_used)
    string_serial += "&hdd_used=" + str(int(hdd_used))

# RAM used
c = wmi.WMI(namespace=r'root\CIMV2')
wql = "SELECT * FROM Win32_OperatingSystem"
for s in c.query(wql):
    #print(s) 
    free = s.FreePhysicalMemory
    total = s.TotalVisibleMemorySize
    # "Percentage used: {0}%", Math.Round(((total - free)/total * 100)
    ram_used = ((int(total) - int(free)) / 1024 / 1024 )
    #print("%d GB RAM used" % ram_used)
    string_serial += "&ram_used=" + str(int(ram_used))

# print(string_serial)

# send to serial
print('Enviando dados para a serial....')
comport = serial.Serial(sys.argv[1], int(sys.argv[2]))
for c in string_serial:
    # print(c)
    comport.write(ord(c))
comport.close()
print('OK')
