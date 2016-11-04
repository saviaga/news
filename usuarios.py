import tweepy
import sys
import operator
import retrive_twitter_info
import time
from bot import *


user1="1agustin_paez"
consumer_key1 = "Bhc1VV6OPmx2ju2mAQGtzHBZR"
consumer_secret1 = "bk1rlVQA9XM13ni6iBs7NqWZgg2y6sXyzVIBGVceEGmlyMu21f"
access_token1 = "716350596123484160-9bZJTSyJny4DeKdBUUXQp2fB5czX8iS"
access_token_secret1 = "j3fItCMatC825W0Uqb0sffN8qoSg59zgjnnBWKF2gDRgn"
auth1 = tweepy.OAuthHandler(consumer_key1, consumer_secret1)
auth1.set_access_token(access_token1, access_token_secret1)
api1 = tweepy.API(auth1)

agustin_paez = retrive_twitter_info.GetTwitterInfo(consumer_key1,consumer_secret1,access_token1,access_token_secret1,user1)


user2 = "dani_mar2343"
consumer_key2 = "QC57Rgc23mifXQKrMeNpBYwVI"
consumer_secret2 = "QFy3c8REqQjQQAz76eleIufgQMJ50UgzKgAUYMNX4ihY6X8r85"
access_token2 = "716357757092278272-z5BHvWaKEdtYQfpvpGfsZO2sHVrRTrj"
access_token_secret2 = "oydh4fDYCI7u2vipMhcVPqJp7t2PqjwF9YnpME5GpMM6a"
auth2 = tweepy.OAuthHandler(consumer_key2, consumer_secret2)
auth2.set_access_token(access_token2, access_token_secret2)
api2 = tweepy.API(auth2)

dani_mar2343 = retrive_twitter_info.GetTwitterInfo(consumer_key2,consumer_secret2,access_token2,access_token_secret2,user2)


user3 = "edgar_s3212"
consumer_key3 = "DGzaxMdt6FI85WjN6FQ7yskb8"
consumer_secret3 = "OfM4sE2vLloNTemzZFjJrnIneRNVnWYVwqL1rxrgQW7FmAvV5k"
access_token3 = "716360499126865920-5LnpWaeIKubyN1DBx6D7X9htuddK9YY"
access_token_secret3 = "ELlSVtwrCm34ij6uOkZLO837aCPwMvucp93ri2GePArTm"
auth3 = tweepy.OAuthHandler(consumer_key3, consumer_secret3)
auth3.set_access_token(access_token3, access_token_secret3)
api3= tweepy.API(auth3)

edgar_s3212 = retrive_twitter_info.GetTwitterInfo(consumer_key3,consumer_secret3,access_token3,access_token_secret3,user3)


#user4 = "VerComunica"
#consumer_key4 = "tC8Vmf3NP3GA0JT4sjh1p21Im"
#consumer_secret4 = "SNpHt4d8yA5Nt32g9NF6Qs73KypzInw0Vq8pf6QZbMwX43aEx2"
#access_token4 = "3526348696-DPVwM3EUcuZRhZQoEnUwHSNpWsECHgULL0h6DRD"
#access_token_secret4 = "SMVckSFCKbuR8d28s5ZSPYiZPNVEWmP9dS2shjpB5PPP9"
#auth4 = tweepy.OAuthHandler(consumer_key4, consumer_secret4)
#auth4.set_access_token(access_token4, access_token_secret4)
#api4= tweepy.API(auth4)

#vercomunica = retrive_twitter_info.GetTwitterInfo(consumer_key4,consumer_secret4,access_token4,access_token_secret4,user4)

user5 = "silvia_gut1"
consumer_key5 = "fRa9liyp3smVvNXhibSvbOLzK"
consumer_secret5 = "1eprDP41I2S1jXpmPQt0F8LYhZzbqYeobyq6PvLuLUdWziBeSG"
access_token5 = "716362815057956864-eW1lfhtCjUrsD3hTYloqEtSy85q9har"
access_token_secret5 = "mkl0ST8U5roc6ZV8Nei5MZK6sZSWlqiDYTqJXqkiGzo7y"
auth5 = tweepy.OAuthHandler(consumer_key5, consumer_secret5)
auth5.set_access_token(access_token5, access_token_secret5)
api5= tweepy.API(auth5)

