from bot import *
from flask import Flask, render_template, request, flash
from usuarios import *
from lxml import html
import requests
import json

app = Flask(__name__)


def identify_bot(user, ck, cs, at, atc):
    global the_bot
    the_bot = Bot(user, ck, cs, at, atc)
    wordToFilter = the_bot.botname
    return wordToFilter, user


@app.route("/")
def hello():
    return render_template('login.html')


@app.route("/login", methods=['POST'])
def imprime():
    opcion1 = request.form['opcion1']
    opcion2 = request.form['opcion2']

    if ((opcion1 == 'SEGOB') and (opcion2 == 'veracruz123')):

        #        return render_template("profile.html",opcion1=opcion1)
        return render_template("notas.html", opcion1=opcion1)
    else:

        return render_template('error.html')


@app.route("/notas", methods=['POST'])
def scrap_note():
    global Link
    global answer
    global Medio
    global a1
    global Titulo_get
    global Texto1
    global Texto
    global news
    news= {}
    answer = request.form.getlist('myInputs[]')

    for a in answer:
        a1=a
        news[a]=a
        print("imprimiendo primera guardada ", news[a])

    #loop through dictionary
    for x in news:
        print("valores ",news[x])

    print(list(news.keys()))
    # This will create a list of buyers:

    # Inputs = []
    # task_Option = request.form.getlist['myInputs[]']

    task_Option = request.form['taskOption']
    print(task_Option)
    # for tas in task_Option:
    #    print(tas)
    # Link  = request.form['link_id']


    if task_Option == 'XEU':
            try:
                #Link = "http://www.xeu.com.mx/nota.cfm?id=883134"
                #Link = a1
                #print("link ",Link)
                Medio = "XEU"
                for d in news:
                    print("dic value ", news[d])
                    page = requests.get(news[d])
                    tree = html.fromstring(page.content)

                    Titulo_get = tree.xpath('//div[@class="fgtitulo"]/text()')
                    #print("titulo get1", Titulo_get)
                    for x in Titulo_get:
                        x = x.encode("utf-8")
                    Titulo_f = Titulo_get[0]
                # This will create a list of prices

                    Texto = tree.xpath('//div[@class="fatrece"]//text()')
                    Texto = [x.rstrip() for x in Texto]
                    Textof = Texto[1]


                    Fecha_get = tree.xpath('//div[@class="faonce"]/text()')
                    Fecha_get = [x.rstrip() for x in Fecha_get]
                    Fecha_getf = Fecha_get[3][1:]

                    news[d] = [Titulo_f]
                    news[d].append(Textof)
                    news[d].append(Fecha_getf)

                    print("titulo1 desp 2o append ", news[d])
                    for k in news:
                        print(k)




            except Exception as e:
                mensaje = ("error", e)

    return render_template("notas.html", datos=task_Option, noticias=news)


