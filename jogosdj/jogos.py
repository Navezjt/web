# Sua lista de texto
lista_texto = """
02:00   Moto2: Grand Prix Of Thailand | https://v2.sportsonline.so/channels/bra/br5.php
03:30   MotoGP: GP of Thailand | https://v2.sportsonline.so/channels/bra/br5.php
04:00   DP World Tour: Qatar Masters - D4 | https://v2.sportsonline.so/channels/pt/sporttv3.php
07:00   Academico Viseu x Nacional | https://v2.sportsonline.so/channels/pt/sporttv1.php
07:00   WRC: Central European Rally - Power Stage | https://v2.sportsonline.so/channels/pt/sporttv5.php
07:30   Cagliari x Frosinone | https://v2.sportsonline.so/channels/pt/sporttv2.php 
08:00   Brest x PSG | https://v2.sportsonline.so/channels/bra/br3.php
09:00   West Ham United x Everton | https://v2.sportsonline.so/channels/bra/br2.php
09:00   ATP World Tour 500: Vienna - Final | https://v2.sportsonline.so/channels/pt/sporttv3.php
09:30   PSV x Ajax | https://v2.sportsonline.so/channels/pt/sporttv1.php
10:00   Liverpool x Nottingham Forest | https://v2.sportsonline.so/channels/bra/br3.php
10:00   Brighton & Hove Albion x Fulham | https://v2.sportsonline.so/channels/pt/eleven3.php 
10:00   Aston Villa x Luton Town | https://v2.sportsonline.so/channels/bra/br5.php
10:00   Monza x Udinese | https://v2.sportsonline.so/channels/pt/sporttv2.php
10:30   Eintracht Frankfurt x Borussia Dortmund | https://v2.sportsonline.so/channels/bra/br4.php
10:30   ATP World Tour 500: Basel - Final | https://v2.sportsonline.so/channels/pt/sporttv5.php
11:30   Manchester United x Manchester City | https://v2.sportsonline.so/channels/bra/br2.php
11:30   Rio Ave x Farense | https://v2.sportsonline.so/channels/pt/sporttv1.php
11:30   Santa Clara x Benfica B | https://v2.sportsonline.so/channels/pt/sporttv3.php
12:05   Rennes x Strasbourg | https://v2.sportsonline.so/channels/pt/eleven3.php 
12:30   Bayer Leverkusen x Freiburg | https://v2.sportsonline.so/channels/bra/br4.php
13:00   Internazionale x Roma | https://v2.sportsonline.so/channels/bra/br3.php
14:00   Estrela x Famalicão | https://v2.sportsonline.so/channels/pt/sporttv1.php
14:00   UD Oliveirense x União de Leiria | https://v2.sportsonline.so/channels/pt/sporttv3.php
14:00   NASCAR Cup Series: Xfinity 500 - Martinsville | https://v2.sportsonline.so/channels/pt/sporttv5.php
15:00   Goiás x Vasco da Gama | https://v2.sportsonline.so/channels/bra/br1.php
15:00   Athletico-PR x São Paulo | https://v2.sportsonline.so/channels/bra/br2.php
15:45   Olympique Marseille x Olympique Lyonnais | https://v2.sportsonline.so/channels/bra/br5.php
15:45   Napoli x Milan | https://v2.sportsonline.so/channels/bra/br3.php
16:00   Atlético Madrid x Deportivo Alavés | https://v2.sportsonline.so/channels/pt/eleven1.php
16:00   F1: Mexico City Grand Prix | https://v2.sportsonline.so/channels/bra/br4.php
16:30   Vizela x Porto | https://v2.sportsonline.so/channels/pt/sporttv1.php
17:30   Gimnasia La Plata x River Plate | https://v2.sportsonline.so/channels/pt/sporttv3.php
17:30   Corinthians x Santos | https://v2.sportsonline.so/channels/bra/br1.php
17:30   Internacional x Coritiba | https://v2.sportsonline.so/channels/bra/br2.php
19:00   Botafogo x Cuiabá | https://v2.sportsonline.so/channels/bra/br3.php
19:30   NBA: Portland Trail Blazers @ Philadelphia 76ers | https://v2.sportsonline.so/channels/pt/sporttv2.php
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
