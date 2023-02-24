from flask import Flask, render_template, redirect, url_for, request
import alphaBot
import time
import sqlite3
import secrets

stringa = secrets.token_urlsafe() #utilizzata per generare un stringa randomica
stringaUrl = "/" + stringa

Ab = alphaBot.AlphaBot() #creo oggetto Ab che riporta la classe AlphaBot()

app = Flask(__name__)
#La funzione Python Flask(__name__) viene utilizzata per creare un'applicazione Web utilizzando il framework Flask.
#Questa funzione inizializza un'istanza della classe Flask, che rappresenta l'applicazione Web che stai per creare.
#Il parametro __name__ viene utilizzato per specificare il nome del modulo corrente, che viene utilizzato da Flask per trovare risorse come
#template e file statici relativi all'applicazione.

def validate(username, password): #funzione per la connessione al DB, tramite la execute svolgo la query e prendo le informazioni che mi servono
    completion = False
    con = sqlite3.connect('./databaseAlphaBot.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM utenti")
    rows = cur.fetchall()
    for row in rows:
        dbUser = row[1]
        dbPass = row[2]
        if dbUser==username:
            completion=check_password(dbPass, password)
    return completion

def check_password(hashed_password, user_password): #funzione per la convalidazione della password
    return hashed_password == user_password

@app.route("/", methods=['GET', 'POST'])
#La sintassi @app.route("/", methods=['GET', 'POST']) è un decoratore in Flask che viene utilizzato per definire una route nell'applicazione Flask.
#La route viene specificata come primo parametro del decoratore (in questo caso "/", ovvero la homepage),
#mentre il parametro methods viene utilizzato per specificare i metodi HTTP supportati dalla route. 
#In questo esempio, la route supporta sia il metodo GET che il metodo POST.

def login(): #funzione per il login al sito web, in caso di corretto login redirecta l'utente alla pagina secret
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = validate(username, password)
        if completion ==False:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route(stringaUrl, methods=['GET', 'POST'])
def index(): #in questa funzione index, vengono passate i "comandi complessi" e viene ripetuta per ognuna di essi l'apertura e la chiusura del db
    if request.method == 'POST':
        if request.form.get('su') == 'su':
            Ab.forward()
            time.sleep(1)
            Ab.stop()
        elif  request.form.get('dx') == 'dx':
            Ab.right()
            time.sleep(1)
            Ab.stop()
        elif  request.form.get('sx') == 'sx':
            Ab.left()
            time.sleep(1)
            Ab.stop()
        elif  request.form.get('giu') == 'giu':
            Ab.backward()
            time.sleep(1)
            Ab.stop()
        elif request.form.get('1') == '1':
            con = sqlite3.connect("./databaseAlphaBot")
            cur = con.cursor()
            res = cur.execute(f"SELECT MOVIMENTO FROM Tabbella_movimenti WHERE ID == 1")
            serie = res.fetchall()
            stringaComandi = serie[0][0]
            msgSplit = stringaComandi.split(";")
            print(msgSplit)
            for k in range(0,3):
                msg = msgSplit[k].split(",")
                print(msg)
                if msg[0] == "f":
                    Ab.forward()
                    time.sleep(float(msg[1]))
                    Ab.stop()
            con.close()
        elif request.form.get('2') == '2':
            con = sqlite3.connect("./databaseAlphaBot")
            cur = con.cursor()
            res = cur.execute(f"SELECT MOVIMENTO FROM Tabbella_movimenti WHERE ID == 2")
            serie = res.fetchall()
            stringaComandi = serie[0][0]
            msgSplit = stringaComandi.split(";")
            print(msgSplit)
            for k in range(0,3):
                msg = msgSplit[k].split(",")
                print(msg)
                if msg[0] == "f":
                    Ab.forward()
                    time.sleep(float(msg[2]))
                    Ab.stop()
            con.close()
        elif request.form.get('3') == '3':
            con = sqlite3.connect("./databaseAlphaBot")
            cur = con.cursor()
            res = cur.execute(f"SELECT MOVIMENTO FROM Tabbella_movimenti WHERE ID == 3")
            serie = res.fetchall()
            stringaComandi = serie[0][0]
            msgSplit = stringaComandi.split(";")
            print(msgSplit)
            for k in range(0,3):
                msg = msgSplit[k].split(",")
                print(msg)
                if msg[0] == "f":
                    Ab.forward()
                    time.sleep(float(msg[3]))
                    Ab.stop()
            con.close()
        elif request.form.get('4') == '4':
            con = sqlite3.connect("./databaseAlphaBot")
            cur = con.cursor()
            res = cur.execute(f"SELECT MOVIMENTO FROM Tabbella_movimenti WHERE ID == 4")
            serie = res.fetchall()
            stringaComandi = serie[0][0]
            msgSplit = stringaComandi.split(";")
            print(msgSplit)
            for k in range(0,3):
                msg = msgSplit[k].split(",")
                print(msg)
                if msg[0] == "f":
                    Ab.forward()
                    time.sleep(float(msg[4]))
                    Ab.stop()
            con.close()
        elif request.form.get('5') == '5':
            con = sqlite3.connect("./databaseAlphaBot")
            cur = con.cursor()
            res = cur.execute(f"SELECT MOVIMENTO FROM Tabbella_movimenti WHERE ID == 5")
            serie = res.fetchall()
            stringaComandi = serie[0][0]
            msgSplit = stringaComandi.split(";")
            print(msgSplit)
            for k in range(0,3):
                msg = msgSplit[k].split(",")
                print(msg)
                if msg[0] == "f":
                    Ab.forward()
                    time.sleep(float(msg[5]))
                    Ab.stop()
            con.close()
        else:
            print("Unknown")
    
    return render_template("alphaBot.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

"""

La funzione Python if __name__ == '__main__': viene utilizzata per verificare se il modulo in cui viene eseguita è il modulo principale dell'applicazione.
Questo controllo viene effettuato per evitare che il codice venga eseguito quando il modulo viene importato da un altro modulo.
Se il modulo viene eseguito come modulo principale, viene avviata l'applicazione Flask utilizzando il metodo run().
Il parametro debug=True viene utilizzato per abilitare la modalità di debug dell'applicazione, che consente di visualizzare
gli errori nella pagina web e di ricaricare automaticamente l'applicazione dopo le modifiche al codice.
Il parametro host='0.0.0.0' viene utilizzato per specificare l'indirizzo IP su cui l'applicazione ascolta le richieste.
L'indirizzo 0.0.0.0 indica che l'applicazione ascolta su tutte le interfacce di rete disponibili, permettendo l'accesso 
all'applicazione da parte di qualsiasi dispositivo sulla stessa rete.
In sintesi, questa funzione viene utilizzata per avviare l'applicazione Flask in modalità di debug, 
ascoltando le richieste su tutte le interfacce di rete disponibili. Quando il modulo viene importato da un altro modulo,
questa funzione non viene eseguita.

"""