silvia_gut1 = retrive_twitter_info.GetTwitterInfo(consumer_key5,consumer_secret5,access_token5,access_token_secret5,user5)


user6 = "karla_truji"
consumer_key6 = "p6lcOkx1N7v4luBor9GQPl4sj"
consumer_secret6 = "VZQQTYZZ1doBtLso16vwurQE5PeQMy5GP18G2TYh2wP64DyTsv"
access_token6 = "716366278185758720-2yCvyZflePZbP2jjor2StNzoxmS5jOF"
access_token_secret6 = "92KTrn56FS7vfLUJ2NGa7FoL7ve13NdAuxxNXh43VXnFI"
auth6 = tweepy.OAuthHandler(consumer_key6, consumer_secret6)
auth6.set_access_token(access_token6, access_token_secret6)
api6= tweepy.API(auth6)

karla_truji = retrive_twitter_info.GetTwitterInfo(consumer_key6,consumer_secret6,access_token6,access_token_secret6,user6)

user7 = "la_basicamente"
consumer_key7 = "hRDJ3298tK7LectpTCK0Ws9QD"
consumer_secret7 = "SO4z15OzaU55sQX8BmZt1dCLoaB4V92roniZxeANPNkaUnTAzw"
access_token7 = "4714297429-l2zuDqj6HfMEHZYuGwf4Wjp0EDCZlaEruF68rWb"
access_token_secret7 = "UZnBAEN5Setksyyf3GMU8u8yKYFz2h2DoimQtSx0axoGr"
auth7 = tweepy.OAuthHandler(consumer_key7, consumer_secret7)
auth7.set_access_token(access_token7, access_token_secret7)
api7= tweepy.API(auth7)


la_basicamente = retrive_twitter_info.GetTwitterInfo(consumer_key7,consumer_secret7,access_token7,access_token_secret7,user7)


user8 = "agustin_mac"
consumer_key8 = "O5r8x4WKmm5G82oq0gBuOkYz2"
consumer_secret8 = "GtmhNbZHxAlm3QNBLdVt6ifZY7OMNrDKS9L6N5XpySKiupOd30"
access_token8 = "3450499154-0LIQ1Qv8eJpYy8qpJu28H9bn3AKCYCzkR06PNKT"
access_token_secret8 = "IcRBj65i9IRbUyMe4rd6kyqCcBVwtyyiTfy0jBPPMFNRl"
auth8 = tweepy.OAuthHandler(consumer_key8, consumer_secret8)
auth8.set_access_token(access_token8, access_token_secret8)
api8= tweepy.API(auth8)

agustin_mac = retrive_twitter_info.GetTwitterInfo(consumer_key8,consumer_secret8,access_token8,access_token_secret8,user8)


user9 = "yol_tenorio"
consumer_key9 = "a9J6Px8sklpctgM95oQ8B7gze"
consumer_secret9 = "iuidl6fXrXYK6DHe7er0MWhluZFtz32OC8HJfkjWSwjbpq6Up3"
access_token9 = "3450392299-Rav1vPVVjtXLrkQsx9AGkFdnVI6JdsGLDZnW7Ng"
access_token_secret9 = "nMsKGjGHc84VEnShx9PZHz6iyxeUcIQWtu1w9a1IOoERK"
auth9 = tweepy.OAuthHandler(consumer_key9, consumer_secret9)
auth9.set_access_token(access_token9, access_token_secret9)
api9= tweepy.API(auth9)

yol_tenorio = retrive_twitter_info.GetTwitterInfo(consumer_key9,consumer_secret9,access_token9,access_token_secret9,user9)

user10 = "_robledomartin"
consumer_key10 = "hVQCTjr1s4vaWsyj3rLfbAfqJ"
consumer_secret10 = "kaOYyDqyuxpRC6r5JdQIVvF9JwoGHzyUKFjyVcedsoVHTNTBQP"
access_token10 = "3307984159-FoFZqPOBZCKwgfmYrDpfWKE4LLH81nqESbOGCzC"
access_token_secret10 = "fZtfMKP1pWnrW42UDyFUdvltYHkTeoVAXv08gX1hkloBf"
auth10 = tweepy.OAuthHandler(consumer_key10, consumer_secret10)
auth10.set_access_token(access_token10, access_token_secret10)
api10= tweepy.API(auth10)

