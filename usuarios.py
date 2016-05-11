import tweepy
import sys
import operator
import retrive_twitter_info
import time
from bot import *


user1="1agustin_paez"
consumer_key1 = "Bhc1VV6OPmx2ju2mAQGtzHBZR"
consumer_secret1 = "bk1rlVQA9XM13ni6iBs7NqWZgg2y6sXyzVIBGVceEGmlyMu21f"
access_token1 = "716350596123484160-AcWVe2FNvF6gd1G2ZftjeA3YBMEpy5G"
access_token_secret1 = "u2QbfrE0AszsZOB1j4gA7m9YJNPCaIJjqSGgkWfofDSsI"
auth1 = tweepy.OAuthHandler(consumer_key1, consumer_secret1)
auth1.set_access_token(access_token1, access_token_secret1)
api1 = tweepy.API(auth1)

agustin_paez = retrive_twitter_info.GetTwitterInfo(consumer_key1,consumer_secret1,access_token1,access_token_secret1,user1)


user2 = "dani_mar2343"
consumer_key2 = "8NODKVSPpHLAF3Zkzobjhc6WS"
consumer_secret2 = "8p3AXNSRkh8bGkMfzdgutgbZ1FjgFWfzOhsguUSvhMASaj9FsV"
access_token2 = "716357757092278272-C6tF6lTcebI0saz4DDXwDGMCNrS0bDY"
access_token_secret2 = "DqBFZNY1TON9npftDupcwetxDtGQRIXxmZPZsNBRP5GJ5"
auth2 = tweepy.OAuthHandler(consumer_key2, consumer_secret2)
auth2.set_access_token(access_token2, access_token_secret2)
api2 = tweepy.API(auth2)

dani_mar2343 = retrive_twitter_info.GetTwitterInfo(consumer_key2,consumer_secret2,access_token2,access_token_secret2,user2)


user3 = "edgar_s3212"
consumer_key3 = "QzW2cFeB7vG10MZygV1aYbORF"
consumer_secret3 = "MpWoasZ5BcmlKf8ED4VYn7sRkkfLOeNTs2e6XUrtzpVGxapI6G"
access_token3 = "716360499126865920-P0HNtm59lW0HnKt5ykorAWjqJDklbBe"
access_token_secret3 = "tBEOcxPwiDsgslJnbd0Q8t2dJW8lbKeZu3TCfq3OZ6Ddr"
auth3 = tweepy.OAuthHandler(consumer_key3, consumer_secret3)
auth3.set_access_token(access_token3, access_token_secret3)
api3= tweepy.API(auth3)

edgar_s3212 = retrive_twitter_info.GetTwitterInfo(consumer_key3,consumer_secret3,access_token3,access_token_secret3,user3)


user4 = "VerComunica"
consumer_key4 = "tC8Vmf3NP3GA0JT4sjh1p21Im"
consumer_secret4 = "SNpHt4d8yA5Nt32g9NF6Qs73KypzInw0Vq8pf6QZbMwX43aEx2"
access_token4 = "3526348696-aHRzH7fdmDRLj12mjpgMbMjBN2GFdjyX69cQuEt"
access_token_secret4 = "3Gt5Vv0b5uXTL5LFxIQVGEqsFRrGM88nnySFKq6zqpP5w"
auth4 = tweepy.OAuthHandler(consumer_key4, consumer_secret4)
auth4.set_access_token(access_token4, access_token_secret4)
api4= tweepy.API(auth4)

vercomunica = retrive_twitter_info.GetTwitterInfo(consumer_key4,consumer_secret4,access_token4,access_token_secret4,user4)

user5 = "silvia_gut1"
consumer_key5 = "fRa9liyp3smVvNXhibSvbOLzK"
consumer_secret5 = "1eprDP41I2S1jXpmPQt0F8LYhZzbqYeobyq6PvLuLUdWziBeSG"
access_token5 = "716362815057956864-wTRqRXopEOZn40E8AVJLgDoHj9Y0aH4"
access_token_secret5 = "3tBhi9aT5WR1AgWQpbqHXuTIGL7qYdgUmg1rQBpetBg76"
auth5 = tweepy.OAuthHandler(consumer_key5, consumer_secret5)
auth5.set_access_token(access_token5, access_token_secret5)
api5= tweepy.API(auth5)

