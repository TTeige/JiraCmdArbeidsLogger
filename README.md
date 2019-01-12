# JiraCmdArbeidsLogger
Automatisk timeføring i jira

## Bruk

Arbeidsloggeren tar inn brukernavn og passord som argumenter. 

Den henter automatisk ned jira issues for brukeren. For å starte en "session" må
det aktive issuet settes

`set_active_issue XXX-1234`

Deretter kan en timer startes med `start`. Hvis det ønskelig å se hvor lang tid
som går underveis kan man bruke `start t`. Dette fører derimot til at 
kommandolinjen blir overskrevet og det er kanskje vanskelig å skrive en kommentar
når man skal avslutte loggingen.

Avslutte loggingen kan gjøres med å skrive `end`. Hvis en kommentar er ønskelig
kan man legge den til etter end slik: `end skriv kommentaren etterpå`. 

Bruk `show_work_log` for å se hva som har blitt ført ned og alle kommentarer.

For å kun se tiden som er brukt har `show_time_spent` kommandoen blitt gjort 
tilgjengelig.

For å dytte arbeidsloggene til jira brukes `commit_work` kommandoen.

### Kommandoer

```
start <any char>  end <comment>   help <command>
get_issues   list_issues   show_active   set_active_issue <issue key>
commit_work   show_work_log <issue key>  show_time_spent <issue key>
```