robledomartin = retrive_twitter_info.GetTwitterInfo(consumer_key10,consumer_secret10,access_token10,access_token_secret10,user10)

user12 = "jor_moca"
consumer_key12 = "rzJQY2tOu5UrY9LyPFvgryKig"
consumer_secret12 = "5nokDyEvk35jPjUtEnt1zlFQpKbZlhpMUaEtKalDfAXzKKRjnM"
access_token12 = "3420551085-3wuuW1piF5CEiBQxlCbF6atYjXYu5bSTwextYek"
access_token_secret12 = "K24Vi4Qum3nX106Pl38P3bWlqBc4yiWqWkgmxAkmanBvO"
auth12 = tweepy.OAuthHandler(consumer_key12, consumer_secret12)
auth12.set_access_token(access_token12, access_token_secret12)
api12= tweepy.API(auth12)

jor_moca = retrive_twitter_info.GetTwitterInfo(consumer_key12,consumer_secret12,access_token12,access_token_secret12,user12)

user13 = "guz_nelly"
consumer_key13 = "ic7rbwsbHFEaAg2Oq49NNX69f"
consumer_secret13 = "IeF61fBJKG2vM7z2jBxPtVgM27S9nbEsx2N6iMfFL6bBgikSMu"
access_token13 = "3420565401-tyKahgmn0xKBBIPJFyQcYgfLaqP4rJW5BUwNVk2"
access_token_secret13 = "dI0BgIJKfw3PEvFZ4iRbT8TQEdtWTADSNQfQvQp0i5mkY"
auth13 = tweepy.OAuthHandler(consumer_key13, consumer_secret13)
auth13.set_access_token(access_token13, access_token_secret13)
api13= tweepy.API(auth13)

guz_nelly = retrive_twitter_info.GetTwitterInfo(consumer_key13,consumer_secret13,access_token13,access_token_secret13,user13)

user14 = "rodriguezbre81"
consumer_key14 = "WRrgq3W48vXLz7x7E9pDPRWpy"
consumer_secret14 = "Rw11RZuZnpxEvo9do1vMmVsGMxtucAHKTRyJgr8ZvCUwPYX91s"
access_token14 = "3420744310-SdlysuyzRSjSmskUzyGUwifpIeX8Z7FYAmE4BRe"
access_token_secret14 = "ViSvKEvyBVFRvzu24R7GEgzh9AZ9w02iGOxN4XSE0Fegv"
auth14 = tweepy.OAuthHandler(consumer_key14, consumer_secret14)
auth14.set_access_token(access_token14, access_token_secret14)
api14= tweepy.API(auth14)

rodriguezbre81 = retrive_twitter_info.GetTwitterInfo(consumer_key14,consumer_secret14,access_token14,access_token_secret14,user14)

user15 = "Informativo_Ver"
consumer_key15 = "xKtju84veeMRe3xxKrX4TF7YJ"
consumer_secret15 = "IxhwyAajV0oL2gEAcsApTQNkUK1PRbeONxdOxn4HCe74iZ3TQY"
access_token15 = "717508674780930048-PTBR3DK7ZZ0LAnhOJ4DOjz3u0kINTai"
access_token_secret15 = "1LSXAKq03I7QZzOzRUvc8tWvH80BQPcdgXa2oUvn1vC3r"
auth15 = tweepy.OAuthHandler(consumer_key15, consumer_secret15)
auth15.set_access_token(access_token15, access_token_secret15)
api15= tweepy.API(auth15)

Informativo_Ver = retrive_twitter_info.GetTwitterInfo(consumer_key15,consumer_secret15,access_token15,access_token_secret15,user15)