silvia_gut1 = retrive_twitter_info.GetTwitterInfo(consumer_key5,consumer_secret5,access_token5,access_token_secret5,user5)


user6 = "karla_truji"
consumer_key6 = "y3awmQFWBeDSBcJHUO5r3yKMR"
consumer_secret6 = "rI2DYkzA2U4HncrlocbWLgo4skwPEkjWgwt7Tlrq7IhrlrMXmD"
access_token6 = "716366278185758720-bDjdUDNwSDB44CTsZJtq3vu5hKzpmUy"
access_token_secret6 = "QjNpQvqYlEfMjfVZcG8d4pWKJzLSCbiBYsBMXL2PUjn31"
auth6 = tweepy.OAuthHandler(consumer_key6, consumer_secret6)
auth6.set_access_token(access_token6, access_token_secret6)
api6= tweepy.API(auth6)

karla_truji = retrive_twitter_info.GetTwitterInfo(consumer_key6,consumer_secret6,access_token6,access_token_secret6,user6)

user7 = "la_basicamente"
consumer_key7 = "hRDJ3298tK7LectpTCK0Ws9QD"
consumer_secret7 = "SO4z15OzaU55sQX8BmZt1dCLoaB4V92roniZxeANPNkaUnTAzw"
access_token7 = "4714297429-Lh2exh2AUFyob5cqGMvx8LsDYuAhVwKuYnOmH3b"
access_token_secret7 = "b0uj9UFIQlnHkxAPAdW0TbvXqpLScQY4PVmvZxcqf6vbq"
auth7 = tweepy.OAuthHandler(consumer_key7, consumer_secret7)
auth7.set_access_token(access_token7, access_token_secret7)
api7= tweepy.API(auth7)


la_basicamente = retrive_twitter_info.GetTwitterInfo(consumer_key7,consumer_secret7,access_token7,access_token_secret7,user7)


user8 = "agustin_mac"
consumer_key8 = "O5r8x4WKmm5G82oq0gBuOkYz2"
consumer_secret8 = "GtmhNbZHxAlm3QNBLdVt6ifZY7OMNrDKS9L6N5XpySKiupOd30"
access_token8 = "3450499154-0wTxeJmWkVZK0jsoiVKTZTLOeBfqbgd1oRmP2f2"
access_token_secret8 = "Dpc3FLC0Gp7ReNIGyzfZh6ogdYdTajLZig7yZ0l3dpb7L"
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
access_token10 = "3307984159-GcGoMvI5ktTXajTKcQvywcTNsJ0IsRJdl5PHiAI"
access_token_secret10 = "SYAN8LwCC58KRQCtDh6NgPsAfiEQVTzJmBzSCMmwXpYAF"
auth10 = tweepy.OAuthHandler(consumer_key10, consumer_secret10)
auth10.set_access_token(access_token10, access_token_secret10)
api10= tweepy.API(auth10)

robledomartin = retrive_twitter_info.GetTwitterInfo(consumer_key10,consumer_secret10,access_token10,access_token_secret10,user10)

user12 = "jor_moca"
consumer_key12 = "rzJQY2tOu5UrY9LyPFvgryKig"
consumer_secret12 = "5nokDyEvk35jPjUtEnt1zlFQpKbZlhpMUaEtKalDfAXzKKRjnM"
access_token12 = "3420551085-LM9ts4Dfjinr3mfKU4q3ULJlP9bFac87yozN8pY"
access_token_secret12 = "rP8i5Wdra4fKjNSEJvi5F5TP8UHnNLgoS5hjcXAstVY0j"
auth12 = tweepy.OAuthHandler(consumer_key12, consumer_secret12)
auth12.set_access_token(access_token12, access_token_secret12)
api12= tweepy.API(auth12)

jor_moca = retrive_twitter_info.GetTwitterInfo(consumer_key12,consumer_secret12,access_token12,access_token_secret12,user12)

