### Project Name
##### Authors

**VERSION : 0.1**

**Authors**  


**REVISION HISTORY**

| Version    | Date        | Authors      | Notes        |
| ----------- | ----------- | ----------- | ----------- |
|  |  |  |


# Table of Contents

1. [User Case](#p1)
	1. [Diagramma](#sp1.1)
	2. [Attori](#sp1.2) 
	3. [Lista Funzionalità](#sp1.3)
2. [Scenari](#p2)
	1. [Login](#sp2.1)
	1.1 [Autenticazione](#sp2.1.1)


<a name="p1"></a>

## 1. User Case

<a name="sp1.1"></a>

### 1.1 Diagramma

![Diagramma UML]()

<a name="sp1.2"></a>

### 1.2 Attori

| Nome | Descrizione |
| ----------- | ----------- | 
|  |  |


<a name="sp1.3"></a>

### 1.3 Lista e Funzionalità 
| ID | Nome | Descrizione |
| ----------- | ----------- | ----------- | 
| 1 | Login | L'utente accede con credenziali valide al sistema |
|  |  |  |

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