user16 = "SamsaraCervant"
consumer_key16 = "N6Ohopb7YrdKZPwwsGm3xkD8v"
consumer_secret16 = "6y16wKke6ccN5SXyuHHoCnx4mUGeLox8oL1jHiGfoxiU4Ip65c"
access_token16 = "4497620121-AxU4pTGZnaJhw6oSnMls5J3NCgY3giVSoUWbLcZ"
access_token_secret16 = "wMN7wxlkNiwpehY1nb6tVpx9rErWDONCSuTlMIYeSC8w4"
auth16 = tweepy.OAuthHandler(consumer_key16, consumer_secret16)
auth16.set_access_token(access_token16, access_token_secret16)
api16= tweepy.API(auth16)


SamsaraCervant = retrive_twitter_info.GetTwitterInfo(consumer_key16,consumer_secret16,access_token16,access_token_secret16,user16)

user17 = "odalys_mendoz"
consumer_key17 = "CB6ri7KuIw6PcQ21HfdSwrUkq"
consumer_secret17 = "VhWFDAUqv5Zo8brrg4rJ0tiR9a0BzvucM5Iolc97BDZTkPMHfD"
access_token17 = "4316192773-5ZsGeuRJ0UTmmg6oqq51loJUgiTNBkgPy6O0oIY"
access_token_secret17 = "dcId0Eenzkz5ndjc1g7Q2zCPhBRofqyKOD1S7eoezRExi"
auth17 = tweepy.OAuthHandler(consumer_key17, consumer_secret17)
auth17.set_access_token(access_token17, access_token_secret17)
api17= tweepy.API(auth17)


odalys_mendoz = retrive_twitter_info.GetTwitterInfo(consumer_key17,consumer_secret17,access_token17,access_token_secret17,user17)

user18 = "prinzoeherrera"
consumer_key18 = "CBHm2CT6sWLpUgIDh6yy2m4Ia"
consumer_secret18 = "ULZVE4alRP3WRlxIFfwaOok3BU0oUXcaufDLC6JZ45Vk9hUQJe"
access_token18 = "3885886873-mo2Er4t1VTrzEaPunwv3MfPZSBZ8RXAN9AzWQpV"
access_token_secret18 = "s82DoxfPMY8Aj5RjFCcg7BcCaMoX5wZE29UbmREqassMk"
auth18 = tweepy.OAuthHandler(consumer_key18, consumer_secret18)
auth18.set_access_token(access_token18, access_token_secret18)
api18= tweepy.API(auth18)

prinzoeherrera = retrive_twitter_info.GetTwitterInfo(consumer_key18,consumer_secret18,access_token18,access_token_secret18,user18)

user19 = "greta_reyes21"
consumer_key19 = "68zC8xM54xZkUwo9GfZLEYqdW"
consumer_secret19 = "yLUxoNgtLRwQ4dirL7wQiJhiLCTi4O1n5eud1ffK1d2io34HuP"
access_token19 = "4813339992-zNBEcsoOi5Ocr2UL1VDmllQMFQkzU5jUdJtA6rh"
access_token_secret19 = "WVp1Mh4swYVEkeB4aNVQKCHzHQCXoW20aVO9WCJO234A7"
auth19 = tweepy.OAuthHandler(consumer_key19, consumer_secret19)
auth19.set_access_token(access_token19, access_token_secret19)
api19= tweepy.API(auth19)

greta_reyes21 = retrive_twitter_info.GetTwitterInfo(consumer_key19,consumer_secret19,access_token19,access_token_secret19,user19)


user20 = "PamyRoche"
consumer_key20 = "lgBzTawJ1C8FkUvIcRWnHOTxQ"
consumer_secret20 = "0FkP8dzyeFxgYwNuPjOsh0SnrE11EKelBzSPWO9qQGk2yFgkMs"
access_token20 = "720698009734881280-0A32up9dZKlfQaJPn92zv1evcGTFZFC"
access_token_secret20 = "JuXK9GGOu6K2ZCRuzwikPdHPTeKOcalQWKigSFcp70U3m"
auth20 = tweepy.OAuthHandler(consumer_key20, consumer_secret20)
auth20.set_access_token(access_token20, access_token_secret20)
api20= tweepy.API(auth20)

#PamyRoche = retrive_twitter_info.GetTwitterInfo(consumer_key20,consumer_secret20,access_token20,access_token_secret20,user20)