user13 = "guz_nelly"
consumer_key13 = "ic7rbwsbHFEaAg2Oq49NNX69f"
consumer_secret13 = "IeF61fBJKG2vM7z2jBxPtVgM27S9nbEsx2N6iMfFL6bBgikSMu"
access_token13 = "3420565401-GytGQfyVtbZjepw0hmO0Pwrg9YteuED1FkOmQ7R"
access_token_secret13 = "oBuTmrDsLBHfIojulWTeGmath93t2c2XRqulhXw55I0WA"
auth13 = tweepy.OAuthHandler(consumer_key13, consumer_secret13)
auth13.set_access_token(access_token13, access_token_secret13)
api13= tweepy.API(auth13)

guz_nelly = retrive_twitter_info.GetTwitterInfo(consumer_key13,consumer_secret13,access_token13,access_token_secret13,user13)

user14 = "rodriguezbre81"
consumer_key14 = "WRrgq3W48vXLz7x7E9pDPRWpy"
consumer_secret14 = "Rw11RZuZnpxEvo9do1vMmVsGMxtucAHKTRyJgr8ZvCUwPYX91s"
access_token14 = "3420744310-KKIJmHtoLT6twgv3pjXk9zaShKXzK6jGQ224BSk"
access_token_secret14 = "MkZpmFPzM7zGGOVxlTDQ9T3ORIzXGVDS6yZie51camb78"
auth14 = tweepy.OAuthHandler(consumer_key14, consumer_secret14)
auth14.set_access_token(access_token14, access_token_secret14)
api14= tweepy.API(auth14)

rodriguezbre81 = retrive_twitter_info.GetTwitterInfo(consumer_key14,consumer_secret14,access_token14,access_token_secret14,user14)

user15 = "Informativo_Ver"
consumer_key15 = "xKtju84veeMRe3xxKrX4TF7YJ"
consumer_secret15 = "IxhwyAajV0oL2gEAcsApTQNkUK1PRbeONxdOxn4HCe74iZ3TQY"
access_token15 = "717508674780930048-veLNsp2g2FIPLZ0SZuMPqy0z7qNsoir"
access_token_secret15 = "VC83zx7UgKOKb63lPfXI4BVZGl7CjvQGlx6ksB4tU7ZHn"
auth15 = tweepy.OAuthHandler(consumer_key15, consumer_secret15)
auth15.set_access_token(access_token15, access_token_secret15)
api15= tweepy.API(auth15)

Informativo_Ver = retrive_twitter_info.GetTwitterInfo(consumer_key15,consumer_secret15,access_token15,access_token_secret15,user15)

user16 = "SamsaraCervant"
consumer_key16 = "N6Ohopb7YrdKZPwwsGm3xkD8v"
consumer_secret16 = "6y16wKke6ccN5SXyuHHoCnx4mUGeLox8oL1jHiGfoxiU4Ip65c"
access_token16 = "4497620121-56lc7lS9iYVpY7nmU4t4Qa94MdIBgLHDEIO7ZH4"
access_token_secret16 = "WAjG1EgA6Owoh5CQxRCuPS0QYmKNkWXmrxNBSuwLyOKen"
auth16 = tweepy.OAuthHandler(consumer_key16, consumer_secret16)
auth16.set_access_token(access_token16, access_token_secret16)
api16= tweepy.API(auth16)


SamsaraCervant = retrive_twitter_info.GetTwitterInfo(consumer_key16,consumer_secret16,access_token16,access_token_secret16,user16)

user17 = "odalys_mendoz"
consumer_key17 = "CB6ri7KuIw6PcQ21HfdSwrUkq"
consumer_secret17 = "VhWFDAUqv5Zo8brrg4rJ0tiR9a0BzvucM5Iolc97BDZTkPMHfD"
access_token17 = "4316192773-2TVaqQRmQklWPKGWeuWLcPKo1BpaTmHF90HL31Z"
access_token_secret17 = "xSZN0wfTqZ23uBdE3STRLPToSZm9vmbpb15VqpyeRb9ic"
auth17 = tweepy.OAuthHandler(consumer_key17, consumer_secret17)
auth17.set_access_token(access_token17, access_token_secret17)
api17= tweepy.API(auth17)


odalys_mendoz = retrive_twitter_info.GetTwitterInfo(consumer_key17,consumer_secret17,access_token17,access_token_secret17,user17)

