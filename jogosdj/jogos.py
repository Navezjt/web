# Sua lista de texto
lista_texto = """
05:00   DP World Tour: Qatar Masters - D1 | https://v2.sportsonline.so/channels/pt/sporttv3.php
09:00   ATP World Tour 500: Basel | https://v2.sportsonline.so/channels/pt/sporttv2.php
09:00   WRC: Central European Rally - Super Special 1 | https://v2.sportsonline.so/channels/pt/sporttv4.php
10:00   Judo: Grand Slam of Abu Dhabi - D3 | https://v2.sportsonline.so/channels/pt/sporttv5.php
13:00   WRC: Central European Rally - Super Special 2 | https://v2.sportsonline.so/channels/pt/sporttv4.php
13:45   Olympiakos Piraeus x West Ham United | https://v2.sportsonline.so/channels/bra/br5.php
13:45   AZ x Aston Villa | https://v2.sportsonline.so/channels/bra/br3.php
13:45   Lille x Slovan Bratislava | https://v2.sportsonline.so/channels/pt/eleven3.php
13:45   Sturm Graz x Atalanta | https://v2.sportsonline.so/channels/pt/sporttv2.php
13:45   Olympique Marseille x AEK Athens | https://v2.sportsonline.so/channels/pt/sporttv3.php 
13:45   Raków Częstochowa x Sporting CP | https://v2.sportsonline.so/channels/bra/br2.php
15:00   Al Ittihad x Al Hazm | https://v2.sportsonline.so/channels/pt/sporttv4.php
16:00   Liverpool x Toulouse | https://v2.sportsonline.so/channels/bra/br1.php
16:00   Brighton & Hove Albion x Ajax | https://v2.sportsonline.so/channels/bra/br4.php
16:00   Bayer Leverkusen x Qarabağ | https://v2.sportsonline.so/channels/bra/br3.php
16:00   Aberdeen x PAOK | https://v2.sportsonline.so/channels/pt/eleven3.php
16:00   Roma x Slavia Praha | https://v2.sportsonline.so/channels/bra/br5.php
19:00   Vasco da Gama x Internacional | https://v2.sportsonline.so/channels/bra/br1.php
19:00   Vasco da Gama x Internacional | https://v2.sportsonline.so/channels/bra/br2.php
19:00   ABC x Avaí | https://v2.sportsonline.so/channels/bra/br3.php
20:30   NBA: Philadelphia 76ers @ Milwaukee Bucks | https://v2.sportsonline.so/channels/pt/sporttv2.php
21:20   NFL: Tampa Bay Buccaneers @ Buffalo Bills | https://v2.sportsonline.so/channels/pt/eleven1.php
21:30   Santos x Coritiba | https://v2.sportsonline.so/channels/bra/br1.php
21:30   Santos x Coritiba | https://v2.sportsonline.so/channels/bra/br2.php
23:00   MotoGP: GP of Thailand FP1 | https://v2.sportsonline.so/channels/bra/br5.php
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
