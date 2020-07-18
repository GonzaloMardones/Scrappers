'''
Autor: Gonzalo Mardones
email: gonzalo-a@hotmail.com
'''


# Importamos las librerias necesarias para request y BeautifulSoup
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# URL tipo cambio Banco Central
url='https://si3.bcentral.cl/Bdemovil/BDE/Series/MOV_SC_TC1'


# Obtenemos documento HTHL
banco_central = requests.get(url)
print(banco_central.text)
'''
<!DOCTYPE html>
<html lang="es">
    <head>
        <meta charset="utf-8">        
        <meta http-equiv="cache-control" CONTENT="no-cache">
        <meta http-equiv="Cache-Control" content="no-store" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta http-equiv="Expires" content="-1">

        <!--meta name="viewport" content="orientation=portrait, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"-->
        <!--meta name="viewport" content="width=device-width, orientation=portrait, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"--> 
        ....
'''

# Obtenemos datos de la lista de tipo de cambio
soup = BeautifulSoup(banco_central.text,'lxml')
lista_tipo_cambio = soup.find('tbody',attrs={'class':'scrollTable'}).find_all('td')
'''
[<td class="col-xs-6 text-center">20-jul-2020</td>,
 <td class="col-xs-6 text-right">787.26</td>,
 <td class="col-xs-6 text-center">17-jul-2020</td>,
 <td class="col-xs-6 text-right">787.50</td>,
 <td class="col-xs-6 text-center">15-jul-2020</td>,
...
'''

# Separamos los dias
lista_dias = soup.find('tbody',attrs={'class':'scrollTable'}).find_all('td',attrs={'class':'col-xs-6 text-center'})
'''
[<td class="col-xs-6 text-center">20-jul-2020</td>,
 <td class="col-xs-6 text-center">17-jul-2020</td>,
 <td class="col-xs-6 text-center">15-jul-2020</td>,
 <td class="col-xs-6 text-center">14-jul-2020</td>,
 <td class="col-xs-6 text-center">13-jul-2020</td>,
 <td class="col-xs-6 text-center">10-jul-2020</td>,
 ...
'''

# Recorremos la lista de dias y los guardamos en un arreglo
list_dias = [dias.text for dias in lista_dias]
'''
['20-jul-2020',
 '17-jul-2020',
 '15-jul-2020',
 '14-jul-2020',
 '13-jul-2020',
 '10-jul-2020',
 '09-jul-2020',
 '08-jul-2020',
 ...]
'''

# Obtenemos la lista de tipo de cambio y los guardamos en un arreglo
list_monedas = [moneda.text for moneda in lista_monedas]
'''
['787.26',
 '787.50',
 '787.87',
...
'''

#Generamos un arreglo con los dias y tipo de cambio
list_dias_moneda = []
for i in range(len(list_monedas)):
    dia = datetime.strptime(list_dias[i],'%d-%b-%Y').date()
    
    moneda = float(list_monedas[i])
    element = [dia,moneda]
    list_dias_moneda.append(element)

'''
[[datetime.date(2020, 7, 20), 787.26],
 [datetime.date(2020, 7, 17), 787.5],
 [datetime.date(2020, 7, 15), 787.87],
 [datetime.date(2020, 7, 14), 788.22],
 [datetime.date(2020, 7, 13), 790.82],
...
'''

#Listo :) tenemos nuestra información