user18 = "prinzoeherrera"
consumer_key18 = "CBHm2CT6sWLpUgIDh6yy2m4Ia"
consumer_secret18 = "ULZVE4alRP3WRlxIFfwaOok3BU0oUXcaufDLC6JZ45Vk9hUQJe"
access_token18 = "3885886873-0FGsvOjJBkPbcZPISpX64k1odORjqlBtAjlpk1E"
access_token_secret18 = "L5D48WqumwyguTOxlrEMm3MhtVlA9elJLT3IwRaDvIjLq"
auth18 = tweepy.OAuthHandler(consumer_key18, consumer_secret18)
auth18.set_access_token(access_token18, access_token_secret18)
api18= tweepy.API(auth18)

prinzoeherrera = retrive_twitter_info.GetTwitterInfo(consumer_key18,consumer_secret18,access_token18,access_token_secret18,user18)

user19 = "greta_reyes21"
consumer_key19 = "68zC8xM54xZkUwo9GfZLEYqdW"
consumer_secret19 = "yLUxoNgtLRwQ4dirL7wQiJhiLCTi4O1n5eud1ffK1d2io34HuP"
access_token19 = "4813339992-l8hLC7uAIlJJ9sikPbnhQMoSpaIhRNg51toP1I1"
access_token_secret19 = "DuXStfeNQnVIGMwgp8pYuUnftLMfUDwe2bGRzQWXrklHO"
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

PamyRoche = retrive_twitter_info.GetTwitterInfo(consumer_key20,consumer_secret20,access_token20,access_token_secret20,user20)

user21 = "GleyFernando"
consumer_key21 = "c1anEPUQYG8QJ2m06Mcz8FhK6"
consumer_secret21 = "y1BJTQLhN6gvid23IfY7j80SGsmzTnTojdAJOsqb9YtJemwyD6"
access_token21 = "4229922446-utjdVHqJAIOZ9nztxvPAYacykBN2AGrlcldNQge"
access_token_secret21 = "DnrMACKmUG7zcSydvEbuNmZHJfVz0nHiQxT4w3K6kogLu"
auth21 = tweepy.OAuthHandler(consumer_key21, consumer_secret21)
auth21.set_access_token(access_token21, access_token_secret21)
api21= tweepy.API(auth21)


GleyFernando = retrive_twitter_info.GetTwitterInfo(consumer_key21,consumer_secret21,access_token21,access_token_secret21,user21)


user22 = "ArrolloRodolfo"
consumer_key22 = "E068uehGVeKylCcHfRvZDCSMU"
consumer_secret22 = "Jxo2UXzVnhjLjNjL5hnBuEdt6yIO27MrE5vMRU0PsweihLrSVh"
access_token22 = "3882769392-UpzneM5i4clewoxj2SXrEhgnnHKKEvUtlxyUuGX"
access_token_secret22 = "A2UCN5B8ZPCusIIlrbOdxx9ax8opn7KEqBJ9jy3v8bgTS"
auth22 = tweepy.OAuthHandler(consumer_key22, consumer_secret22)
auth22.set_access_token(access_token22, access_token_secret22)
api22= tweepy.API(auth22)

ArrolloRodolfo = retrive_twitter_info.GetTwitterInfo(consumer_key22,consumer_secret22,access_token22,access_token_secret22,user22)

user23 = "EpicentroVer"
consumer_key23 = "bwp4YiPyGkf7WokI9UyRJlhgp"
consumer_secret23 = "Si6b2KcPEN8SH2ug3OfHGy2LbXQbwPqj6Z33rK3P1DNh4QpTWv"
access_token23 = "718609815417716736-rgmU22MjYqwnl7dtOy1dBLTdcg99gzN"
access_token_secret23 = "jdqjXr2p43eZnnai8RzxzHxicwDbKDFkQzCURpLti6nhY"
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
access_token25 = "3409070725-7O14ZaoKRG1i3yWre6P0JWnHZISJiMVmHCkAwj6"
access_token_secret25 = "kJeBKQ4wvfPXwC4fvmm4QAXr6TsoweWh1ex8JQxj4ZXK4"
auth25 = tweepy.OAuthHandler(consumer_key25, consumer_secret25)
auth25.set_access_token(access_token25, access_token_secret25)
api25= tweepy.API(auth25)



leocasol = retrive_twitter_info.GetTwitterInfo(consumer_key25,consumer_secret25,access_token25,access_token_secret25,user25)