# Project 5

## Task

Given unigram models for 15 languages, build a naive Bayesian language identification model.

## Results

On the test set, the (non-verbose) results were:

```Predicted 'eng' for 'The scope of the discipline of statistics broadened in the early 19th century to include the collection and analysis of data in general.'
Predicted 'gla' for 'C? go bhfuil an chuma air nach f?idir ruda? deimhneacha a r? faoi eachtra? randamacha, le coincheap na d?ch?lachta, is f?idir a r? cad ? an seans go dtarl?idh eachtra f?nach agus mar sin, is f?idir cur s?os a dh?anamh ar an gc?ras.'
Predicted 'pol' for 'Na przyklad wzrost czlowieka jest uwarunkowany ogromna iloscia czynnik?w, takich jak genetyka, dieta, srodowisko, przy czym niekt?re z nich r?wniez maja losowa nature.'
Predicted 'ita' for 'approccio i dati risultati da un esperimento vengono indagati attraverso metodi di sintesi al fine di formulare ipotesi riguardo la legge di probabilit? sottesa'
Predicted 'spa' for 'dedica a la generaci?n de los modelos, inferencias y predicciones asociadas a los fen?menos en cuesti?n teniendo en cuenta lo aleatorio e incertidumbre en las observaciones. Se usa para modelar patrones en los datos'
Predicted 'fra' for 'Cette distinction ne consiste pas ? d?finir plusieurs domaines ?tanches. En effet, le traitement et l'interpr?tation des donn?es ne peuvent se faire que lorsque celles-ci ont ?t? r?colt?es.'
Predicted 'por' for 'Porque o objetivo da estat?stica ? a produ??o da melhor informa??o poss?vel a partir dos dados dispon?veis, alguns autores sugerem que a estat?stica ? um ramo da teoria da decis?o.'
Predicted 'dut' for 'Door de tweeledigheid van populatie en steekproef ontstaat veel verwarring. Men dient steeds goed te onderscheiden of men over de populatie (verdeling) spreekt dan wel over de steekproef.'
Predicted 'deu' for 'Die deskriptive Statistik (auch beschreibende Statistik oder empirische Statistik): mit der vorliegende Daten in geeigneter Weise beschrieben und zusammengefasst werden.'
Predicted 'nob' for 'Den er basert p? statistisk teori som er en gren av matematikk. Innenfor statistisk teori er tilfeldighet og usikkerhet utformet ved hjelp av sannsynlighetsteori.'
Predicted 'swe' for 'Ordet statistik kan dels avse datauppgifter som ofta presenteras i numerisk form, vanligen i tabeller eller diagram, dels vetenskapen om hur dessa datauppgifter skall samlas in, utv?rderas, analyseras och presenteras.'
Predicted 'dan' for 'Det kan v?re, at det er dyrt at lave m?lingerne eller, at det ikke er fysisk muligt at unders?ge mere end et udsnit af populationen. For eksempel er det ikke muligt at unders?ge alt vandet i verdenshavene.'
Predicted 'swh' for 'Hisabati ni somo inayohusika na idadi, upimaji na ukubwa. Kwa ujumla ni somo inayohusika na miundo na vielezo. Hisabati inatimiza somo mbalimbali, kama hesabu, jiometria na aljebra.'
Predicted 'tgl' for 'na nanggaling ang salitang Italyano na statista, na nangangahulugang "dalubhasa sa pagpapalakad ng pamahalaan" o "pulitiko", at ang Aleman na Statistik, sa orihinal na kahulugan, ang pagpipili ng pagsusuri ng datos tungkol sa estado.'
Predicted 'fin' for 'Aineistoa on tavallisesti mahdollista ker?t? vain populaation osajoukosta, jolloin tutkimuksen kohteena on otos. Otoksesta voidaan ker?t? aineistoa joko havainnoiden tai kokeellisessa asetelmassa.'
Predicted 'swh' for 'Palikuwa pia na vipindi na utamaduni ambako wapiganaji walikuwa watu wa pekee wenye jukumu hii ama kwa sababu walipaswa kuwa askari kufuatana na sheria za nchi au kwa sababu walikodiwa kwa kazi hii.'
Predicted 'por' for 'considera-se o estado "ideal" de guerra, ou seja, uma guerra em que prevalece a diplomacia, a estrat?gia e a racionalidade, n?o havendo inspira??o de ordem emocional ou moralista.'
Predicted 'dut' for 'Vanaf het begin is oorlog voeren al onderworpen geweest aan wetten en reglementen, al zijn die in de loop der tijd wel veranderd. Er is met name veel nagedacht over de rechtvaardiging van een oorlog.'
Predicted 'spa' for 'El concepto de qui?nes son los combatientes tambi?n var?a con el grado de organizaci?n de las sociedades enfrentadas. Las dos posibilidades m?s frecuentes son civiles sacados de la poblaci?n general, generalmente varones j?venes,'
Predicted 'gla' for 'Bhris an cogadh amach sa bhliain 1775 nuair a ghlac na r?abhl?idithe seilbh ar na rialtais i ngach coil?neacht agus chuireadar an Dara Chomhdh?il Ilchr?ochach agus an tArm Ilchr?ochach nua ar bun.'
Predicted 'fra' for 'la guerre ?conomique pouvant alors, sous une apparence plus socialement et ?thiquement acceptable, satisfaire d'autres app?tits de pouvoirs que ceux qui animaient les auteurs des guerres ethniques, de religions, de classe,'
Predicted 'swe' for 'Kriget framtr?der antingen som f?rsvarskrig, till avv?rjande av framst?llda anspr?k, som ej kan godtas, eller anfallskrig, som avser att framtvinga s?dana anspr?ks godk?nnande:'
Predicted 'tgl' for 'Karamihan sa mga isla dito ay mabundok, at ang iba ay may mga bulkan, kabilang na ang pinakamataas na bahagi ng bansa, Ang Hapon ay pangsampu sa may pinakamalaking populasyon, na may 128 milyong katao.'
Predicted 'eng' for 'For a state to prosecute a war it must have the support of its leadership, its military forces, and the population. For example, in the'
Predicted 'ita' for 'Si giunge alla guerra quando il contrasto di interessi economici, ideologici, strategici o di altra natura non riesce a trovare una soluzione negoziata, o quando almeno una delle parti percepisce l'inesistenza di altri mezzi per il conseguimento'
Predicted 'dan' for 'Krig kan defineres som, erkl?rede fjendtlige handlinger mellem to eller flere lande eller stater. ?rsagerne til krig kan v?re mange, for eksempel: ?nske om at udvide landet,'
Predicted 'pol' for 'Wojna jest zjawiskiem spoleczno-politycznym i jako takie jest obecna w historii czlowieka od poczatk?w jego spolecznej organizacji. Zasieg wojny jest zalezny od stopnia rozwoju technologicznego.'
Predicted 'deu' for 'W?hrend individuelles oder kollektives Rauben und absichtliches T?ten von Menschen heute generell als Verbrechen gilt und in einem Rechtsstaat strafbar ist, wird "Krieg" nicht als gew?hnliche Kriminalit?t betrachtet,'
Predicted 'fin' for 'Tavoitteellisuus tekee sodasta poliittista toimintaa. Jos tavoitteisiin p??st??n neuvottelemalla tai sodan uhalla, ei kalliiseen taisteluun ole tarvetta. Vihollisen taistelukyky voidaan poistaa tappamalla ja vangitsemalla sen johtajat ja riisumalla sen armeija aseista.'
Predicted 'nob' for 'Fysisk styrke og v?pen har i uminnelige tider v?rt brukt som et maktmiddel i konflikter mellom mennesker. Et organisert milit?rvesen av et eller annet slag har derfor v?rt et viktig del av maktapparatet'
```

## Approach

I created models for each language where the probability of drawing a word from that language is the count divided by
the total number of words in the unigram model. I assigned words out-of-vocabulary a sampling probability of the
rarest word in each vocabulary.

## Tools

For this project, I used primarily the Python standard library with the exception of a few helper libraries:

- Numpy, a mathematical library for Python

## Testing

The model correctly outputs all training predictions and test predictions validated by Google Translate.

## To do

Extra credit language model could be improved by adding a character n-gram prediciton model and by filtering out most common and most rare words, which tend to be noisy.
