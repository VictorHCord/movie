# -*- coding: utf-8 -*-
import media
import fresh_tomatoes

''' Filmes / Movies '''

Animais = media.Movie("Animais fantasticos",
                     "2h 30m",
                      "16/11/2018",
                     "O Mundo Bruxo que você conhece, a história que você ainda não sabe",
                     "https://www.youtube.com/watch?v=YNskLKO_FzE&t=6s",
                     "https://upload.wikimedia.org/wikipedia/pt/2/25/Fantastic_Beasts_The_Crimes_of_Grindelwald.jpg")


infinitywar = media.Movie("Animais fantasticos",
                     "2h 40m",
                      "26/04/2018",
                     "Thanos (Josh Brolin) enfim chega à Terra, disposto a reunir as Joias do Infinito",
                     "https://www.youtube.com/watch?v=6ZfuNTqbHE8&t=1s",
                     "http://t2.gstatic.com/images?q=tbn:ANd9GcS4neC_Y4U1G6u2QlEFqbCizheGBUnZg1w874qWbIcVlv9tPuSu")


logan = media.Movie("Logan",
                     "2h 21m",
                      "02/03/2017",
                     "Em um futuro próximo, um cansado Logan cuida do doente Professor Xavier.",
                     "https://www.youtube.com/watch?v=KPND6SgkN7Q",
                     "http://t0.gstatic.com/images?q=tbn:ANd9GcR_k0ShtzP-2rhzHtF30v9DiH0bgSogYU99juiiDna_oQEgo2dx")




''' Tv Series '''

mrrobot = media.Movie("Mr Robot",
                        "n/a",
                        "n/a",
                        "Elliot é um jovem programador que trabalha como engenheiro de segurança virtual durante o dia.",
                        "https://www.youtube.com/watch?v=Xnv5pKJW34w",
                      "https://upload.wikimedia.org/wikipedia/en/9/95/MrRobot_intertitle.png")

movies = [Animais,infinitywar,logan,mrrobot]
fresh_tomatoes.open_movies_page(movies)