@app.route("/profile", methods=['POST'])
def retweet_me():
    # identifica
    user, ck, cs, at, atc = [line.rstrip('\n') for line in open('my_twitter_info.txt', 'r')]
    wordToFilter, user = identify_bot(user, ck, cs, at, atc)
    global botname
    botname = user
    # fin identifica
    mensaje = ''
    tweet_id = request.form['tweet_id']
    lenght = len(tweet_id)
    str1 = str(tweet_id)
    str2 = "/"

    datos = str1.rfind(str2)
    datos = datos + 1
    tweetes = tweet_id[datos:]

    usuario_id = int(request.form['usuario_id'])

    if usuario_id == 1:
        try:
            agustin_paez.api.retweet(tweetes)
            mensaje = 'agustin_paez ha retuiteado'
        except Exception as e:
            mensaje = ("error", e)

    elif usuario_id == 2:
        try:
            dani_mar2343.api.retweet(tweetes)
            mensaje = 'adani_mar2343 ha retuiteado'
        except Exception as e:
            mensaje = ("error", e)

    elif usuario_id == 3:
        try:
            edgar_s3212.api.retweet(tweetes)
            mensaje = 'edgar_s3212 ha retuiteado'
        except Exception as e:
            mensaje = ("error", e)

            # return render_template("profile.html",usuario_id='retuiteando agustin_paez')
    elif usuario_id == 4:
        try:
            silvia_gut1.api.retweet(tweetes)
            mensaje = 'silvia_gut1 ha retuiteado'
        except Exception as e:
            mensaje = ("error", e)

    elif usuario_id == 5:
        try:
            karla_truji.api.retweet(tweetes)
            mensaje = 'karla_truji ha retuiteado'
        except Exception as e:
            mensaje = ("error", e)

    elif usuario_id == 6:
        try:
            la_basicamente.api.retweet(tweetes)
            mensaje = 'la_basicamente ha retuiteado'
        except Exception as e:
            mensaje = ("error", e)

    elif usuario_id == 7:
        try:
            agustin_mac.api.retweet(tweetes)
            mensaje = 'agustin_mac ha retuiteado'
        except Exception as e:
            mensaje = ("error", e)

    elif usuario_id == 8:
        try:
            yol_tenorio.api.retweet(tweetes)
            mensaje = 'yol_tenorio ha retuiteado'
        except Exception as e:
            mensaje = ("error", e)

    elif usuario_id == 9:
        try:
            robledomartin.api.retweet(tweetes)
            mensaje = 'robledomartin ha retuiteado'
        except Exception as e:
            mensaje = ("error", e)

    elif usuario_id == 10:
        try:
            jor_moca.api.retweet(tweetes)
            mensaje = 'jor_moca ha retuiteado'
        except Exception as e:
            mensaje = ("error", e)

    elif usuario_id == 11:
        try:
            guz_nelly.api.retweet(tweetes)
            mensaje = 'guz_nelly ha retuiteado'
        except Exception as e:
            mensaje = ("error", e)

    elif usuario_id == 12:
        try:
            rodriguezbre81.api.retweet(tweetes)
            mensaje = 'rodriguezbre81 ha retuiteado'
        except Exception as e:
            mensaje = ("error", e)

    elif usuario_id == 13:
        try:
            Informativo_Ver.api.retweet(tweetes)
            mensaje = 'Informativo_Ver ha retuiteado'
        except Exception as e:
            mensaje = ("error", e)

    elif usuario_id == 14:
        try:
            SamsaraCervant.api.retweet(tweetes)
            mensaje = 'SamsaraCervant ha retuiteado'
        except Exception as e:
            mensaje = ("error", e)

    elif usuario_id == 15:
        try:
            odalys_mendoz.api.retweet(tweetes)
            mensaje = 'odalys_mendoz ha retuiteado'
        except Exception as e:
            mensaje = ("error", e)

    elif usuario_id == 16:
        try:
            prinzoeherrera.api.retweet(tweetes)
            mensaje = 'prinzoeherrera ha retuiteado'
        except Exception as e:
            mensaje = ("error", e)

    elif usuario_id == 17:
        try:
            greta_reyes21.api.retweet(tweetes)
            mensaje = 'greta_reyes21 ha retuiteado'
        except Exception as e:
            mensaje = ("error", e)

    elif usuario_id == 18:
        try:
            # PamyRoche.api.retweet(tweetes)
            mensaje = 'PamyRoche ha retuiteado'
        except Exception as e:
            mensaje = ("error", e)

    elif usuario_id == 19:
        try:
            GleyFernando.api.retweet(tweetes)
            mensaje = 'GleyFernando ha retuiteado'
        except Exception as e:
            mensaje = ("error", e)

    elif usuario_id == 20:
        try:
            ArrolloRodolfo.api.retweet(tweetes)
            mensaje = 'ArrolloRodolfo ha retuiteado'
        except Exception as e:
            mensaje = ("error", e)

    elif usuario_id == 21:
        try:
            EpicentroVer.api.retweet(tweetes)
            mensaje = 'EpicentroVer ha retuiteado'
        except Exception as e:
            mensaje = ("error", e)

    elif usuario_id == 22:
        try:
            armandoferrarif.api.retweet(tweetes)
            mensaje = 'armandoferrarif ha retuiteado'
        except Exception as e:
            mensaje = ("error", e)

    elif usuario_id == 23:
        try:
            leocasol.api.retweet(tweetes)
            mensaje = 'leocasol ha retuiteado'
        except Exception as e:
            mensaje = ("error", e)


    elif usuario_id == 24:
        try:
            agustin_paez.api.retweet(tweetes)
            mensaje = 'agustin_paez ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)

        try:
            dani_mar2343.api.retweet(tweetes)
            mensaje = 'dani_mar2343 ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)

        try:
            edgar_s3212.api.retweet(tweetes)
            mensaje = 'edgar_s3212 ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)

        try:
            silvia_gut1.api.retweet(tweetes)
            mensaje = 'silvia_gut1 ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)

        try:
            karla_truji.api.retweet(tweetes)
            mensaje = 'karla_truji ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)

        try:
            la_basicamente.api.retweet(tweetes)
            mensaje = 'la_basicamente ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)

        try:
            agustin_mac.api.retweet(tweetes)
            mensaje = 'agustin_mac ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)

        try:
            yol_tenorio.api.retweet(tweetes)
            mensaje = 'yol_tenorio ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)

        try:
            robledomartin.api.retweet(tweetes)
            mensaje = 'robledomartin ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)

        try:
            jor_moca.api.retweet(tweetes)
            mensaje = 'jor_moca ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)

        try:
            guz_nelly.api.retweet(tweetes)
            mensaje = 'guz_nelly ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)

        try:
            rodriguezbre81.api.retweet(tweetes)
            mensaje = 'rodriguezbre81 ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)

        try:
            Informativo_Ver.api.retweet(tweetes)
            mensaje = 'Informativo_Ver ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)

        try:
            SamsaraCervant.api.retweet(tweetes)
            mensaje = 'SamsaraCervant ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)

        try:
            odalys_mendoz.api.retweet(tweetes)
            mensaje = 'odalys_mendoz ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)

        try:
            prinzoeherrera.api.retweet(tweetes)
            mensaje = 'prinzoeherrera ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)

        try:
            greta_reyes21.api.retweet(tweetes)
            mensaje = 'greta_reyes21 ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)

        try:
            PamyRoche.api.retweet(tweetes)
            mensaje = 'PamyRoche ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)

        try:
            GleyFernando.api.retweet(tweetes)
            mensaje = 'GleyFernando ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)

        try:
            ArrolloRodolfo.api.retweet(tweetes)
            mensaje = 'ArrolloRodolfo ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)

        try:
            EpicentroVer.api.retweet(tweetes)
            mensaje = 'EpicentroVer ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)

        try:
            armandoferrarif.api.retweet(tweetes)
            mensaje = 'armandoferrarif ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)

        try:
            leocasol.api.retweet(tweetes)
            mensaje = 'leocasol ya ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)

    # return render_template("profile.html",tweet_id=texto)
    return render_template("profile.html", tweet_id=tweet_id, usuario_id=usuario_id, datos=mensaje)


if __name__ == "__main__":
    app.debug = True
    app.run()