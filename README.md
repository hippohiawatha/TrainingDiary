# TrainingDiary

TrainingDiary on perinteisen vihon korvaava kuntosaliharjoitusten merkitsemiseen käytettävä sivusto.
TD tarjoaa myös helpomman tavan seurata ja tilastoida esim. omia ennätyksiään. 

### Nykytilanne/käyttöohjeita:

Rekisteröidy tai kirjaudu sivulle. Kirjauduttuasi voit lisätä treeniohjelmia, mutta vain penkkiohjelmien lisäys toimii tällä hetkellä. 
Treenihistorian sivu listaa käyttäjän treenit, mutta treenien linkit johtavat toistaiseksi vain tyhjälle sivulle.

Jonkin verran puuttuu myös perus checkejä. Esim. jos yrität mennä uuden treenin sivulle ilman, että olet kirjautunut sisään, niin saat vain internal server errorin. Jokin verran olen yrittänyt näitä korjata, mutta voi olla että jotain on jäänyt.

### WIP:

##### Tärkeimmät:

- Ainakin maastaveto- ja kyykkytreenien lisäämisen implementointi.
- Yleinen arkkitehtuuri (tällä hetkellä esim. app.py täynnä tavaraa joka olisi hyvä laittaa muualle -> koodi ei kovin nättiä)
- Register formin voisi tehdä vähän järkevämmäksi, mutta toistaiseksi tämä ihan perus riittää.
- Treenihistorian implementointi

##### Jatkokehitys:

- Lisää vaihtoehtoja liikkeille (ehkä joku add custom, eikä vain predefined)
- Treeniohjelma (Smolov), johon voi laittaa omat painot saadakseen itselleen hyvän kyykky/penkki/maastaveto-ohjelman.
- Toiminto kavereiden kehityksen seuraamiseksi.
- Leaderboardit painoluokkien mukaan.

Voit kokeilla appia [täällä](https://tsoha-trainingdiary.herokuapp.com/)
