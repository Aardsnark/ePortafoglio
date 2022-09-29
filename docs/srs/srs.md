### UniSkaven UniApp
##### ITS ICT - Gruppo di Lavoro 2

**VERSION : 0.1**

**Authors**  
Serena Schincaglia
Federico Zunino
Tiziano De Falco

**REVISION HISTORY**

| Version    | Date        | Authors      | Notes        |
| ----------- | ----------- | ----------- | ----------- |
|0.1| 25/09 | Serena, Federico, Tiziano | Update lista funzionalità e scenario 6 - 21 |
|0.1| 22/09 | Serena | Update Diagramma UML |
|0.1| 22/09 | Serena, Federico, Tiziano | Update lista funzionalità e scenario 1 to 5 |
|0.1| 22/09 | Federico Zunino | Creazione documento srs, update lista attori|

# Table of Contents

1. [User Case](#p1)
	1. [Diagramma](#sp1.1)
	2. [Attori](#sp1.2) 
	3. [Lista Funzionalità](#sp1.3)
2. [Scenari](#p2)
	1. [Login](#sp2.1)
	1.1 [Autenticazione](#sp2.1.1)
	2. [Consulta Lista Corsi](#sp2.2)
	3. [Lista Studenti iscritti al corso](#sp2.3)
	4. [Elenco Esami Attivi Corso](#sp2.4)
	5. [Aggiunta Esame Corso](#sp2.5)
	6. [Consulta Lista Corsi superati con relativa votazione](#sp2.6)
	7. [Consulta Lista Esami a cui è iscritto](#sp2.7)
	8. [Iscrizione Esami](#sp2.8)
	9. [Rimuovere iscrizione ad un Esame](#sp2.9)
	10. [Informazioni Account](#sp2.10)
	11. [Creazione dei dipartimenti](#sp2.11)
	12. [Creazione scheda personale docente](#sp2.12)
	13. [Modifica dell'ID dei docenti](#sp2.13)
	14. [Creazione profilo studente](#sp2.14)
	15. [Modifica dell'ID degli studenti](#sp2.15)
	16. [Creazione dei corsi di laurea](#sp2.16)
	17. [Creazione dei singoli insegnamenti](#sp2.17)
	18. [Elimina Esame](#sp2.18)
	19. [Aggiorna profilo utente](#sp2.19)
	20. [Aggiunte voto ad esame](#sp2.20)
	21. [Lista Studenti iscritti ad esame](#sp2.21)
	22. [](#sp2.22)

<a name="p1"></a>

## 1. User Case

<a name="sp1.1"></a>

### 1.1 Diagramma

![Diagramma UML](https://github.com/mnarizzano/M1.4.4-p2/blob/main/docs/srs/imgs/Es%20UniSkaven.png)

<a name="sp1.2"></a>

### 1.2 Attori

| Nome | Descrizione |
| ----------- | ----------- | 
|Studente| Utente frequentante i corsi di Skaven University che vuole iscriveri agli esami e consultare le informazioni sui corsi |
|Docente| Utente che insegna uno o più corsi a Skaven Univerisity, consulta le informazioni e gli elenchi dei corsi e assegna voti agli esami |
|Amministrazione| Utente generale dell'amministrazione che crea i corsi, i profili degl altri utenti e ne gestisce le info uniche, come l'ID |

<a name="sp1.3"></a>

### 1.3 Lista e Funzionalità 
| ID | Nome | Descrizione |
| ----------- | ----------- | ----------- | 
| 1 | Login | L'utente accede con credenziali valide al sistema |
| 2 | Consulta Lista Corsi | L'utente accede alla lista dei corsi a cui è iscritto |
| 3 | Lista Studenti iscritti al corso | L'utente può visualizzare l'elenco degli studenti iscritti al corso|
| 4 | Elenco Esami Attivi Corso | L'utente visualizza gli esami attivi per il corso selezionato |
| 5 | Aggiunta Esame Corso | L'utente aggiunge un appello al corso selezionato | 
| 6 | Consulta Lista Corsi superati | L'utente consulta la lista dei corsi che ha superato, con relativa votazione |
| 7 | Consulta Esami a cui è iscritto | L'utente accede alla lista degli esami a cui è iscritto e alle relative informazioni di ognuno |
| 8 | Iscrizione Esami | L'utente visualizza le date  degli appelli disponibili e si iscrive |
| 9 | Rimuovere iscrizione ad un Esame | L'utente si disiscrive da un esame a cui è iscritto |
| 10 | Informazioni Account | L'utente consulta le informazioni del suo profilo |
| 11 | Creazione dipartimento | L'utente crea un nuovo dipartimento |
| 12 | Creazione profilo docente | L'utente crea un nuovo profilo docente |
| 13 | Modifica dell'ID dei docenti | L'utente aggiorna l'ID del docente |
| 14 | Creazione profilo studente | L'utente crea un nuovo profilo studente |
| 15 | Modifica dell'ID degli studenti | L'utente aggiorna l'ID dello studente |
| 16 | Creazione corso di laurea | L'utente crea un nuovo corso di laurea |
| 17 | Creazione insegnamento | L'utente crea un nuovo insegnamento |
| 18 | Elimina Esame | L'utente elimina l'esame selezionato |
| 19 | Aggiorna profilo utente | L'utente aggiorna le sue info ad esclusione dell'ID |
| 20 | Aggiunte voto ad esame | L'utente aggiunge la votazione all'esame di uno studente |
| 21 | Lista Studenti iscritti ad esame | L'utente accede alla lista degli studenti iscritti ad un esame |
| 22 |  |  |

<a name="p2"></a>

## Scenari

<a name="sp2.1"></a>

### 2.1 Login

| ID: 1 | <u>Login</u> |
| ----------- | ----------- | 
| Attore | Docente, Studente, Amministrazione |
| Tipo | Primario | 
| Precondizione | L'utente ha delle credenziali uniche e personali valide per il sistema |
| Scenario Principale | |
| 1. | L'utente inserisce la sua ID |
| 2. | L'utente inserisce la password |
| 3. | Il Sistema conferma che che la combinazione delle credenziali è valida e corrisponde ad un utente | 
| 4. | Il sistema scarica o aggiorna il certificato di autenticazione |
| Postcondizione: | L'utente ha accesso al sistema |
| 3a | Scenario Alternativo: Autneticazione non valida |
| 1. | Il sistema segnala che non esiste un account per l'ID inserito |
| 2. | Il sistema suggerisce di contattare l'Amministrazione per la creazione di un account |
| 3. | Il sistema ritorna al punto 1 principale |
| 3b | Scenario Alternativo: L'utente inserisce la password non corretta < 3 volte |
| 1. | Il sistema notifica che la password non è valida e invita a digitarla di nuovo |
| 2. | Il sistema incrementa il counter dei fallimenti |
| 3. | Il sistema torna al punto 2 principale |
| 3c | Scenario Alternativo: L'utente inserisce la password non valide per la terza volta |
| 1. | Il sistema notifica che la password è errata per la terza volta |
| 2. | Il sistema blocca l'account e invia una mail di sblocco all'utente |
| 3. | Il sistema invita l'utente ad aggiornare la password dalla mail |

<a name ="sp2.1.1"></a>

| ID: 1.1 | Autenticazione (Opzionale se pre-condizione è semplicemente "avere un certificato valido") |
| ----------- | ----------- | 
| Attore | Docente, Studente, Amministrazione (Principale) |
| Tipo | Secondario | 
| Precondizione | |
| Scenario Principale | |
| 1. | Il sistema controlla che la password ed ID siano valide e corrispondano ad un utente |
| 2. | Il sistema autentica le credenziali |
| 3. | Il sistema rilascia o aggiorna il certificato di autenticazione |
| Postcondizione: | L'utente è autentificato |
|| Scenario Alternativo: Certificato Scaduto |
|| Scenario Alternativo: Certificato Non Valido |


<a name="sp2.2"></a>

### 2.2 Consulta Lista Corsi

| ID: 2 | <b>Consulta Lista Corsi</b> |
| ----------- | ----------- | 
| Attore | Docente (Principale), Studente (Principale) |
| Tipo | Primario |
| Precondizione | L'utente ha un certificato di autenticazione valido; l'utente è autorizzato ad accedere ai corsi |
| Scenario Principale | |
| 1. | L'Utente seleziona l'anno scolastico |
| 2. | Il Sistema riporta i corsi di quell'anno per cui il docente è registrato |
| 3. | L'Utente clicca sul corso che vuole esaminare |
| 4. | Il sistema mostra le informazioni identificative del corso |
| Postcondizione | L'Utente ha accesso alle informazioni del corso specificato |

<a name="sp2.3"></a>

### 2.3 Lista Studenti iscritti al corso

| ID: 3 | <b>Lista Studenti iscritti al corso </b> |
| ----------- | ----------- | 
| Attore | Docente (Principale), Amministrazione (Principale) |
| Tipo | Primario | 
| Precondizione | L'utente ha un certificato di autenticazione valido; Il Docente insegna il corso dell'esame |
| Scenario Principale | |
| 1. | Il Docente seleziona il corso |
| 2. | Il Docente sceglie l'opzione "Mostra Studenti Iscritti" |
| 3. | Il Sistema fornisce l'elenco degli studenti iscritti al corso |
| Postcondizione: | Il docente ha accesso alla lista degli studenti iscritti ad un corso |


<a name="sp2.4"></a>

### 2.4 Elenco Esami Attivi Corso

| ID: 4 | <b>Elenco Esami Attivi Corso</b> |
| ----------- | ----------- | 
| Attore | Docente (Principale) |
| Tipo | Primario | 
| Precondizione | L'utente ha un certificato di autenticazione valido; Il Docente insegna il corso dell'esame |
| Scenario Principale | |
| 1. | Il Docente selezione il corso |
| 2. | Il Docente clicca su opzione "Lista Esami Corso" |
| 3. | Il Sistema mostra la lista degli esami del corso. |
| Postcondizione: | Il Docente visualizza la lista degli esami attivi |

<a name="sp2.5"></a>

### 2.5 Aggiunta Esame Corso

| ID: 5 | <b>Aggiunta Esame Corso</b> |
| ----------- | ----------- | 
| Attore | Docente (Principale) |
| Tipo | Primario | 
| Precondizione | L'utente ha un certificato di autenticazione valido; Il Docente insegna il corso dell'esame |
| Scenario Principale | |
| 1. | L'utente visualizza la lista esami del corso |
| 2. | L'utense sceglie l'opzione "Aggiungi Esame" |
| 3. | L'utente inserisce la data/le date dell'appello |
| 4. | L'utente salva le informazioni |
| 5. | Il Sistema notifica la creazione dell'appello |
| 6. | Il Sistema invia una mail a tutti gli iscritti al corso |
| Postcondizione: | L'esame per il corso è stato creato |


<a name="sp2.6"></a>

### 2.6 Consulta Corsi superati con relativa votazione

| ID: 6 |<b>Consulta Corsi superati con relativa votazione</b>|
| ---------- | ------------|
| Attore | Studente (Principale) |
| Tipo | Primario |
| Precondizione |L'utente ha un certificato di autenticazione valido; Lo studente è iscritto all'università |
| Scenario principale | |
| 1. | L'utente visualizza la lista dei corsi |
| 2. | L'utense sceglie l'opzione "Visualizza corsi superati" |
| 3. | L'utense sceglie l'opzione "Visualizza votazione" del corso desiderato |
| Postcondizione: | Lo studente visualizza la lista dei corsi superati |

<a name="sp2.7"></a>

### 2.7 Consulta Esami a cui è iscritto

| ID: 7 |<b>Consulta Esami a cui è iscritto</b> |
| ---------- | ------------|
| Attore | Studente (Principale)|
| Tipo | Primario|
| Precondizione | L'utente ha un certificato di autenticazione valido; l'utente è autorizzato ad accedere ai corsi |
| Scenario Principale | |
| 1. | L'Utente seleziona l'anno scolastico |
| 2. | Il Sistema riporta gli esami di quell'anno per cui lo studente è iscritto |
| 3. | L'Utente clicca sull'esame che vuole esaminare |
| 4. | Il sistema mostra le informazioni identificative dell'esame |
| Postcondizione | L'Utente ha accesso alle informazioni dell'esame specificato |

<a name="sp2.8"></a>

### 2.8 Iscrizione Esami

| ID: 8 |<b>Iscrizione Esami</b> |
| ---------- | ------------|
| Attore | Studente (Principale)|
| Tipo | Primario|
| Precondizione | L'utente ha un certificato di autenticazione valido; Lo stuente è iscritto al corso dell'esame |
| Scenario Principale | |
| 1. | L'utente visualizza la lista esami del corso |
| 2. | L'utense sceglie l'opzione "Aggiungi Esame" |
| 4. | L'utente visualizza la data/le date dell'appello |
| 5. | L'utente conferma l'iscrizione |
| 6. | Il Sistema notifica all'utente l'iscrizione all'appello |
| 6. | Il Sistema invia una mail al docente del corso |
| Postcondizione: | Lo studente è iscritto all'esame |

<a name="sp2.9"></a>

### 2.9 Rimuovere iscrizione ad un Esame

|ID: 9 |<b>Rimuovere iscrizione ad un Esame</b> |
| ---------- | ------------|
| Attore | Studente (Principale) |
| Tipo | Primario|
| Preconzione | L'utente ha un certificato di autenticazione valido; Lo studente è iscritto al corso dell'esame |
| Scenario Principale | |
| 1. | L'utente visualizza la lista esami del corso |
| 2. | L'utense sceglie l'opzione "Visualizza Esame" |
| 3. | L'utente sceglie l'opzione "Rimuovi Esame" |
| 5. | L'utente conferma la disiscrizione |
| 6. | Il Sistema notifica l'iscrizione all'appello |
| 6. | Il Sistema invia una mail al docente del corso |
| Postcondizione: | Lo studente ha rimosso l'iscritto all'esame |

<a name="sp2.10"></a>

### 2.10 Informazioni Account

| ID: 10 |<b>Informazioni Account</b> |
| ---------- | ------------|
| Attore | Studente (Principale), Docente(Principale) |
| Tipo | Primario|
| Precondizione | L'utente ha un certificato di autenticazione valido; l'utente è iscritto all'università |
| Scenario Principale | |
| 1. | L'utente sceglie l'opzione "visualizza account" |
| 2. | L'utente può consultare le sue informazioni |
| 3. | L'utente può modificare o lasciarle invariate |
| 5. | L'utente salva le informazioni |
| Postcondizione | Lo studente verifica le informazioni di account|

<a name="sp2.11"></a>

### 2.11 Creazione dipartimenti
| ID: 11|<b>Creazione dipartimenti</b> |
| ---------- | ------------|
| Attore | Amministratore (Principale) |
| Tipo | Primario |
| Precondizione | L'utente ha un certificato di autenticazione valido |
| Scenario Principale | |
|1. | L'utente sceglie il modello Dipartimento |
|2. | L'utente per ogni Dipartimento istanzia i relativi Oggetti |
|3. | L'utente salva tutte le informazioni inserite |
|4. | L'utente verifica che i Dipartimenti creati corrispondano a quelli delle direttive di Ateneo |
| Postcondizione | L'utente ha creato un nuovo dipartimento |

<a name="sp2.12"></a>

### 2.12 Creazione Profilo Docente
| ID: 12|<b>Creazione Profilo Docente </b> |
| ---------- | ------------|
| Attore | Amministratore |
| Tipo | Primario |
| Precondizione | L'utente ha un certificato di autenticazione valido; l'utente ha creato la lista dei Dipartimenti |
| Scenario Principale | |
|1. | L'Amministratore crea la classe docente |
|2. | Il costruttore della classe docente acquisice i seguenti dati in input: {Nome, Cognome, Data di Nascita, Luogo di Nascita, Residenza, Codice Fiscale, Area            disciplinare, Insegnamenti attivi, Periodo di servizio, tipo di contratto, Conto corrente stipendio, Notizie di servizio, lista recapiti personali} |
|3. | L'amministratore assegna la scheda docente al Dipartimento prescelto |
|4. | L'Amministratore salva tutte le informazioni inserite |
|Postcondizione| Si ottiene l'organigramma del personale docente |
|Scenario secondario| problema nell'inserimento dei dati nei campi e coerenza dei dati |

<a name="sp2.13"></a>

### 2.13 Modifica ID docenti
| ID: 13|<b> Modifica dell'ID dei docenti </b> |
| ---------- | ------------|
| Attore | Amministratore |
| Tipo | Primario |
|Precondizione| L'utente ha un certificato di autenticazione valido; l'utente ha creato la lista dei Dipartimenti |
|Scenario principale| |
|1. | l'Amministratore cerca il docente in base al codice fiscale |
|2. | l'Amministratore può modificare le informazioni della scheda aggiornandole |
|3. | l'Amministratore può modificare le informazioni della scheda cancellandole |
|Postcondizione| Schedario personale aggiornato |
|Scenario secondario| Problemi nella sovrascrittura dei dati |

<a name="sp2.14"></a>

### 2.14 Creazione profilo studente
| ID: 14|<b> Creazione profilo studente </b> |
| ---------- | ------------|
| Attore | Amministratore |
| Tipo | Primario |
|Precondizione| L'utente ha un certificato di autenticazione valido |
|Scenario principale| |
|1. | l'Amministratore crea la classe studente |
|2. | Il costruttore della classe studente acquisisce i seguenti dati in input: {Nome, Cognome, Data di nascita, Luogo di Nascita, Residenza, Codice Fiscale, Lista           recapiti personali, Scuola superiore di provenienza, voto di diploma di maturità, Certificazione ISEE-U, Ricevuta pagamento iscrizione all'universita per l'a.a.,       Data di iscrizione all'a.a., Iscrizione al corso di Laurea offerto dall’Università, Piano di Studi per l’anno a.a. corrente} |
|3. | Per ogni aspirante universitario viene istanziato un oggetto di tipo studente |
|Postcondizione| la classe studente permette: il calcolo di tasse e benefici, l'assegnazione di una matricola, la creazione di una carriera universitaria, la         creazione del libretto universitario digitale |
|Scenario secondario| problema nell'inserimento dei dati nei campi e coerenza dei dati |
<a name="sp2.15"></a>

### 2.15 Modifica ID studenti
| ID: 15|<b> Modifica dell'ID degli studenti </b> |
| ---------- | ------------|
| Attore | Amministratore |
| Tipo | Primario |
|Precondizione| L'utente ha un certificato di autenticazione valido, l'utente ha creato un profilo studente |
|Scenario principale| |
|1. | l'Amministratore cerca studente tramite numero matricola
|2. | l'Amministratore può modificare le informazioni della scheda aggiornandole |
|3. | l'Amministratore può modificare le informazioni della scheda cancellandole |
|Postcondizione| Schedario studenti aggiornato |
|Scenario secondario| problemi nella sovrascrittura dei dati |
<a name="sp2.16"></a>

### 2.16 Creazione corso di laurea
| ID: 16|<b> Creazione corso di laurea </b> |
| ---------- | ------------|
| Attore | Amministratore |
| Tipo | Primario |
|Precondizione| L'utente ha un certificato di autenticazione valido |
| Scenario principale | |
|1. | Creazione di una classe Laurea |
|2. | Creati tanti oggetti quanti sono i corsi di laurea |
|Postcondizione| Si ottiene lista dei corsi di laurea, successivamente vanno inseriti gli insegnamenti |
|Scenario secondario| incogruenze con le direttive di Ateneo |

<a name="sp2.17"></a>

### 2.17 Creazione insegnamento
| ID: 17|<b> Creazione insegnamento </b> |
| ---------- | ------------|
| Attore | Amministratore (Principale) |
| Tipo | Primario |
|Precondizione| L'utente ha un certificato di autenticazione valido, l'utente ha creato i corsi di laurea |
|Scenario principale | |
|1. | Creazione di una classe insegnamento |
|2. | Il costruttore della classe insegnamento acquisisce i seguenti dati in input: {titolo, area disciplinare, codice, docente, CFU, ore totali, programma} |
|3. | Istanziati tanti oggetti insegnamento quanti sono gli insegnamenti offerti dall'Ateneo |
|4. | Ogni insegnamento va inserito nel corso di Laurea deciso dall'Ateneo |
|Postcondizione| Ogni corso di laurea ha la sua lista di insegnamenti |

<a name="p2.17"></a>

### 2.18 Elimina Esame
| ID: 18 | <b> Elimina Esame </b>  |
| ----------- | ----------- | 
| Attore | Docente(Primario) |
| Tipo | Primario | 
| Precondizione | L'utente ha un certificato di autenticazione valido, l'utente è inserito nel gruppo user "Docenti" |
| Scenario Principale | |
| 1. | L'utente seleziona Esame che desidera cancellare |
| 2. | L'utente seleziona opzione "Elimina Esame" |
| 3. | Il Sistema chiede conferma della scelta |
| 4. | L'utente da la conferma |
| 5. | Il Sistema da conferma dell'avvenuta cancellazione |
| Postcondizione: | L'esame scelto è stato cancellato |

<a name="p2.18"></a>

### 2.19 Aggiorna Profilo Utente
| ID: 19 | <b> Aggiorna Profilo Utente </b> |
| ----------- | ----------- | 
| Attore | Studente(Primario), Docente(Primario)|
| Tipo | Primario | 
| Precondizione | L'utente ha un certificato di autenticazione valido, l'utente ha un profilo attivo |
| Scenario Principale | |
| 1. | L'utente seleziona l'opzione "modifica informazioni" | 
| 2. | Il Sistema presenta le tab info che possono essere modificate (non ID) |
| 3. | L'utente aggiorna le informazioni che desidera modificare |
| 4. | L'utente salva le modifiche |
| 5. | Il Sistema notifica il successo nel salvataggio delle modifiche |
| 6. | Il Sistema riporta l'utente al riepilogo informazioni |
| Postcondizione: | L'utente ha modificato le sue info account |

<a name="p2.19"></a>

### 2.20 Aggiorna voto esame studente
| ID: 20 | <b> Aggiunta voto esame studente </b> |
| ----------- | ----------- | 
| Attore | Docente(Primario), Studente(Secondario)|
| Tipo | Primario | 
| Precondizione | L'utente ha un certificato di autenticazione valido, l'utente è inserito nel gruppo user "Docenti", l'utente è un docente per il corso d'esame |
| Scenario Principale | |
| 1. | L'utente seleziona il corso per cui lo studente ha sostenuto l'esame| 
| 2. | L'utente seleziona l'appello che lo studento ha sostenuto |
| 3. | L'utente seleziona lo studente a cui aggiungere il voto |
| 4. | L'utente inserisce il voto d'esame |
| 5. | L'utente conferma che il voto non è aggiornabile e salva le modifiche |
| 6. | Il Sistema notifica il successo nel salvataggio delle modifiche |
| 7. | Il Sistema notifica lo studente il cui voto è stato inserito |
| 8. | Il Sistema riporta l'utente alla lista degli studenti che hanno sostenuto l'esame |
| Postcondizione: | L'utente ha aggiunto il voto d'esame ad uno studente |

<a name="p2.20"></a>