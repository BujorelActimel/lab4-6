## P5. Administrator de bloc

Creați o aplicație pentru gestiunea cheltuielilor lunare de la apartamentele unui bloc de locuințe. Aplicația stochează cheltuielile pentru fiecare apartament: suma și tipul cheltuielii (tip poate fi una dintre: apa, canal, încălzire, gaz, altele). Aplicația permite:

1. **Adăugare**
    - Adaugă cheltuială pentru un apartament
    - Modifică cheltuială

2. **Ștergere**
    - Șterge toate cheltuielile de la un apartament
    - Șterge cheltuielile de la apartamente consecutive (Ex. se dau două numere de apartament 2 și 5 și se șterg toate cheltuielile de la apartamentele 1,2,3,4 și 5)
    - Șterge cheltuielile de un anumit tip de la toate apartamentele

3. **Căutări**
    - Tipărește toate apartamentele care au cheltuieli mai mari decât o sumă dată
    - Tipărește cheltuielile de un anumit tip de la toate apartamentele
    - Tipărește toate cheltuielile efectuate înainte de o zi și mai mari decât o sumă (se dă suma și ziua)

4. **Rapoarte**
    - Tipărește suma totală pentru un tip de cheltuială
    - Tipărește toate apartamentele sortate după un tip de cheltuială
    - Tipărește totalul de cheltuieli pentru un apartament dat

5. **Filtru**
    - Elimină toate cheltuielile de un anumit tip
    - Elimină toate cheltuielile mai mici decât o sumă dată

6. **Undo**
    - Reface ultima operație (lista de cheltuieli revine la ce exista înainte de ultima operație care a modificat lista). – Nu folosiți funcția deepCopy
