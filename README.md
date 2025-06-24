# Prezentarea Aplicației de Editare a Imaginilor

Ecranul principal al aplicației de editare a imaginilor conține o interfață grafică simplă și intuitivă, construită folosind biblioteca **Tkinter** în limbajul de programare **Python**. Acest ecran este împărțit în două secțiuni principale: un **panou de comenzi** localizat în partea stângă și o **zonă de vizualizare** a imaginilor în partea dreaptă.

![Interfața principală a aplicației](https://github.com/user-attachments/assets/2c11a315-3c4d-4528-838e-f8eb646eeb53)

## Panoul de Comenzi

Panoul de comenzi conține butoane pentru funcționalitățile cheie ale aplicației. Aceste butoane includ:

*   **Încărcarea Imaginilor:** Folosind butonul cu iconița "Adaugă imagine", utilizatorul poate selecta și încărca o imagine din sistemul de fișiere.
*   **Oglindirea Imaginilor:** Butonul cu iconița "Oglindire" permite utilizatorului să inverseze imaginea pe orizontală.
*   **Rotirea Imaginilor:** Butoanele "Rotire la stânga" și "Rotire la dreapta" permit rotirea imaginii cu 90 de grade în sensul acelor de ceasornic sau în sens opus.
*   **Selectarea Culorii Penei:** Utilizatorul poate alege culoarea pentru instrumentul de desenare folosind butonul cu iconița "Culoare".
*   **Instrumentul de Desenare:** Butoanele "Desenare" și "Ștergere" activează și dezactivează instrumentul de desenare, permițând adăugarea sau ștergerea de linii pe imagine.
*   **Revenirea la poza inițială:** Acest buton anulează toate modificările, fără a fi nevoie să reîncărcați imaginea.
*   **Salvare:** Butonul cu iconița "Salvare" oferă posibilitatea de a salva imaginea editată într-un fișier.

## Filtre și Efecte

Ecranul principal oferă și o gamă variată de filtre și efecte pe care utilizatorii le pot aplica imaginilor încărcate:

*   **Alb și Negru:** Convertește imaginea color într-una alb-negru, păstrând doar intensitățile luminoase.
*   **Blurring (Estompare):** Creează un efect de estompare, reducând detaliile și oferind un aspect general neted.
*   **Afișare Detaliată (Detaliat):** Accentuează detaliile din imagine, evidențiind texturile și muchiile obiectelor.
*   **Estompare Fină (Fin):** Aplică un efect de estompare subtil, reducând contrastul și evidențiind tonurile uniforme.
*   **Emboss (În Relief):** Adaugă un efect de relief imaginii, conferind un aspect tridimensional.
*   **Îmbunătățire a Marginilor:** Accentuează marginile din imagine, sporind claritatea acestora.
*   **Contur:** Evidențiază contururile obiectelor, conferind un aspect grafic distinct.

![Demonstrație filtre pe imagine](https://github.com/user-attachments/assets/ae2ca10d-191b-4a7d-97f7-2362650b160c)

## Zona de Vizualizare

Zona de vizualizare a imaginilor este situată în partea dreaptă a ecranului. Aici, imaginea încărcată este afișată într-un **canvas**, iar utilizatorul poate vedea efectele modificărilor aplicate **în timp real**. Această zonă oferă o experiență interactivă, permițând utilizatorului să vizualizeze și să lucreze cu imaginea în timp ce explorează diferitele funcționalități ale aplicației.

În general, ecranul principal al aplicației îmbină utilitatea și accesibilitatea, facilitând utilizatorilor editarea și vizualizarea imaginilor într-un mod eficient și prietenos.
