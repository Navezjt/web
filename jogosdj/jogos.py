# Sua lista de texto
lista_texto = """
11:00   Arsenal x Sheffield United | https://v2.sportsonline.so/channels/bra/br5.php
11:00   AFC Bournemouth x Burnley | https://v2.sportsonline.so/channels/bra/br2.php
11:15   Barcelona x Real Madrid | https://v2.sportsonline.so/channels/bra/br3.php
11:30   Portimonense x Estoril | https://v2.sportsonline.so/channels/pt/sporttv1.php
11:30   Marítimo x Tondela | https://v2.sportsonline.so/channels/pt/sporttv5.php
12:00   Al Feiha x Al Nassr | https://v2.sportsonline.so/channels/bra/br4.php
13:00   Lecce x Torino | https://v2.sportsonline.so/channels/pt/sporttv2.php
13:30   Wolverhampton Wanderers x Newcastle United | https://v2.sportsonline.so/channels/bra/br5.php
13:30   RB Leipzig x Köln | https://v2.sportsonline.so/channels/pt/eleven2.php
13:30   Mallorca x Getafe | https://v2.sportsonline.so/channels/pt/eleven3.php 
14:00   Benfica x Casa Pia | https://v2.sportsonline.so/channels/pt/btv.php
14:00   Vitória Guimarães x Chaves | https://v2.sportsonline.so/channels/pt/sporttv1.php
14:15   F1: Mexico City Practice 3 | https://v2.sportsonline.so/channels/bra/br4.php
15:30   Criciúma x Sampaio Corrêa | https://v2.sportsonline.so/channels/bra/br1.php
15:30   Ituano x Mirassol | https://v2.sportsonline.so/channels/bra/br2.php
15:45   Juventus x Hellas Verona | https://v2.sportsonline.so/channels/bra/br5.php
16:00   Cádiz x Sevilla | https://v2.sportsonline.so/channels/pt/eleven1.php
16:00   Lens x Nantes | https://v2.sportsonline.so/channels/pt/eleven2.php
16:00   Rugby World Cup: New Zealand x South Africa | https://v2.sportsonline.so/channels/pt/sporttv3.php
16:30   Gil Vicente x Sporting Braga | https://v2.sportsonline.so/channels/pt/sporttv1.php
16:30   F1: Mexico City Qualifying | https://v2.sportsonline.so/channels/bra/br4.php
16:30   NASCAR Xfinity Series: Dead on Tools 250 - Martinsville Raceway | https://v2.sportsonline.so/channels/pt/sporttv5.php
17:00   Fortaleza x LDU Quito | https://v2.sportsonline.so/channels/bra/br3.php
20:00   Boca Juniors x Estudiantes | https://v2.sportsonline.so/channels/bra/br5.php
20:00   Palmeiras x Bahia | https://v2.sportsonline.so/channels/bra/br1.php
20:00   América Mineiro x Grêmio | https://v2.sportsonline.so/channels/bra/br2.php
20:00   NBA: New York Knicks @ New Orleans Pelicans | https://v2.sportsonline.so/channels/pt/sporttv1.php
20:30   NBA: Indiana Pacers @ Cleveland Cavaliers | https://v2.sportsonline.so/channels/pt/sporttv3.php
21:00   Atlético Mineiro x Fluminense | https://v2.sportsonline.so/channels/bra/br3.php
00:15   Moto3: Grand Prix Of Thailand | https://v2.sportsonline.so/channels/bra/br5.php
"""

# Divide as linhas em uma lista
linhas = lista_texto.strip().split('\n')

# Loop através das linhas e gere o formato desejado
for linha in linhas:
    partes = linha.split('|')
    horario_equipe = partes[0].strip()
    link = partes[1].strip()

    # Imprima o formato desejado
    print(f'<button style="width: 95%; margin: 10px; font-size: 20px; font-weight: bold;" class="waves-effect waves-light btn-large" onclick="openMovie(\'{horario_equipe}\', \'{link}\')">{horario_equipe}</button>')
