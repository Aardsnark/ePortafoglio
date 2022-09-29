
### Progetto "Company Banking " ePortafoglio URS
##### ITS-ICT 11.2

**VERSION : X.X**

**Authors**  
Federico Zunino

**REVISION HISTORY**

| Version    | Date        | Authors      | Notes        |
| ----------- | ----------- | ----------- | ----------- |
| X.X |  | |  |

# Table of Contents

1. [Introduction](#p1)
	1. [Document Scope](#sp1.1)
	2. [Definitios and Acronym](#sp1.2) 
	3. [References](#sp1.3)
2. [System Description](#p2)
	1. [Context and Motivation](#sp2.1)
	2. [Project Objectives](#sp2.2)
3. [Requirement](#p3)
 	1. [Stakeholders](#sp3.1)
 	2. [Functional Requirements](#sp3.2)
 	3. [Non-Functional Requirements](#sp3.3)
  
  

<a name="p1"></a>

## 1. Introduction

<a name="sp1.1"></a>

### 1.1 Document Scope

Il presente documento va a definire ed illustrare i requisiti e le funzionalità del progetto "ePortafoglio", comissionato dal Prof

<a name="sp1.2"></a>

### 1.2 Definitios and Acronym

| Acronym				| Definition | 
| ------------------------------------- | ----------- | 


<a name="sp1.3"></a>

### 1.3 References 

<a name="p2"></a>
## 2. System Description

<a name="sp2.1"></a>
### 2.1 Context and Motivation
Il committente necessita un software custom che permetta la creazione e gestione di conti correnti e trasferimenti fra gli stessi sia all'interno del circuito interno all'azienda, sia da e verso conti di aziende esterne

<a name="sp2.2"></a>
### 2.2 Project Obectives 
La 

<a name="p3"></a>

## 3. Requirements

| Priorità | Significato | 
| --------------- | ----------- | 
| M | **Mandatory:**   |
| D | **Desiderable:** |
| O | **Optional:**    |
| E | **future Enhancement:** |

<a name="sp3.1"></a>
### 3.1 Stakeholders

| Categoria | Obbiettivo |
| ----------- | ---------- | 
| Cliente | Accedere al conto corrente tramite credenziali, trasferire e ricevere denaro, visualizzare estratto conto |
| Direzione | Creare e cancellare profili aziendali e conti correnti |
| Aziende Esterne | Ricevere ed effettuare operazioni di trasferimento di denare da e verso conti dell'azienda ePortafoglio |

<a name="sp3.2"></a>
### 3.2 Functional Requirements 

#### 3.2.0 Requisiti Generali
| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| 0.1 | Ogni conto corrente deve avere almeno un intestatario | M |
| 0.2 | Ogni conto corrente può avere un solo set di credenziali valide | M |
| 0.3 | Ogni conto corrente deve aver disponibile l'opzione di autenticazione a due fattori | M |

#### 3.2.1 Requisiti Funzionali Cliente
| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| 1.0 |  Il cliente può modificare le sue informazioni utente, tranne il codice univoco del conto |M|
| 1.1.0 |  Il cliente può trasferire denaro verso un conto corrente interno a ePortafoglio, individuandolo tramite codice univoco |M|
| 1.1.1 |  Il cliente può ricevere denaro da un conto corrente interno a ePortafoglio, individuandolo tramite codice univoco |M|
| 1.2.0 |  Il cliente può trasferire denaro verso un conto corrente esterno a ePortafoglio, individuandolo tramite codice univoco |M|
| 1.2.1 |  Il cliente può ricevere denaro da un conto corrente esterno a ePortafoglio, individuandolo tramite codice univoco |M|
| 1.3.0 |  Il cliente può visualizzare il report delle sue operazioni |M|
| 1.3.1 |  Il cliente può stampare il report delle sue operazioni |M|
| 1.4.0 |  Il cliente può reimpostare la sua password |M|
| 1.5.0 |  Il cliente può chiudere il suo conto |M|


#### 3.2.2 Requisiti Funzionali Direzione
| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| 2.0 |  La Direzione può creare un conto corrente con codice univoco |M|
| 2.0.1 |  La Direzione può eliminare un conto corrente con codice univoco |M|

#### 3.2.3 Requisiti Funzionali Azienda Esterna
| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| 3.0|  L'azienda esterna può trasferire denaro verso un conto corrente interno al circuito a ePortafoglio, individuandolo tramite codice univoco |M|
| 3.0.1 |  L'azienda esterna può ricevere denaro da un conto corrente interno al circuito ePortafoglio, individuandolo tramite codice univoco |M|

<a name="sp3.3"></a>
### 3.3 Non-Functional Requirements 
 
| ID | Descrizione | Priorità |
| --------------- | ----------- | ---------- | 
| R1 | Il software deve essere compatibile con Windows, MACOS, e Linux |M|
| R2 | Il software deve essere accessibile tramite tutti i browser |M|
| R3 | Il software deve essere accessibile tramite app dedicata (Android e IoS) |M|
| R4 | Il software deve rispettare i dettami del GDPR nell'acquisizione e protezione dei dati |M|
| R5 | Il software deve appoggiarsi su un database dedicato |M|
| R6 | Il database deve avere back-up bigiornalieri sia in fisico che in cloud ai fini di una veloce disaster recovery |M|
| R7 | Il software deve essere disponibile in lingua inglese |D|