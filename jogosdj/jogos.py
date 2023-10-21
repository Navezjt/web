# Sua lista de texto
lista_texto = """
10:30   Wolfsburg x Bayer Leverkusen | https://v2.sportsonline.so/channels/bra/br1.php
11:00   Manchester City x Brighton & Hove Albion | https://v2.sportsonline.so/channels/bra/br3.php
11:00   Newcastle United x Crystal Palace | https://v2.sportsonline.so/channels/bra/br2.php
11:15   Getafe x Real Betis | https://v2.sportsonline.so/channels/pt/eleven3.php
12:00   Al Nassr x Dhamk | https://v2.sportsonline.so/channels/bra/br5.php
13:00   Torino x Internazionale | https://v2.sportsonline.so/channels/pt/sporttv2.php
13:00   UFC 294: Prelims | https://v2.sportsonline.so/channels/bra/br4.php
13:30   Chelsea x Arsenal | https://v2.sportsonline.so/channels/bra/br2.php
13:30   Sevilla x Real Madrid | https://v2.sportsonline.so/channels/bra/br3.php
13:30   Mainz 05 x Bayern München | https://v2.sportsonline.so/channels/bra/br1.php
14:00   F1: USA Sprint Shootout | https://v2.sportsonline.so/channels/pt/sporttv4.php
15:00   Al Ahli x Al Wahda | https://v2.sportsonline.so/channels/bra/br5.php
15:00   UFC 294: Alexander Volkanovski vs Islam Makhachev | https://v2.sportsonline.so/channels/bra/br4.php
15:00   Rugby World Cup: England x South Africa | https://v2.sportsonline.so/channels/pt/sporttv3.php
15:45   Sassuolo x Lazio | https://v2.sportsonline.so/channels/pt/sporttv4.php
16:00   Sheffield United x Manchester United | https://v2.sportsonline.so/channels/bra/br2.php
16:00   Celta de Vigo x Atlético Madrid | https://v2.sportsonline.so/channels/pt/eleven2.php
16:00   Nice x Olympique Marseille | https://v2.sportsonline.so/channels/pt/eleven3.php
16:45   CD Olivais e Moscavide x Sporting | https://v2.sportsonline.so/channels/pt/sporttv1.php
18:15   F1: USA Sprint | https://v2.sportsonline.so/channels/pt/sporttv4.php
18:30   São Paulo x Grêmio | https://v2.sportsonline.so/channels/bra/br1.php
18:30   Bahia x Fortaleza | https://v2.sportsonline.so/channels/bra/br2.php
18:30   Cuiabá x Goiás | https://v2.sportsonline.so/channels/bra/br3.php
20:15   Moto3: GP of Australia | https://v2.sportsonline.so/channels/bra/br4.php
21:00   Botafogo x Athletico-PR | https://v2.sportsonline.so/channels/bra/br1.php
21:00   Botafogo x Athletico-PR | https://v2.sportsonline.so/channels/bra/br2.php
22:00   Moto2: GP of Australia | https://v2.sportsonline.so/channels/bra/br4.php
23:30   MotoGP: GP of Australia | https://v2.sportsonline.so/channels/bra/br4.php
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
