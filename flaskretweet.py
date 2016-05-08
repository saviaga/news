from bot import *
from flask import Flask,render_template,request,flash
from usuarios import *

app = Flask(__name__)


def identify_bot(user,ck,cs,at,atc):
    global the_bot
    the_bot = Bot(user,ck,cs,at,atc)
    wordToFilter = the_bot.botname
    return wordToFilter,user


@app.route("/")
def hello():
    return render_template('login.html')


@app.route("/login",methods=['POST'])
def imprime():
    opcion1 = request.form['opcion1']
    opcion2 = request.form['opcion2']

    if ((opcion1=='SEGOB') and (opcion2=='veracruz123')):

        return render_template("profile.html",opcion1=opcion1)
    else:

        return render_template('error.html')



@app.route("/profile",methods=['POST'])
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
    tweetes= tweet_id[datos:]




    usuario_id = int(request.form['usuario_id'])

    if usuario_id == 1:
        try:
            agustin_paez.api.retweet(tweetes)
            mensaje='agustin_paez ha retuiteado'
        except Exception as e:
            mensaje = ("error",e)

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

        #return render_template("profile.html",usuario_id='retuiteando agustin_paez')
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
            PamyRoche.api.retweet(tweetes)
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
            mensaje = 'leocasol ha retuiteado'
            time.sleep(60)

        except Exception as e:
            mensaje = ("error", e)


    #return render_template("profile.html",tweet_id=texto)
    return render_template("profile.html", tweet_id=tweet_id, usuario_id=usuario_id,datos=mensaje)


if __name__ == "__main__":
    app.debug = True
    app.run()