user21 = "GleyFernando"
consumer_key21 = "c1anEPUQYG8QJ2m06Mcz8FhK6"
consumer_secret21 = "y1BJTQLhN6gvid23IfY7j80SGsmzTnTojdAJOsqb9YtJemwyD6"
access_token21 = "4229922446-1Gv72C9REgD4HIa2iW38tXg1STAMQwpiLYzELpI"
access_token_secret21 = "YiIs0QqmTPFLd6Mw69vs29Wj7P1wDhg8LLrOsf4sy1YX7"
auth21 = tweepy.OAuthHandler(consumer_key21, consumer_secret21)
auth21.set_access_token(access_token21, access_token_secret21)
api21= tweepy.API(auth21)


GleyFernando = retrive_twitter_info.GetTwitterInfo(consumer_key21,consumer_secret21,access_token21,access_token_secret21,user21)


user22 = "ArrolloRodolfo"
consumer_key22 = "E068uehGVeKylCcHfRvZDCSMU"
consumer_secret22 = "Jxo2UXzVnhjLjNjL5hnBuEdt6yIO27MrE5vMRU0PsweihLrSVh"
access_token22 = "3882769392-GD2leg4csjx9QuuaGpevukUEUGnXN5kS6jhKTRT"
access_token_secret22 = "zEzcG8Wdct4gGgVLmoEqBFHqWIcCGVBEgZo9sV9ZBvvC0"
auth22 = tweepy.OAuthHandler(consumer_key22, consumer_secret22)
auth22.set_access_token(access_token22, access_token_secret22)
api22= tweepy.API(auth22)

ArrolloRodolfo = retrive_twitter_info.GetTwitterInfo(consumer_key22,consumer_secret22,access_token22,access_token_secret22,user22)

user23 = "EpicentroVer"
consumer_key23 = "bwp4YiPyGkf7WokI9UyRJlhgp"
consumer_secret23 = "Si6b2KcPEN8SH2ug3OfHGy2LbXQbwPqj6Z33rK3P1DNh4QpTWv"
access_token23 = "718609815417716736-IoSL3DnYy4ggrxHW3Qj5rTNT5sSv7Gu"
access_token_secret23 = "CMN9aU74rmXfP1FDEdjVxKf3LCqpSUP8PjyVGmii3lONL"
auth23 = tweepy.OAuthHandler(consumer_key23, consumer_secret23)
auth23.set_access_token(access_token23, access_token_secret23)
api23= tweepy.API(auth23)

EpicentroVer = retrive_twitter_info.GetTwitterInfo(consumer_key23,consumer_secret23,access_token23,access_token_secret23,user23)

user24 = "armandoferrarif"
consumer_key24 = "VSg9b9S11jQbllSXNKX2vO4zD"
consumer_secret24 = "EACnRXgbmrNum6OybyqOPEmfrk91BvAZt7yoBYsoWHx91DbggQ"
access_token24 = "3408747912-PWHewzRi9dV2m74fLY4F2rIoMQp3bthSmAp46VO"
access_token_secret24 = "p5UBf5x8K42ZY8QedoxcVTWpxFTyUdf6cvXPkxbrVKfHy"
auth24 = tweepy.OAuthHandler(consumer_key24, consumer_secret24)
auth24.set_access_token(access_token24, access_token_secret24)
api24= tweepy.API(auth24)

armandoferrarif = retrive_twitter_info.GetTwitterInfo(consumer_key24,consumer_secret24,access_token24,access_token_secret24,user24)

user25 = "leocasol"
consumer_key25 = "OuoLmQhquecjFsMapWoRw92f2"
consumer_secret25 = "Mkdm9u89fbBjiCtLvG6Jnp3Ah9qLhXgYt6gIOXVazVsIgl5lwh"
access_token25 = "3409070725-TLYGjksZ4QIFM3nM2EZC7lMNV00zIEej1VPsX51"
access_token_secret25 = "hKKix3TzqlZRFzdojrfUlqcw04ADDKC76tGeIVS3ycnTS"
auth25 = tweepy.OAuthHandler(consumer_key25, consumer_secret25)
auth25.set_access_token(access_token25, access_token_secret25)
api25= tweepy.API(auth25)



leocasol = retrive_twitter_info.GetTwitterInfo(consumer_key25,consumer_secret25,access_token25,access_token_secret25,user25)