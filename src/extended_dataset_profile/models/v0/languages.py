from typing import Annotated

from pydantic import AfterValidator


def is_iso369_3(text: str) -> bool:
    return text in _ISO369_3_LANGUAGES


def _iso369_3_validator(text: str) -> str:
    text = text.lower()
    if not is_iso369_3(text):
        raise ValueError(f'"{text}" is not a ISO369-3 language string!')
    return text


Language = Annotated[str, AfterValidator(_iso369_3_validator)]


_ISO369_3_LANGUAGES = set(
    [
        "duo",  # Dupaninan Agta
        "lai",  # Lambya
        "tjl",  # Tai Laing
        "lol",  # Mongo
        "pmh",  # Māhārāṣṭri Prākrit
        "kyl",  # Kalapuya
        "urw",  # Sop
        "kqu",  # Seroa
        "snj",  # Riverain Sango
        "snl",  # Sangil
        "mwk",  # Kita Maninkakan
        "qxh",  # Panao Huánuco Quechua
        "iki",  # Iko
        "hik",  # Seit-Kaitetu
        "ess",  # Central Siberian Yupik
        "jle",  # Ngile
        "kyz",  # Kayabí
        "njo",  # Ao Naga
        "ahp",  # Aproumu Aizi
        "kqs",  # Northern Kissi
        "xmm",  # Manado Malay
        "ksa",  # Shuwa-Zamani
        "amt",  # Amto
        "bht",  # Bhattiyali
        "bqe",  # Navarro-Labourdin Basque
        "cur",  # Chhulung
        "nbi",  # Mao Naga
        "sbb",  # Simbo
        "kot",  # Lagwan
        "ing",  # Degexit'an
        "sew",  # Sewa Bay
        "khh",  # Kehu
        "guj",  # Gujarati
        "gaz",  # West Central Oromo
        "keb",  # Kélé
        "tbo",  # Tawala
        "eip",  # Eipomek
        "mga",  # Middle Irish (900-1200)
        "srz",  # Shahmirzadi
        "nnz",  # Nda'nda'
        "jpr",  # Judeo-Persian
        "bsg",  # Bashkardi
        "caa",  # Chortí
        "tzb",  # Bachajón Tzeltal
        "ubm",  # Upper Baram Kenyah
        "nnx",  # Ngong
        "tna",  # Tacana
        "elx",  # Elamite
        "hps",  # Hawai'i Sign Language (HSL)
        "eli",  # Nding
        "aap",  # Pará Arára
        "anp",  # Angika
        "mwb",  # Juwal
        "yty",  # Yatay
        "hmr",  # Hmar
        "snp",  # Siane
        "tpl",  # Tlacoapa Me'phaa
        "bha",  # Bharia
        "kgf",  # Kube
        "nnd",  # West Ambae
        "vit",  # Viti
        "xow",  # Kowaki
        "hwo",  # Hwana
        "ina",  # Interlingua (International Auxiliary Language Association)
        "luf",  # Laua
        "pye",  # Pye Krumen
        "ego",  # Eggon
        "omw",  # South Tairora
        "kyh",  # Karok
        "zkn",  # Kanan
        "gss",  # Greek Sign Language
        "pnq",  # Pana (Burkina Faso)
        "dme",  # Dugwor
        "coa",  # Cocos Islands Malay
        "hmp",  # Northern Mashan Hmong
        "swy",  # Sarua
        "byx",  # Qaqet
        "bdg",  # Bonggi
        "mcf",  # Matsés
        "moi",  # Mboi
        "trl",  # Traveller Scottish
        "ttr",  # Tera
        "yih",  # Western Yiddish
        "tcm",  # Tanahmerah
        "bhm",  # Bathari
        "xpv",  # Northern Tasmanian
        "aeq",  # Aer
        "tht",  # Tahltan
        "zkv",  # Krevinian
        "ard",  # Arabana
        "lvl",  # Lwel
        "gug",  # Paraguayan Guaraní
        "wew",  # Wejewa
        "gew",  # Gera
        "bsj",  # Bangwinji
        "bqi",  # Bakhtiari
        "xpe",  # Liberia Kpelle
        "shq",  # Sala
        "mzg",  # Monastic Sign Language
        "slt",  # Sila
        "cng",  # Northern Qiang
        "nug",  # Nungali
        "akb",  # Batak Angkola
        "dja",  # Djadjawurrung
        "okz",  # Old Khmer
        "mcr",  # Menya
        "coz",  # Chochotec
        "nni",  # North Nuaulu
        "plt",  # Plateau Malagasy
        "wtm",  # Mewati
        "ght",  # Kuke
        "cay",  # Cayuga
        "enl",  # Enlhet
        "kqa",  # Mum
        "xtt",  # Tacahua Mixtec
        "dhm",  # Zemba
        "zka",  # Kaimbulawa
        "btw",  # Butuanon
        "ise",  # Italian Sign Language
        "olk",  # Olkol
        "bdi",  # Burun
        "hix",  # Hixkaryána
        "ukv",  # Kuku
        "sri",  # Siriano
        "ett",  # Etruscan
        "yau",  # Yuwana
        "kja",  # Mlap
        "aia",  # Arosi
        "ypb",  # Labo Phowa
        "dag",  # Dagbani
        "cru",  # Carútana
        "tzh",  # Tzeltal
        "mbd",  # Dibabawon Manobo
        "bvz",  # Bauzi
        "lmf",  # South Lembata
        "mzl",  # Mazatlán Mixe
        "xbd",  # Bindal
        "tpn",  # Tupinambá
        "lmb",  # Merei
        "spa",  # Spanish
        "mvp",  # Duri
        "sur",  # Mwaghavul
        "swo",  # Shanenawa
        "mrh",  # Mara Chin
        "vem",  # Vemgo-Mabas
        "dbf",  # Edopi
        "yik",  # Dongshanba Lalo
        "nko",  # Nkonya
        "dyn",  # Dyangadi
        "ret",  # Retta
        "clw",  # Chulym
        "msj",  # Ma (Democratic Republic of Congo)
        "tqo",  # Toaripi
        "rhg",  # Rohingya
        "bwz",  # Bwisi
        "knn",  # Konkani (individual language)
        "bkx",  # Baikeno
        "aqc",  # Archi
        "lub",  # Luba-Katanga
        "kxv",  # Kuvi
        "snu",  # Senggi
        "tea",  # Temiar
        "ill",  # Iranun
        "wrl",  # Warlmanpa
        "ciy",  # Chaima
        "klv",  # Maskelynes
        "kvg",  # Kuni-Boazi
        "mlk",  # Ilwana
        "xle",  # Lemnian
        "bhy",  # Bhele
        "ymq",  # Qila Muji
        "kjv",  # Kaikavian Literary Language
        "bqr",  # Burusu
        "mnt",  # Maykulan
        "kpy",  # Koryak
        "nfu",  # Mfumte
        "psh",  # Southwest Pashai
        "swl",  # Swedish Sign Language
        "saj",  # Sahu
        "kbx",  # Ap Ma
        "mrx",  # Maremgi
        "ull",  # Ullatan
        "lzh",  # Literary Chinese
        "swg",  # Swabian
        "pcp",  # Pacahuara
        "ang",  # Old English (ca. 450-1100)
        "yen",  # Yendang
        "ypw",  # Puwa Yi
        "gid",  # Gidar
        "arg",  # Aragonese
        "ddi",  # West Goodenough
        "irk",  # Iraqw
        "zla",  # Zula
        "vmu",  # Muluridyi
        "kzh",  # Kenuzi-Dongola
        "mcx",  # Mpiemo
        "bwe",  # Bwe Karen
        "bcq",  # Bench
        "kmf",  # Kare (Papua New Guinea)
        "mmy",  # Migaama
        "nme",  # Mzieme Naga
        "waw",  # Waiwai
        "trw",  # Torwali
        "bko",  # Kwa'
        "siu",  # Sinagen
        "bck",  # Bunuba
        "bso",  # Buso
        "lnb",  # Mbalanhu
        "uby",  # Ubykh
        "vmr",  # Marenje
        "zyj",  # Youjiang Zhuang
        "eiv",  # Askopan
        "khc",  # Tukang Besi North
        "bjq",  # Southern Betsimisaraka Malagasy
        "bxu",  # China Buriat
        "mwt",  # Moken
        "gds",  # Ghandruk Sign Language
        "zaz",  # Zari
        "mep",  # Miriwoong
        "nhb",  # Beng
        "kxl",  # Nepali Kurux
        "aww",  # Awun
        "mha",  # Manda (India)
        "mxr",  # Murik (Malaysia)
        "crq",  # Iyo'wujwa Chorote
        "nrx",  # Ngurmbur
        "urf",  # Uradhi
        "szb",  # Ngalum
        "slw",  # Sialum
        "mie",  # Ocotepec Mixtec
        "gul",  # Sea Island Creole English
        "oko",  # Old Korean (3rd-9th cent.)
        "stw",  # Satawalese
        "vgt",  # Vlaamse Gebarentaal
        "fal",  # South Fali
        "mjs",  # Miship
        "yiv",  # Northern Nisu
        "nun",  # Anong
        "xhr",  # Hernican
        "yum",  # Quechan
        "kfs",  # Bilaspuri
        "bxz",  # Binahari
        "zuy",  # Zumaya
        "mft",  # Mokerang
        "dgs",  # Dogoso
        "esh",  # Eshtehardi
        "xes",  # Kesawai
        "jna",  # Jangshung
        "bhp",  # Bima
        "opk",  # Kopkaka
        "bpd",  # Banda-Banda
        "ccj",  # Kasanga
        "noh",  # Nomu
        "max",  # North Moluccan Malay
        "nkm",  # Namat
        "sdc",  # Sassarese Sardinian
        "toy",  # Topoiyo
        "vka",  # Kariyarra
        "wnd",  # Wandarang
        "bve",  # Berau Malay
        "ncu",  # Chumburung
        "ayp",  # North Mesopotamian Arabic
        "osa",  # Osage
        "ttu",  # Torau
        "hui",  # Huli
        "mih",  # Chayuco Mixtec
        "ibd",  # Iwaidja
        "lem",  # Nomaande
        "fkv",  # Kven Finnish
        "cas",  # Tsimané
        "nec",  # Nedebang
        "mtv",  # Asaro'o
        "prg",  # Prussian
        "jmr",  # Kamara
        "cby",  # Carabayo
        "cmr",  # Mro-Khimi Chin
        "gin",  # Hinukh
        "cqd",  # Chuanqiandian Cluster Miao
        "tjm",  # Timucua
        "spi",  # Saponi
        "rug",  # Roviana
        "tyj",  # Tai Do
        "psi",  # Southeast Pashai
        "mzr",  # Marúbo
        "xvn",  # Vandalic
        "ptn",  # Patani
        "brg",  # Baure
        "lbx",  # Lawangan
        "hak",  # Hakka Chinese
        "nzu",  # Teke-Nzikou
        "sbh",  # Sori-Harengan
        "ofs",  # Old Frisian
        "xbe",  # Bigambal
        "xpm",  # Pumpokol
        "xho",  # Xhosa
        "tun",  # Tunica
        "ngz",  # Ngungwel
        "bkz",  # Bungku
        "kjn",  # Kunjen
        "kju",  # Kashaya
        "avi",  # Avikam
        "dbw",  # Bankan Tey Dogon
        "sld",  # Sissala
        "san",  # Sanskrit
        "bef",  # Benabena
        "xug",  # Kunigami
        "syc",  # Classical Syriac
        "dta",  # Daur
        "ysl",  # Yugoslavian Sign Language
        "tar",  # Central Tarahumara
        "msl",  # Molof
        "pib",  # Yine
        "kvz",  # Tsakwambo
        "dil",  # Dilling
        "sox",  # Swo
        "zrn",  # Zerenkel
        "thy",  # Tha
        "kbh",  # Camsá
        "cbq",  # Tsucuba
        "olr",  # Olrat
        "abe",  # Western Abnaki
        "zoq",  # Tabasco Zoque
        "skx",  # Seko Padang
        "wam",  # Wampanoag
        "jaa",  # Jamamadí
        "kvy",  # Yintale Karen
        "aey",  # Amele
        "mwn",  # Nyamwanga
        "ylg",  # Yelogu
        "bvl",  # Bolivian Sign Language
        "unp",  # Worora
        "ikh",  # Ikhin-Arokho
        "pno",  # Panobo
        "taj",  # Eastern Tamang
        "ium",  # Iu Mien
        "csq",  # Croatia Sign Language
        "ian",  # Iatmul
        "glj",  # Gula Iro
        "nzb",  # Njebi
        "rrt",  # Arritinngithigh
        "vel",  # Veluws
        "xbn",  # Kenaboi
        "pez",  # Eastern Penan
        "uig",  # Uighur
        "tdq",  # Tita
        "mus",  # Creek
        "dmg",  # Upper Kinabatangan
        "non",  # Old Norse
        "cml",  # Campalagian
        "sgi",  # Suga
        "hav",  # Havu
        "esg",  # Aheri Gondi
        "oht",  # Old Hittite
        "kim",  # Karagas
        "bay",  # Batuley
        "khv",  # Khvarshi
        "myl",  # Moma
        "jko",  # Kubo
        "loz",  # Lozi
        "mnj",  # Munji
        "fry",  # Western Frisian
        "xaa",  # Andalusian Arabic
        "pey",  # Petjo
        "avs",  # Aushiri
        "gza",  # Ganza
        "sht",  # Shasta
        "ndw",  # Ndobo
        "zmg",  # Marti Ke
        "xns",  # Kanashi
        "mmo",  # Mangga Buang
        "nia",  # Nias
        "kge",  # Komering
        "ylu",  # Aribwaung
        "ulw",  # Ulwa
        "bev",  # Daloa Bété
        "cub",  # Cubeo
        "gfk",  # Patpatar
        "nak",  # Nakanai
        "suf",  # Tarpia
        "wrp",  # Waropen
        "chd",  # Highland Oaxaca Chontal
        "fly",  # Flaaitaal
        "jii",  # Jiiddu
        "xpk",  # Kulina Pano
        "nyj",  # Nyanga
        "apw",  # Western Apache
        "crv",  # Chaura
        "mna",  # Mbula
        "kdj",  # Karamojong
        "fag",  # Finongan
        "btq",  # Batek
        "shp",  # Shipibo-Conibo
        "iin",  # Thiin
        "wba",  # Warao
        "lht",  # Lo-Toga
        "mzk",  # Nigeria Mambila
        "giu",  # Mulao
        "tda",  # Tagdal
        "lig",  # Ligbi
        "bet",  # Guiberoua Béte
        "stl",  # Stellingwerfs
        "hbn",  # Heiban
        "bwi",  # Baniwa
        "hnj",  # Hmong Njua
        "kie",  # Kibet
        "bit",  # Berinomo
        "kqz",  # Korana
        "sgm",  # Singa
        "cjy",  # Jinyu Chinese
        "wgg",  # Wangkangurru
        "bna",  # Bonerate
        "koe",  # Kacipo-Bale Suri
        "phr",  # Pahari-Potwari
        "pud",  # Punan Aput
        "tdc",  # Emberá-Tadó
        "tef",  # Teressa
        "ukr",  # Ukrainian
        "brx",  # Bodo (India)
        "nmw",  # Nimoa
        "ils",  # International Sign
        "ksf",  # Bafia
        "lld",  # Ladin
        "npa",  # Nar Phu
        "kqe",  # Kalagan
        "zah",  # Zangwal
        "wyi",  # Woiwurrung
        "xcb",  # Cumbric
        "koy",  # Koyukon
        "mbu",  # Mbula-Bwazza
        "tok",  # Toki Pona
        "bho",  # Bhojpuri
        "ktz",  # Juǀʼhoan
        "aqp",  # Atakapa
        "xnu",  # Nukunul
        "arr",  # Karo (Brazil)
        "bsw",  # Baiso
        "tmn",  # Taman (Indonesia)
        "uzn",  # Northern Uzbek
        "xkp",  # Kabatei
        "ygs",  # Yolŋu Sign Language
        "llm",  # Lasalimu
        "unn",  # Kurnai
        "iyx",  # Yaka (Congo)
        "kjg",  # Khmu
        "onk",  # Kabore One
        "cpi",  # Chinese Pidgin English
        "wet",  # Perai
        "lzl",  # Litzlitz
        "kkz",  # Kaska
        "mya",  # Burmese
        "okl",  # Old Kentish Sign Language
        "wuh",  # Wutunhua
        "pag",  # Pangasinan
        "dsb",  # Lower Sorbian
        "bxm",  # Mongolia Buriat
        "wuu",  # Wu Chinese
        "lgz",  # Ligenza
        "ayu",  # Ayu
        "txg",  # Tangut
        "daj",  # Dar Fur Daju
        "rau",  # Raute
        "mvn",  # Minaveha
        "kmt",  # Kemtuik
        "pas",  # Papasena
        "igg",  # Igana
        "xet",  # Xetá
        "xpb",  # Northeastern Tasmanian
        "gal",  # Galolen
        "tit",  # Tinigua
        "swi",  # Sui
        "tjg",  # Tunjung
        "wit",  # Wintu
        "acw",  # Hijazi Arabic
        "ays",  # Sorsogon Ayta
        "zmj",  # Maridjabin
        "wbl",  # Wakhi
        "kkf",  # Kalaktang Monpa
        "mkx",  # Kinamiging Manobo
        "ebk",  # Eastern Bontok
        "pmq",  # Northern Pame
        "tjp",  # Tjupany
        "bsx",  # Yangkam
        "vto",  # Vitou
        "ksq",  # Kwaami
        "hla",  # Halia
        "wnc",  # Wantoat
        "ckn",  # Kaang Chin
        "zyn",  # Yongnan Zhuang
        "ngd",  # Ngando (Central African Republic)
        "ewe",  # Ewe
        "kkn",  # Kon Keu
        "kyy",  # Kambaira
        "hmd",  # Large Flowery Miao
        "tel",  # Telugu
        "tbp",  # Taworta
        "sjk",  # Kemi Sami
        "dem",  # Dem
        "noi",  # Noiri
        "doh",  # Dong
        "lzn",  # Leinong Naga
        "bcs",  # Kohumono
        "mvc",  # Central Mam
        "bim",  # Bimoba
        "xpc",  # Pecheneg
        "ajz",  # Amri Karbi
        "uly",  # Buli
        "onu",  # Unua
        "bmq",  # Bomu
        "ypm",  # Phuma
        "hux",  # Nüpode Huitoto
        "sko",  # Seko Tengah
        "gyy",  # Gunya
        "tbn",  # Barro Negro Tunebo
        "kaj",  # Jju
        "bnc",  # Bontok
        "mzz",  # Maiadomu
        "pwa",  # Pawaia
        "asv",  # Asoa
        "mbv",  # Mbulungish
        "sjp",  # Surjapuri
        "yuj",  # Karkar-Yuri
        "quz",  # Cusco Quechua
        "kbp",  # Kabiyè
        "yib",  # Yinglish
        "zzj",  # Zuojiang Zhuang
        "nnb",  # Nande
        "ymb",  # Yambes
        "kzl",  # Kayeli
        "pak",  # Parakanã
        "dkl",  # Kolum So Dogon
        "kek",  # Kekchí
        "mnf",  # Mundani
        "kzb",  # Kaibobo
        "lhh",  # Laha (Indonesia)
        "fax",  # Fala
        "zaa",  # Sierra de Juárez Zapotec
        "ngm",  # Ngatik Men's Creole
        "glh",  # Northwest Pashai
        "bab",  # Bainouk-Gunyuño
        "not",  # Nomatsiguenga
        "sov",  # Sonsorol
        "lkh",  # Lakha
        "gaa",  # Ga
        "okn",  # Oki-No-Erabu
        "xyl",  # Yalakalore
        "nuw",  # Nguluwan
        "arx",  # Aruá (Rodonia State)
        "qxa",  # Chiquián Ancash Quechua
        "lnz",  # Lonzo
        "zro",  # Záparo
        "ran",  # Riantana
        "sep",  # Sìcìté Sénoufo
        "gaw",  # Nobonob
        "xkq",  # Koroni
        "bjk",  # Barok
        "pcf",  # Paliyan
        "igb",  # Ebira
        "agw",  # Kahua
        "tee",  # Huehuetla Tepehua
        "src",  # Logudorese Sardinian
        "kqb",  # Kovai
        "mzm",  # Mumuye
        "ckb",  # Central Kurdish
        "dim",  # Dime
        "dua",  # Duala
        "bdv",  # Bodo Parja
        "pmz",  # Southern Pame
        "sya",  # Siang
        "khk",  # Halh Mongolian
        "mtg",  # Una
        "kfy",  # Kumaoni
        "kos",  # Kosraean
        "nty",  # Mantsi
        "anm",  # Anal
        "mqd",  # Madang
        "ipi",  # Ipili
        "gnh",  # Lere
        "xni",  # Ngarigu
        "mdu",  # Mboko
        "kze",  # Kosena
        "mvi",  # Miyako
        "udm",  # Udmurt
        "yee",  # Yimas
        "zmh",  # Makolkol
        "bya",  # Batak
        "swk",  # Malawi Sena
        "kol",  # Kol (Papua New Guinea)
        "mav",  # Sateré-Mawé
        "utu",  # Utu
        "zmt",  # Maringarr
        "lip",  # Sekpele
        "xbb",  # Lower Burdekin
        "xpy",  # Puyo
        "swr",  # Saweru
        "mik",  # Mikasuki
        "sho",  # Shanga
        "bgt",  # Bughotu
        "tbe",  # Tanimbili
        "ado",  # Abu
        "dov",  # Dombe
        "jak",  # Jakun
        "phg",  # Phuong
        "bke",  # Bengkulu
        "blo",  # Anii
        "myp",  # Pirahã
        "auz",  # Uzbeki Arabic
        "qxc",  # Chincha Quechua
        "xvs",  # Vestinian
        "god",  # Godié
        "zap",  # Zapotec
        "ywl",  # Western Lalu
        "kpx",  # Mountain Koiali
        "akx",  # Aka-Kede
        "bmn",  # Bina (Papua New Guinea)
        "gih",  # Githabul
        "ngw",  # Ngwaba
        "loc",  # Inonhan
        "lac",  # Lacandon
        "lom",  # Loma (Liberia)
        "wrr",  # Wardaman
        "xrt",  # Aranama-Tamique
        "ide",  # Idere
        "emy",  # Epigraphic Mayan
        "kvr",  # Kerinci
        "orc",  # Orma
        "bva",  # Barein
        "dda",  # Dadi Dadi
        "tek",  # Ibali Teke
        "spm",  # Akukem
        "xna",  # Ancient North Arabian
        "agx",  # Aghul
        "sbk",  # Safwa
        "gon",  # Gondi
        "zbw",  # West Berawan
        "pug",  # Phuie
        "sni",  # Sensi
        "aob",  # Abom
        "mzw",  # Deg
        "kag",  # Kajaman
        "npo",  # Pochuri Naga
        "ope",  # Old Persian
        "ggr",  # Aghu Tharnggalu
        "mtu",  # Tututepec Mixtec
        "ndg",  # Ndengereko
        "tao",  # Yami
        "beh",  # Biali
        "mwz",  # Moingi
        "pgz",  # Papua New Guinean Sign Language
        "pcg",  # Paniya
        "nij",  # Ngaju
        "dgx",  # Doghoro
        "xac",  # Kachari
        "bhh",  # Bukharic
        "gnl",  # Gangulu
        "ytl",  # Tanglang
        "kqg",  # Khe
        "ata",  # Pele-Ata
        "azm",  # Ipalapa Amuzgo
        "cly",  # Eastern Highland Chatino
        "bxr",  # Russia Buriat
        "qwc",  # Classical Quechua
        "msx",  # Moresada
        "diw",  # Northwestern Dinka
        "kky",  # Guugu Yimidhirr
        "knd",  # Konda
        "njt",  # Ndyuka-Trio Pidgin
        "njx",  # Kunyi
        "nit",  # Southeastern Kolami
        "vis",  # Vishavan
        "cbo",  # Izora
        "tic",  # Tira
        "gaf",  # Gende
        "btg",  # Gagnoa Bété
        "kub",  # Kutep
        "pwm",  # Molbog
        "pbr",  # Pangwa
        "byd",  # Benyadu'
        "ypg",  # Phola
        "sjm",  # Mapun
        "mvh",  # Mulgi
        "nbj",  # Ngarinyman
        "ihi",  # Ihievbe
        "akm",  # Aka-Bo
        "kvw",  # Wersing
        "sav",  # Saafi-Saafi
        "kqv",  # Okolod
        "lek",  # Leipon
        "tba",  # Aikanã
        "brl",  # Birwa
        "hrp",  # Nhirrpi
        "ags",  # Esimbi
        "agu",  # Aguacateco
        "lab",  # Linear A
        "xml",  # Malaysian Sign Language
        "ind",  # Indonesian
        "luz",  # Southern Luri
        "dum",  # Middle Dutch (ca. 1050-1350)
        "mth",  # Munggui
        "ril",  # Riang Lang
        "mim",  # Alacatlatzala Mixtec
        "ikx",  # Ik
        "lua",  # Luba-Lulua
        "seb",  # Shempire Senoufo
        "azd",  # Eastern Durango Nahuatl
        "wsr",  # Owenia
        "pny",  # Pinyin
        "mom",  # Mangue
        "ngo",  # Ngoni
        "gbm",  # Garhwali
        "bls",  # Balaesang
        "flr",  # Fuliiru
        "pou",  # Southern Pokomam
        "yww",  # Yawarawarga
        "tyi",  # Teke-Tsaayi
        "mmb",  # Momina
        "dka",  # Dakpakha
        "agt",  # Central Cagayan Agta
        "rsn",  # Rwandan Sign Language
        "nqk",  # Kura Ede Nago
        "yey",  # Yeyi
        "myw",  # Muyuw
        "wkw",  # Wakawaka
        "fmu",  # Far Western Muria
        "ywq",  # Wuding-Luquan Yi
        "nmb",  # Big Nambas
        "xbx",  # Kabixí
        "ena",  # Apali
        "soq",  # Kanasi
        "cod",  # Cocama-Cocamilla
        "bik",  # Bikol
        "lrm",  # Marama
        "kdx",  # Kam
        "lei",  # Lemio
        "mtl",  # Montol
        "zpr",  # Santiago Xanica Zapotec
        "rjg",  # Rajong
        "tcb",  # Tanacross
        "ite",  # Itene
        "emb",  # Embaloh
        "try",  # Turung
        "knt",  # Panoan Katukína
        "mvq",  # Moere
        "tdk",  # Tambas
        "lir",  # Liberian English
        "bec",  # Iceve-Maci
        "mrc",  # Maricopa
        "csh",  # Asho Chin
        "xii",  # Xiri
        "vkl",  # Kulisusu
        "gvs",  # Gumawana
        "wgu",  # Wirangu
        "ets",  # Yekhee
        "afh",  # Afrihili
        "mcl",  # Macaguaje
        "lbm",  # Lodhi
        "bmg",  # Bamwe
        "llq",  # Lolak
        "wlk",  # Wailaki
        "bjc",  # Bariji
        "ksm",  # Kumba
        "aph",  # Athpariya
        "kjb",  # Q'anjob'al
        "bfd",  # Bafut
        "xte",  # Ketengban
        "nby",  # Ningera
        "pnd",  # Mpinda
        "abr",  # Abron
        "myq",  # Forest Maninka
        "rit",  # Ritharrngu
        "auv",  # Auvergnat
        "nhu",  # Noone
        "qvp",  # Pacaraos Quechua
        "njl",  # Njalgulgule
        "mze",  # Morawa
        "xaj",  # Ararandewára
        "onx",  # Onin Based Pidgin
        "tlf",  # Telefol
        "ani",  # Andi
        "mqx",  # Mamuju
        "mxn",  # Moi (Indonesia)
        "kyf",  # Kouya
        "imt",  # Imotong
        "tqb",  # Tembé
        "bwp",  # Mandobo Bawah
        "cob",  # Chicomuceltec
        "run",  # Rundi
        "top",  # Papantla Totonac
        "lsm",  # Saamia
        "mib",  # Atatláhuca Mixtec
        "sab",  # Buglere
        "ckm",  # Chakavian
        "atm",  # Ata
        "ppl",  # Pipil
        "lsa",  # Lasgerdi
        "kki",  # Kagulu
        "kzo",  # Kaningi
        "ynb",  # Yamben
        "sps",  # Saposa
        "urd",  # Urdu
        "kcz",  # Konongo
        "wth",  # Wathawurrung
        "aqm",  # Atohwaim
        "knb",  # Lubuagan Kalinga
        "ncx",  # Central Puebla Nahuatl
        "dks",  # Southeastern Dinka
        "ulm",  # Ulumanda'
        "ork",  # Orokaiva
        "bkt",  # Boloki
        "adh",  # Adhola
        "tvm",  # Tela-Masbuar
        "esq",  # Esselen
        "maj",  # Jalapa De Díaz Mazatec
        "twn",  # Twendi
        "nyw",  # Nyaw
        "coj",  # Cochimi
        "tkm",  # Takelma
        "iwo",  # Iwur
        "iow",  # Iowa-Oto
        "kqo",  # Eastern Krahn
        "iqu",  # Iquito
        "aam",  # Aramanik
        "cjs",  # Shor
        "ywn",  # Yawanawa
        "loj",  # Lou
        "gbh",  # Defi Gbe
        "msi",  # Sabah Malay
        "fse",  # Finnish Sign Language
        "rkt",  # Rangpuri
        "nhk",  # Isthmus-Cosoleacaque Nahuatl
        "glv",  # Manx
        "bdl",  # Indonesian Bajau
        "csl",  # Chinese Sign Language
        "jat",  # Jakati
        "due",  # Umiray Dumaget Agta
        "gye",  # Gyem
        "mvm",  # Muya
        "mns",  # Mansi
        "inn",  # Isinai
        "tpz",  # Tinputz
        "tti",  # Tobati
        "aoa",  # Angolar
        "kwa",  # Dâw
        "kff",  # Koya
        "nbu",  # Rongmei Naga
        "pwo",  # Pwo Western Karen
        "pcm",  # Nigerian Pidgin
        "dyk",  # Land Dayak
        "dak",  # Dakota
        "nri",  # Chokri Naga
        "lal",  # Lalia
        "cmm",  # Michigamea
        "dof",  # Domu
        "npn",  # Mondropolon
        "iti",  # Inlaod Itneg
        "oro",  # Orokolo
        "luh",  # Leizhou Chinese
        "bjx",  # Banao Itneg
        "isu",  # Isu (Menchum Division)
        "kbm",  # Iwal
        "bsm",  # Busami
        "nsy",  # Nasal
        "pnh",  # Penrhyn
        "ndj",  # Ndamba
        "kmk",  # Limos Kalinga
        "ndn",  # Ngundi
        "bvj",  # Baan
        "enc",  # En
        "fum",  # Fum
        "mfm",  # Marghi South
        "myg",  # Manta
        "nhz",  # Santa María La Alta Nahuatl
        "krd",  # Kairui-Midiki
        "srs",  # Sarsi
        "tcc",  # Datooga
        "aui",  # Anuki
        "kcp",  # Kanga
        "rri",  # Ririo
        "klb",  # Kiliwa
        "tpw",  # Tupí
        "inp",  # Iñapari
        "oin",  # Inebu One
        "biu",  # Biete
        "mdg",  # Massalat
        "wom",  # Wom (Nigeria)
        "ije",  # Biseni
        "pgu",  # Pagu
        "hoe",  # Horom
        "zca",  # Coatecas Altas Zapotec
        "mwy",  # Mosiro
        "kcg",  # Tyap
        "hvk",  # Haveke
        "mvo",  # Marovo
        "njd",  # Ndonde Hamba
        "tay",  # Atayal
        "ncj",  # Northern Puebla Nahuatl
        "ckr",  # Kairak
        "siz",  # Siwi
        "axl",  # Lower Southern Aranda
        "ndp",  # Ndo
        "yul",  # Yulu
        "asb",  # Assiniboine
        "ddd",  # Dongotono
        "ifk",  # Tuwali Ifugao
        "kea",  # Kabuverdianu
        "sod",  # Songoora
        "esy",  # Eskayan
        "urz",  # Uru-Eu-Wau-Wau
        "nyv",  # Nyulnyul
        "lgk",  # Lingarak
        "ych",  # Chesu
        "vmd",  # Mudu Koraga
        "agd",  # Agarabi
        "xgw",  # Guwa
        "phd",  # Phudagi
        "ksd",  # Kuanua
        "bxa",  # Tairaha
        "okx",  # Okpe (Northwestern Edo)
        "cns",  # Central Asmat
        "knr",  # Kaningra
        "tri",  # Trió
        "mob",  # Moinba
        "prq",  # Ashéninka Perené
        "dox",  # Bussa
        "lts",  # Tachoni
        "ygp",  # Gepo
        "imo",  # Imbongu
        "vol",  # Volapük
        "ida",  # Idakho-Isukha-Tiriki
        "phn",  # Phoenician
        "xtl",  # Tijaltepec Mixtec
        "tqm",  # Turumsa
        "pka",  # Ardhamāgadhī Prākrit
        "jeg",  # Jeng
        "zaw",  # Mitla Zapotec
        "bwq",  # Southern Bobo Madaré
        "tcg",  # Tamagario
        "bqm",  # Wumboko
        "lmi",  # Lombi
        "yss",  # Yessan-Mayo
        "bjs",  # Bajan
        "kvf",  # Kabalai
        "ash",  # Abishira
        "mpz",  # Mpi
        "ghh",  # Northern Ghale
        "nnc",  # Nancere
        "giq",  # Green Gelao
        "ysr",  # Sirenik Yupik
        "gym",  # Ngäbere
        "sil",  # Tumulung Sisaala
        "tnu",  # Tay Khang
        "tru",  # Turoyo
        "kzd",  # Kadai
        "mjk",  # Matukar
        "kcf",  # Ukaan
        "std",  # Sentinel
        "ekp",  # Ekpeye
        "ilb",  # Ila
        "mjd",  # Northwest Maidu
        "moa",  # Mwan
        "gbs",  # Gbesi Gbe
        "jay",  # Yan-nhangu
        "kku",  # Tumi
        "jor",  # Jorá
        "rei",  # Reli
        "pmk",  # Pamlico
        "gle",  # Irish
        "cbc",  # Carapana
        "aue",  # ǂKxʼauǁʼein
        "luc",  # Aringa
        "mcv",  # Minanibai
        "tqq",  # Tunni
        "aux",  # Aurá
        "azj",  # North Azerbaijani
        "pmx",  # Poumei Naga
        "nax",  # Nakwi
        "txi",  # Ikpeng
        "xby",  # Batjala
        "kdp",  # Kaningdon-Nindem
        "ibe",  # Akpes
        "sgc",  # Kipsigis
        "buu",  # Budu
        "sdi",  # Sindang Kelingi
        "wmw",  # Mwani
        "ceb",  # Cebuano
        "emw",  # Emplawas
        "eit",  # Eitiep
        "mii",  # Chigmecatitlán Mixtec
        "ofo",  # Ofo
        "bwk",  # Bauwaki
        "xmr",  # Meroitic
        "mmt",  # Malalamai
        "sta",  # Settla
        "tou",  # Tho
        "txa",  # Tombonuo
        "sdn",  # Gallurese Sardinian
        "kca",  # Khanty
        "sez",  # Senthang Chin
        "kcq",  # Kamo
        "ukp",  # Ukpe-Bayobiri
        "xdy",  # Malayic Dayak
        "pll",  # Shwe Palaung
        "yns",  # Yansi
        "baw",  # Bambili-Bambui
        "sxr",  # Saaroa
        "kvx",  # Parkari Koli
        "kej",  # Kadar
        "usp",  # Uspanteco
        "zns",  # Mangas
        "pan",  # Panjabi
        "kmi",  # Kami (Nigeria)
        "yyz",  # Ayizi
        "aar",  # Afar
        "caj",  # Chané
        "nye",  # Nyengo
        "mhn",  # Mócheno
        "jbk",  # Barikewa
        "bvr",  # Burarra
        "lmk",  # Lamkang
        "dha",  # Dhanwar (India)
        "nxg",  # Ngad'a
        "aye",  # Ayere
        "rng",  # Ronga
        "bul",  # Bulgarian
        "mny",  # Manyawa
        "mkr",  # Malas
        "toe",  # Tomedes
        "brb",  # Brao
        "ywg",  # Yinhawangka
        "rkh",  # Rakahanga-Manihiki
        "bth",  # Biatah Bidayuh
        "shr",  # Shi
        "tub",  # Tübatulabal
        "bgz",  # Banggai
        "atq",  # Aralle-Tabulahan
        "mzb",  # Tumzabt
        "sjr",  # Siar-Lak
        "nkb",  # Khoibu Naga
        "sdo",  # Bukar-Sadung Bidayuh
        "tsl",  # Ts'ün-Lao
        "gmu",  # Gumalu
        "bte",  # Gamo-Ningi
        "meu",  # Motu
        "ykn",  # Kua-nsi
        "mpu",  # Makuráp
        "auo",  # Auyokawa
        "tdi",  # Tomadino
        "bax",  # Bamun
        "min",  # Minangkabau
        "bmi",  # Bagirmi
        "tgy",  # Togoyo
        "kxn",  # Kanowit-Tanjong Melanau
        "plv",  # Southwest Palawano
        "sdq",  # Semandang
        "sds",  # Sened
        "sjn",  # Sindarin
        "swb",  # Maore Comorian
        "xpz",  # Bruny Island Tasmanian
        "aqt",  # Angaité
        "mta",  # Cotabato Manobo
        "mre",  # Martha's Vineyard Sign Language
        "sde",  # Surubu
        "chk",  # Chuukese
        "esu",  # Central Yupik
        "jbo",  # Lojban
        "nkq",  # Nkami
        "mlg",  # Malagasy
        "tcz",  # Thado Chin
        "xco",  # Chorasmian
        "don",  # Toura (Papua New Guinea)
        "bty",  # Bobot
        "wub",  # Wunambal
        "xod",  # Kokoda
        "krc",  # Karachay-Balkar
        "yev",  # Yapunda
        "ify",  # Keley-I Kallahan
        "lul",  # Olu'bo
        "dip",  # Northeastern Dinka
        "ria",  # Riang (India)
        "blf",  # Buol
        "coc",  # Cocopa
        "mut",  # Western Muria
        "yia",  # Yinggarda
        "cnm",  # Ixtatán Chuj
        "yiz",  # Azhe
        "pum",  # Puma
        "jya",  # Jiarong
        "hgm",  # Haiǁom
        "lia",  # West-Central Limba
        "koa",  # Konomala
        "vmq",  # Soyaltepec Mixtec
        "msu",  # Musom
        "wme",  # Wambule
        "pps",  # San Luís Temalacayuca Popoloca
        "pdt",  # Plautdietsch
        "sop",  # Songe
        "otk",  # Old Turkish
        "mdo",  # Southwest Gbaya
        "alw",  # Alaba-K’abeena
        "mme",  # Mae
        "ome",  # Omejes
        "gog",  # Gogo
        "rsk",  # Ruthenian
        "brj",  # Bieria
        "dgz",  # Daga
        "bvy",  # Baybayanon
        "kne",  # Kankanaey
        "zpy",  # Mazaltepec Zapotec
        "ztn",  # Santa Catarina Albarradas Zapotec
        "kac",  # Kachin
        "duc",  # Duna
        "ttd",  # Tauade
        "lsb",  # Burundian Sign Language
        "irr",  # Ir
        "ldm",  # Landoma
        "emi",  # Mussau-Emira
        "itl",  # Itelmen
        "caz",  # Canichana
        "kah",  # Kara (Central African Republic)
        "kox",  # Coxima
        "ayn",  # Sanaani Arabic
        "sfm",  # Small Flowery Miao
        "myd",  # Maramba
        "mro",  # Mru
        "nbn",  # Kuri
        "til",  # Tillamook
        "xvo",  # Volscian
        "ncd",  # Nachering
        "jiq",  # Guanyinqiao
        "ckw",  # Western Cakchiquel
        "mlo",  # Mlomp
        "jmi",  # Jimi (Nigeria)
        "ebu",  # Embu
        "llu",  # Lau
        "bvi",  # Belanda Viri
        "dbj",  # Ida'an
        "cpu",  # Pichis Ashéninka
        "mzq",  # Mori Atas
        "jaj",  # Zazao
        "nma",  # Maram Naga
        "han",  # Hangaza
        "ras",  # Tegali
        "msw",  # Mansoanka
        "jgb",  # Ngbee
        "kys",  # Baram Kayan
        "tno",  # Toromono
        "gdd",  # Gedaged
        "hrt",  # Hértevin
        "urr",  # Lehalurup
        "fuu",  # Furu
        "gvj",  # Guajá
        "dun",  # Dusun Deyah
        "ynq",  # Yendang
        "mrj",  # Western Mari
        "ypp",  # Phupa
        "npu",  # Puimei Naga
        "ajt",  # Judeo-Tunisian Arabic
        "moz",  # Mukulu
        "sqh",  # Shau
        "sul",  # Surigaonon
        "gni",  # Gooniyandi
        "vep",  # Veps
        "bjt",  # Balanta-Ganja
        "hid",  # Hidatsa
        "obt",  # Old Breton
        "mfb",  # Bangka
        "gno",  # Northern Gondi
        "umi",  # Ukit
        "twm",  # Tawang Monpa
        "kpb",  # Mullu Kurumba
        "npb",  # Nupbikha
        "kvu",  # Yinbaw Karen
        "dnj",  # Dan
        "ddn",  # Dendi (Benin)
        "suq",  # Tirmaga-Chai Suri
        "plg",  # Pilagá
        "txu",  # Kayapó
        "upv",  # Uripiv-Wala-Rano-Atchin
        "emn",  # Eman
        "zil",  # Zialo
        "kci",  # Kamantan
        "bgn",  # Western Balochi
        "rgn",  # Romagnol
        "sak",  # Sake
        "zsk",  # Kaskean
        "aks",  # Akaselem
        "aoc",  # Pemon
        "dws",  # Dutton World Speedwords
        "sax",  # Sa
        "zpk",  # Tlacolulita Zapotec
        "bvt",  # Bati (Indonesia)
        "plb",  # Polonombauk
        "wsg",  # Adilabad Gondi
        "bnl",  # Boon
        "keq",  # Kamar
        "mjl",  # Mandeali
        "hrx",  # Hunsrik
        "ssz",  # Sengseng
        "mcb",  # Machiguenga
        "rdb",  # Rudbari
        "nuv",  # Northern Nuni
        "mdq",  # Mbole
        "nbp",  # Nnam
        "waf",  # Wakoná
        "gbw",  # Gabi-Gabi
        "kpt",  # Karata
        "mxg",  # Mbangala
        "str",  # Straits Salish
        "fon",  # Fon
        "cma",  # Maa
        "bjo",  # Mid-Southern Banda
        "wwb",  # Wakabunga
        "kmg",  # Kâte
        "tgg",  # Tangga
        "lic",  # Hlai
        "sig",  # Paasaal
        "lih",  # Lihir
        "nkc",  # Nkongho
        "dlg",  # Dolgan
        "mhc",  # Mocho
        "pbv",  # Pnar
        "kai",  # Karekare
        "ren",  # Rengao
        "bii",  # Bisu
        "bcy",  # Bacama
        "neb",  # Toura (Côte d'Ivoire)
        "lrn",  # Lorang
        "sru",  # Suruí
        "tpx",  # Acatepec Me'phaa
        "yip",  # Pholo
        "knu",  # Kono (Guinea)
        "wag",  # Wa'ema
        "khz",  # Keapara
        "eya",  # Eyak
        "zpf",  # San Pedro Quiatoni Zapotec
        "jen",  # Dza
        "meh",  # Southwestern Tlaxiaco Mixtec
        "kbi",  # Kaptiau
        "nab",  # Southern Nambikuára
        "ush",  # Ushojo
        "eyo",  # Keiyo
        "cfa",  # Dijim-Bwilim
        "kna",  # Dera (Nigeria)
        "mgu",  # Mailu
        "lob",  # Lobi
        "mct",  # Mengisa
        "jer",  # Jere
        "ibu",  # Ibu
        "twu",  # Termanu
        "dyo",  # Jola-Fonyi
        "csz",  # Coos
        "mdc",  # Male (Papua New Guinea)
        "paf",  # Paranawát
        "zne",  # Zande (individual language)
        "mgv",  # Matengo
        "kid",  # Koshin
        "prf",  # Paranan
        "xnh",  # Kuanhua
        "ruy",  # Mala (Nigeria)
        "pro",  # Old Provençal (to 1500)
        "ojw",  # Western Ojibwa
        "mhw",  # Mbukushu
        "tol",  # Tolowa
        "bbn",  # Uneapa
        "nrp",  # North Picene
        "dan",  # Danish
        "glu",  # Gula (Chad)
        "lim",  # Limburgan
        "zhw",  # Zhoa
        "lel",  # Lele (Democratic Republic of Congo)
        "fra",  # French
        "fss",  # Finland-Swedish Sign Language
        "rme",  # Angloromani
        "kir",  # Kirghiz
        "xai",  # Kaimbé
        "xbm",  # Middle Breton
        "shd",  # Kundal Shahi
        "kzu",  # Kayupulau
        "leq",  # Lembena
        "ciw",  # Chippewa
        "xtg",  # Transalpine Gaulish
        "gbu",  # Gagadu
        "mds",  # Maria (Papua New Guinea)
        "alm",  # Amblong
        "ayb",  # Ayizo Gbe
        "kuy",  # Kuuku-Ya'u
        "tpo",  # Tai Pao
        "wux",  # Wulna
        "kpk",  # Kpan
        "bbm",  # Babango
        "akn",  # Amikoana
        "siw",  # Siwai
        "att",  # Pamplona Atta
        "lie",  # Likila
        "otn",  # Tenango Otomi
        "kzm",  # Kais
        "dti",  # Ana Tinga Dogon
        "lez",  # Lezghian
        "wms",  # Wambon
        "itu",  # Itutang
        "krm",  # Krim
        "mwr",  # Marwari
        "ken",  # Kenyang
        "kvc",  # Kove
        "ldd",  # Luri
        "gad",  # Gaddang
        "rae",  # Ranau
        "pth",  # Pataxó Hã-Ha-Hãe
        "bbg",  # Barama
        "sdx",  # Sibu Melanau
        "otw",  # Ottawa
        "nuz",  # Tlamacazapa Nahuatl
        "rro",  # Waima
        "sks",  # Maia
        "tsh",  # Tsuvan
        "lus",  # Lushai
        "rmh",  # Murkim
        "kwr",  # Kwer
        "nng",  # Maring Naga
        "plp",  # Palpa
        "dnw",  # Western Dani
        "rax",  # Rang
        "kel",  # Kela (Democratic Republic of Congo)
        "peq",  # Southern Pomo
        "zpp",  # El Alto Zapotec
        "mol",  # Moldavian
        "oyy",  # Oya'oya
        "btu",  # Batu
        "bib",  # Bissa
        "eso",  # Estonian Sign Language
        "dbb",  # Deno
        "lja",  # Golpa
        "gel",  # ut-Ma'in
        "waa",  # Walla Walla
        "xly",  # Elymian
        "lnd",  # Lundayeh
        "pbb",  # Páez
        "nms",  # Letemboi
        "xnn",  # Northern Kankanay
        "iru",  # Irula
        "wan",  # Wan
        "mma",  # Mama
        "kvi",  # Kwang
        "raj",  # Rajasthani
        "urx",  # Urimo
        "crn",  # El Nayar Cora
        "otl",  # Tilapa Otomi
        "brf",  # Bira
        "bqn",  # Bulgarian Sign Language
        "pwn",  # Paiwan
        "tbx",  # Kapin
        "xct",  # Classical Tibetan
        "ule",  # Lule
        "kbc",  # Kadiwéu
        "tld",  # Talaud
        "bep",  # Besoa
        "zpd",  # Southeastern Ixtlán Zapotec
        "tvx",  # Taivoan
        "htx",  # Middle Hittite
        "ile",  # Interlingue
        "cad",  # Caddo
        "kjk",  # Highland Konjo
        "nuo",  # Nguôn
        "wca",  # Yanomámi
        "xkk",  # Kachok
        "pax",  # Pankararé
        "plm",  # Palembang
        "wtb",  # Matambwe
        "kpw",  # Kobon
        "kme",  # Bakole
        "ams",  # Southern Amami-Oshima
        "zak",  # Zanaki
        "pml",  # Lingua Franca
        "mwg",  # Aiklep
        "atk",  # Ati
        "dsi",  # Disa
        "plj",  # Polci
        "tvi",  # Tulai
        "skr",  # Saraiki
        "xwe",  # Xwela Gbe
        "kcw",  # Kabwari
        "mdr",  # Mandar
        "ktg",  # Kalkutung
        "law",  # Lauje
        "pej",  # Northern Pomo
        "eky",  # Eastern Kayah
        "wmb",  # Wambaya
        "bdn",  # Baldemu
        "git",  # Gitxsan
        "axg",  # Mato Grosso Arára
        "kew",  # West Kewa
        "asf",  # Auslan
        "ajw",  # Ajawa
        "abu",  # Abure
        "que",  # Quechua
        "zgn",  # Guibian Zhuang
        "pat",  # Papitalai
        "ues",  # Kioko
        "lgl",  # Wala
        "aox",  # Atorada
        "hmf",  # Hmong Don
        "lsn",  # Tibetan Sign Language
        "djo",  # Jangkang
        "pcn",  # Piti
        "xbg",  # Bunganditj
        "pnj",  # Pinjarup
        "wai",  # Wares
        "kcy",  # Korandje
        "sag",  # Sango
        "nxu",  # Narau
        "seh",  # Sena
        "pbu",  # Northern Pashto
        "rgu",  # Ringgou
        "zkg",  # Koguryo
        "rav",  # Sampang
        "ats",  # Gros Ventre
        "kjx",  # Ramopa
        "aeu",  # Akeu
        "zas",  # Santo Domingo Albarradas Zapotec
        "nyo",  # Nyoro
        "nkx",  # Nkoroo
        "cni",  # Asháninka
        "ndc",  # Ndau
        "com",  # Comanche
        "ngq",  # Ngurimi
        "xtd",  # Diuxi-Tilantongo Mixtec
        "aha",  # Ahanta
        "kgk",  # Kaiwá
        "sce",  # Dongxiang
        "neo",  # Ná-Meo
        "wbf",  # Wara
        "yuk",  # Yuki
        "dln",  # Darlong
        "ywt",  # Xishanba Lalo
        "giz",  # South Giziga
        "ssr",  # Swiss-French Sign Language
        "ghe",  # Southern Ghale
        "nef",  # Nefamese
        "mxy",  # Southeastern Nochixtlán Mixtec
        "bfn",  # Bunak
        "yiu",  # Awu
        "sdk",  # Sos Kundi
        "fla",  # Kalispel-Pend d'Oreille
        "cst",  # Northern Ohlone
        "agb",  # Legbo
        "hms",  # Southern Qiandong Miao
        "nnq",  # Ngindo
        "das",  # Daho-Doo
        "enw",  # Enwan (Akwa Ibom State)
        "gcf",  # Guadeloupean Creole French
        "mra",  # Mlabri
        "cbb",  # Cabiyarí
        "say",  # Saya
        "yai",  # Yagnobi
        "suu",  # Sungkai
        "gmm",  # Gbaya-Mbodomo
        "cks",  # Tayo
        "ekm",  # Elip
        "bqj",  # Bandial
        "csj",  # Songlai Chin
        "goo",  # Gone Dau
        "lbk",  # Central Bontok
        "kfw",  # Kharam Naga
        "ler",  # Lenkau
        "slb",  # Kahumamahon Saluan
        "xcl",  # Classical Armenian
        "eki",  # Eki
        "heh",  # Hehe
        "xkt",  # Kantosi
        "tbd",  # Kaki Ae
        "moy",  # Shekkacho
        "wkb",  # Kumbaran
        "xua",  # Alu Kurumba
        "azb",  # South Azerbaijani
        "tpk",  # Tupinikin
        "kwp",  # Kodia
        "xdo",  # Kwandu
        "enx",  # Enxet
        "bfm",  # Mmen
        "rmw",  # Welsh Romani
        "xtb",  # Chazumba Mixtec
        "dre",  # Dolpo
        "kwe",  # Kwerba
        "bou",  # Bondei
        "mxt",  # Jamiltepec Mixtec
        "mgb",  # Mararit
        "xnj",  # Ngoni (Tanzania)
        "bca",  # Central Bai
        "zib",  # Zimbabwe Sign Language
        "anv",  # Denya
        "wsi",  # Wusi
        "cfd",  # Cara
        "eze",  # Uzekwe
        "czo",  # Min Zhong Chinese
        "sgd",  # Surigaonon
        "kqn",  # Kaonde
        "djk",  # Eastern Maroon Creole
        "swa",  # Swahili (macrolanguage)
        "bhj",  # Bahing
        "hsl",  # Hausa Sign Language
        "mkf",  # Miya
        "aae",  # Arbëreshë Albanian
        "agi",  # Agariya
        "wrh",  # Wiradjuri
        "yio",  # Dayao Yi
        "daz",  # Moi-Wadea
        "lat",  # Latin
        "xab",  # Sambe
        "omc",  # Mochica
        "ssm",  # Semnam
        "mng",  # Eastern Mnong
        "sol",  # Solos
        "cuq",  # Cun
        "hlb",  # Halbi
        "ikl",  # Ikulu
        "ntu",  # Natügu
        "keu",  # Akebu
        "kgq",  # Kamoro
        "meo",  # Kedah Malay
        "mbf",  # Baba Malay
        "oie",  # Okolie
        "jia",  # Jina
        "bhw",  # Biak
        "bkq",  # Bakairí
        "pel",  # Pekal
        "kkp",  # Gugubera
        "xxt",  # Tambora
        "ncg",  # Nisga'a
        "bym",  # Bidjara
        "nem",  # Nemi
        "lxm",  # Lakurumau
        "fin",  # Finnish
        "bal",  # Baluchi
        "arf",  # Arafundi
        "xsi",  # Sio
        "tbc",  # Takia
        "poa",  # Eastern Pokomam
        "axb",  # Abipon
        "kml",  # Tanudan Kalinga
        "hai",  # Haida
        "pgk",  # Rerep
        "apb",  # Sa'a
        "psn",  # Panasuan
        "lui",  # Luiseno
        "cnq",  # Chung
        "mes",  # Masmaje
        "qvs",  # San Martín Quechua
        "rwm",  # Amba (Uganda)
        "sif",  # Siamou
        "kxr",  # Koro (Papua New Guinea)
        "laa",  # Southern Subanen
        "bnk",  # Bierebo
        "lni",  # Daantanai'
        "ykl",  # Khlula
        "nho",  # Takuu
        "soa",  # Thai Song
        "ddo",  # Dido
        "ziw",  # Zigula
        "omn",  # Minoan
        "kkk",  # Kokota
        "myh",  # Makah
        "xrb",  # Eastern Karaboro
        "mch",  # Maquiritari
        "jhs",  # Jhankot Sign Language
        "tih",  # Timugon Murut
        "osu",  # Southern One
        "chz",  # Ozumacín Chinantec
        "itr",  # Iteri
        "kyo",  # Kelon
        "chx",  # Chantyal
        "kxt",  # Koiwat
        "zms",  # Mbesa
        "mul",  # Multiple languages
        "kvh",  # Komodo
        "hoj",  # Hadothi
        "kbn",  # Kare (Central African Republic)
        "rki",  # Rakhine
        "ktm",  # Kurti
        "llb",  # Lolo
        "dob",  # Dobu
        "tst",  # Tondi Songway Kiini
        "adu",  # Aduge
        "lhs",  # Mlahsö
        "mwq",  # Mün Chin
        "naw",  # Nawuri
        "atg",  # Ivbie North-Okpela-Arhe
        "sou",  # Southern Thai
        "acl",  # Akar-Bale
        "nei",  # Neo-Hittite
        "ifa",  # Amganad Ifugao
        "mpl",  # Middle Watut
        "sqq",  # Sou
        "rmt",  # Domari
        "byk",  # Biao
        "kly",  # Kalao
        "mgl",  # Maleu-Kilenge
        "aso",  # Dano
        "jam",  # Jamaican Creole English
        "pnn",  # Pinai-Hagahai
        "mqo",  # Modole
        "mwc",  # Are
        "baf",  # Nubaca
        "mqq",  # Minokok
        "oti",  # Oti
        "koj",  # Sara Dunjo
        "hpo",  # Hpon
        "gir",  # Red Gelao
        "syx",  # Samay
        "zmx",  # Bomitaba
        "wbt",  # Warnman
        "oke",  # Okpe (Southwestern Edo)
        "rmr",  # Caló
        "gku",  # ǂUngkue
        "lto",  # Tsotso
        "mjo",  # Malankuravan
        "nlm",  # Mankiyali
        "nkt",  # Nyika (Tanzania)
        "gue",  # Gurindji
        "nac",  # Narak
        "hmt",  # Hamtai
        "wei",  # Kiunum
        "rjs",  # Rajbanshi
        "xse",  # Sempan
        "rwo",  # Rawa
        "ojg",  # Eastern Ojibwa
        "lji",  # Laiyolo
        "sbg",  # Seget
        "rer",  # Rer Bare
        "mpr",  # Vangunu
        "lvs",  # Standard Latvian
        "xut",  # Kuthant
        "dsl",  # Danish Sign Language
        "toj",  # Tojolabal
        "kdt",  # Kuy
        "zkk",  # Karankawa
        "dno",  # Ndrulo
        "ixi",  # Nebaj Ixil
        "aiw",  # Aari
        "ctz",  # Zacatepec Chatino
        "bzr",  # Biri
        "guh",  # Guahibo
        "tlb",  # Tobelo
        "jab",  # Hyam
        "wim",  # Wik-Mungkan
        "mbr",  # Nukak Makú
        "jee",  # Jerung
        "czn",  # Zenzontepec Chatino
        "swx",  # Suruahá
        "tby",  # Tabaru
        "pks",  # Pakistan Sign Language
        "nlj",  # Nyali
        "kfu",  # Katkari
        "mjx",  # Mahali
        "khj",  # Kuturmi
        "rhp",  # Yahang
        "bij",  # Vaghat-Ya-Bijim-Legeri
        "kli",  # Kalumpang
        "gen",  # Geman Deng
        "ntw",  # Nottoway
        "pen",  # Penesak
        "krb",  # Karkin
        "byb",  # Bikya
        "kma",  # Konni
        "var",  # Huarijio
        "oca",  # Ocaina
        "ker",  # Kera
        "clj",  # Laitu Chin
        "lpe",  # Lepki
        "mjr",  # Malavedan
        "mls",  # Masalit
        "pbm",  # Puebla Mazatec
        "aka",  # Akan
        "xjt",  # Jaitmatang
        "bdb",  # Basap
        "sdp",  # Sherdukpen
        "yet",  # Yetfa
        "bow",  # Rema
        "xdq",  # Kaitag
        "jib",  # Jibu
        "tua",  # Wiarumus
        "uvh",  # Uri
        "rsm",  # Miriwoong Sign Language
        "klg",  # Tagakaulo
        "jmw",  # Mouwase
        "aon",  # Bumbita Arapesh
        "clk",  # Idu-Mishmi
        "bql",  # Karian
        "buc",  # Bushi
        "mhi",  # Ma'di
        "wgo",  # Waigeo
        "lpx",  # Lopit
        "dgw",  # Daungwurrung
        "hmk",  # Maek
        "cok",  # Santa Teresa Cora
        "toc",  # Coyutla Totonac
        "grv",  # Central Grebo
        "dva",  # Duau
        "kyr",  # Kuruáya
        "tau",  # Upper Tanana
        "mjt",  # Sauria Paharia
        "zpa",  # Lachiguiri Zapotec
        "dww",  # Dawawa
        "eto",  # Eton (Cameroon)
        "kyp",  # Kang
        "lil",  # Lillooet
        "nzk",  # Nzakara
        "tas",  # Tay Boi
        "vag",  # Vagla
        "tzt",  # Western Tzutujil
        "ndi",  # Samba Leko
        "tsx",  # Mubami
        "buz",  # Bukwen
        "apx",  # Aputai
        "roe",  # Ronji
        "bwv",  # Bahau River Kenyah
        "heb",  # Hebrew
        "skp",  # Sekapan
        "auk",  # Heyo
        "rkw",  # Arakwal
        "imr",  # Imroing
        "sqn",  # Susquehannock
        "cmi",  # Emberá-Chamí
        "yrn",  # Yerong
        "bug",  # Buginese
        "nnk",  # Nankina
        "bxh",  # Buhutu
        "juo",  # Jiba
        "gmz",  # Mgbolizhia
        "llx",  # Lauan
        "uon",  # Kulon
        "asg",  # Cishingini
        "hnn",  # Hanunoo
        "zhn",  # Nong Zhuang
        "gus",  # Guinean Sign Language
        "pha",  # Pa-Hng
        "dnk",  # Dengka
        "kfx",  # Kullu Pahari
        "tnc",  # Tanimuca-Retuarã
        "ste",  # Liana-Seti
        "pnu",  # Jiongnai Bunu
        "xki",  # Kenyan Sign Language
        "nxj",  # Nyadu
        "twl",  # Tawara
        "ror",  # Rongga
        "nal",  # Nalik
        "pnw",  # Banyjima
        "ppo",  # Folopa
        "tci",  # Wára
        "tos",  # Highland Totonac
        "vms",  # Moksela
        "obo",  # Obo Manobo
        "ruu",  # Lanas Lobu
        "skj",  # Seke (Nepal)
        "pfl",  # Pfaelzisch
        "ayl",  # Libyan Arabic
        "ary",  # Moroccan Arabic
        "smb",  # Simbari
        "mde",  # Maba (Chad)
        "wku",  # Kunduvadi
        "yuf",  # Havasupai-Walapai-Yavapai
        "lqr",  # Logir
        "uok",  # Uokha
        "pic",  # Pinji
        "yrk",  # Nenets
        "ykt",  # Kathu
        "ehs",  # Miyakubo Sign Language
        "pce",  # Ruching Palaung
        "nvh",  # Nasarian
        "clo",  # Lowland Oaxaca Chontal
        "ksw",  # S'gaw Karen
        "wre",  # Ware
        "wkr",  # Keerray-Woorroong
        "ngy",  # Tibea
        "xcr",  # Carian
        "srm",  # Saramaccan
        "kfb",  # Northwestern Kolami
        "bfy",  # Bagheli
        "laq",  # Qabiao
        "kch",  # Vono
        "kdq",  # Koch
        "tlw",  # South Wemale
        "grn",  # Guarani
        "xbj",  # Birrpayi
        "prl",  # Peruvian Sign Language
        "las",  # Lama (Togo)
        "ita",  # Italian
        "kym",  # Kpatili
        "otu",  # Otuke
        "drb",  # Dair
        "kmo",  # Kwoma
        "mww",  # Hmong Daw
        "irx",  # Kamberau
        "phv",  # Pahlavani
        "tgc",  # Tigak
        "mda",  # Mada (Nigeria)
        "nct",  # Chothe Naga
        "npg",  # Ponyo-Gongwang Naga
        "mxp",  # Tlahuitoltepec Mixe
        "gkn",  # Gokana
        "lbq",  # Wampar
        "bue",  # Beothuk
        "xem",  # Kembayan
        "cls",  # Classical Sanskrit
        "xnr",  # Kangri
        "gfx",  # Mangetti Dune ǃXung
        "bpq",  # Banda Malay
        "rnw",  # Rungwa
        "xmq",  # Kuku-Mangk
        "xda",  # Darkinyung
        "nsh",  # Ngoshie
        "cie",  # Cineni
        "hap",  # Hupla
        "tif",  # Tifal
        "xdk",  # Dharuk
        "van",  # Valman
        "jeb",  # Jebero
        "nmc",  # Ngam
        "sva",  # Svan
        "nys",  # Nyungar
        "etn",  # Eton (Vanuatu)
        "anw",  # Anaang
        "gvo",  # Gavião Do Jiparaná
        "gua",  # Shiki
        "viv",  # Iduna
        "bll",  # Biloxi
        "iou",  # Tuma-Irumu
        "mmc",  # Michoacán Mazahua
        "wiu",  # Wiru
        "bpx",  # Palya Bareli
        "sjw",  # Shawnee
        "twq",  # Tasawaq
        "tce",  # Southern Tutchone
        "loi",  # Loma (Côte d'Ivoire)
        "wuy",  # Wauyai
        "lkn",  # Lakon
        "siy",  # Sivandi
        "ktu",  # Kituba (Democratic Republic of Congo)
        "ybi",  # Yamphu
        "zko",  # Kott
        "yml",  # Iamalele
        "gvn",  # Kuku-Yalanji
        "lrg",  # Laragia
        "nfa",  # Dhao
        "kxx",  # Likuba
        "snv",  # Sa'ban
        "amf",  # Hamer-Banna
        "cnk",  # Khumi Chin
        "imn",  # Imonda
        "zoc",  # Copainalá Zoque
        "bng",  # Benga
        "fub",  # Adamawa Fulfulde
        "amo",  # Amo
        "cdy",  # Chadong
        "mdp",  # Mbala
        "slk",  # Slovak
        "tum",  # Tumbuka
        "lkt",  # Lakota
        "bzn",  # Boano (Maluku)
        "djl",  # Djiwarli
        "nas",  # Naasioi
        "aaz",  # Amarasi
        "aif",  # Agi
        "cia",  # Cia-Cia
        "kll",  # Kagan Kalagan
        "ttw",  # Long Wat
        "bdm",  # Buduma
        "wsv",  # Wotapuri-Katarqalai
        "xsb",  # Sambal
        "ymj",  # Muji Yi
        "nlw",  # Walangama
        "nik",  # Southern Nicobarese
        "tlp",  # Filomena Mata-Coahuitlán Totonac
        "mnu",  # Mer
        "mfg",  # Mogofin
        "iks",  # Inuit Sign Language
        "wos",  # Hanga Hundi
        "juy",  # Juray
        "jbt",  # Jabutí
        "tah",  # Tahitian
        "ksg",  # Kusaghe
        "hrv",  # Croatian
        "tlh",  # Klingon
        "trv",  # Sediq
        "guv",  # Gey
        "txc",  # Tsetsaut
        "kzx",  # Kamarian
        "tyt",  # Tày Tac
        "cax",  # Chiquitano
        "can",  # Chambri
        "frr",  # Northern Frisian
        "sux",  # Sumerian
        "agg",  # Angor
        "ero",  # Horpa
        "wnk",  # Wanukaka
        "lbl",  # Libon Bikol
        "wmo",  # Wom (Papua New Guinea)
        "fro",  # Old French (842-ca. 1400)
        "sum",  # Sumo-Mayangna
        "bxd",  # Pela
        "yuu",  # Yugh
        "tms",  # Tima
        "uga",  # Ugaritic
        "xmd",  # Mbudum
        "yae",  # Pumé
        "kha",  # Khasi
        "led",  # Lendu
        "obi",  # Obispeño
        "nur",  # Nukuria
        "yva",  # Yawa
        "yll",  # Yil
        "udg",  # Muduga
        "htu",  # Hitu
        "djb",  # Djinba
        "gyo",  # Gyalsumdo
        "drt",  # Drents
        "xra",  # Krahô
        "bcw",  # Bana
        "txb",  # Tokharian B
        "woe",  # Woleaian
        "onj",  # Onjob
        "omg",  # Omagua
        "tab",  # Tabassaran
        "lwu",  # Lawu
        "akt",  # Akolet
        "knp",  # Kwanja
        "lse",  # Lusengo
        "ish",  # Esan
        "xur",  # Urartian
        "lix",  # Liabuku
        "prd",  # Parsi-Dari
        "ncs",  # Nicaraguan Sign Language
        "blb",  # Bilua
        "ncp",  # Ndaktup
        "suh",  # Suba
        "rts",  # Yurats
        "nyr",  # Nyiha (Malawi)
        "acd",  # Gikyode
        "tkg",  # Tesaka Malagasy
        "enm",  # Middle English (1100-1500)
        "ljl",  # Li'o
        "izh",  # Ingrian
        "lbj",  # Ladakhi
        "knj",  # Western Kanjobal
        "lsd",  # Lishana Deni
        "vmw",  # Makhuwa
        "mmu",  # Mmaala
        "soz",  # Temi
        "cbn",  # Nyahkur
        "tiu",  # Adasen
        "xbp",  # Bibbulman
        "vmp",  # Soyaltepec Mazatec
        "mqz",  # Pano
        "zac",  # Ocotlán Zapotec
        "mzh",  # Wichí Lhamtés Güisnay
        "pmy",  # Papuan Malay
        "pbc",  # Patamona
        "rmu",  # Tavringer Romani
        "hhy",  # Hoyahoya
        "nlk",  # Ninia Yali
        "rwa",  # Rawo
        "vme",  # East Masela
        "xsq",  # Makhuwa-Saka
        "bji",  # Burji
        "cme",  # Cerma
        "mkd",  # Macedonian
        "twe",  # Tewa (Indonesia)
        "cta",  # Tataltepec Chatino
        "mqv",  # Mosimo
        "ppu",  # Papora
        "xto",  # Tokharian A
        "wkl",  # Kalanadi
        "aez",  # Aeka
        "azr",  # Adzera
        "jmb",  # Zumbun
        "ppt",  # Pare
        "xin",  # Xinca
        "mua",  # Mundang
        "adw",  # Amundava
        "gdx",  # Godwari
        "wec",  # Wè Western
        "zlq",  # Liuqian Zhuang
        "tji",  # Northern Tujia
        "dgt",  # Ndra'ngith
        "glr",  # Glaro-Twabo
        "hva",  # San Luís Potosí Huastec
        "wrv",  # Waruna
        "yar",  # Yabarana
        "rmx",  # Romam
        "aan",  # Anambé
        "abk",  # Abkhazian
        "nbm",  # Ngbaka Ma'bo
        "bzf",  # Boikin
        "bds",  # Burunge
        "drs",  # Gedeo
        "zao",  # Ozolotepec Zapotec
        "lsw",  # Seychelles Sign Language
        "bcj",  # Bardi
        "ppv",  # Papavô
        "kes",  # Kugbo
        "naa",  # Namla
        "pma",  # Paama
        "tvk",  # Southeast Ambrym
        "mpt",  # Mian
        "xtw",  # Tawandê
        "esl",  # Egypt Sign Language
        "tkl",  # Tokelau
        "lik",  # Lika
        "zav",  # Yatzachi Zapotec
        "hwa",  # Wané
        "nsr",  # Maritime Sign Language
        "xsk",  # Sakan
        "omx",  # Old Mon
        "wtk",  # Watakataui
        "lle",  # Lele (Papua New Guinea)
        "sbz",  # Sara Kaba
        "zml",  # Matngala
        "ulc",  # Ulch
        "wdu",  # Wadjigu
        "lst",  # Trinidad and Tobago Sign Language
        "mkg",  # Mak (China)
        "ayc",  # Southern Aymara
        "oma",  # Omaha-Ponca
        "hib",  # Hibito
        "idi",  # Idi
        "mfv",  # Mandjak
        "kgv",  # Karas
        "cop",  # Coptic
        "twc",  # Teshenawa
        "byw",  # Belhariya
        "bud",  # Ntcham
        "bge",  # Bauria
        "qxp",  # Puno Quechua
        "nds",  # Low German
        "bol",  # Bole
        "gnm",  # Ginuman
        "bma",  # Lame
        "tuk",  # Turkmen
        "mzn",  # Mazanderani
        "gml",  # Middle Low German
        "moe",  # Innu
        "zku",  # Kaurna
        "ttx",  # Tutong 1
        "crz",  # Cruzeño
        "nui",  # Ngumbi
        "reg",  # Kara (Tanzania)
        "nmx",  # Nama (Papua New Guinea)
        "sut",  # Subtiaba
        "unz",  # Unde Kaili
        "aju",  # Judeo-Moroccan Arabic
        "mmz",  # Mabaale
        "ikw",  # Ikwere
        "bkr",  # Bakumpai
        "cbj",  # Ede Cabe
        "mtp",  # Wichí Lhamtés Nocten
        "nap",  # Neapolitan
        "haq",  # Ha
        "ljw",  # Yirandali
        "kbs",  # Kande
        "nev",  # Nyaheun
        "ktr",  # Kota Marudu Tinagas
        "tct",  # T'en
        "nns",  # Ningye
        "mxk",  # Monumbo
        "rad",  # Rade
        "nht",  # Ometepec Nahuatl
        "wlr",  # Wailapa
        "bzp",  # Kemberano
        "dwl",  # Walo Kumbe Dogon
        "khx",  # Kanu
        "gpn",  # Taiap
        "avd",  # Alviri-Vidari
        "kwo",  # Kwomtari
        "idr",  # Indri
        "kut",  # Kutenai
        "zpj",  # Quiavicuzas Zapotec
        "kcr",  # Katla
        "cds",  # Chadian Sign Language
        "kmm",  # Kom (India)
        "isi",  # Nkem-Nkum
        "skf",  # Sakirabiá
        "bkf",  # Beeke
        "bum",  # Bulu (Cameroon)
        "ocu",  # Atzingo Matlatzinca
        "alp",  # Alune
        "kaz",  # Kazakh
        "kjy",  # Erave
        "utr",  # Etulo
        "rmo",  # Sinte Romani
        "inm",  # Minaean
        "oui",  # Old Uighur
        "lgi",  # Lengilu
        "gsm",  # Guatemalan Sign Language
        "pui",  # Puinave
        "cbv",  # Cacua
        "sci",  # Sri Lankan Creole Malay
        "tsk",  # Tseku
        "njr",  # Njerep
        "mgc",  # Morokodo
        "acy",  # Cypriot Arabic
        "cbs",  # Cashinahua
        "xoo",  # Xukurú
        "dtd",  # Ditidaht
        "xkf",  # Khengkha
        "vsi",  # Moldova Sign Language
        "nir",  # Nimboran
        "srj",  # Serawai
        "caw",  # Callawalla
        "awb",  # Awa (Papua New Guinea)
        "dtu",  # Tebul Ure Dogon
        "mgf",  # Maklew
        "nam",  # Ngan'gityemerri
        "ako",  # Akurio
        "gvf",  # Golin
        "mho",  # Mashi (Zambia)
        "adz",  # Adzera
        "kjd",  # Southern Kiwai
        "ldg",  # Lenyima
        "nae",  # Naka'ela
        "aaq",  # Eastern Abnaki
        "xht",  # Hattic
        "kgg",  # Kusunda
        "hin",  # Hindi
        "tni",  # Tandia
        "aoe",  # Angal Enen
        "dah",  # Gwahatike
        "pkg",  # Pak-Tong
        "kjp",  # Pwo Eastern Karen
        "wbb",  # Wabo
        "wgi",  # Wahgi
        "occ",  # Occidental
        "paj",  # Ipeka-Tapuia
        "thd",  # Kuuk Thaayorre
        "rmi",  # Lomavren
        "gdo",  # Ghodoberi
        "has",  # Haisla
        "bst",  # Basketo
        "ccl",  # Cutchi-Swahili
        "yuz",  # Yuracare
        "hng",  # Hungu
        "dup",  # Duano
        "glb",  # Belning
        "sed",  # Sedang
        "tsm",  # Turkish Sign Language
        "bpy",  # Bishnupriya
        "pov",  # Upper Guinea Crioulo
        "yas",  # Nugunu (Cameroon)
        "tbb",  # Tapeba
        "zsr",  # Southern Rincon Zapotec
        "bdw",  # Baham
        "spn",  # Sanapaná
        "woi",  # Kamang
        "cwd",  # Woods Cree
        "avl",  # Eastern Egyptian Bedawi Arabic
        "ute",  # Ute-Southern Paiute
        "csc",  # Catalan Sign Language
        "mfu",  # Mbwela
        "ura",  # Urarina
        "zpw",  # Zaniza Zapotec
        "dnt",  # Mid Grand Valley Dani
        "okb",  # Okobo
        "fat",  # Fanti
        "bfp",  # Beba
        "byz",  # Banaro
        "sba",  # Ngambay
        "xmi",  # Miarrã
        "sar",  # Saraveca
        "lsc",  # Albarradas Sign Language
        "esk",  # Northwest Alaska Inupiatun
        "szg",  # Sengele
        "sah",  # Yakut
        "mrr",  # Maria (India)
        "eko",  # Koti
        "orm",  # Oromo
        "ktx",  # Kaxararí
        "saw",  # Sawi
        "chy",  # Cheyenne
        "aht",  # Ahtena
        "xgi",  # Garingbal
        "mbt",  # Matigsalug Manobo
        "ada",  # Adangme
        "eot",  # Beti (Côte d'Ivoire)
        "akh",  # Angal Heneng
        "wnu",  # Usan
        "mrf",  # Elseng
        "cms",  # Messapic
        "lme",  # Pévé
        "xag",  # Aghwan
        "ulb",  # Ulukwumi
        "ske",  # Seke (Vanuatu)
        "zeh",  # Eastern Hongshuihe Zhuang
        "kgy",  # Kyerung
        "sgw",  # Sebat Bet Gurage
        "nnu",  # Dwang
        "far",  # Fataleka
        "sga",  # Old Irish (to 900)
        "zlu",  # Zul
        "kue",  # Kuman (Papua New Guinea)
        "vrs",  # Varisi
        "sgo",  # Songa
        "psr",  # Portuguese Sign Language
        "rmv",  # Romanova
        "nsq",  # Northern Sierra Miwok
        "afp",  # Tapei
        "qux",  # Yauyos Quechua
        "ysd",  # Samatao
        "kit",  # Agob
        "slc",  # Sáliba
        "urn",  # Uruangnirin
        "tne",  # Tinoc Kallahan
        "oyb",  # Oy
        "tsw",  # Tsishingini
        "apy",  # Apalaí
        "izr",  # Izere
        "rkb",  # Rikbaktsa
        "siq",  # Sonia
        "alu",  # 'Are'are
        "bqk",  # Banda-Mbrès
        "kxm",  # Northern Khmer
        "sbv",  # Sabine
        "wrw",  # Gugu Warra
        "smf",  # Auwe
        "soh",  # Aka
        "iyo",  # Mesaka
        "icr",  # Islander Creole English
        "diu",  # Diriku
        "mvy",  # Indus Kohistani
        "ymt",  # Mator-Taygi-Karagas
        "bwy",  # Cwi Bwamu
        "njh",  # Lotha Naga
        "tnr",  # Ménik
        "txn",  # West Tarangan
        "kbt",  # Abadi
        "box",  # Buamu
        "kyv",  # Kayort
        "vnm",  # Vinmavis
        "ayh",  # Hadrami Arabic
        "bbl",  # Bats
        "kcm",  # Gula (Central African Republic)
        "bhi",  # Bhilali
        "akg",  # Anakalangu
        "cwa",  # Kabwa
        "vic",  # Virgin Islands Creole English
        "sjg",  # Assangori
        "bgj",  # Bangolan
        "chb",  # Chibcha
        "bin",  # Bini
        "abb",  # Bankon
        "yyu",  # Yau (Sandaun Province)
        "xeb",  # Eblan
        "adn",  # Adang
        "itx",  # Itik
        "vbk",  # Southwestern Bontok
        "nsa",  # Sangtam Naga
        "bex",  # Jur Modo
        "ksi",  # Krisa
        "ngj",  # Ngie
        "xke",  # Kereho
        "nck",  # Na-kara
        "opm",  # Oksapmin
        "alk",  # Alak
        "yan",  # Mayangna
        "hul",  # Hula
        "nwe",  # Ngwe
        "nnf",  # Ngaing
        "tor",  # Togbo-Vara Banda
        "mvv",  # Tagal Murut
        "kia",  # Kim
        "olt",  # Old Lithuanian
        "iya",  # Iyayu
        "nqg",  # Southern Nago
        "eza",  # Ezaa
        "ofu",  # Efutop
        "xnt",  # Narragansett
        "nso",  # Pedi
        "tul",  # Tula
        "bqf",  # Baga Kaloum
        "beq",  # Beembe
        "lau",  # Laba
        "ses",  # Koyraboro Senni Songhai
        "grj",  # Southern Grebo
        "ojv",  # Ontong Java
        "ojc",  # Central Ojibwa
        "prk",  # Parauk
        "gou",  # Gavar
        "crl",  # Northern East Cree
        "ttj",  # Tooro
        "pkh",  # Pankhu
        "aku",  # Akum
        "fwa",  # Fwâi
        "gao",  # Gants
        "kum",  # Kumyk
        "kfn",  # Kuk
        "aua",  # Asumboa
        "pac",  # Pacoh
        "wbk",  # Waigali
        "cdn",  # Chaudangsi
        "ney",  # Neyo
        "mzx",  # Mawayana
        "swc",  # Congo Swahili
        "wkd",  # Wakde
        "kde",  # Makonde
        "pnr",  # Panim
        "alq",  # Algonquin
        "ymk",  # Makwe
        "gsw",  # Swiss German
        "poy",  # Pogolo
        "obl",  # Oblo
        "hmn",  # Hmong
        "dhg",  # Dhangu-Djangu
        "bcp",  # Bali (Democratic Republic of Congo)
        "cnr",  # Montenegrin
        "cco",  # Comaltepec Chinantec
        "ona",  # Ona
        "ham",  # Hewa
        "iri",  # Rigwe
        "kod",  # Kodi
        "hmh",  # Southwestern Huishui Hmong
        "spx",  # South Picene
        "hoc",  # Ho
        "asx",  # Muratayak
        "nfr",  # Nafaanra
        "wyy",  # Western Fijian
        "qvj",  # Loja Highland Quichua
        "bla",  # Siksika
        "xmf",  # Mingrelian
        "cke",  # Eastern Cakchiquel
        "cwb",  # Maindo
        "vkm",  # Kamakan
        "lad",  # Ladino
        "csg",  # Chilean Sign Language
        "bkm",  # Kom (Cameroon)
        "trm",  # Tregami
        "gvc",  # Guanano
        "lgo",  # Lango (South Sudan)
        "muu",  # Yaaku
        "cit",  # Chittagonian
        "pea",  # Peranakan Indonesian
        "thh",  # Northern Tarahumara
        "urv",  # Uruava
        "kug",  # Kupa
        "xal",  # Kalmyk
        "dei",  # Demisa
        "kig",  # Kimaama
        "skz",  # Sekar
        "vmz",  # Mazatlán Mazatec
        "lbg",  # Laopang
        "typ",  # Thaypan
        "jkr",  # Koro (India)
        "vlp",  # Valpei
        "bom",  # Berom
        "nop",  # Numanggang
        "snw",  # Selee
        "kmy",  # Koma
        "tkw",  # Teanu
        "rod",  # Rogo
        "vwa",  # Awa (China)
        "mgo",  # Meta'
        "oso",  # Ososo
        "brn",  # Boruca
        "sto",  # Stoney
        "szs",  # Solomon Islands Sign Language
        "nne",  # Ngandyera
        "klm",  # Migum
        "mcu",  # Cameroon Mambila
        "blr",  # Blang
        "lll",  # Lilau
        "rog",  # Northern Roglai
        "nbd",  # Ngbinda
        "emz",  # Mbessa
        "ndq",  # Ndombe
        "tsc",  # Tswa
        "mxj",  # Miju-Mishmi
        "kec",  # Keiga
        "muk",  # Mugom
        "kgm",  # Karipúna
        "spb",  # Sepa (Indonesia)
        "mst",  # Cataelano Mandaya
        "kqj",  # Koromira
        "oco",  # Old Cornish
        "sii",  # Shom Peng
        "del",  # Delaware
        "isg",  # Irish Sign Language
        "tth",  # Upper Ta'oih
        "sso",  # Sissano
        "sqk",  # Albanian Sign Language
        "nmn",  # ǃXóõ
        "cik",  # Chitkuli Kinnauri
        "mdv",  # Santa Lucía Monteverde Mixtec
        "kwc",  # Likwala
        "mpq",  # Matís
        "gsl",  # Gusilay
        "kpr",  # Korafe-Yegha
        "afg",  # Afghan Sign Language
        "lup",  # Lumbu
        "ytw",  # Yout Wam
        "sle",  # Sholaga
        "bhr",  # Bara Malagasy
        "bpb",  # Barbacoas
        "gwu",  # Guwamu
        "lbr",  # Lohorung
        "prh",  # Porohanon
        "bhu",  # Bhunjia
        "anj",  # Anor
        "mrs",  # Maragus
        "blk",  # Pa'o Karen
        "sug",  # Suganga
        "bka",  # Kyak
        "ema",  # Emai-Iuleha-Ora
        "umm",  # Umon
        "iff",  # Ifo
        "rnb",  # Brunca Sign Language
        "yos",  # Yos
        "wtw",  # Wotu
        "bbf",  # Baibai
        "dsn",  # Dusner
        "hub",  # Huambisa
        "sbn",  # Sindhi Bhil
        "tlg",  # Tofanma
        "rat",  # Razajerdi
        "cow",  # Cowlitz
        "myt",  # Sangab Mandaya
        "dek",  # Dek
        "mfj",  # Mefele
        "mmm",  # Maii
        "zad",  # Cajonos Zapotec
        "sea",  # Semai
        "kom",  # Komi
        "kae",  # Ketangalan
        "ynh",  # Yangho
        "mzj",  # Manya
        "kyn",  # Northern Binukidnon
        "gyi",  # Gyele
        "ryn",  # Northern Amami-Oshima
        "cje",  # Chru
        "ldb",  # Dũya
        "bzc",  # Southern Betsimisaraka Malagasy
        "kil",  # Kariya
        "sbc",  # Kele (Papua New Guinea)
        "zte",  # Elotepec Zapotec
        "cqu",  # Chilean Quechua
        "rws",  # Rawas
        "ayd",  # Ayabadhu
        "bsp",  # Baga Sitemu
        "osx",  # Old Saxon
        "glc",  # Bon Gula
        "zun",  # Zuni
        "nad",  # Nijadali
        "pim",  # Powhatan
        "eaa",  # Karenggapa
        "tiw",  # Tiwi
        "xia",  # Xiandao
        "jks",  # Amami Koniya Sign Language
        "bci",  # Baoulé
        "dto",  # Tommo So Dogon
        "xmo",  # Morerebi
        "bpi",  # Bagupi
        "umc",  # Marrucinian
        "ssd",  # Siroi
        "mnl",  # Tiale
        "wlo",  # Wolio
        "tec",  # Terik
        "gav",  # Gabutamon
        "nps",  # Nipsan
        "kiw",  # Northeast Kiwai
        "tdy",  # Tadyawan
        "bmv",  # Bum
        "bgb",  # Bobongko
        "brr",  # Birao
        "xed",  # Hdi
        "ssf",  # Thao
        "tnx",  # Tanema
        "vra",  # Vera'a
        "chv",  # Chuvash
        "ymp",  # Yamap
        "sbt",  # Kimki
        "ppq",  # Pei
        "mmn",  # Mamanwa
        "din",  # Dinka
        "mpp",  # Migabac
        "pie",  # Piro
        "wlg",  # Kunbarlang
        "etu",  # Ejagham
        "asa",  # Asu (Tanzania)
        "shz",  # Syenara Senoufo
        "xrq",  # Karranga
        "bnh",  # Banawá
        "cyo",  # Cuyonon
        "aut",  # Austral
        "vai",  # Vai
        "gqi",  # Guiqiong
        "djc",  # Dar Daju Daju
        "mck",  # Mbunda
        "nmy",  # Namuyi
        "szn",  # Sula
        "mjn",  # Ma (Papua New Guinea)
        "slv",  # Slovenian
        "yac",  # Pass Valley Yali
        "gwr",  # Gwere
        "ngr",  # Engdewu
        "vmm",  # Mitlatongo Mixtec
        "bmw",  # Bomwali
        "nmf",  # Tangkhul Naga (India)
        "xkd",  # Mendalam Kayan
        "tmm",  # Tai Thanh
        "jge",  # Judeo-Georgian
        "aod",  # Andarum
        "cui",  # Cuiba
        "fam",  # Fam
        "svx",  # Skalvian
        "wod",  # Wolani
        "trr",  # Taushiro
        "boh",  # Boma
        "kxp",  # Wadiyara Koli
        "awm",  # Arawum
        "dso",  # Desiya
        "tus",  # Tuscarora
        "cmg",  # Classical Mongolian
        "yao",  # Yao
        "kgt",  # Somyev
        "xri",  # Krikati-Timbira
        "kmx",  # Waboda
        "zen",  # Zenaga
        "gro",  # Groma
        "xxb",  # Boro (Ghana)
        "ibi",  # Ibilo
        "omi",  # Omi
        "yah",  # Yazgulyam
        "pmd",  # Pallanganmiddang
        "nyh",  # Nyikina
        "fab",  # Fa d'Ambu
        "ffm",  # Maasina Fulfulde
        "oub",  # Glio-Oubi
        "scs",  # North Slavey
        "ges",  # Geser-Gorom
        "aat",  # Arvanitika Albanian
        "dwz",  # Dewas Rai
        "bss",  # Akoose
        "blu",  # Hmong Njua
        "sve",  # Serili
        "kns",  # Kensiu
        "asn",  # Xingú Asuriní
        "pjt",  # Pitjantjatjara
        "tnq",  # Taino
        "xsm",  # Kasem
        "gok",  # Gowli
        "xpt",  # Punthamara
        "quw",  # Tena Lowland Quichua
        "mdt",  # Mbere
        "sub",  # Suku
        "gyr",  # Guarayu
        "brp",  # Barapasi
        "cun",  # Cunén Quiché
        "zpm",  # Mixtepec Zapotec
        "cht",  # Cholón
        "nar",  # Iguta
        "paw",  # Pawnee
        "tim",  # Timbe
        "qws",  # Sihuas Ancash Quechua
        "gzn",  # Gane
        "slh",  # Southern Puget Sound Salish
        "bxt",  # Buxinhua
        "ymm",  # Maay
        "xum",  # Umbrian
        "eni",  # Enim
        "mez",  # Menominee
        "trx",  # Tringgus-Sembaan Bidayuh
        "ctd",  # Tedim Chin
        "kww",  # Kwinti
        "itz",  # Itzá
        "ikr",  # Ikaranggal
        "xiv",  # Indus Valley Language
        "pmw",  # Plains Miwok
        "onw",  # Old Nubian
        "api",  # Apiaká
        "tmw",  # Temuan
        "ewo",  # Ewondo
        "zmr",  # Maranunggu
        "syl",  # Sylheti
        "ayq",  # Ayi (Papua New Guinea)
        "lra",  # Rara Bakati'
        "ich",  # Etkywan
        "wav",  # Waka
        "njn",  # Liangmai Naga
        "nqy",  # Akyaung Ari Naga
        "nol",  # Nomlaki
        "ate",  # Atemble
        "anf",  # Animere
        "ngp",  # Ngulu
        "yde",  # Yangum Dey
        "gbz",  # Zoroastrian Dari
        "tuz",  # Turka
        "yij",  # Yindjibarndi
        "nxo",  # Ndambomo
        "cbd",  # Carijona
        "uwa",  # Kuku-Uwanh
        "ynk",  # Naukan Yupik
        "xar",  # Karami
        "mxs",  # Huitepec Mixtec
        "vro",  # Võro
        "myo",  # Anfillo
        "xpo",  # Pochutec
        "yku",  # Kuamasi
        "dma",  # Duma
        "nrf",  # Jèrriais
        "ptp",  # Patep
        "ykr",  # Yekora
        "zos",  # Francisco León Zoque
        "sap",  # Sanapaná
        "msr",  # Mongolian Sign Language
        "keg",  # Tese
        "wyn",  # Wyandot
        "csn",  # Colombian Sign Language
        "bdq",  # Bahnar
        "kxo",  # Kanoé
        "gum",  # Guambiano
        "kkb",  # Kwerisa
        "ior",  # Inor
        "lmm",  # Lamam
        "mgi",  # Lijili
        "psm",  # Pauserna
        "ndd",  # Nde-Nsele-Nta
        "gti",  # Gbati-ri
        "ahi",  # Tiagbamrin Aizi
        "cty",  # Moundadan Chetty
        "ggb",  # Gbii
        "afe",  # Putukwam
        "aci",  # Aka-Cari
        "gec",  # Gboloo Grebo
        "nrr",  # Norra
        "rmf",  # Kalo Finnish Romani
        "crs",  # Seselwa Creole French
        "rar",  # Rarotongan
        "scf",  # San Miguel Creole French
        "nmr",  # Nimbari
        "kpo",  # Ikposo
        "mvx",  # Meoswar
        "raz",  # Rahambuu
        "slj",  # Salumá
        "wrx",  # Wae Rana
        "xpw",  # Northwestern Tasmanian
        "cnt",  # Tepetotutla Chinantec
        "ted",  # Tepo Krumen
        "dio",  # Dibo
        "prn",  # Prasuni
        "eme",  # Emerillon
        "zmz",  # Mbandja
        "bww",  # Bwa
        "boi",  # Barbareño
        "shh",  # Shoshoni
        "bjg",  # Bidyogo
        "bor",  # Borôro
        "dmf",  # Medefaidrin
        "drd",  # Darmiya
        "nyl",  # Nyeu
        "sxk",  # Southern Kalapuya
        "tdf",  # Talieng
        "tuc",  # Mutu
        "xzm",  # Zemgalian
        "fur",  # Friulian
        "jbr",  # Jofotek-Bromnya
        "lje",  # Rampi
        "vkk",  # Kaur
        "loe",  # Saluan
        "bxx",  # Borna (Democratic Republic of Congo)
        "nor",  # Norwegian
        "bto",  # Rinconada Bikol
        "dbt",  # Ben Tey Dogon
        "nxl",  # South Nuaulu
        "bce",  # Bamenyam
        "msm",  # Agusan Manobo
        "yrm",  # Yirrk-Mel
        "lgt",  # Pahi
        "rou",  # Runga
        "sqi",  # Albanian
        "gas",  # Adiwasi Garasia
        "chr",  # Cherokee
        "zpe",  # Petapa Zapotec
        "xhc",  # Hunnic
        "zyg",  # Yang Zhuang
        "msa",  # Malay (macrolanguage)
        "lit",  # Lithuanian
        "tml",  # Tamnim Citak
        "amk",  # Ambai
        "emg",  # Eastern Meohang
        "tyr",  # Tai Daeng
        "goa",  # Guro
        "ygl",  # Yangum Gel
        "vkz",  # Koro Zuba
        "frp",  # Arpitan
        "tlj",  # Talinga-Bwisi
        "mai",  # Maithili
        "krw",  # Western Krahn
        "pbp",  # Badyara
        "tew",  # Tewa (USA)
        "pcc",  # Bouyei
        "wls",  # Wallisian
        "gnt",  # Guntai
        "gwj",  # ǀGwi
        "tdh",  # Thulung
        "mhg",  # Margu
        "ole",  # Olekha
        "wyr",  # Wayoró
        "sda",  # Toraja-Sa'dan
        "thu",  # Thuri
        "apc",  # Levantine Arabic
        "ehu",  # Ehueun
        "gbe",  # Niksek
        "kvv",  # Kola
        "zch",  # Central Hongshuihe Zhuang
        "sgl",  # Sanglechi-Ishkashimi
        "bvd",  # Baeggu
        "ggg",  # Gurgula
        "mqj",  # Mamasa
        "ilu",  # Ili'uun
        "tro",  # Tarao Naga
        "tkx",  # Tangko
        "nkp",  # Niuatoputapu
        "kxh",  # Karo (Ethiopia)
        "kcs",  # Koenoem
        "ylb",  # Yaleba
        "omo",  # Utarmbung
        "bvf",  # Boor
        "sbo",  # Sabüm
        "laj",  # Lango (Uganda)
        "mps",  # Dadibi
        "nlc",  # Nalca
        "kcv",  # Kete
        "uzs",  # Southern Uzbek
        "amj",  # Amdang
        "bvn",  # Buna
        "jwi",  # Jwira-Pepesa
        "lsv",  # Sivia Sign Language
        "naq",  # Khoekhoe
        "bvm",  # Bamunka
        "urk",  # Urak Lawoi'
        "bej",  # Beja
        "kok",  # Konkani (macrolanguage)
        "ben",  # Bengali
        "luv",  # Luwati
        "haz",  # Hazaragi
        "yig",  # Wusa Nasu
        "ysg",  # Sonaga
        "llf",  # Hermit
        "duu",  # Drung
        "puj",  # Punan Tubu
        "wmg",  # Western Minyag
        "asj",  # Sari
        "jbi",  # Badjiri
        "wbv",  # Wajarri
        "jai",  # Western Jacalteco
        "jnl",  # Rawat
        "arj",  # Arapaso
        "unu",  # Unubahe
        "bye",  # Pouye
        "fer",  # Feroge
        "byg",  # Baygo
        "rpt",  # Rapting
        "wnn",  # Wunumara
        "bup",  # Busoa
        "nav",  # Navajo
        "xwj",  # Wajuk
        "bbe",  # Bangba
        "gob",  # Playero
        "nrg",  # Narango
        "pdo",  # Padoe
        "dne",  # Ndendeule
        "gwt",  # Gawar-Bati
        "klk",  # Kono (Nigeria)
        "vmi",  # Miwa
        "sih",  # Zire
        "trs",  # Chicahuaxtla Triqui
        "gry",  # Barclayville Grebo
        "nhy",  # Northern Oaxaca Nahuatl
        "tkk",  # Takpa
        "cea",  # Lower Chehalis
        "gju",  # Gujari
        "nnj",  # Nyangatom
        "djj",  # Djeebbana
        "uya",  # Doko-Uyanga
        "klz",  # Kabola
        "acp",  # Eastern Acipa
        "bgc",  # Haryanvi
        "aid",  # Alngith
        "hya",  # Hya
        "bjj",  # Kanauji
        "shw",  # Shwai
        "xha",  # Harami
        "kfo",  # Koro (Côte d'Ivoire)
        "pwi",  # Patwin
        "kux",  # Kukatja
        "ttc",  # Tektiteko
        "lyg",  # Lyngngam
        "hmz",  # Hmong Shua
        "aas",  # Aasáx
        "hob",  # Mari (Madang Province)
        "kei",  # Kei
        "mty",  # Nabi
        "neu",  # Neo
        "mxl",  # Maxi Gbe
        "avv",  # Avá-Canoeiro
        "ycl",  # Lolopo
        "yry",  # Yarluyandi
        "iap",  # Iapama
        "wbr",  # Wagdi
        "tap",  # Taabwa
        "twd",  # Twents
        "rnl",  # Ranglong
        "idb",  # Indo-Portuguese
        "psd",  # Plains Indian Sign Language
        "yil",  # Yindjilandji
        "pyn",  # Poyanáwa
        "ycn",  # Yucuna
        "quc",  # K'iche'
        "inl",  # Indonesian Sign Language
        "boz",  # Tiéyaxo Bozo
        "mwu",  # Mittu
        "ahl",  # Igo
        "mnd",  # Mondé
        "wja",  # Waja
        "itb",  # Binongan Itneg
        "nxr",  # Ninggerum
        "tds",  # Doutai
        "gap",  # Gal
        "tnk",  # Kwamera
        "arl",  # Arabela
        "tvn",  # Tavoyan
        "npi",  # Nepali (individual language)
        "dus",  # Dumi
        "tny",  # Tongwe
        "wbh",  # Wanda
        "tjo",  # Temacine Tamazight
        "gay",  # Gayo
        "hao",  # Hakö
        "wbm",  # Wa
        "nwr",  # Nawaru
        "idd",  # Ede Idaca
        "grw",  # Gweda
        "gqr",  # Gor
        "bqc",  # Boko (Benin)
        "key",  # Kupia
        "tso",  # Tsonga
        "nux",  # Mehek
        "dry",  # Darai
        "gdg",  # Ga'dang
        "cnl",  # Lalana Chinantec
        "saz",  # Saurashtra
        "kdf",  # Mamusi
        "kxy",  # Kayong
        "ckd",  # South Central Cakchiquel
        "kik",  # Kikuyu
        "pmu",  # Mirpur Panjabi
        "cca",  # Cauca
        "apu",  # Apurinã
        "kwq",  # Kwak
        "bvv",  # Baniva
        "bas",  # Basa (Cameroon)
        "jeh",  # Jeh
        "kua",  # Kuanyama
        "auq",  # Anus
        "lva",  # Maku'a
        "gia",  # Kija
        "zkp",  # São Paulo Kaingáng
        "foi",  # Foi
        "ksv",  # Kusu
        "nhe",  # Eastern Huasteca Nahuatl
        "haj",  # Hajong
        "mkp",  # Moikodi
        "kks",  # Giiwo
        "mgh",  # Makhuwa-Meetto
        "dzo",  # Dzongkha
        "bgf",  # Bangandu
        "yad",  # Yagua
        "woy",  # Weyto
        "tqr",  # Torona
        "xwr",  # Kwerba Mamberamo
        "ymr",  # Malasar
        "tvu",  # Tunen
        "qxn",  # Northern Conchucos Ancash Quechua
        "yus",  # Chan Santa Cruz Maya
        "ydd",  # Eastern Yiddish
        "nwo",  # Nauo
        "tpv",  # Tanapag
        "xkl",  # Mainstream Kenyah
        "gur",  # Farefare
        "ikt",  # Inuinnaqtun
        "pam",  # Pampanga
        "nhp",  # Isthmus-Pajapan Nahuatl
        "har",  # Harari
        "mlq",  # Western Maninkakan
        "pnt",  # Pontic
        "rub",  # Gungu
        "sco",  # Scots
        "bpw",  # Bo (Papua New Guinea)
        "gjm",  # Gunditjmara
        "sue",  # Suena
        "kjl",  # Western Parbate Kham
        "tii",  # Tiene
        "mjv",  # Mannan
        "ogn",  # Ogan
        "ncc",  # Ponam
        "mas",  # Masai
        "ala",  # Alago
        "smv",  # Samvedi
        "obk",  # Southern Bontok
        "ggm",  # Gugu Mini
        "fif",  # Faifi
        "kuk",  # Kepo'
        "gag",  # Gagauz
        "scn",  # Sicilian
        "lri",  # Marachi
        "dhi",  # Dhimal
        "kun",  # Kunama
        "xmg",  # Mengaka
        "puy",  # Purisimeño
        "dza",  # Tunzu
        "vmb",  # Barbaram
        "skh",  # Sikule
        "nxq",  # Naxi
        "nfg",  # Nyeng
        "ppn",  # Papapana
        "vls",  # Vlaams
        "pbi",  # Parkwa
        "fln",  # Flinders Island
        "oki",  # Okiek
        "cor",  # Cornish
        "jmn",  # Makuri Naga
        "efi",  # Efik
        "xdm",  # Edomite
        "mne",  # Naba
        "drn",  # West Damar
        "nmk",  # Namakura
        "kem",  # Kemak
        "yit",  # Eastern Lalu
        "aaf",  # Aranadan
        "kpf",  # Komba
        "inz",  # Ineseño
        "xyk",  # Mayi-Kulan
        "akz",  # Alabama
        "bxb",  # Belanda Bor
        "xeg",  # ǁXegwi
        "srq",  # Sirionó
        "kfz",  # Koromfé
        "bsf",  # Bauchi
        "lak",  # Laka (Nigeria)
        "hss",  # Harsusi
        "mug",  # Musgu
        "cey",  # Ekai Chin
        "nyd",  # Nyore
        "brh",  # Brahui
        "let",  # Lesing-Gelimi
        "pss",  # Kaulong
        "aak",  # Ankave
        "csr",  # Costa Rican Sign Language
        "dnu",  # Danau
        "gmg",  # Magɨyi
        "jul",  # Jirel
        "aik",  # Ake
        "wdk",  # Wadikali
        "pch",  # Pardhan
        "brw",  # Bellari
        "ndx",  # Nduga
        "dsh",  # Daasanach
        "hsh",  # Hungarian Sign Language
        "lcq",  # Luhu
        "bbo",  # Northern Bobo Madaré
        "ktl",  # Koroshi
        "kyi",  # Kiput
        "sry",  # Sera
        "huq",  # Tsat
        "ztt",  # Tejalapan Zapotec
        "mxq",  # Juquila Mixe
        "dzn",  # Dzando
        "dav",  # Taita
        "oge",  # Old Georgian
        "nfk",  # Shakara
        "vma",  # Martuyhunira
        "duq",  # Dusun Malang
        "xkw",  # Kembra
        "ale",  # Aleut
        "lhn",  # Lahanan
        "thw",  # Thudam
        "wya",  # Wyandot
        "liy",  # Banda-Bambari
        "bnx",  # Bangubangu
        "mse",  # Musey
        "ory",  # Odia
        "ahm",  # Mobumrin Aizi
        "dbd",  # Dadiya
        "tia",  # Tidikelt Tamazight
        "kru",  # Kurukh
        "iba",  # Iban
        "row",  # Dela-Oenale
        "bfu",  # Gahri
        "xhd",  # Hadrami
        "abt",  # Ambulas
        "twb",  # Western Tawbuid
        "dow",  # Doyayo
        "srl",  # Isirawa
        "anh",  # Nend
        "asi",  # Buruwai
        "nex",  # Neme
        "kke",  # Kakabe
        "lex",  # Luang
        "utp",  # Amba (Solomon Islands)
        "kjm",  # Kháng
        "swt",  # Sawila
        "qwh",  # Huaylas Ancash Quechua
        "kjf",  # Khalaj
        "tog",  # Tonga (Nyasa)
        "bkw",  # Bekwel
        "svb",  # Ulau-Suain
        "ygr",  # Yagaria
        "huo",  # Hu
        "guq",  # Aché
        "ass",  # Ipulo
        "kif",  # Eastern Parbate Kham
        "lku",  # Kungkari
        "ttk",  # Totoro
        "rma",  # Rama
        "hif",  # Fiji Hindi
        "mjy",  # Mahican
        "jml",  # Jumli
        "sxm",  # Samre
        "fuv",  # Nigerian Fulfulde
        "nil",  # Nila
        "smx",  # Samba
        "dnr",  # Danaru
        "itv",  # Itawit
        "yph",  # Phupha
        "tbu",  # Tubar
        "tcl",  # Taman (Myanmar)
        "bjr",  # Binumarien
        "luu",  # Lumba-Yakkha
        "put",  # Putoh
        "enq",  # Enga
        "won",  # Wongo
        "ltc",  # Late Middle Chinese
        "mrg",  # Mising
        "ell",  # Modern Greek (1453-)
        "khs",  # Kasua
        "vkj",  # Kujarge
        "jct",  # Krymchak
        "nan",  # Min Nan Chinese
        "zpv",  # Chichicapan Zapotec
        "saf",  # Safaliba
        "kwb",  # Kwa
        "cfg",  # Como Karim
        "vaj",  # Sekele
        "xrn",  # Arin
        "mcn",  # Masana
        "ljx",  # Yuru
        "dmv",  # Dumpas
        "egl",  # Emilian
        "bic",  # Bikaru
        "mpc",  # Mangarrayi
        "sno",  # Snohomish
        "nis",  # Nimi
        "btf",  # Birgit
        "agc",  # Agatu
        "pnp",  # Pancana
        "aio",  # Aiton
        "bqd",  # Bung
        "grg",  # Madi
        "adl",  # Galo
        "kzg",  # Kikai
        "mqk",  # Rajah Kabunsuwan Manobo
        "kza",  # Western Karaboro
        "ude",  # Udihe
        "xcy",  # Cayuse
        "xpr",  # Parthian
        "sza",  # Semelai
        "klt",  # Nukna
        "djw",  # Djawi
        "adt",  # Adnyamathanha
        "ths",  # Thakali
        "yuc",  # Yuchi
        "bxv",  # Berakou
        "btb",  # Beti (Cameroon)
        "kgh",  # Upper Tanudan Kalinga
        "bju",  # Busuu
        "odt",  # Old Dutch
        "krq",  # Krui
        "tpy",  # Trumai
        "mgt",  # Mongol
        "aij",  # Lishanid Noshan
        "yrw",  # Yarawata
        "ndm",  # Ndam
        "pmc",  # Palumata
        "zmk",  # Mandandanyi
        "zat",  # Tabaa Zapotec
        "msq",  # Caac
        "xir",  # Xiriâna
        "coo",  # Comox
        "stg",  # Trieng
        "bcl",  # Central Bikol
        "cym",  # Welsh
        "lko",  # Khayo
        "awn",  # Awngi
        "ydg",  # Yidgha
        "niy",  # Ngiti
        "tlm",  # Tolomako
        "arz",  # Egyptian Arabic
        "her",  # Herero
        "bjz",  # Baruga
        "png",  # Pangu
        "iry",  # Iraya
        "szd",  # Seru
        "mto",  # Totontepec Mixe
        "cri",  # Sãotomense
        "otb",  # Old Tibetan
        "ayk",  # Akuku
        "suj",  # Shubi
        "nce",  # Yale
        "jmc",  # Machame
        "tza",  # Tanzanian Sign Language
        "sae",  # Sabanê
        "deg",  # Degema
        "ktw",  # Kato
        "tlo",  # Talodi
        "sdt",  # Shuadit
        "ktk",  # Kaniet
        "hug",  # Huachipaeri
        "kup",  # Kunimaipa
        "hts",  # Hadza
        "wxw",  # Wardandi
        "nlz",  # Nalögo
        "onb",  # Lingao
        "acv",  # Achumawi
        "djm",  # Jamsay Dogon
        "mqp",  # Manipa
        "xat",  # Katawixi
        "nup",  # Nupe-Nupe-Tako
        "ybe",  # West Yugur
        "jje",  # Jejueo
        "aur",  # Aruek
        "sob",  # Sobei
        "bes",  # Besme
        "cbu",  # Candoshi-Shapra
        "fir",  # Firan
        "oym",  # Wayampi
        "ymn",  # Yamna
        "mdy",  # Male (Ethiopia)
        "pqa",  # Pa'a
        "wof",  # Gambian Wolof
        "txs",  # Tonsea
        "jhi",  # Jehai
        "mqh",  # Tlazoyaltepec Mixtec
        "daq",  # Dandami Maria
        "kdh",  # Tem
        "aba",  # Abé
        "bip",  # Bila
        "bqt",  # Bamukumbit
        "dac",  # Dambi
        "boa",  # Bora
        "ksn",  # Kasiguranin
        "slz",  # Ma'ya
        "kkr",  # Kir-Balar
        "uro",  # Ura (Papua New Guinea)
        "wti",  # Berta
        "huk",  # Hulung
        "tns",  # Tenis
        "mxa",  # Northwest Oaxaca Mixtec
        "xvi",  # Kamviri
        "adr",  # Adonara
        "xkm",  # Mahakam Kenyah
        "nmo",  # Moyon Naga
        "sky",  # Sikaiana
        "yav",  # Yangben
        "gan",  # Gan Chinese
        "aol",  # Alor
        "cou",  # Wamey
        "kph",  # Kplang
        "pok",  # Pokangá
        "pni",  # Aoheng
        "mtk",  # Mbe'
        "tyh",  # O'du
        "lls",  # Lithuanian Sign Language
        "tnt",  # Tontemboan
        "juk",  # Wapan
        "xwa",  # Kwaza
        "brm",  # Barambu
        "aah",  # Abu' Arapesh
        "xer",  # Xerénte
        "gct",  # Colonia Tovar German
        "yur",  # Yurok
        "pbn",  # Kpasam
        "ulf",  # Usku
        "jvd",  # Javindo
        "pse",  # Central Malay
        "ksl",  # Kumalu
        "laz",  # Aribwatsa
        "vaa",  # Vaagri Booli
        "bmp",  # Bulgebi
        "uru",  # Urumi
        "lng",  # Langobardic
        "lav",  # Latvian
        "lue",  # Luvale
        "nxi",  # Nindi
        "bqv",  # Koro Wachi
        "syb",  # Central Subanen
        "ven",  # Venda
        "bdd",  # Bunama
        "kmz",  # Khorasani Turkish
        "nlu",  # Nchumbulu
        "tts",  # Northeastern Thai
        "jut",  # Jutish
        "ert",  # Eritai
        "liv",  # Liv
        "szv",  # Isu (Fako Division)
        "bdt",  # Bokoto
        "bkg",  # Buraka
        "ckx",  # Caka
        "dlk",  # Dahalik
        "xmu",  # Kamu
        "lcm",  # Tungag
        "amd",  # Amapá Creole
        "cib",  # Ci Gbe
        "ppi",  # Paipai
        "kps",  # Tehit
        "six",  # Sumau
        "nbx",  # Ngura
        "old",  # Mochi
        "nmj",  # Ngombe (Central African Republic)
        "duj",  # Dhuwal
        "gnq",  # Gana
        "erh",  # Eruwa
        "wsa",  # Warembori
        "pgl",  # Primitive Irish
        "tgl",  # Tagalog
        "nvm",  # Namiae
        "ont",  # Ontenu
        "uka",  # Kaburi
        "dec",  # Dagik
        "bmc",  # Biem
        "kco",  # Kinalakna
        "kvn",  # Border Kuna
        "smc",  # Som
        "sge",  # Segai
        "url",  # Urali
        "bgy",  # Benggoi
        "tnb",  # Western Tunebo
        "cdf",  # Chiru
        "tse",  # Tunisian Sign Language
        "ttg",  # Tutong
        "slr",  # Salar
        "oyd",  # Oyda
        "lec",  # Leco
        "yug",  # Yug
        "wik",  # Wikalkan
        "kqp",  # Kimré
        "tbm",  # Tagbu
        "pcb",  # Pear
        "goz",  # Gozarkhani
        "bph",  # Botlikh
        "dnd",  # Daonda
        "hni",  # Hani
        "yol",  # Yola
        "mzd",  # Malimba
        "rtc",  # Rungtu Chin
        "apr",  # Arop-Lokep
        "sby",  # Soli
        "sbj",  # Surbakhal
        "mrm",  # Merlav
        "kpp",  # Paku Karen
        "kon",  # Kongo
        "kdw",  # Koneraw
        "ltg",  # Latgalian
        "mau",  # Huautla Mazatec
        "nsb",  # Lower Nossob
        "wow",  # Wawonii
        "bnu",  # Bentong
        "lno",  # Lango (South Sudan)
        "mil",  # Peñoles Mixtec
        "zha",  # Zhuang
        "nrl",  # Ngarluma
        "kaw",  # Kawi
        "trh",  # Turaka
        "xsp",  # Silopi
        "ajn",  # Andajin
        "one",  # Oneida
        "dig",  # Digo
        "xip",  # Xipináwa
        "xkb",  # Northern Nago
        "mwm",  # Sar
        "ubl",  # Buhi'non Bikol
        "okh",  # Koresh-e Rostam
        "bhc",  # Biga
        "moq",  # Mor (Bomberai Peninsula)
        "akq",  # Ak
        "idu",  # Idoma
        "hkk",  # Hunjara-Kaina Ke
        "bnp",  # Bola
        "lma",  # East Limba
        "plu",  # Palikúr
        "arv",  # Arbore
        "dmx",  # Dema
        "bzw",  # Basa (Nigeria)
        "saa",  # Saba
        "nqt",  # Nteng
        "bvc",  # Baelelea
        "dng",  # Dungan
        "jbm",  # Bijim
        "jih",  # sTodsde
        "tbf",  # Mandara
        "kgs",  # Kumbainggar
        "buh",  # Younuo Bunu
        "ohu",  # Old Hungarian
        "khr",  # Kharia
        "vas",  # Vasavi
        "keh",  # Keak
        "ktt",  # Ketum
        "dkx",  # Mazagway
        "neq",  # North Central Mixe
        "yna",  # Aluo
        "kfk",  # Kinnauri
        "klc",  # Kolbila
        "zmf",  # Mfinu
        "kdd",  # Yankunytjatjara
        "cky",  # Cakfem-Mushere
        "ryu",  # Central Okinawan
        "hvc",  # Haitian Vodoun Culture Language
        "zlm",  # Malay (individual language)
        "yaf",  # Yaka (Democratic Republic of Congo)
        "xub",  # Betta Kurumba
        "naj",  # Nalu
        "ptq",  # Pattapu
        "gab",  # Gabri
        "tdt",  # Tetun Dili
        "kvb",  # Kubu
        "ram",  # Canela
        "yxy",  # Yabula Yabula
        "kis",  # Kis
        "dzg",  # Dazaga
        "orh",  # Oroqen
        "uth",  # ut-Hun
        "gsp",  # Wasembo
        "pcr",  # Panang
        "kdg",  # Seba
        "mrb",  # Marino
        "qya",  # Quenya
        "wut",  # Wutung
        "aex",  # Amerax
        "pns",  # Ponosakan
        "kqk",  # Kotafon Gbe
        "haf",  # Haiphong Sign Language
        "xnm",  # Ngumbarl
        "tmr",  # Jewish Babylonian Aramaic (ca. 200-1200 CE)
        "hio",  # Tsoa
        "goh",  # Old High German (ca. 750-1050)
        "zsm",  # Standard Malay
        "pxm",  # Quetzaltepec Mixe
        "klp",  # Kamasa
        "asq",  # Austrian Sign Language
        "axk",  # Yaka (Central African Republic)
        "bpm",  # Biyom
        "xuf",  # Kunfal
        "atp",  # Pudtol Atta
        "goe",  # Gongduk
        "wrd",  # Warduji
        "aca",  # Achagua
        "ksz",  # Kodaku
        "nhg",  # Tetelcingo Nahuatl
        "yap",  # Yapese
        "esm",  # Esuma
        "hmy",  # Southern Guiyang Hmong
        "nyb",  # Nyangbo
        "bny",  # Bintulu
        "nsv",  # Southwestern Nisu
        "mxh",  # Mvuba
        "kfa",  # Kodava
        "aof",  # Bragat
        "kbg",  # Khamba
        "twx",  # Tewe
        "kuo",  # Kumukio
        "gdi",  # Gundi
        "ndu",  # Dugun
        "bxe",  # Birale
        "isv",  # Interslavic
        "axe",  # Ayerrerenge
        "nte",  # Nathembo
        "gup",  # Gunwinggu
        "xwo",  # Written Oirat
        "mvk",  # Mekmek
        "mcq",  # Ese
        "buj",  # Basa-Gurmana
        "jra",  # Jarai
        "pmr",  # Paynamar
        "nat",  # Ca̱hungwa̱rya̱
        "dga",  # Southern Dagaare
        "ttt",  # Muslim Tat
        "mkv",  # Mafea
        "kiu",  # Kirmanjki (individual language)
        "sny",  # Saniyo-Hiyewe
        "niz",  # Ningil
        "pae",  # Pagibete
        "acs",  # Acroá
        "ebg",  # Ebughu
        "nbh",  # Ngamo
        "nxx",  # Nafri
        "sec",  # Sechelt
        "spc",  # Sapé
        "vao",  # Vao
        "amg",  # Amurdak
        "sts",  # Shumashti
        "bnw",  # Bisis
        "wlh",  # Welaun
        "ylm",  # Limi
        "avn",  # Avatime
        "xku",  # Kaamba
        "lmt",  # Lematang
        "mjb",  # Makalero
        "moj",  # Monzombo
        "idt",  # Idaté
        "ksr",  # Borong
        "nrc",  # Noric
        "ngu",  # Guerrero Nahuatl
        "dmy",  # Demta
        "mlm",  # Mulam
        "lfa",  # Lefa
        "cir",  # Tiri
        "qum",  # Sipacapense
        "tsa",  # Tsaangi
        "xkh",  # Karahawyana
        "acu",  # Achuar-Shiwiar
        "wua",  # Wikngenchera
        "lnc",  # Languedocien
        "dgn",  # Dagoman
        "zpi",  # Santa María Quiegolani Zapotec
        "lwm",  # Laomian
        "dwa",  # Diri
        "gla",  # Scottish Gaelic
        "lot",  # Otuho
        "oua",  # Tagargrent
        "erg",  # Sie
        "tmf",  # Toba-Maskoy
        "yby",  # Yaweyuha
        "pnl",  # Paleni
        "stc",  # Santa Cruz
        "zpu",  # Yalálag Zapotec
        "biy",  # Birhor
        "yma",  # Yamphe
        "kin",  # Kinyarwanda
        "cya",  # Nopala Chatino
        "sro",  # Campidanese Sardinian
        "hoa",  # Hoava
        "plh",  # Paulohi
        "gdt",  # Kungardutyi
        "abw",  # Pal
        "msp",  # Maritsauá
        "cuy",  # Cuitlatec
        "twy",  # Tawoyan
        "rmc",  # Carpathian Romani
        "smm",  # Musasa
        "ttf",  # Tuotomb
        "ruo",  # Istro Romanian
        "mew",  # Maaka
        "kgw",  # Karon Dori
        "kpd",  # Koba
        "zpo",  # Amatlán Zapotec
        "kva",  # Bagvalal
        "lmg",  # Lamogai
        "bgg",  # Bugun
        "ztp",  # Loxicha Zapotec
        "kxs",  # Kangjia
        "ngb",  # Northern Ngbandi
        "ypa",  # Phala
        "hrz",  # Harzani
        "tbt",  # Tembo (Kitembo)
        "usi",  # Usui
        "snq",  # Sangu (Gabon)
        "snd",  # Sindhi
        "bti",  # Burate
        "dya",  # Dyan
        "bpg",  # Bonggo
        "bwr",  # Bura-Pabir
        "nib",  # Nakame
        "ban",  # Balinese
        "aro",  # Araona
        "asm",  # Assamese
        "gde",  # Gude
        "nao",  # Naaba
        "gnw",  # Western Bolivian Guaraní
        "luw",  # Luo (Cameroon)
        "und",  # Undetermined
        "mdj",  # Mangbetu
        "cha",  # Chamorro
        "bvq",  # Birri
        "puz",  # Purum Naga
        "pda",  # Anam
        "hom",  # Homa
        "lvi",  # Lavi
        "jbj",  # Arandai
        "cih",  # Chinali
        "aiz",  # Aari
        "ybj",  # Hasha
        "niq",  # Nandi
        "bgu",  # Mbongno
        "cpg",  # Cappadocian Greek
        "zhb",  # Zhaba
        "yxu",  # Yuyu
        "pyx",  # Pyu (Myanmar)
        "gjn",  # Gonja
        "hal",  # Halang
        "nyx",  # Nganyaywana
        "yua",  # Yucateco
        "bov",  # Tuwuli
        "nez",  # Nez Perce
        "qvw",  # Huaylla Wanca Quechua
        "swn",  # Sawknah
        "bpr",  # Koronadal Blaan
        "cug",  # Chungmboko
        "bfo",  # Malba Birifor
        "jah",  # Jah Hut
        "ijj",  # Ede Ije
        "ybo",  # Yabong
        "gdh",  # Gadjerawang
        "dmu",  # Dubu
        "tca",  # Ticuna
        "nwb",  # Nyabwa
        "ztg",  # Xanaguía Zapotec
        "ctu",  # Chol
        "nut",  # Nung (Viet Nam)
        "khg",  # Khams Tibetan
        "phq",  # Phana'
        "eur",  # Europanto
        "agv",  # Remontado Dumagat
        "ssp",  # Spanish Sign Language
        "piu",  # Pintupi-Luritja
        "nbq",  # Nggem
        "sid",  # Sidamo
        "swm",  # Samosa
        "dhr",  # Dhargari
        "ugo",  # Ugong
        "gko",  # Kok-Nar
        "tvw",  # Sedoa
        "bop",  # Bonkiman
        "ccr",  # Cacaopera
        "aec",  # Saidi Arabic
        "xcu",  # Curonian
        "dia",  # Dia
        "mqb",  # Mbuko
        "dms",  # Dampelas
        "knc",  # Central Kanuri
        "lyn",  # Luyana
        "xxk",  # Ke'o
        "khy",  # Kele (Democratic Republic of Congo)
        "qvh",  # Huamalíes-Dos de Mayo Huánuco Quechua
        "bmk",  # Ghayavi
        "pom",  # Southeastern Pomo
        "pry",  # Pray 3
        "bru",  # Eastern Bru
        "xga",  # Galatian
        "noo",  # Nootka
        "hur",  # Halkomelem
        "ykk",  # Yakaikeke
        "kqc",  # Doromu-Koki
        "syy",  # Al-Sayyid Bedouin Sign Language
        "bbx",  # Bubia
        "jye",  # Judeo-Yemeni Arabic
        "qxr",  # Cañar Highland Quichua
        "sis",  # Siuslaw
        "nrk",  # Ngarla
        "iar",  # Purari
        "wes",  # Cameroon Pidgin
        "sxe",  # Sighu
        "est",  # Estonian
        "kpl",  # Kpala
        "aib",  # Ainu (China)
        "hca",  # Andaman Creole Hindi
        "thv",  # Tahaggart Tamahaq
        "klh",  # Weliki
        "jui",  # Ngadjuri
        "rol",  # Romblomanon
        "zbc",  # Central Berawan
        "xwc",  # Woccon
        "zme",  # Mangerr
        "mly",  # Malay (individual language)
        "vor",  # Voro
        "kqh",  # Kisankasa
        "nyp",  # Nyang'i
        "rmm",  # Roma
        "dcr",  # Negerhollands
        "kuv",  # Kur
        "zhd",  # Dai Zhuang
        "kgp",  # Kaingang
        "jvn",  # Caribbean Javanese
        "kjt",  # Phrae Pwo Karen
        "wdj",  # Wadjiginy
        "lgm",  # Lega-Mwenga
        "noa",  # Woun Meu
        "mzc",  # Madagascar Sign Language
        "pto",  # Zo'é
        "ktd",  # Kokata
        "mqu",  # Mandari
        "mhx",  # Maru
        "kyd",  # Karey
        "tam",  # Tamil
        "mli",  # Malimpung
        "thn",  # Thachanadan
        "mxf",  # Malgbe
        "onp",  # Sartang
        "twr",  # Southwestern Tarahumara
        "myb",  # Mbay
        "knk",  # Kuranko
        "lch",  # Luchazi
        "cti",  # Tila Chol
        "dwy",  # Dhuwaya
        "ssu",  # Susuami
        "wrs",  # Waris
        "woo",  # Manombai
        "bgk",  # Bit
        "dgl",  # Andaandi
        "qub",  # Huallaga Huánuco Quechua
        "igm",  # Kanggape
        "ula",  # Fungwa
        "bjw",  # Bakwé
        "mfy",  # Mayo
        "lzz",  # Laz
        "beg",  # Belait
        "and",  # Ansus
        "ndk",  # Ndaka
        "ibr",  # Ibuoro
        "ral",  # Ralte
        "kgu",  # Kobol
        "mop",  # Mopán Maya
        "elu",  # Elu
        "krx",  # Karon
        "mat",  # San Francisco Matlatzinca
        "lud",  # Ludian
        "lnn",  # Lorediakarkar
        "ykg",  # Northern Yukaghir
        "ktb",  # Kambaata
        "bbc",  # Batak Toba
        "cjm",  # Eastern Cham
        "wiv",  # Vitu
        "drw",  # Darwazi
        "kwi",  # Awa-Cuaiquer
        "nge",  # Ngemba
        "ymh",  # Mili
        "ikz",  # Ikizu
        "con",  # Cofán
        "qur",  # Yanahuanca Pasco Quechua
        "bsb",  # Brunei Bisaya
        "uba",  # Ubang
        "cnb",  # Chinbon Chin
        "bne",  # Bintauna
        "mig",  # San Miguel El Grande Mixtec
        "clu",  # Caluyanun
        "pek",  # Penchal
        "lpo",  # Lipo
        "tmt",  # Tasmate
        "sns",  # South West Bay
        "mhq",  # Mandan
        "lkm",  # Kalaamaya
        "hno",  # Northern Hindko
        "szl",  # Silesian
        "fui",  # Bagirmi Fulfulde
        "rom",  # Romany
        "mwd",  # Mudbura
        "bcz",  # Bainouk-Gunyaamolo
        "scb",  # Chut
        "nhj",  # Tlalitzlipa Nahuatl
        "yud",  # Judeo-Tripolitanian Arabic
        "pij",  # Pijao
        "ilp",  # Iranun (Philippines)
        "tsd",  # Tsakonian
        "bzl",  # Boano (Sulawesi)
        "btv",  # Bateri
        "hkh",  # Khah
        "kau",  # Kanuri
        "tfr",  # Teribe
        "ctn",  # Chhintange
        "scl",  # Shina
        "sxo",  # Sorothaptic
        "xsj",  # Subi
        "mys",  # Mesmes
        "phh",  # Phukha
        "cbl",  # Bualkhaw Chin
        "jdg",  # Jadgali
        "tcx",  # Toda
        "afn",  # Defaka
        "mpe",  # Majang
        "mxd",  # Modang
        "yam",  # Yamba
        "aih",  # Ai-Cham
        "fun",  # Fulniô
        "sek",  # Sekani
        "ost",  # Osatu
        "tak",  # Tala
        "srp",  # Serbian
        "zeg",  # Zenag
        "yri",  # Yarí
        "pzn",  # Jejara Naga
        "poj",  # Lower Pokomo
        "zik",  # Zimakani
        "qxt",  # Santa Ana de Tusi Pasco Quechua
        "tvo",  # Tidore
        "vko",  # Kodeoha
        "sxc",  # Sicanian
        "mfa",  # Pattani Malay
        "mrz",  # Marind
        "liu",  # Logorik
        "mcg",  # Mapoyo
        "bos",  # Bosnian
        "ane",  # Xârâcùù
        "kxi",  # Keningau Murut
        "ngh",  # Nǁng
        "zmu",  # Muruwari
        "xae",  # Aequian
        "wbs",  # West Bengal Sign Language
        "mpw",  # Mapidian
        "grd",  # Guruntum-Mbaaru
        "kpj",  # Karajá
        "srv",  # Southern Sorsoganon
        "ckt",  # Chukot
        "rag",  # Logooli
        "net",  # Nete
        "bdc",  # Emberá-Baudó
        "rrm",  # Moriori
        "bzd",  # Bribri
        "gyg",  # Gbayi
        "asu",  # Tocantins Asurini
        "bez",  # Bena (Tanzania)
        "lcs",  # Lisabata-Nuniali
        "umg",  # Morrobalama
        "auc",  # Waorani
        "lmo",  # Lombard
        "lnw",  # Lanima
        "ulk",  # Meriam Mir
        "ikp",  # Ikpeshi
        "kls",  # Kalasha
        "kkh",  # Khün
        "khe",  # Korowai
        "yei",  # Yeni
        "wwa",  # Waama
        "csp",  # Southern Ping Chinese
        "nay",  # Ngarrindjeri
        "pdu",  # Kayan
        "bvx",  # Dibole
        "yuy",  # East Yugur
        "juh",  # Hõne
        "oni",  # Onin
        "nih",  # Nyiha (Tanzania)
        "gda",  # Gade Lohar
        "ywu",  # Wumeng Nasu
        "kat",  # Georgian
        "noq",  # Ngongo
        "gvy",  # Guyani
        "ysp",  # Southern Lolopo
        "ffi",  # Foia Foia
        "oka",  # Okanagan
        "taw",  # Tai
        "clc",  # Chilcotin
        "cav",  # Cavineña
        "bxw",  # Bankagooma
        "kdm",  # Kagoma
        "brz",  # Bilbil
        "aup",  # Makayam
        "nhw",  # Western Huasteca Nahuatl
        "vav",  # Varli
        "wok",  # Longto
        "leh",  # Lenje
        "tkq",  # Tee
        "bgx",  # Balkan Gagauz Turkish
        "tan",  # Tangale
        "xso",  # Solano
        "arb",  # Standard Arabic
        "tat",  # Tatar
        "phu",  # Phuan
        "ato",  # Atong (Cameroon)
        "qvc",  # Cajamarca Quechua
        "cmk",  # Chimakum
        "gse",  # Ghanaian Sign Language
        "kzv",  # Komyandaret
        "nkf",  # Inpui Naga
        "juc",  # Jurchen
        "miv",  # Mimi
        "kas",  # Kashmiri
        "lwe",  # Lewo Eleng
        "ugb",  # Kuku-Ugbanh
        "dix",  # Dixon Reef
        "hmq",  # Eastern Qiandong Miao
        "ddr",  # Dhudhuroa
        "atz",  # Arta
        "caq",  # Car Nicobarese
        "xib",  # Iberian
        "kcd",  # Ngkâlmpw Kanum
        "kuj",  # Kuria
        "lmy",  # Lamboya
        "zbe",  # East Berawan
        "sim",  # Mende (Papua New Guinea)
        "pmt",  # Tuamotuan
        "wmi",  # Wamin
        "bzb",  # Andio
        "wwr",  # Warrwa
        "boe",  # Mundabli
        "xwg",  # Kwegu
        "lgb",  # Laghu
        "xlu",  # Cuneiform Luwian
        "xst",  # Silt'e
        "sam",  # Samaritan Aramaic
        "sin",  # Sinhala
        "psa",  # Asue Awyu
        "rml",  # Baltic Romani
        "mcj",  # Mvanip
        "zax",  # Xadani Zapotec
        "mef",  # Megam
        "bcn",  # Bali (Nigeria)
        "syk",  # Sukur
        "hns",  # Caribbean Hindustani
        "agk",  # Isarog Agta
        "cho",  # Choctaw
        "jms",  # Mashi (Nigeria)
        "itk",  # Judeo-Italian
        "kve",  # Kalabakan
        "klr",  # Khaling
        "pli",  # Pali
        "ora",  # Oroha
        "toi",  # Tonga (Zambia)
        "ruk",  # Che
        "all",  # Allar
        "bof",  # Bolon
        "clt",  # Lautu Chin
        "ism",  # Masimasi
        "aho",  # Ahom
        "mem",  # Mangala
        "fni",  # Fania
        "act",  # Achterhoeks
        "tfn",  # Tanaina
        "une",  # Uneme
        "xsn",  # Sanga (Nigeria)
        "afb",  # Gulf Arabic
        "smu",  # Somray
        "ruq",  # Megleno Romanian
        "wle",  # Wolane
        "mkb",  # Mal Paharia
        "ekc",  # Eastern Karnic
        "elk",  # Elkei
        "kkt",  # Koi
        "ong",  # Olo
        "sad",  # Sandawe
        "sbi",  # Seti
        "mht",  # Mandahuaca
        "nwy",  # Nottoway-Meherrin
        "kny",  # Kanyok
        "mqg",  # Kota Bangun Kutai Malay
        "tre",  # East Tarangan
        "bra",  # Braj
        "oue",  # Oune
        "bog",  # Bamako Sign Language
        "kqy",  # Koorete
        "kcj",  # Kobiana
        "yla",  # Yaul
        "auj",  # Awjilah
        "lao",  # Lao
        "tln",  # Talondo'
        "tix",  # Southern Tiwa
        "nkn",  # Nkangala
        "wic",  # Wichita
        "whu",  # Wahau Kayan
        "mwv",  # Mentawai
        "auw",  # Awyi
        "zmd",  # Maridan
        "byu",  # Buyang
        "nrm",  # Narom
        "ski",  # Sika
        "kbv",  # Dera (Indonesia)
        "ngt",  # Kriang
        "mwl",  # Mirandese
        "tzx",  # Tabriak
        "asw",  # Australian Aborigines Sign Language
        "taz",  # Tocho
        "shn",  # Shan
        "lnm",  # Langam
        "bwd",  # Bwaidoka
        "tkb",  # Buksa
        "kgx",  # Kamaru
        "zkt",  # Kitan
        "krl",  # Karelian
        "bdf",  # Biage
        "acf",  # Saint Lucian Creole French
        "mae",  # Bo-Rukul
        "tmk",  # Northwestern Tamang
        "yly",  # Nyâlayu
        "xnq",  # Ngoni (Mozambique)
        "rop",  # Kriol
        "yec",  # Yeniche
        "uda",  # Uda
        "ksb",  # Shambala
        "sct",  # Southern Katang
        "leb",  # Lala-Bisa
        "mdi",  # Mamvu
        "was",  # Washo
        "sgs",  # Samogitian
        "naf",  # Nabak
        "nnp",  # Wancho Naga
        "kdu",  # Kadaru
        "cwt",  # Kuwaataay
        "taf",  # Tapirapé
        "xkz",  # Kurtokha
        "nzr",  # Dir-Nyamzak-Mbarimi
        "sbm",  # Sagala
        "mwa",  # Mwatebu
        "blh",  # Kuwaa
        "aog",  # Angoram
        "mrk",  # Hmwaveke
        "tlq",  # Tai Loi
        "dhs",  # Dhaiso
        "pgn",  # Paelignian
        "buo",  # Terei
        "syw",  # Kagate
        "alj",  # Alangan
        "acb",  # Áncá
        "scc",  # Serbian
        "tmx",  # Tomyang
        "bhz",  # Bada (Indonesia)
        "abg",  # Abaga
        "skv",  # Skou
        "nsd",  # Southern Nisu
        "cjv",  # Chuave
        "bek",  # Bebeli
        "tya",  # Tauya
        "ymz",  # Muzi
        "xon",  # Konkomba
        "lda",  # Kla-Dan
        "tks",  # Takestani
        "vid",  # Vidunda
        "wal",  # Wolaytta
        "wll",  # Wali (Sudan)
        "gkd",  # Magɨ (Madang Province)
        "quy",  # Ayacucho Quechua
        "tdm",  # Taruma
        "sxw",  # Saxwe Gbe
        "mub",  # Mubi
        "bcg",  # Baga Pokur
        "tcn",  # Tichurong
        "nqn",  # Nen
        "grt",  # Garo
        "kzf",  # Da'a Kaili
        "ack",  # Aka-Kora
        "urt",  # Urat
        "nnv",  # Nugunu (Australia)
        "nju",  # Ngadjunmaya
        "nkj",  # Nakai
        "riu",  # Riung
        "wky",  # Wangkayutyuru
        "dju",  # Kapriman
        "lla",  # Lala-Roba
        "mxo",  # Mbowe
        "nuf",  # Nusu
        "nyk",  # Nyaneka
        "qxl",  # Salasaca Highland Quichua
        "nru",  # Narua
        "jns",  # Jaunsari
        "noe",  # Nimadi
        "nbs",  # Namibian Sign Language
        "aum",  # Asu (Nigeria)
        "xno",  # Anglo-Norman
        "bui",  # Bongili
        "xuu",  # Kxoe
        "tme",  # Tremembé
        "mdk",  # Mangbutu
        "ibn",  # Ibino
        "rel",  # Rendille
        "kkv",  # Kangean
        "kwd",  # Kwaio
        "ort",  # Adivasi Oriya
        "asd",  # Asas
        "cle",  # Lealao Chinantec
        "ctp",  # Western Highland Chatino
        "ket",  # Ket
        "efe",  # Efe
        "kev",  # Kanikkaran
        "mxc",  # Manyika
        "iku",  # Inuktitut
        "kqi",  # Koitabu
        "lbo",  # Laven
        "pnk",  # Paunaka
        "aee",  # Northeast Pashai
        "cot",  # Caquinte
        "ino",  # Inoke-Yate
        "psp",  # Philippine Sign Language
        "jiy",  # Buyuan Jinuo
        "yln",  # Langnian Buyang
        "ynd",  # Yandruwandha
        "nxe",  # Nage
        "mnk",  # Mandinka
        "mkq",  # Bay Miwok
        "rem",  # Remo
        "grq",  # Gorovu
        "fod",  # Foodo
        "skd",  # Southern Sierra Miwok
        "cka",  # Khumi Awa Chin
        "xsh",  # Shamang
        "xpu",  # Punic
        "lrr",  # Southern Yamphu
        "mea",  # Menka
        "yzk",  # Zokhuo
        "cuh",  # Chuka
        "zaq",  # Aloápam Zapotec
        "pir",  # Piratapuyo
        "rxw",  # Karuwali
        "dgo",  # Dogri (individual language)
        "iii",  # Sichuan Yi
        "nul",  # Nusa Laut
        "ayy",  # Tayabas Ayta
        "loh",  # Laarim
        "tdx",  # Tandroy-Mahafaly Malagasy
        "njj",  # Njen
        "sne",  # Bau Bidayuh
        "wao",  # Wappo
        "doi",  # Dogri (macrolanguage)
        "umd",  # Umbindhamu
        "mab",  # Yutanduchi Mixtec
        "tdu",  # Tempasuk Dusun
        "urh",  # Urhobo
        "sst",  # Sinasina
        "ncm",  # Nambo
        "eng",  # English
        "xzh",  # Zhang-Zhung
        "haa",  # Han
        "sia",  # Akkala Sami
        "rnp",  # Rongpo
        "tue",  # Tuyuca
        "kgn",  # Karingani
        "wly",  # Waling
        "yzg",  # E'ma Buyang
        "ilm",  # Iranun (Malaysia)
        "psw",  # Port Sandwich
        "ggu",  # Gagu
        "yme",  # Yameo
        "kxu",  # Kui (India)
        "umb",  # Umbundu
        "blw",  # Balangao
        "shg",  # Shua
        "kii",  # Kitsai
        "lrk",  # Loarki
        "btp",  # Budibud
        "tja",  # Tajuasohn
        "pub",  # Purum
        "beb",  # Bebele
        "cre",  # Cree
        "itw",  # Ito
        "ixj",  # Chajul Ixil
        "lbu",  # Labu
        "rji",  # Raji
        "nod",  # Northern Thai
        "gmo",  # Gamo-Gofa-Dawro
        "mlu",  # To'abaita
        "pus",  # Pushto
        "ank",  # Goemai
        "cac",  # Chuj
        "xtz",  # Tasmanian
        "sef",  # Cebaara Senoufo
        "nnw",  # Southern Nuni
        "sdl",  # Saudi Arabian Sign Language
        "bpo",  # Anasi
        "ynu",  # Yahuna
        "bnr",  # Butmas-Tur
        "cto",  # Emberá-Catío
        "poe",  # San Juan Atzingo Popoloca
        "brc",  # Berbice Creole Dutch
        "ndh",  # Ndali
        "ibg",  # Ibanag
        "nkg",  # Nekgini
        "sws",  # Seluwasan
        "amn",  # Amanab
        "kih",  # Kilmeri
        "amu",  # Guerrero Amuzgo
        "wif",  # Wik-Keyangan
        "hir",  # Himarimã
        "jbu",  # Jukun Takum
        "slg",  # Selungai Murut
        "aky",  # Aka-Kol
        "fas",  # Persian
        "ktq",  # Katabaga
        "yrl",  # Nhengatu
        "ntr",  # Delo
        "uzb",  # Uzbek
        "wru",  # Waru
        "orz",  # Ormu
        "scw",  # Sha
        "lnu",  # Longuda
        "pti",  # Pindiini
        "jkm",  # Mobwa Karen
        "niw",  # Nimo
        "avu",  # Avokaya
        "ypz",  # Phuza
        "kzj",  # Coastal Kadazan
        "dse",  # Dutch Sign Language
        "njz",  # Nyishi
        "syr",  # Syriac
        "tde",  # Tiranige Diga Dogon
        "klw",  # Tado
        "lbe",  # Lak
        "mkj",  # Mokilese
        "omp",  # Old Manipuri
        "uri",  # Urim
        "apo",  # Ambul
        "zgm",  # Minz Zhuang
        "bqb",  # Bagusa
        "tdr",  # Todrah
        "cde",  # Chenchu
        "nwa",  # Nawathinehena
        "tlz",  # Toala'
        "ase",  # American Sign Language
        "grc",  # Ancient Greek (to 1453)
        "lsr",  # Aruop
        "odk",  # Od
        "dyi",  # Djimini Senoufo
        "nnt",  # Nanticoke
        "hmb",  # Humburi Senni Songhay
        "two",  # Tswapong
        "tzo",  # Tzotzil
        "bbt",  # Mburku
        "bdz",  # Badeshi
        "gpe",  # Ghanaian Pidgin English
        "sna",  # Shona
        "wiw",  # Wirangu
        "lgs",  # Guinea-Bissau Sign Language
        "nts",  # Natagaimas
        "wae",  # Walser
        "jap",  # Jaruára
        "wnb",  # Mokati
        "gsg",  # German Sign Language
        "sfw",  # Sehwi
        "cuj",  # Mashco Piro
        "kts",  # South Muyu
        "hmg",  # Southwestern Guiyang Hmong
        "tcw",  # Tecpatlán Totonac
        "msk",  # Mansaka
        "sse",  # Balangingi
        "pnz",  # Pana (Central African Republic)
        "mux",  # Bo-Ung
        "ajp",  # South Levantine Arabic
        "kuf",  # Western Katu
        "adi",  # Adi
        "lhm",  # Lhomi
        "fuc",  # Pulaar
        "hij",  # Hijuk
        "knm",  # Kanamarí
        "nwc",  # Classical Newari
        "tzm",  # Central Atlas Tamazight
        "mok",  # Morori
        "ipo",  # Ipiko
        "wul",  # Silimo
        "rmp",  # Rempi
        "spd",  # Saep
        "aug",  # Aguna
        "tcq",  # Kaiy
        "bni",  # Bangi
        "urg",  # Urigina
        "kbl",  # Kanembu
        "kjc",  # Coastal Konjo
        "tnz",  # Ten'edn
        "csm",  # Central Sierra Miwok
        "jod",  # Wojenaka
        "gev",  # Eviya
        "nmp",  # Nimanbur
        "apg",  # Ampanang
        "afo",  # Eloyi
        "dif",  # Dieri
        "ssj",  # Sausi
        "etr",  # Edolo
        "vmg",  # Lungalunga
        "cuv",  # Cuvok
        "crk",  # Plains Cree
        "mtc",  # Munit
        "val",  # Vehes
        "fpe",  # Fernando Po Creole English
        "abd",  # Manide
        "nbk",  # Nake
        "npx",  # Noipx
        "kgi",  # Selangor Sign Language
        "rbp",  # Barababaraba
        "amw",  # Western Neo-Aramaic
        "abm",  # Abanyom
        "xti",  # Sinicahua Mixtec
        "ixl",  # Ixil
        "lsl",  # Latvian Sign Language
        "mbh",  # Mangseng
        "kta",  # Katua
        "dbu",  # Bondum Dom Dogon
        "gvl",  # Gulay
        "crc",  # Lonwolwol
        "khm",  # Khmer
        "mzp",  # Movima
        "brd",  # Baraamu
        "bff",  # Bofi
        "nrz",  # Lala
        "weh",  # Weh
        "xsc",  # Scythian
        "bjd",  # Bandjigali
        "srw",  # Serua
        "yaj",  # Banda-Yangere
        "ykm",  # Kap
        "isl",  # Icelandic
        "xuj",  # Jennu Kurumba
        "uks",  # Urubú-Kaapor Sign Language
        "jao",  # Yanyuwa
        "smz",  # Simeku
        "mfz",  # Mabaan
        "nej",  # Neko
        "pem",  # Phende
        "kdc",  # Kutu
        "kni",  # Kanufi
        "sxu",  # Upper Saxon
        "evh",  # Uvbie
        "tvl",  # Tuvalu
        "krg",  # North Korowai
        "ido",  # Ido
        "ace",  # Achinese
        "bgl",  # Bo (Laos)
        "mms",  # Southern Mam
        "mfl",  # Putai
        "smj",  # Lule Sami
        "xve",  # Venetic
        "pip",  # Pero
        "ztu",  # Güilá Zapotec
        "zln",  # Lianshan Zhuang
        "wuv",  # Wuvulu-Aua
        "fue",  # Borgu Fulfulde
        "bde",  # Bade
        "llg",  # Lole
        "ons",  # Ono
        "sus",  # Susu
        "kql",  # Kyenele
        "qve",  # Eastern Apurímac Quechua
        "anr",  # Andh
        "nok",  # Nooksack
        "puw",  # Puluwatese
        "txy",  # Tanosy Malagasy
        "azo",  # Awing
        "tsz",  # Purepecha
        "akp",  # Siwu
        "nkd",  # Koireng
        "dmb",  # Mombo Dogon
        "nkz",  # Nkari
        "ksk",  # Kansa
        "mbn",  # Macaguán
        "aki",  # Aiome
        "ggt",  # Gitua
        "inj",  # Jungle Inga
        "ggk",  # Kungarakany
        "kio",  # Kiowa
        "itm",  # Itu Mbon Uzo
        "oav",  # Old Avar
        "dji",  # Djinang
        "mlj",  # Miltu
        "nof",  # Nomane
        "dhu",  # Dhurga
        "mci",  # Mese
        "kms",  # Kamasau
        "kzz",  # Kalabra
        "ckf",  # Southern Cakchiquel
        "nnr",  # Narungga
        "tch",  # Turks And Caicos Creole English
        "cdj",  # Churahi
        "gam",  # Kandawo
        "uln",  # Unserdeutsch
        "gwb",  # Gwa
        "nhi",  # Zacatlán-Ahuacatlán-Tepetzintla Nahuatl
        "oru",  # Ormuri
        "dis",  # Dimasa
        "anq",  # Jarawa (India)
        "ife",  # Ifè
        "mgx",  # Omati
        "ain",  # Ainu (Japan)
        "kye",  # Krache
        "gkp",  # Guinea Kpelle
        "mow",  # Moi (Congo)
        "pcd",  # Picard
        "bfe",  # Betaf
        "huj",  # Northern Guiyang Hmong
        "lhu",  # Lahu
        "ots",  # Estado de México Otomi
        "mxe",  # Mele-Fila
        "nsl",  # Norwegian Sign Language
        "nsn",  # Nehan
        "oum",  # Ouma
        "gmy",  # Mycenaean Greek
        "lbn",  # Rmeet
        "aii",  # Assyrian Neo-Aramaic
        "chp",  # Chipewyan
        "snz",  # Kou
        "ndl",  # Ndolo
        "sun",  # Sundanese
        "krf",  # Koro (Vanuatu)
        "pix",  # Piu
        "dmo",  # Kemedzung
        "vbb",  # Southeast Babar
        "tiv",  # Tiv
        "sdu",  # Sarudu
        "geh",  # Hutterite German
        "wgy",  # Warrgamay
        "pee",  # Taje
        "twa",  # Twana
        "seq",  # Senara Sénoufo
        "sqr",  # Siculo Arabic
        "gbx",  # Eastern Xwla Gbe
        "seg",  # Segeju
        "pid",  # Piaroa
        "phw",  # Phangduwali
        "dai",  # Day
        "suz",  # Sunwar
        "cno",  # Con
        "uvl",  # Lote
        "wfg",  # Yafi
        "rsi",  # Rennellese Sign Language
        "ztx",  # Zaachila Zapotec
        "myi",  # Mina (India)
        "fad",  # Wagi
        "kyt",  # Kayagar
        "bbh",  # Bugan
        "lnj",  # Leningitij
        "hrk",  # Haruku
        "aab",  # Alumu-Tesu
        "tnp",  # Whitesands
        "tpc",  # Azoyú Me'phaa
        "xcw",  # Coahuilteco
        "zwa",  # Zay
        "ghs",  # Guhu-Samane
        "bqa",  # Tchumbuli
        "jdt",  # Judeo-Tat
        "ldq",  # Lufu
        "ugh",  # Kubachi
        "mcs",  # Mambai
        "ori",  # Oriya (macrolanguage)
        "wea",  # Wewaw
        "yhs",  # Yan-nhaŋu Sign Language
        "bzo",  # Bozaba
        "nke",  # Duke
        "akl",  # Aklanon
        "xma",  # Mushungulu
        "kyc",  # Kyaka
        "tgz",  # Tagalaka
        "umr",  # Umbugarla
        "tli",  # Tlingit
        "atv",  # Northern Altai
        "nym",  # Nyamwezi
        "kmd",  # Majukayang Kalinga
        "ner",  # Yahadian
        "ldh",  # Lamja-Dengsa-Tola
        "dor",  # Dori'o
        "swf",  # Sere
        "aml",  # War-Jaintia
        "kzn",  # Kokola
        "mar",  # Marathi
        "upi",  # Umeda
        "vnk",  # Vano
        "qxu",  # Arequipa-La Unión Quechua
        "muv",  # Muthuvan
        "acm",  # Mesopotamian Arabic
        "oor",  # Oorlams
        "ngk",  # Dalabon
        "xxm",  # Minkin
        "ddj",  # Jaru
        "tbs",  # Tanguat
        "nin",  # Ninzo
        "tlt",  # Sou Nama
        "bhs",  # Buwal
        "tck",  # Tchitchege
        "isn",  # Isanzu
        "yuw",  # Yau (Morobe Province)
        "tev",  # Teor
        "bwm",  # Biwat
        "mky",  # East Makian
        "fak",  # Fang (Cameroon)
        "ojp",  # Old Japanese
        "aou",  # A'ou
        "fud",  # East Futuna
        "gac",  # Mixed Great Andamanese
        "nom",  # Nocamán
        "cup",  # Cupeño
        "alz",  # Alur
        "blj",  # Bolongan
        "yea",  # Ravula
        "bif",  # Biafada
        "goi",  # Gobasi
        "gcd",  # Ganggalida
        "abs",  # Ambonese Malay
        "wat",  # Kaninuwa
        "guc",  # Wayuu
        "xtc",  # Katcha-Kadugli-Miri
        "oun",  # ǃOǃung
        "tpu",  # Tampuan
        "ceg",  # Chamacoco
        "mod",  # Mobilian
        "vaf",  # Vafsi
        "kwt",  # Kwesten
        "obm",  # Moabite
        "tze",  # Chenalhó Tzotzil
        "gau",  # Mudhili Gadaba
        "stf",  # Seta
        "mpy",  # Mapia
        "bxs",  # Busam
        "sau",  # Saleman
        "suw",  # Sumbwa
        "dhv",  # Dehu
        "tig",  # Tigre
        "abp",  # Abellen Ayta
        "jda",  # Jad
        "kud",  # 'Auhelawa
        "mah",  # Marshallese
        "nla",  # Ngombale
        "www",  # Wawa
        "blm",  # Beli (South Sudan)
        "chw",  # Chuwabu
        "crh",  # Crimean Tatar
        "pec",  # Southern Pesisir
        "lmc",  # Limilngan
        "nek",  # Neku
        "nou",  # Ewage-Notu
        "ami",  # Amis
        "tes",  # Tengger
        "mrq",  # North Marquesan
        "bcf",  # Bamu
        "hrr",  # Horuru
        "tuy",  # Tugen
        "tdd",  # Tai Nüa
        "nbt",  # Na
        "aqg",  # Arigidi
        "tju",  # Tjurruru
        "cnh",  # Hakha Chin
        "gke",  # Ndai
        "bnf",  # Masiwang
        "xhu",  # Hurrian
        "win",  # Ho-Chunk
        "tav",  # Tatuyo
        "lns",  # Lamnso'
        "bah",  # Bahamas Creole English
        "tbr",  # Tumtum
        "mbs",  # Sarangani Manobo
        "zam",  # Miahuatlán Zapotec
        "psy",  # Piscataway
        "pue",  # Puelche
        "zrp",  # Zarphatic
        "lhp",  # Lhokpu
        "chn",  # Chinook jargon
        "cso",  # Sochiapam Chinantec
        "ihw",  # Bidhawal
        "bsa",  # Abinomn
        "lmx",  # Laimbue
        "nln",  # Durango Nahuatl
        "xtn",  # Northern Tlaxiaco Mixtec
        "zoo",  # Asunción Mixtepec Zapotec
        "wma",  # Mawa (Nigeria)
        "yin",  # Riang Lai
        "kmu",  # Kanite
        "mfd",  # Mendankwe-Nkwen
        "nau",  # Nauru
        "uan",  # Kuan
        "ley",  # Lemolang
        "tjj",  # Tjungundji
        "zsa",  # Sarasira
        "piz",  # Pije
        "xth",  # Yitha Yitha
        "wsk",  # Waskia
        "den",  # Slave (Athapascan)
        "tyx",  # Teke-Tyee
        "mjz",  # Majhi
        "thk",  # Tharaka
        "snc",  # Sinaugoro
        "zmo",  # Molo
        "cnw",  # Ngawn Chin
        "mld",  # Malakhel
        "nsf",  # Northwestern Nisu
        "bqz",  # Bakaka
        "lvu",  # Levuka
        "sxg",  # Shuhi
        "vmc",  # Juxtlahuaca Mixtec
        "aly",  # Alyawarr
        "byc",  # Ubaghara
        "smy",  # Semnani
        "kbu",  # Kabutra
        "bzj",  # Belize Kriol English
        "sma",  # Southern Sami
        "wgw",  # Wagawaga
        "abi",  # Abidji
        "bpt",  # Barrow Point
        "yky",  # Yakoma
        "aic",  # Ainbai
        "kmq",  # Kwama
        "ckv",  # Kavalan
        "gsn",  # Nema
        "mzi",  # Ixcatlán Mazatec
        "btz",  # Batak Alas-Kluet
        "smw",  # Sumbawa
        "lmn",  # Lambadi
        "paz",  # Pankararú
        "oku",  # Oku
        "kgl",  # Kunggari
        "byv",  # Medumba
        "ypl",  # Pula Yi
        "kya",  # Kwaya
        "ems",  # Pacific Gulf Yupik
        "opo",  # Opao
        "buw",  # Bubi
        "mhm",  # Makhuwa-Moniga
        "njm",  # Angami Naga
        "okv",  # Orokaiva
        "oda",  # Odut
        "twi",  # Twi
        "shb",  # Ninam
        "gud",  # Yocoboué Dida
        "rzh",  # Rāziḥī
        "dae",  # Duupa
        "hat",  # Haitian
        "otq",  # Querétaro Otomi
        "drg",  # Rungus
        "xap",  # Apalachee
        "pnx",  # Phong-Kniang
        "egm",  # Benamanga
        "wlv",  # Wichí Lhamtés Vejoz
        "hke",  # Hunde
        "zaj",  # Zaramo
        "plq",  # Palaic
        "xtv",  # Thawa
        "ybb",  # Yemba
        "acz",  # Acheron
        "aub",  # Alugu
        "aws",  # South Awyu
        "twg",  # Tereweng
        "bzk",  # Nicaragua Creole English
        "tpt",  # Tlachichilco Tepehua
        "kjj",  # Khinalugh
        "bbu",  # Kulung (Nigeria)
        "pze",  # Pesse
        "fgr",  # Fongoro
        "rib",  # Bribri Sign Language
        "ele",  # Elepi
        "sir",  # Siri
        "fuy",  # Fuyug
        "yrs",  # Yarsun
        "mdw",  # Mbosi
        "sgk",  # Sangkong
        "tha",  # Thai
        "wer",  # Weri
        "dth",  # Adithinngithigh
        "liq",  # Libido
        "mke",  # Mawchi
        "mit",  # Southern Puebla Mixtec
        "mpj",  # Martu Wangka
        "ngi",  # Ngizim
        "bub",  # Bua
        "wmc",  # Wamas
        "rtm",  # Rotuman
        "bqy",  # Bengkala Sign Language
        "asp",  # Algerian Sign Language
        "nhx",  # Isthmus-Mecayapan Nahuatl
        "bhl",  # Bimin
        "bfr",  # Bazigar
        "nig",  # Ngalakgan
        "zza",  # Zaza
        "kkc",  # Odoodee
        "blg",  # Balau
        "ssx",  # Samberigi
        "uhn",  # Damal
        "lss",  # Lasi
        "pev",  # Pémono
        "otm",  # Eastern Highland Otomi
        "gdj",  # Gurdjar
        "nhc",  # Tabasco Nahuatl
        "svk",  # Slovakian Sign Language
        "ibo",  # Igbo
        "qxq",  # Qashqa'i
        "mwi",  # Labo
        "sym",  # Maya Samo
        "vut",  # Vute
        "hml",  # Luopohe Hmong
        "nga",  # Ngbaka
        "tva",  # Vaghua
        "cag",  # Nivaclé
        "ysy",  # Sanie
        "myk",  # Mamara Senoufo
        "oty",  # Old Tamil
        "stn",  # Owa
        "mcc",  # Bitur
        "mrn",  # Cheke Holo
        "srd",  # Sardinian
        "bsz",  # Souletin Basque
        "ali",  # Amaimon
        "blv",  # Kibala
        "bav",  # Vengo
        "tmy",  # Tami
        "ztc",  # Lachirioag Zapotec
        "nre",  # Southern Rengma Naga
        "trq",  # San Martín Itunyoso Triqui
        "kzt",  # Tambunan Dusun
        "kte",  # Nubri
        "abf",  # Abai Sungai
        "qxs",  # Southern Qiang
        "ypn",  # Ani Phowa
        "pad",  # Paumarí
        "aai",  # Arifama-Miniafia
        "kam",  # Kamba (Kenya)
        "msc",  # Sankaran Maninka
        "opt",  # Opata
        "xeu",  # Keoru-Ahia
        "sln",  # Salinan
        "xav",  # Xavánte
        "ncb",  # Central Nicobarese
        "mca",  # Maca
        "ngl",  # Lomwe
        "yup",  # Yukpa
        "nrn",  # Norn
        "rbl",  # Miraya Bikol
        "djr",  # Djambarrpuyngu
        "gso",  # Southwest Gbaya
        "hax",  # Southern Haida
        "fom",  # Foma
        "nbw",  # Southern Ngbandi
        "pbo",  # Papel
        "tkp",  # Tikopia
        "mtx",  # Tidaá Mixtec
        "kxq",  # Smärky Kanum
        "onr",  # Northern One
        "goc",  # Gorakor
        "gut",  # Maléku Jaíka
        "piw",  # Pimbwe
        "nus",  # Nuer
        "tsj",  # Tshangla
        "vin",  # Vinza
        "xnk",  # Nganakarti
        "sqs",  # Sri Lankan Sign Language
        "qut",  # West Central Quiché
        "mxb",  # Tezoatlán Mixtec
        "bia",  # Badimaya
        "nse",  # Nsenga
        "afk",  # Nanubae
        "hmv",  # Hmong Dô
        "kso",  # Kofa
        "nzd",  # Nzadi
        "fwe",  # Fwe
        "bky",  # Bokyi
        "epi",  # Epie
        "okr",  # Kirike
        "bkv",  # Bekwarra
        "csd",  # Chiangmai Sign Language
        "duz",  # Duli-Gey
        "zmp",  # Mpuono
        "tep",  # Tepecano
        "ghk",  # Geko Karen
        "nkr",  # Nukuoro
        "ssl",  # Western Sisaala
        "dij",  # Dai
        "yis",  # Yis
        "yux",  # Southern Yukaghir
        "xcm",  # Comecrudo
        "ntk",  # Ikoma-Nata-Isenye
        "dgr",  # Tlicho
        "aax",  # Mandobo Atas
        "xlp",  # Lepontic
        "ziz",  # Zizilivakan
        "xru",  # Marriammu
        "zum",  # Kumzari
        "pri",  # Paicî
        "mcy",  # South Watut
        "mfc",  # Mba
        "vsl",  # Venezuelan Sign Language
        "btt",  # Bete-Bendi
        "tcs",  # Torres Strait Creole
        "nos",  # Eastern Nisu
        "btn",  # Ratagnon
        "apn",  # Apinayé
        "ntj",  # Ngaanyatjarra
        "csx",  # Cambodian Sign Language
        "enr",  # Emumu
        "pio",  # Piapoco
        "ccd",  # Cafundo Creole
        "geq",  # Geme
        "jgo",  # Ngomba
        "kxg",  # Katingan
        "grb",  # Grebo
        "leg",  # Lengua
        "sow",  # Sowanda
        "drh",  # Darkhat
        "oia",  # Oirata
        "ads",  # Adamorobe Sign Language
        "tag",  # Tagoi
        "tpj",  # Tapieté
        "mbz",  # Amoltepec Mixtec
        "bkj",  # Pande
        "tlr",  # Talise
        "usa",  # Usarufa
        "hop",  # Hopi
        "tip",  # Trimuris
        "mrw",  # Maranao
        "dsz",  # Mardin Sign Language
        "maw",  # Mampruli
        "nuj",  # Nyole
        "ury",  # Orya
        "bqw",  # Buru (Nigeria)
        "kcn",  # Nubi
        "nku",  # Bouna Kulango
        "pol",  # Polish
        "tug",  # Tunia
        "sra",  # Saruga
        "urp",  # Uru-Pa-In
        "jog",  # Jogi
        "wnw",  # Wintu
        "bfk",  # Ban Khor Sign Language
        "mou",  # Mogum
        "pot",  # Potawatomi
        "ged",  # Gade
        "hae",  # Eastern Oromo
        "khw",  # Khowar
        "xks",  # Kumbewaha
        "cbg",  # Chimila
        "gli",  # Guliguli
        "chj",  # Ojitlán Chinantec
        "aqn",  # Northern Alta
        "yim",  # Yimchungru Naga
        "fvr",  # Fur
        "cbw",  # Kinabalian
        "nsx",  # Nsongo
        "tuq",  # Tedaga
        "gcc",  # Mali
        "tte",  # Bwanabwana
        "aji",  # Ajië
        "kzy",  # Kango (Tshopo District)
        "mql",  # Mbelime
        "ztl",  # Lapaguía-Guivini Zapotec
        "sdz",  # Sallands
        "plw",  # Brooke's Point Palawano
        "bux",  # Boghom
        "gnk",  # ǁGana
        "hji",  # Haji
        "swq",  # Sharwa
        "blq",  # Baluan-Pam
        "duv",  # Duvle
        "ais",  # Nataoran Amis
        "xun",  # Unggaranggu
        "wji",  # Warji
        "ara",  # Arabic
        "lkl",  # Laeko-Libuat
        "dhl",  # Dhalandji
        "mri",  # Maori
        "cab",  # Garifuna
        "mjw",  # Karbi
        "geb",  # Kire
        "tuv",  # Turkana
        "ana",  # Andaqui
        "mnz",  # Moni
        "pon",  # Pohnpeian
        "bbw",  # Baba
        "quk",  # Chachapoyas Quechua
        "phj",  # Pahari
        "mxv",  # Metlatónoc Mixtec
        "gdu",  # Gudu
        "rmd",  # Traveller Danish
        "yxa",  # Mayawali
        "kiq",  # Kosadle
        "glo",  # Galambu
        "cua",  # Cua
        "zpg",  # Guevea De Humboldt Zapotec
        "sog",  # Sogdian
        "hab",  # Hanoi Sign Language
        "nbc",  # Chang Naga
        "yng",  # Yango
        "lij",  # Ligurian
        "ppm",  # Papuma
        "txx",  # Tatana
        "pst",  # Central Pashto
        "zay",  # Zayse-Zergulla
        "fkk",  # Kirya-Konzəl
        "kfp",  # Korwa
        "szc",  # Semaq Beri
        "hyw",  # Western Armenian
        "sgp",  # Singpho
        "jaq",  # Yaqay
        "aed",  # Argentine Sign Language
        "nwg",  # Ngayawung
        "vmk",  # Makhuwa-Shirima
        "owi",  # Owiniga
        "twf",  # Northern Tiwa
        "jnd",  # Jandavra
        "sdb",  # Shabak
        "duy",  # Dicamay Agta
        "klu",  # Klao
        "bfx",  # Bantayanon
        "rac",  # Rasawa
        "rga",  # Roria
        "oml",  # Ombo
        "kwl",  # Kofyar
        "mdf",  # Moksha
        "add",  # Lidzonka
        "hit",  # Hittite
        "bcc",  # Southern Balochi
        "wro",  # Worrorra
        "awv",  # Jair Awyu
        "vmv",  # Valley Maidu
        "gui",  # Eastern Bolivian Guaraní
        "gby",  # Gbari
        "sck",  # Sadri
        "gat",  # Kenati
        "spy",  # Sabaot
        "nmd",  # Ndumu
        "pab",  # Parecís
        "thf",  # Thangmi
        "tei",  # Torricelli
        "vig",  # Viemo
        "int",  # Intha
        "udi",  # Udi
        "mwe",  # Mwera (Chimwera)
        "jet",  # Manem
        "gbj",  # Bodo Gadaba
        "cip",  # Chiapanec
        "bwo",  # Boro (Ethiopia)
        "btm",  # Batak Mandailing
        "fap",  # Paloor
        "mle",  # Manambu
        "xil",  # Illyrian
        "mlv",  # Motlav
        "dml",  # Dameli
        "dat",  # Darang Deng
        "zin",  # Zinza
        "gea",  # Geruma
        "afs",  # Afro-Seminole Creole
        "ahg",  # Qimant
        "pil",  # Yom
        "ald",  # Alladian
        "sel",  # Selkup
        "ckk",  # Acatenango Southwestern Cakchiquel
        "mqi",  # Mariri
        "ctc",  # Chetco
        "aun",  # Molmo One
        "zom",  # Zou
        "tdv",  # Toro
        "ron",  # Romanian
        "giy",  # Giyug
        "mia",  # Miami
        "waj",  # Waffa
        "sje",  # Pite Sami
        "pos",  # Sayula Popoluca
        "bjn",  # Banjar
        "nyy",  # Nyakyusa-Ngonde
        "jub",  # Wannu
        "bhx",  # Bhalay
        "rob",  # Tae'
        "loy",  # Loke
        "tof",  # Gizrra
        "cwg",  # Chewong
        "thm",  # Aheu
        "gae",  # Guarequena
        "aos",  # Taikat
        "mdm",  # Mayogo
        "nyn",  # Nyankole
        "big",  # Biangai
        "ybl",  # Yukuben
        "ila",  # Ile Ape
        "cps",  # Capiznon
        "ixc",  # Ixcatec
        "ree",  # Rejang Kayan
        "mog",  # Mongondow
        "crf",  # Caramanta
        "kul",  # Kulere
        "zpq",  # Zoogocho Zapotec
        "mlh",  # Mape
        "eri",  # Ogea
        "hbb",  # Huba
        "boy",  # Bodo (Central African Republic)
        "vie",  # Vietnamese
        "tij",  # Tilung
        "brk",  # Birked
        "pnc",  # Pannei
        "shs",  # Shuswap
        "uum",  # Urum
        "faj",  # Faita
        "frq",  # Forak
        "mhp",  # Balinese Malay
        "wbj",  # Alagwa
        "kxd",  # Brunei
        "zkh",  # Khorezmian
        "kof",  # Kubi
        "poo",  # Central Pomo
        "xmh",  # Kugu-Muminh
        "psl",  # Puerto Rican Sign Language
        "gov",  # Goo
        "ybn",  # Yabaâna
        "lka",  # Lakalei
        "ybx",  # Yawiyo
        "zal",  # Zauzou
        "puu",  # Punu
        "jgk",  # Gwak
        "pdn",  # Podena
        "tjn",  # Tonjon
        "apd",  # Sudanese Arabic
        "jru",  # Japrería
        "ung",  # Ngarinyin
        "tmv",  # Tembo (Motembo)
        "sgb",  # Mag-antsi Ayta
        "szw",  # Sawai
        "thr",  # Rana Tharu
        "pef",  # Northeastern Pomo
        "bco",  # Kaluli
        "cpb",  # Ucayali-Yurúa Ashéninka
        "jiv",  # Shuar
        "syi",  # Seki
        "faf",  # Fagani
        "tgn",  # Tandaganon
        "bfh",  # Blafe
        "bvp",  # Bumang
        "ssq",  # So'a
        "bsn",  # Barasana-Eduria
        "mgg",  # Mpumpong
        "drq",  # Dura
        "huc",  # ǂHua
        "bed",  # Bedoanas
        "jig",  # Jingulu
        "fng",  # Fanagalo
        "mmg",  # North Ambrym
        "nyi",  # Ama (Sudan)
        "snh",  # Shinabo
        "mso",  # Mombum
        "lks",  # Kisa
        "coy",  # Coyaima
        "shu",  # Chadian Arabic
        "nph",  # Phom Naga
        "paq",  # Parya
        "lin",  # Lingala
        "ump",  # Umpila
        "hiw",  # Hiw
        "puo",  # Puoc
        "xsy",  # Saisiyat
        "lam",  # Lamba
        "bae",  # Baré
        "ure",  # Uru
        "doz",  # Dorze
        "dbe",  # Dabe
        "mwh",  # Mouk-Aria
        "the",  # Chitwania Tharu
        "mki",  # Dhatki
        "sdf",  # Sarli
        "mal",  # Malayalam
        "izz",  # Izii
        "dgu",  # Degaru
        "lke",  # Kenyi
        "aip",  # Burumakok
        "sjl",  # Sajalong
        "dos",  # Dogosé
        "ggd",  # Gugadj
        "pkt",  # Maleng
        "mnc",  # Manchu
        "ldp",  # Tso
        "awk",  # Awabakal
        "ldi",  # Laari
        "mjh",  # Mwera (Nyasa)
        "nha",  # Nhanda
        "cam",  # Cemuhî
        "dzl",  # Dzalakha
        "air",  # Airoran
        "hru",  # Hruso
        "iwm",  # Iwam
        "nmq",  # Nambya
        "sjc",  # Shaojiang Chinese
        "bdp",  # Bende
        "bxn",  # Burduna
        "kor",  # Korean
        "poi",  # Highland Popoluca
        "kwg",  # Sara Kaba Deme
        "kss",  # Southern Kisi
        "nud",  # Ngala
        "adq",  # Adangbe
        "hdn",  # Northern Haida
        "vil",  # Vilela
        "yvt",  # Yavitero
        "ppp",  # Pelende
        "dro",  # Daro-Matu Melanau
        "nba",  # Nyemba
        "bix",  # Bijori
        "bjh",  # Bahinemo
        "dze",  # Djiwarli
        "snb",  # Sebuyau
        "uar",  # Tairuma
        "tez",  # Tetserret
        "set",  # Sentani
        "icl",  # Icelandic Sign Language
        "kcb",  # Kawacha
        "kra",  # Kumhali
        "dii",  # Dimbong
        "ple",  # Palu'e
        "mla",  # Malo
        "wbe",  # Waritai
        "yxm",  # Yinwum
        "wga",  # Wagaya
        "hlu",  # Hieroglyphic Luwian
        "byt",  # Berti
        "ydk",  # Yoidik
        "afd",  # Andai
        "zar",  # Rincón Zapotec
        "tlk",  # Taloki
        "maz",  # Central Mazahua
        "nrb",  # Nara
        "kob",  # Kohoroxitari
        "btd",  # Batak Dairi
        "cmn",  # Mandarin Chinese
        "wgb",  # Wagawaga
        "xyj",  # Mayi-Yapi
        "aga",  # Aguano
        "gft",  # Gafat
        "kfd",  # Korra Koraga
        "xyy",  # Yorta Yorta
        "tty",  # Sikaritai
        "mbl",  # Maxakalí
        "orn",  # Orang Kanaq
        "nnn",  # Ngete
        "how",  # Honi
        "hme",  # Eastern Huishui Hmong
        "tnd",  # Angosturas Tunebo
        "mpx",  # Misima-Panaeati
        "vml",  # Malgana
        "pau",  # Palauan
        "uun",  # Kulon-Pazeh
        "agq",  # Aghem
        "pop",  # Pwapwâ
        "bzu",  # Burmeso
        "nhf",  # Nhuwala
        "doc",  # Northern Dong
        "cid",  # Chimariko
        "mkw",  # Kituba (Congo)
        "jaf",  # Jara
        "cpo",  # Kpeego
        "tcu",  # Southeastern Tarahumara
        "gez",  # Geez
        "mnv",  # Rennell-Bellona
        "mti",  # Maiwa (Papua New Guinea)
        "wax",  # Watam
        "apm",  # Mescalero-Chiricahua Apache
        "uss",  # us-Saare
        "ttm",  # Northern Tutchone
        "opa",  # Okpamheri
        "mxz",  # Central Masela
        "ckc",  # Northern Cakchiquel
        "kiy",  # Kirikiri
        "rsb",  # Romano-Serbian
        "bfi",  # British Sign Language
        "jyy",  # Jaya
        "ltn",  # Latundê
        "gom",  # Goan Konkani
        "tvd",  # Tsuvadi
        "jka",  # Kaera
        "kep",  # Kaikadi
        "mfp",  # Makassar Malay
        "pcl",  # Pardhi
        "yka",  # Yakan
        "ins",  # Indian Sign Language
        "csw",  # Swampy Cree
        "ica",  # Ede Ica
        "shc",  # Sonde
        "mlf",  # Mal
        "bvo",  # Bolgo
        "lea",  # Lega-Shabunda
        "khl",  # Lusi
        "gii",  # Girirra
        "lso",  # Laos Sign Language
        "kbq",  # Kamano
        "ubu",  # Umbu-Ungu
        "yel",  # Yela
        "aea",  # Areba
        "cgk",  # Chocangacakha
        "psg",  # Penang Sign Language
        "def",  # Dezfuli
        "avk",  # Kotava
        "xoi",  # Kominimung
        "czh",  # Huizhou Chinese
        "aiq",  # Aimaq
        "mek",  # Mekeo
        "ssw",  # Swati
        "sjo",  # Xibe
        "asc",  # Casuarina Coast Asmat
        "nmu",  # Northeast Maidu
        "yxg",  # Yagara
        "atd",  # Ata Manobo
        "sww",  # Sowa
        "eja",  # Ejamat
        "cdr",  # Cinda-Regi-Tiyal
        "sbl",  # Botolan Sambal
        "qvm",  # Margos-Yarowilca-Lauricocha Quechua
        "gjk",  # Kachi Koli
        "jbn",  # Nafusi
        "pmf",  # Pamona
        "nlv",  # Orizaba Nahuatl
        "kkm",  # Kiong
        "xwt",  # Wotjobaluk
        "gka",  # Guya
        "lag",  # Rangi
        "wrm",  # Warumungu
        "jur",  # Jurúna
        "kpq",  # Korupun-Sela
        "gcn",  # Gaina
        "pob",  # Western Pokomchí
        "nxm",  # Numidian
        "zmw",  # Mbo (Democratic Republic of Congo)
        "mor",  # Moro
        "psq",  # Pasi
        "ptv",  # Port Vato
        "prs",  # Dari
        "zpz",  # Texmelucan Zapotec
        "spt",  # Spiti Bhoti
        "gge",  # Gurr-goni
        "nmh",  # Monsang Naga
        "kuq",  # Karipuna
        "gya",  # Northwest Gbaya
        "nii",  # Nii
        "gne",  # Ganang
        "clm",  # Clallam
        "dna",  # Upper Grand Valley Dani
        "lef",  # Lelemi
        "yii",  # Yidiny
        "cxh",  # Cha'ari
        "grz",  # Guramalum
        "yds",  # Yiddish Sign Language
        "bns",  # Bundeli
        "sjt",  # Ter Sami
        "ybm",  # Yaben
        "vau",  # Vanuma
        "bhv",  # Bahau
        "itd",  # Southern Tidung
        "ihb",  # Iha Based Pidgin
        "kwz",  # Kwadi
        "bil",  # Bile
        "lee",  # Lyélé
        "gna",  # Kaansa
        "kgr",  # Abun
        "xhv",  # Khua
        "tqu",  # Touo
        "xlo",  # Loup A
        "chg",  # Chagatai
        "bpa",  # Daakaka
        "weo",  # Wemale
        "bzs",  # Brazilian Sign Language
        "kno",  # Kono (Sierra Leone)
        "bxf",  # Bilur
        "coe",  # Koreguaje
        "vay",  # Wayu
        "aya",  # Awar
        "rea",  # Rerau
        "bjf",  # Barzani Jewish Neo-Aramaic
        "mhz",  # Mor (Mor Islands)
        "mve",  # Marwari (Pakistan)
        "mju",  # Manna-Dora
        "kjh",  # Khakas
        "raw",  # Rawang
        "kyq",  # Kenga
        "gbk",  # Gaddi
        "mum",  # Maiwala
        "pyu",  # Puyuma
        "ntm",  # Nateni
        "brs",  # Baras
        "aym",  # Aymara
        "kdk",  # Numèè
        "mru",  # Mono (Cameroon)
        "omy",  # Old Malay
        "wri",  # Wariyangga
        "stj",  # Matya Samo
        "xbo",  # Bolgarian
        "sie",  # Simaa
        "rie",  # Rien
        "xpi",  # Pictish
        "noz",  # Nayi
        "tvs",  # Taveta
        "bsi",  # Bassossi
        "nrt",  # Northern Kalapuya
        "mbb",  # Western Bukidnon Manobo
        "okj",  # Oko-Juwoi
        "als",  # Tosk Albanian
        "khd",  # Bädi Kanum
        "pso",  # Polish Sign Language
        "nsu",  # Sierra Negra Nahuatl
        "dbl",  # Dyirbal
        "mnn",  # Southern Mnong
        "bzz",  # Evant
        "rys",  # Yaeyama
        "gar",  # Galeya
        "kad",  # Adara
        "dyy",  # Djabugay
        "kyu",  # Western Kayah
        "nvo",  # Nyokon
        "gji",  # Geji
        "kiz",  # Kisi
        "snf",  # Noon
        "pnv",  # Pinigura
        "olm",  # Oloma
        "sml",  # Central Sama
        "vmx",  # Tamazola Mixtec
        "bre",  # Breton
        "ajg",  # Aja (Benin)
        "pii",  # Pini
        "qun",  # Quinault
        "amp",  # Alamblak
        "srb",  # Sora
        "krz",  # Sota Kanum
        "spo",  # Spokane
        "bqs",  # Bosngun
        "teq",  # Temein
        "aoz",  # Uab Meto
        "bsh",  # Kati
        "opy",  # Ofayé
        "zxx",  # No linguistic content
        "fau",  # Fayu
        "cga",  # Changriwa
        "hei",  # Heiltsuk
        "hut",  # Humla
        "tin",  # Tindi
        "dul",  # Alabat Island Agta
        "yso",  # Nisi (China)
        "ijn",  # Kalabari
        "nfd",  # Ahwai
        "bjv",  # Bedjond
        "qvl",  # Cajatambo North Lima Quechua
        "pwg",  # Gapapaiwa
        "gbn",  # Mo'da
        "ggl",  # Ganglau
        "trz",  # Torá
        "xmn",  # Manichaean Middle Persian
        "chq",  # Quiotepec Chinantec
        "plk",  # Kohistani Shina
        "qud",  # Calderón Highland Quichua
        "yaq",  # Yaqui
        "ifu",  # Mayoyao Ifugao
        "boo",  # Tiemacèwè Bozo
        "wum",  # Wumbvu
        "cts",  # Northern Catanduanes Bikol
        "aot",  # Atong (India)
        "gow",  # Gorowa
        "jax",  # Jambi Malay
        "unr",  # Mundari
        "shi",  # Tachelhit
        "akk",  # Akkadian
        "bun",  # Sherbro
        "pmn",  # Pam
        "bmu",  # Somba-Siawari
        "pbg",  # Paraujano
        "kop",  # Waube
        "mhv",  # Arakanese
        "dtr",  # Lotud
        "crj",  # Southern East Cree
        "gnd",  # Zulgo-Gemzek
        "gbd",  # Karajarri
        "lun",  # Lunda
        "tbi",  # Gaam
        "ima",  # Mala Malasar
        "suk",  # Sukuma
        "yix",  # Axi Yi
        "ccy",  # Southern Zhuang
        "tet",  # Tetum
        "kpe",  # Kpelle
        "lrt",  # Larantuka Malay
        "gra",  # Rajput Garasia
        "bmr",  # Muinane
        "tkf",  # Tukumanféd
        "xps",  # Pisidian
        "pay",  # Pech
        "lli",  # Teke-Laali
        "bze",  # Jenaama Bozo
        "msv",  # Maslam
        "ahn",  # Àhàn
        "kip",  # Sheshi Kham
        "mdn",  # Mbati
        "pmb",  # Pambia
        "gmr",  # Mirning
        "ndb",  # Kenswei Nsei
        "mnm",  # Mapena
        "bks",  # Northern Sorsoganon
        "sbe",  # Saliba
        "dud",  # Hun-Saare
        "mvu",  # Marfa
        "ttn",  # Towei
        "dbr",  # Dabarre
        "ood",  # Tohono O'odham
        "zua",  # Zeem
        "fie",  # Fyer
        "sgh",  # Shughni
        "kck",  # Kalanga
        "tgx",  # Tagish
        "cbi",  # Chachi
        "msb",  # Masbatenyo
        "mqf",  # Momuna
        "kur",  # Kurdish
        "kle",  # Kulung (Nepal)
        "nca",  # Iyo
        "aix",  # Aighon
        "puk",  # Pu Ko
        "lba",  # Lui
        "lgh",  # Laghuu
        "khu",  # Nkhumbi
        "mmp",  # Siawi
        "kmw",  # Komo (Democratic Republic of Congo)
        "lap",  # Laka (Chad)
        "tur",  # Turkish
        "bga",  # Gwamhi-Wuri
        "tge",  # Eastern Gorkha Tamang
        "mhb",  # Mahongwe
        "tir",  # Tigrinya
        "vjk",  # Bajjika
        "ega",  # Ega
        "dad",  # Marik
        "dtb",  # Labuk-Kinabatangan Kadazan
        "rth",  # Ratahan
        "tsp",  # Northern Toussian
        "lce",  # Loncong
        "gwm",  # Awngthim
        "kmc",  # Southern Dong
        "nzi",  # Nzima
        "noc",  # Nuk
        "tve",  # Te'un
        "crr",  # Carolina Algonquian
        "veo",  # Ventureño
        "akj",  # Aka-Jeru
        "ldj",  # Lemoro
        "pmi",  # Northern Pumi
        "hus",  # Huastec
        "men",  # Mende (Sierra Leone)
        "wmn",  # Waamwang
        "gie",  # Gaɓogbo
        "smr",  # Simeulue
        "usk",  # Usaghade
        "amr",  # Amarakaeri
        "xzp",  # Ancient Zapotec
        "thl",  # Dangaura Tharu
        "hwc",  # Hawai'i Creole English
        "mye",  # Myene
        "bfc",  # Panyi Bai
        "nuc",  # Nukuini
        "srh",  # Sarikoli
        "shk",  # Shilluk
        "sss",  # Sô
        "ntd",  # Northern Tidung
        "nbf",  # Naxi
        "lid",  # Nyindrou
        "jac",  # Popti'
        "juw",  # Wãpha
        "ame",  # Yanesha'
        "ikk",  # Ika
        "ljp",  # Lampung Api
        "lbw",  # Tolaki
        "gwc",  # Gawri
        "azz",  # Highland Puebla Nahuatl
        "ruf",  # Luguru
        "ast",  # Asturian
        "aor",  # Aore
        "cum",  # Cumeral
        "gtu",  # Aghu-Tharnggala
        "dbg",  # Dogul Dom Dogon
        "sdj",  # Suundi
        "xis",  # Kisan
        "mbe",  # Molale
        "mel",  # Central Melanau
        "afr",  # Afrikaans
        "pms",  # Piemontese
        "sxs",  # Sasaru
        "lcf",  # Lubu
        "myc",  # Mayeka
        "vec",  # Venetian
        "snm",  # Southern Ma'di
        "wog",  # Wogamusin
        "tcd",  # Tafi
        "epo",  # Esperanto
        "tye",  # Kyanga
        "prw",  # Parawen
        "bdu",  # Oroko
        "pwb",  # Panawa
        "xau",  # Kauwera
        "mdd",  # Mbum
        "gbq",  # Gbaya-Bozoum
        "mzo",  # Matipuhy
        "dtn",  # Daatsʼíin
        "kmr",  # Northern Kurdish
        "sms",  # Skolt Sami
        "dau",  # Dar Sila Daju
        "hmj",  # Ge
        "nzz",  # Nanga Dama Dogon
        "sys",  # Sinyar
        "alr",  # Alutor
        "hre",  # Hre
        "war",  # Waray (Philippines)
        "mku",  # Konyanka Maninka
        "hea",  # Northern Qiandong Miao
        "mfk",  # North Mofu
        "dty",  # Dotyali
        "dny",  # Dení
        "ssn",  # Waata
        "flh",  # Foau
        "pit",  # Pitta Pitta
        "ynl",  # Yangulam
        "ukw",  # Ukwuani-Aboh-Ndoni
        "pkb",  # Pokomo
        "mui",  # Musi
        "ito",  # Itonama
        "zqe",  # Qiubei Zhuang
        "kfh",  # Kurichiya
        "yuq",  # Yuqui
        "tnv",  # Tangchangya
        "lya",  # Layakha
        "xrd",  # Gundungurra
        "bio",  # Nai
        "yox",  # Yoron
        "aeb",  # Tunisian Arabic
        "nmz",  # Nawdm
        "cte",  # Tepinapa Chinantec
        "nkk",  # Nokuku
        "msh",  # Masikoro Malagasy
        "lmj",  # West Lembata
        "tsv",  # Tsogo
        "muz",  # Mursi
        "kje",  # Kisar
        "ecy",  # Eteocypriot
        "kwx",  # Khirwar
        "kbd",  # Kabardian
        "agf",  # Arguni
        "goq",  # Gorap
        "bjm",  # Bajelani
        "xpg",  # Phrygian
        "bvw",  # Boga
        "dwu",  # Dhuwal
        "fos",  # Siraya
        "muc",  # Ajumbu
        "mup",  # Malvi
        "adx",  # Amdo Tibetan
        "bys",  # Burak
        "bcv",  # Shoo-Minda-Nye
        "dep",  # Pidgin Delaware
        "ctg",  # Chittagonian
        "otd",  # Ot Danum
        "eth",  # Ethiopian Sign Language
        "xtr",  # Early Tripuri
        "tku",  # Upper Necaxa Totonac
        "bli",  # Bolia
        "pck",  # Paite Chin
        "wpc",  # Maco
        "gnc",  # Guanche
        "avt",  # Au
        "arn",  # Mapudungun
        "zbl",  # Blissymbols
        "bpe",  # Bauni
        "hnm",  # Hainanese
        "ono",  # Onondaga
        "asz",  # As
        "kyj",  # Karao
        "ahk",  # Akha
        "cnp",  # Northern Ping Chinese
        "mlx",  # Malfaxal
        "lnh",  # Lanoh
        "btr",  # Baetora
        "ebo",  # Teke-Ebo
        "cuu",  # Tai Ya
        "jpn",  # Japanese
        "qup",  # Southern Pastaza Quechua
        "mjj",  # Mawak
        "prx",  # Purik
        "rmn",  # Balkan Romani
        "css",  # Southern Ohlone
        "oar",  # Old Aramaic (up to 700 BCE)
        "its",  # Isekiri
        "zpl",  # Lachixío Zapotec
        "jar",  # Jarawa (Nigeria)
        "inb",  # Inga
        "lbi",  # La'bi
        "apv",  # Alapmunte
        "mtq",  # Muong
        "suo",  # Bouni
        "xqa",  # Karakhanid
        "elm",  # Eleme
        "wni",  # Ndzwani Comorian
        "prt",  # Phai
        "sth",  # Shelta
        "xkc",  # Kho'ini
        "rsl",  # Russian Sign Language
        "kxw",  # Konai
        "ckl",  # Cibak
        "fan",  # Fang (Equatorial Guinea)
        "nuk",  # Nuu-chah-nulth
        "bmd",  # Baga Manduri
        "bkl",  # Berik
        "wob",  # Wè Northern
        "ulu",  # Uma' Lung
        "kwy",  # San Salvador Kongo
        "bey",  # Beli (Papua New Guinea)
        "byh",  # Bhujel
        "nhh",  # Nahari
        "mqt",  # Mok
        "khp",  # Kapori
        "skc",  # Ma Manda
        "tdo",  # Teme
        "bpl",  # Broome Pearling Lugger Pidgin
        "pux",  # Puare
        "tuu",  # Tututni
        "skt",  # Sakata
        "nsz",  # Nisenan
        "zmv",  # Mbariman-Gudhinma
        "kho",  # Khotanese
        "waz",  # Wampur
        "cji",  # Chamalal
        "bid",  # Bidiyo
        "dwk",  # Dawik Kui
        "kct",  # Kaian
        "kji",  # Zabana
        "beo",  # Beami
        "for",  # Fore
        "tto",  # Lower Ta'oih
        "ymg",  # Yamongeri
        "crb",  # Island Carib
        "hra",  # Hrangkhol
        "sbx",  # Seberuang
        "zea",  # Zeeuws
        "mmw",  # Emae
        "nti",  # Natioro
        "bus",  # Bokobaru
        "gex",  # Garre
        "lrz",  # Lemerig
        "mwx",  # Mediak
        "ykh",  # Khamnigan Mongol
        "aoj",  # Mufian
        "grr",  # Taznatit
        "kbe",  # Kanju
        "apz",  # Safeyoka
        "bzm",  # Bolondo
        "jil",  # Jilim
        "kmj",  # Kumarbhag Paharia
        "xpj",  # Mpalitjanh
        "smk",  # Bolinao
        "zma",  # Manda (Australia)
        "xmv",  # Antankarana Malagasy
        "gbi",  # Galela
        "hia",  # Lamang
        "sgg",  # Swiss-German Sign Language
        "mfo",  # Mbe
        "wih",  # Wik-Me'anha
        "mcz",  # Mawan
        "xng",  # Middle Mongolian
        "jng",  # Yangman
        "mpf",  # Tajumulco Mam
        "lay",  # Lama Bai
        "onn",  # Onobasulu
        "byr",  # Baruya
        "soj",  # Soi
        "ntz",  # Natanzi
        "giw",  # White Gelao
        "bsr",  # Bassa-Kontagora
        "tjs",  # Southern Tujia
        "bnb",  # Bookan
        "jas",  # New Caledonian Javanese
        "yaa",  # Yaminahua
        "hbu",  # Habu
        "srg",  # Sulod
        "dtm",  # Tomo Kan Dogon
        "akv",  # Akhvakh
        "bjp",  # Fanamaket
        "knf",  # Mankanya
        "bnd",  # Banda (Indonesia)
        "ddw",  # Dawera-Daweloor
        "rim",  # Nyaturu
        "mag",  # Magahi
        "gqn",  # Guana (Brazil)
        "cra",  # Chara
        "pre",  # Principense
        "dyg",  # Villa Viciosa Agta
        "mkn",  # Kupang Malay
        "kdz",  # Kwaja
        "kvd",  # Kui (Indonesia)
        "cbt",  # Chayahuita
        "spr",  # Saparua
        "kwn",  # Kwangali
        "aaa",  # Ghotuo
        "jus",  # Jumla Sign Language
        "mja",  # Mahei
        "grm",  # Kota Marudu Talantang
        "tmo",  # Temoq
        "xpf",  # Southeast Tasmanian
        "prb",  # Lua'
        "sre",  # Sara
        "csy",  # Siyin Chin
        "xlb",  # Loup B
        "lod",  # Berawan
        "grs",  # Gresi
        "ivb",  # Ibatan
        "bua",  # Buriat
        "ufi",  # Ufim
        "wng",  # Wanggom
        "yej",  # Yevanic
        "mhj",  # Mogholi
        "zuh",  # Tokano
        "bkn",  # Bukitan
        "awx",  # Awara
        "asy",  # Yaosakor Asmat
        "zba",  # Balaibalan
        "dhd",  # Dhundari
        "trn",  # Trinitario
        "lth",  # Thur
        "ibm",  # Agoi
        "hbo",  # Ancient Hebrew
        "tmp",  # Tai Mène
        "buv",  # Bun
        "ckh",  # Chak
        "jun",  # Juang
        "ngn",  # Ngwo
        "ktf",  # Kwami
        "faa",  # Fasu
        "bhe",  # Bhaya
        "gyn",  # Guyanese Creole English
        "lgq",  # Logba
        "xld",  # Lydian
        "tud",  # Tuxá
        "ctl",  # Tlacoatzintepec Chinantec
        "cwe",  # Kwere
        "dba",  # Bangime
        "hvv",  # Santa María Del Mar Huave
        "zai",  # Isthmus Zapotec
        "bml",  # Bomboli
        "lgg",  # Lugbara
        "kkw",  # Teke-Kukuya
        "wsu",  # Wasu
        "pln",  # Palenquero
        "cdg",  # Chamari
        "dde",  # Doondo
        "bno",  # Bantoanon
        "sej",  # Sene
        "boq",  # Bogaya
        "duh",  # Dungra Bhil
        "kwv",  # Sara Kaba Náà
        "kxk",  # Zayein Karen
        "rof",  # Rombo
        "cmt",  # Camtho
        "bwb",  # Namosi-Naitasiri-Serua
        "hag",  # Hanga
        "deh",  # Dehwari
        "mbm",  # Ombamba
        "jsl",  # Japanese Sign Language
        "nqq",  # Kyan-Karyaw Naga
        "tbg",  # North Tairora
        "zaf",  # Ayoquesco Zapotec
        "djd",  # Djamindjung
        "kvq",  # Geba Karen
        "nyt",  # Nyawaygi
        "cyb",  # Cayubaba
        "tpq",  # Tukpa
        "mpa",  # Mpoto
        "oog",  # Ong
        "jiu",  # Youle Jinuo
        "nno",  # Norwegian Nynorsk
        "kqr",  # Kimaragang
        "tsb",  # Tsamai
        "ten",  # Tama (Colombia)
        "zag",  # Zaghawa
        "dar",  # Dargwa
        "tiq",  # Tiéfo
        "thp",  # Thompson
        "kjz",  # Bumthangkha
        "pwr",  # Powari
        "sbf",  # Chabu
        "klf",  # Kendeje
        "wha",  # Sou Upaa
        "hor",  # Horo
        "ghc",  # Hiberno-Scottish Gaelic
        "hum",  # Hungana
        "ahh",  # Aghu
        "fut",  # Futuna-Aniwa
        "rsw",  # Rishiwa
        "wnp",  # Wanap
        "gyd",  # Kayardild
        "kln",  # Kalenjin
        "xwl",  # Western Xwla Gbe
        "uki",  # Kui (India)
        "llk",  # Lelak
        "axx",  # Xârâgurè
        "mzs",  # Macanese
        "end",  # Ende
        "xad",  # Adai
        "kuu",  # Upper Kuskokwim
        "kzr",  # Karang
        "crd",  # Coeur d'Alene
        "chc",  # Catawba
        "hve",  # San Dionisio Del Mar Huave
        "bfz",  # Mahasu Pahari
        "gxx",  # Wè Southern
        "nue",  # Ngundu
        "wmt",  # Walmajarri
        "mws",  # Mwimbi-Muthambi
        "gqa",  # Ga'anda
        "xpa",  # Pirriya
        "dyu",  # Dyula
        "ktc",  # Kholok
        "trd",  # Turi
        "anc",  # Ngas
        "ktj",  # Plapo Krumen
        "lmw",  # Lake Miwok
        "tkr",  # Tsakhur
        "tsg",  # Tausug
        "wny",  # Wanyi
        "mgd",  # Moru
        "dkk",  # Dakka
        "mam",  # Mam
        "flm",  # Falam Chin
        "are",  # Western Arrarnta
        "bme",  # Limassa
        "nbv",  # Ngamambo
        "ige",  # Igede
        "lae",  # Pattani
        "nee",  # Nêlêmwa-Nixumwak
        "som",  # Somali
        "gis",  # North Giziga
        "ipk",  # Inupiaq
        "hkn",  # Mel-Khaonh
        "rak",  # Tulu-Bohuai
        "sey",  # Secoya
        "akw",  # Akwa
        "btx",  # Batak Karo
        "mtb",  # Anyin Morofo
        "mmq",  # Musak
        "cuk",  # San Blas Kuna
        "ape",  # Bukiyip
        "nlq",  # Lao Naga
        "kee",  # Eastern Keres
        "zlj",  # Liujiang Zhuang
        "mmk",  # Mukha-Dora
        "ore",  # Orejón
        "guu",  # Yanomamö
        "acq",  # Ta'izzi-Adeni Arabic
        "pga",  # Sudanese Creole Arabic
        "lop",  # Lopa
        "urm",  # Urapmin
        "yot",  # Yotti
        "mmf",  # Mundat
        "gdf",  # Guduf-Gava
        "lwh",  # White Lachi
        "ote",  # Mezquital Otomi
        "nhn",  # Central Nahuatl
        "hay",  # Haya
        "low",  # Tampias Lobu
        "gdq",  # Mehri
        "gio",  # Gelao
        "mee",  # Mengen
        "nkh",  # Khezha Naga
        "myx",  # Masaaba
        "poh",  # Poqomchi'
        "ssk",  # Sunam
        "mlb",  # Mbule
        "okk",  # Kwamtim One
        "rui",  # Rufiji
        "ids",  # Idesa
        "lis",  # Lisu
        "ugn",  # Ugandan Sign Language
        "aes",  # Alsea
        "kdr",  # Karaim
        "svm",  # Slavomolisano
        "coq",  # Coquille
        "pcj",  # Parenga
        "udl",  # Wuzlam
        "acc",  # Cubulco Achí
        "bjl",  # Bulu (Papua New Guinea)
        "pei",  # Chichimeca-Jonaz
        "kix",  # Khiamniungan Naga
        "aew",  # Ambakich
        "ayt",  # Magbukun Ayta
        "dmk",  # Domaaki
        "len",  # Lenca
        "nch",  # Central Huasteca Nahuatl
        "cjo",  # Ashéninka Pajonal
        "fmp",  # Fe'fe'
        "tnw",  # Tonsawang
        "mpi",  # Mpade
        "ndf",  # Nadruvian
        "ndr",  # Ndoola
        "skk",  # Sok
        "huy",  # Hulaulá
        "irn",  # Irántxe
        "bdx",  # Budong-Budong
        "trc",  # Copala Triqui
        "bak",  # Bashkir
        "mhu",  # Digaro-Mishmi
        "ktp",  # Kaduo
        "nqo",  # N'Ko
        "mxi",  # Mozarabic
        "mwf",  # Murrinh-Patha
        "azt",  # Faire Atta
        "gig",  # Goaria
        "bgo",  # Baga Koga
        "vki",  # Ija-Zuba
        "etb",  # Etebi
        "nhm",  # Morelos Nahuatl
        "sgy",  # Sanglechi
        "ecs",  # Ecuadorian Sign Language
        "ggn",  # Eastern Gurung
        "lcc",  # Legenyem
        "rue",  # Rusyn
        "byp",  # Bumaji
        "cnu",  # Chenoua
        "wir",  # Wiraféd
        "hue",  # San Francisco Del Mar Huave
        "gva",  # Guana (Paraguay)
        "pko",  # Pökoot
        "ocm",  # Old Cham
        "kjr",  # Kurudu
        "sib",  # Sebop
        "tgj",  # Tagin
        "kyx",  # Rapoisi
        "kwk",  # Kwakiutl
        "mqr",  # Mander
        "agr",  # Aguaruna
        "uli",  # Ulithian
        "mrd",  # Western Magar
        "bmm",  # Northern Betsimisaraka Malagasy
        "xya",  # Yaygir
        "ttz",  # Tsum
        "dux",  # Duungooma
        "wad",  # Wamesa
        "emp",  # Northern Emberá
        "sgu",  # Salas
        "xss",  # Assan
        "svs",  # Savosavo
        "bnz",  # Beezen
        "xgu",  # Unggumi
        "ars",  # Najdi Arabic
        "diz",  # Ding
        "hdy",  # Hadiyya
        "vsn",  # Vedic Sanskrit
        "wbp",  # Warlpiri
        "yon",  # Yongkom
        "loq",  # Lobala
        "pqm",  # Malecite-Passamaquoddy
        "koo",  # Konzo
        "aok",  # Arhö
        "hau",  # Hausa
        "wlu",  # Wuliwuli
        "gai",  # Borei
        "cko",  # Anufo
        "puc",  # Punan Merap
        "baz",  # Tunen
        "boc",  # Bakung Kenyah
        "kay",  # Kamayurá
        "tox",  # Tobian
        "afu",  # Awutu
        "hah",  # Hahon
        "kxe",  # Kakihum
        "kfg",  # Kudiya
        "okc",  # Kobo
        "blz",  # Balantak
        "zkr",  # Zakhring
        "bod",  # Tibetan
        "akr",  # Araki
        "xel",  # Kelo
        "daw",  # Davawenyo
        "thi",  # Tai Long
        "jbw",  # Yawijibaya
        "cuw",  # Chukwa
        "gic",  # Gail
        "meq",  # Merey
        "ojs",  # Severn Ojibwa
        "bcr",  # Babine
        "lnl",  # South Central Banda
        "mph",  # Maung
        "shm",  # Shahrudi
        "csi",  # Coast Miwok
        "xao",  # Khao
        "ire",  # Iresim
        "mox",  # Molima
        "ldn",  # Láadan
        "tdn",  # Tondano
        "sei",  # Seri
        "mks",  # Silacayoapan Mixtec
        "ded",  # Dedua
        "roc",  # Cacgia Roglai
        "mtn",  # Matagalpa
        "arc",  # Official Aramaic (700-300 BCE)
        "kxa",  # Kairiru
        "khb",  # Lü
        "kxj",  # Kulfa
        "tlc",  # Yecuatla Totonac
        "ext",  # Extremaduran
        "vmh",  # Maraghei
        "xpx",  # Southwestern Tasmanian
        "mbk",  # Malol
        "bqu",  # Boguru
        "xcn",  # Cotoname
        "zgr",  # Magori
        "xnb",  # Kanakanabu
        "jeu",  # Jonkor Bourmataguil
        "pho",  # Phunoi
        "wol",  # Wolof
        "xln",  # Alanic
        "bzq",  # Buli (Indonesia)
        "isk",  # Ishkashimi
        "tgt",  # Central Tagbanwa
        "jrr",  # Jiru
        "ble",  # Balanta-Kentohe
        "gmb",  # Gula'alaa
        "guw",  # Gun
        "mot",  # Barí
        "szk",  # Sizaki
        "yaz",  # Lokaa
        "tww",  # Tuwari
        "rpn",  # Repanbitip
        "amx",  # Anmatyerre
        "soe",  # Songomeno
        "tbk",  # Calamian Tagbanwa
        "job",  # Joba
        "dho",  # Dhodia
        "mlz",  # Malaynon
        "ukl",  # Ukrainian Sign Language
        "tac",  # Lowland Tarahumara
        "zbt",  # Batui
        "lbt",  # Lachi
        "pbt",  # Southern Pashto
        "prc",  # Parachi
        "wor",  # Woria
        "krs",  # Gbaya (Sudan)
        "bjb",  # Banggarla
        "hmw",  # Western Mashan Hmong
        "tdj",  # Tajio
        "gri",  # Ghari
        "gbv",  # Gbanu
        "mmh",  # Mehináku
        "see",  # Seneca
        "tfi",  # Tofin Gbe
        "cld",  # Chaldean Neo-Aramaic
        "uha",  # Uhami
        "mhr",  # Eastern Mari
        "zpx",  # San Baltazar Loxicha Zapotec
        "bwx",  # Bu-Nao Bunu
        "kcx",  # Kachama-Ganjule
        "pbz",  # Palu
        "cjk",  # Chokwe
        "hsf",  # Southeastern Huastec
        "tpp",  # Pisaflores Tepehua
        "tmi",  # Tutuba
        "pfa",  # Pááfang
        "jim",  # Jimi (Cameroon)
        "yut",  # Yopno
        "imi",  # Anamgura
        "ntx",  # Tangkhul Naga (Myanmar)
        "ypo",  # Alo Phola
        "hnu",  # Hung
        "nkv",  # Nyika (Malawi and Zambia)
        "xpq",  # Mohegan-Pequot
        "lna",  # Langbashe
        "vlr",  # Vatrata
        "too",  # Xicotepec De Juárez Totonac
        "gey",  # Enya
        "dnn",  # Dzùùngoo
        "cjr",  # Chorotega
        "nmv",  # Ngamini
        "czt",  # Zotung Chin
        "kax",  # Kao
        "koh",  # Koyo
        "ksy",  # Kharia Thar
        "cku",  # Koasati
        "fai",  # Faiwol
        "crt",  # Iyojwa'ja Chorote
        "wxa",  # Waxianghua
        "nsm",  # Sumi Naga
        "tjw",  # Djabwurrung
        "nyg",  # Nyindu
        "tqp",  # Tomoip
        "xkg",  # Kagoro
        "xrm",  # Armazic
        "krp",  # Durop
        "gce",  # Galice
        "pdi",  # Pa Di
        "tss",  # Taiwan Sign Language
        "xmj",  # Majera
        "bag",  # Tuki
        "aer",  # Eastern Arrernte
        "bvh",  # Bure
        "pur",  # Puruborá
        "slq",  # Salchuq
        "lon",  # Malawi Lomwe
        "xbi",  # Kombio
        "dok",  # Dondo
        "xgr",  # Garza
        "isc",  # Isconahua
        "bcm",  # Bannoni
        "myz",  # Classical Mandaic
        "bnn",  # Bunun
        "mkc",  # Siliput
        "hrc",  # Niwer Mil
        "kfi",  # Kannada Kurumba
        "cse",  # Czech Sign Language
        "xty",  # Yoloxochitl Mixtec
        "ywm",  # Wumeng Yi
        "nsw",  # Navut
        "plz",  # Paluan
        "emo",  # Emok
        "twt",  # Turiwára
        "mza",  # Santa María Zacatepec Mixtec
        "kmh",  # Kalam
        "msn",  # Vurës
        "dit",  # Dirari
        "alf",  # Alege
        "umn",  # Makyan Naga
        "cvn",  # Valle Nacional Chinantec
        "luy",  # Luyia
        "kmp",  # Gimme
        "naz",  # Coatepec Nahuatl
        "zty",  # Yatee Zapotec
        "mpd",  # Machinere
        "taa",  # Lower Tanana
        "xrr",  # Raetic
        "spe",  # Sepa (Papua New Guinea)
        "soo",  # Songo
        "mcm",  # Malaccan Creole Portuguese
        "oss",  # Ossetian
        "bqh",  # Baima
        "mtm",  # Mator
        "wij",  # Wik-Iiyanh
        "krv",  # Kavet
        "xgd",  # Gudang
        "tcy",  # Tulu
        "trg",  # Lishán Didán
        "faz",  # Northwestern Fars
        "wym",  # Wymysorys
        "xny",  # Nyiyaparli
        "mjp",  # Malapandaram
        "mon",  # Mongolian
        "vrt",  # Burmbar
        "gim",  # Gimi (Eastern Highlands)
        "txq",  # Tii
        "gub",  # Guajajára
        "eee",  # E
        "rnn",  # Roon
        "nya",  # Nyanja
        "arq",  # Algerian Arabic
        "zim",  # Mesme
        "mni",  # Manipuri
        "yms",  # Mysian
        "omb",  # East Ambae
        "bmo",  # Bambalang
        "amy",  # Ami
        "dic",  # Lakota Dida
        "kfq",  # Korku
        "pav",  # Pakaásnovos
        "doq",  # Dominican Sign Language
        "egy",  # Egyptian (Ancient)
        "bbq",  # Bamali
        "bdh",  # Baka (South Sudan)
        "bea",  # Beaver
        "ruh",  # Ruga
        "wie",  # Wik-Epa
        "skb",  # Saek
        "ahe",  # Ahe
        "ncn",  # Nauna
        "sbw",  # Simba
        "pig",  # Pisabo
        "yre",  # Yaouré
        "yym",  # Yuanjiang-Mojiang Yi
        "dhw",  # Dhanwar (Nepal)
        "pht",  # Phu Thai
        "uam",  # Uamué
        "wnm",  # Wanggamala
        "diy",  # Diuwe
        "enh",  # Tundra Enets
        "ymx",  # Northern Muji
        "mxx",  # Mahou
        "gmd",  # Mághdì
        "bsd",  # Sarawak Bisaya
        "tuo",  # Tucano
        "mhe",  # Besisi
        "cro",  # Crow
        "yor",  # Yoruba
        "hed",  # Herdé
        "fcs",  # Quebec Sign Language
        "nde",  # North Ndebele
        "kds",  # Lahu Shi
        "nto",  # Ntomba
        "chh",  # Chinook
        "vky",  # Kayu Agung
        "toh",  # Gitonga
        "dzd",  # Daza
        "bzv",  # Naami
        "ojb",  # Northwestern Ojibwa
        "klx",  # Koluwawa
        "gaj",  # Gadsup
        "gmv",  # Gamo
        "yoy",  # Yoy
        "enn",  # Engenni
        "tsn",  # Tswana
        "xkn",  # Kayan River Kayan
        "waq",  # Wagiman
        "gdn",  # Umanakaina
        "hye",  # Armenian
        "sfs",  # South African Sign Language
        "ver",  # Mom Jango
        "otx",  # Texcatepec Otomi
        "yid",  # Yiddish
        "pex",  # Petats
        "qug",  # Chimborazo Highland Quichua
        "kwj",  # Kwanga
        "tem",  # Timne
        "zng",  # Mang
        "xgf",  # Gabrielino-Fernandeño
        "ssy",  # Saho
        "ogb",  # Ogbia
        "ayz",  # Mai Brat
        "smq",  # Samo
        "mbp",  # Malayo
        "snr",  # Sihan
        "ygw",  # Yagwoia
        "szy",  # Sakizaya
        "res",  # Reshe
        "tpe",  # Tippera
        "anx",  # Andra-Hus
        "bkd",  # Binukid
        "abc",  # Ambala Ayta
        "ray",  # Rapa
        "phm",  # Phimbi
        "ayg",  # Ginyanga
        "byj",  # Bina (Nigeria)
        "cbe",  # Chipiajes
        "gma",  # Gambera
        "any",  # Anyin
        "jei",  # Yei
        "jel",  # Yelmek
        "soi",  # Sonha
        "mvw",  # Machinga
        "hoz",  # Hozo
        "ubi",  # Ubi
        "fao",  # Faroese
        "nda",  # Ndasa
        "bhq",  # Tukang Besi South
        "ter",  # Tereno
        "xwk",  # Wangkumara
        "zna",  # Zan Gula
        "ksj",  # Uare
        "jow",  # Jowulu
        "rej",  # Rejang
        "bhd",  # Bhadrawahi
        "ebr",  # Ebrié
        "kib",  # Koalib
        "kef",  # Kpessi
        "amq",  # Amahai
        "nwi",  # Southwest Tanna
        "cov",  # Cao Miao
        "eke",  # Ekit
        "loa",  # Loloda
        "zpn",  # Santa Inés Yatzechi Zapotec
        "mkl",  # Mokole
        "kdv",  # Kado
        "glk",  # Gilaki
        "twp",  # Ere
        "cpa",  # Palantla Chinantec
        "efa",  # Efai
        "wdg",  # Wadaginam
        "nny",  # Nyangga
        "ruc",  # Ruuli
        "ady",  # Adyghe
        "jjr",  # Bankal
        "uta",  # Otank
        "trf",  # Trinidadian Creole English
        "nim",  # Nilamba
        "ymc",  # Southern Muji
        "bmt",  # Biao Mon
        "smo",  # Samoan
        "zcd",  # Las Delicias Zapotec
        "zbu",  # Bu (Bauchi State)
        "lwg",  # Wanga
        "lga",  # Lungga
        "gru",  # Kistane
        "tbl",  # Tboli
        "kak",  # Kalanguya
        "did",  # Didinga
        "ttq",  # Tawallammat Tamajaq
        "yli",  # Angguruk Yali
        "zkz",  # Khazar
        "meg",  # Mea
        "kkx",  # Kohin
        "bct",  # Bendi
        "chf",  # Tabasco Chontal
        "hov",  # Hovongan
        "ksp",  # Kaba
        "itt",  # Maeng Itneg
        "tbv",  # Tobo
        "twh",  # Tai Dón
        "zem",  # Zeem
        "nml",  # Ndemli
        "aie",  # Amara
        "yhd",  # Judeo-Iraqi Arabic
        "mmd",  # Maonan
        "wdd",  # Wandji
        "dgg",  # Doga
        "fah",  # Baissa Fali
        "aek",  # Haeke
        "kfe",  # Kota (India)
        "bwl",  # Bwela
        "rgs",  # Southern Roglai
        "bgv",  # Warkay-Bipim
        "wrz",  # Waray (Australia)
        "hol",  # Holu
        "dtp",  # Kadazan Dusun
        "ese",  # Ese Ejja
        "prz",  # Providencia Sign Language
        "lmd",  # Lumun
        "cli",  # Chakali
        "ces",  # Czech
        "emu",  # Eastern Muria
        "zrg",  # Mirgan
        "mix",  # Mixtepec Mixtec
        "niv",  # Gilyak
        "xko",  # Kiorr
        "nlo",  # Ngul
        "lpn",  # Long Phuri Naga
        "abq",  # Abaza
        "bei",  # Bekati'
        "kus",  # Kusaal
        "aln",  # Gheg Albanian
        "fil",  # Filipino
        "byl",  # Bayono
        "nfl",  # Ayiwo
        "tzl",  # Talossan
        "yax",  # Yauma
        "xbw",  # Kambiwá
        "ked",  # Kerewe
        "quh",  # South Bolivian Quechua
        "jup",  # Hupdë
        "kvk",  # Korean Sign Language
        "wdy",  # Wadjabangayi
        "cth",  # Thaiphum Chin
        "vmf",  # Mainfränkisch
        "kby",  # Manga Kanuri
        "whg",  # North Wahgi
        "mnw",  # Mon
        "awg",  # Anguthimri
        "eml",  # Emiliano-Romagnolo
        "mlc",  # Cao Lan
        "apf",  # Pahanan Agta
        "sdr",  # Oraon Sadri
        "kqx",  # Mser
        "pkc",  # Paekche
        "xam",  # ǀXam
        "amz",  # Atampaya
        "aem",  # Arem
        "dev",  # Domung
        "kfv",  # Kurmukar
        "byf",  # Bete
        "ijc",  # Izon
        "rap",  # Rapanui
        "tgr",  # Tareng
        "xhe",  # Khetrani
        "bqg",  # Bago-Kusuntu
        "bwa",  # Bwatoo
        "sui",  # Suki
        "tgs",  # Nume
        "axm",  # Middle Armenian
        "mgp",  # Eastern Magar
        "dhn",  # Dhanki
        "emk",  # Eastern Maninkakan
        "kkl",  # Kosarek Yale
        "suv",  # Puroik
        "heg",  # Helong
        "neh",  # Nyenkha
        "cdz",  # Koda
        "csk",  # Jola-Kasa
        "vkt",  # Tenggarong Kutai Malay
        "yaw",  # Yawalapití
        "csf",  # Cuba Sign Language
        "thx",  # The
        "lbc",  # Lakkia
        "pru",  # Puragi
        "gax",  # Borana-Arsi-Guji Oromo
        "sch",  # Sakachep
        "vot",  # Votic
        "lmu",  # Lamenu
        "slu",  # Selaru
        "dub",  # Dubli
        "glw",  # Glavda
        "mss",  # West Masela
        "xok",  # Xokleng
        "qvz",  # Northern Pastaza Quichua
        "kaq",  # Capanahua
        "jid",  # Bu (Kaduna State)
        "sgr",  # Sangisari
        "xcg",  # Cisalpine Gaulish
        "mzu",  # Inapang
        "pme",  # Pwaamei
        "ime",  # Imeraguen
        "mvz",  # Mesqan
        "nsc",  # Nshi
        "gng",  # Ngangam
        "kuw",  # Kpagua
        "uge",  # Ughele
        "bau",  # Bada (Nigeria)
        "ygm",  # Yagomi
        "rna",  # Runa
        "che",  # Chechen
        "wmm",  # Maiwa (Indonesia)
        "zrs",  # Mairasi
        "lwt",  # Lewotobi
        "gyb",  # Garus
        "miw",  # Akoye
        "yrb",  # Yareba
        "bsc",  # Bassari
        "buf",  # Bushoong
        "mtr",  # Mewari
        "bzi",  # Bisu
        "hds",  # Honduras Sign Language
        "pzh",  # Pazeh
        "mva",  # Manam
        "ogu",  # Ogbronuagum
        "yub",  # Yugambal
        "khn",  # Khandesi
        "mdl",  # Maltese Sign Language
        "psu",  # Sauraseni Prākrit
        "xnz",  # Kenzi
        "gly",  # Gule
        "mev",  # Mano
        "tex",  # Tennet
        "scv",  # Sheni
        "vmy",  # Ayautla Mazatec
        "muq",  # Eastern Xiangxi Miao
        "wil",  # Wilawila
        "bbr",  # Girawa
        "tnf",  # Tangshewi
        "kkg",  # Mabaka Valley Kalinga
        "jau",  # Yaur
        "tgp",  # Tangoa
        "vae",  # Vale
        "xsa",  # Sabaean
        "ngc",  # Ngombe (Democratic Republic of Congo)
        "ccq",  # Chaungtha
        "djn",  # Jawoyn
        "eud",  # Eudeve
        "sxl",  # Selian
        "tmu",  # Iau
        "lrl",  # Lari
        "bku",  # Buhid
        "tdb",  # Panchpargania
        "tsf",  # Southwestern Tamang
        "tkd",  # Tukudede
        "elp",  # Elpaputih
        "sgj",  # Surgujia
        "gox",  # Gobu
        "kpc",  # Curripaco
        "tmd",  # Haruai
        "hgw",  # Haigwai
        "scr",  # Croatian
        "lgu",  # Longgu
        "dby",  # Dibiyaso
        "lep",  # Lepcha
        "ant",  # Antakarinya
        "drc",  # Minderico
        "tzn",  # Tugun
        "pww",  # Pwo Northern Karen
        "tqn",  # Tenino
        "xoc",  # O'chi'chi'
        "mff",  # Naki
        "soc",  # So (Democratic Republic of Congo)
        "awa",  # Awadhi
        "mdb",  # Morigi
        "mdh",  # Maguindanaon
        "bar",  # Bavarian
        "atl",  # Mt. Iraya Agta
        "nqm",  # Ndom
        "abx",  # Inabaknon
        "got",  # Gothic
        "atu",  # Reel
        "deq",  # Dendi (Central African Republic)
        "aim",  # Aimol
        "siv",  # Sumariup
        "alt",  # Southern Altai
        "lsh",  # Lish
        "tov",  # Upper Taromi
        "txj",  # Tarjumo
        "urb",  # Urubú-Kaapor
        "hii",  # Hinduri
        "wbi",  # Vwanji
        "cbh",  # Cagua
        "tcf",  # Malinaltepec Me'phaa
        "bmh",  # Kein
        "krh",  # Kurama
        "nua",  # Yuanga
        "peg",  # Pengo
        "dkg",  # Kadung
        "pun",  # Pubian
        "gdl",  # Dirasha
        "adf",  # Dhofari Arabic
        "neg",  # Negidal
        "bgh",  # Bogan
        "mcw",  # Mawa (Chad)
        "wrg",  # Warungu
        "qvy",  # Queyu
        "mlr",  # Vame
        "pup",  # Pulabu
        "bgr",  # Bawm Chin
        "sdd",  # Semendo
        "cbr",  # Cashibo-Cacataibo
        "ped",  # Mala (Papua New Guinea)
        "umo",  # Umotína
        "bot",  # Bongo
        "wmd",  # Mamaindé
        "xsl",  # South Slavey
        "thz",  # Tayart Tamajeq
        "kgb",  # Kawe
        "tui",  # Tupuri
        "ukh",  # Ukhwejo
        "pis",  # Pijin
        "sic",  # Malinguat
        "ysm",  # Myanmar Sign Language
        "tma",  # Tama (Chad)
        "ksu",  # Khamyang
        "orx",  # Oro
        "bpj",  # Binji
        "huv",  # San Mateo Del Mar Huave
        "emq",  # Eastern Minyag
        "kth",  # Karanga
        "shj",  # Shatt
        "bkh",  # Bakoko
        "hne",  # Chhattisgarhi
        "dgd",  # Dagaari Dioula
        "xlg",  # Ligurian (Ancient)
        "skq",  # Sininkere
        "ave",  # Avestan
        "kbb",  # Kaxuiâna
        "lms",  # Limousin
        "tie",  # Tingal
        "dtk",  # Tene Kan Dogon
        "ygi",  # Yiningayi
        "nhd",  # Chiripá
        "xta",  # Alcozauca Mixtec
        "buy",  # Bullom So
        "unk",  # Enawené-Nawé
        "rwl",  # Ruwila
        "xmk",  # Ancient Macedonian
        "bkc",  # Baka (Cameroon)
        "ogg",  # Ogbogolo
        "atc",  # Atsahuaca
        "hsb",  # Upper Sorbian
        "kws",  # Kwese
        "mdz",  # Suruí Do Pará
        "mhk",  # Mungaka
        "nwx",  # Middle Newar
        "kkq",  # Kaeku
        "haw",  # Hawaiian
        "wmh",  # Waima'a
        "xah",  # Kahayan
        "kgj",  # Gamale Kham
        "kxc",  # Konso
        "chl",  # Cahuilla
        "swe",  # Swedish
        "tdg",  # Western Tamang
        "sgz",  # Sursurunga
        "kmn",  # Awtuw
        "wem",  # Weme Gbe
        "ums",  # Pendau
        "kyg",  # Keyagana
        "bld",  # Bolango
        "osc",  # Oscan
        "bhg",  # Binandere
        "ilg",  # Garig-Ilgar
        "ask",  # Ashkun
        "xrw",  # Karawa
        "rnd",  # Ruund
        "ssg",  # Seimat
        "bzy",  # Obanliku
        "par",  # Panamint
        "xre",  # Kreye
        "xas",  # Kamas
        "mbx",  # Mari (East Sepik Province)
        "nes",  # Bhoti Kinnauri
        "ahb",  # Axamb
        "ndo",  # Ndonga
        "nbo",  # Nkukoli
        "stq",  # Saterfriesisch
        "tax",  # Tamki
        "khq",  # Koyra Chiini Songhay
        "bmz",  # Baramu
        "quf",  # Lambayeque Quechua
        "ptu",  # Bambam
        "umu",  # Munsee
        "tpg",  # Kula
        "akf",  # Akpa
        "oac",  # Oroch
        "reb",  # Rembong
        "drr",  # Dororo
        "knq",  # Kintaq
        "mjc",  # San Juan Colorado Mixtec
        "fuf",  # Pular
        "dir",  # Dirim
        "wss",  # Wasa
        "ihp",  # Iha
        "esn",  # Salvadoran Sign Language
        "mfq",  # Moba
        "loo",  # Lombo
        "lbb",  # Label
        "tad",  # Tause
        "shx",  # She
        "mnh",  # Mono (Democratic Republic of Congo)
        "kab",  # Kabyle
        "mzt",  # Mintil
        "nco",  # Sibe
        "prr",  # Puri
        "kdy",  # Keder
        "ful",  # Fulah
        "bta",  # Bata
        "zmb",  # Zimba
        "mvj",  # Todos Santos Cuchumatán Mam
        "yxl",  # Yardliyawarra
        "sfe",  # Eastern Subanen
        "kvl",  # Kayaw
        "gof",  # Gofa
        "imy",  # Milyan
        "kex",  # Kukna
        "gbp",  # Gbaya-Bossangoa
        "nld",  # Dutch
        "bcb",  # Bainouk-Samik
        "nle",  # East Nyala
        "tgw",  # Tagwana Senoufo
        "mfi",  # Wandala
        "xls",  # Lusitanian
        "njs",  # Nisa
        "pbl",  # Mak (Nigeria)
        "baj",  # Barakai
        "tbh",  # Dharawal
        "nif",  # Nek
        "prm",  # Kibiri
        "tql",  # Lehali
        "hod",  # Holma
        "kvs",  # Kunggara
        "amm",  # Ama (Papua New Guinea)
        "yga",  # Malyangapa
        "stk",  # Arammba
        "gux",  # Gourmanchéma
        "nsi",  # Nigerian Sign Language
        "lwa",  # Lwalu
        "syo",  # Suoy
        "wah",  # Watubela
        "skg",  # Sakalava Malagasy
        "tgu",  # Tanggu
        "wra",  # Warapu
        "tob",  # Toba
        "nbg",  # Nagarchal
        "lvk",  # Lavukaleve
        "ann",  # Obolo
        "xmc",  # Makhuwa-Marrevone
        "dgi",  # Northern Dagara
        "nst",  # Tase Naga
        "pys",  # Paraguayan Sign Language
        "sku",  # Sakao
        "dal",  # Dahalo
        "vsv",  # Valencian Sign Language
        "asl",  # Asilulu
        "zgb",  # Guibei Zhuang
        "tyz",  # Tày
        "rbb",  # Rumai Palaung
        "xog",  # Soga
        "ytp",  # Thopho
        "byo",  # Biyo
        "kry",  # Kryts
        "sen",  # Nanerigé Sénoufo
        "ghn",  # Ghanongga
        "stv",  # Silt'e
        "hma",  # Southern Mashan Hmong
        "sze",  # Seze
        "bbj",  # Ghomálá'
        "koq",  # Kota (Gabon)
        "nbb",  # Ndoe
        "tdl",  # Sur
        "ska",  # Skagit
        "gvp",  # Pará Gavião
        "kbf",  # Kakauhua
        "cla",  # Ron
        "yro",  # Yaroamë
        "lov",  # Lopi
        "fsl",  # French Sign Language
        "kbz",  # Duhwa
        "ton",  # Tonga (Tonga Islands)
        "zph",  # Totomachapan Zapotec
        "rif",  # Tarifit
        "col",  # Columbia-Wenatchi
        "zkd",  # Kadu
        "oon",  # Önge
        "mje",  # Muskum
        "aja",  # Aja (South Sudan)
        "llo",  # Khlor
        "bqx",  # Baangi
        "pod",  # Ponares
        "sqa",  # Shama-Sambuga
        "raf",  # Western Meohang
        "koc",  # Kpati
        "bwc",  # Bwile
        "mvs",  # Massep
        "jaz",  # Jawe
        "abn",  # Abua
        "hem",  # Hemba
        "jud",  # Worodougou
        "lug",  # Ganda
        "pgs",  # Pangseng
        "kfm",  # Khunsari
        "duf",  # Dumbea
        "ylo",  # Naluo Yi
        "ahr",  # Ahirani
        "qvn",  # North Junín Quechua
        "dmw",  # Mudburra
        "bpu",  # Bongu
        "zau",  # Zangskari
        "agl",  # Fembe
        "les",  # Lese
        "cal",  # Carolinian
        "lrc",  # Northern Luri
        "ktn",  # Karitiâna
        "aby",  # Aneme Wake
        "wrb",  # Waluwarra
        "hhr",  # Kerak
        "zsu",  # Sukurum
        "nky",  # Khiamniungan Naga
        "aft",  # Afitti
        "xka",  # Kalkoti
        "ubr",  # Ubir
        "mpv",  # Mungkip
        "nyc",  # Nyanga-li
        "pkr",  # Attapady Kurumba
        "dts",  # Toro So Dogon
        "bzx",  # Kɛlɛngaxo Bozo
        "bhn",  # Bohtan Neo-Aramaic
        "gmn",  # Gimnime
        "maa",  # San Jerónimo Tecóatl Mazatec
        "tlx",  # Khehek
        "wrk",  # Garrwa
        "pym",  # Fyam
        "vkp",  # Korlai Creole Portuguese
        "mgq",  # Malila
        "rmq",  # Caló
        "xcc",  # Camunic
        "sbu",  # Stod Bhoti
        "goj",  # Gowlan
        "kqd",  # Koy Sanjaq Surat
        "lgn",  # T'apo
        "kqt",  # Klias River Kadazan
        "tom",  # Tombulu
        "myy",  # Macuna
        "wne",  # Waneci
        "mgm",  # Mambae
        "aad",  # Amal
        "jae",  # Yabem
        "ncz",  # Natchez
        "daa",  # Dangaléat
        "vkn",  # Koro Nulu
        "xbr",  # Kambera
        "mbq",  # Maisin
        "mkt",  # Vamale
        "lii",  # Lingkhim
        "dru",  # Rukai
        "tyu",  # Kua
        "amb",  # Ambo
        "igs",  # Interglossa
        "snn",  # Siona
        "awu",  # Central Awyu
        "rgr",  # Resígaro
        "vum",  # Vumbu
        "otz",  # Ixtenco Otomi
        "zmn",  # Mbangwe
        "yiy",  # Yir Yoront
        "bfj",  # Bafanji
        "bgw",  # Bhatri
        "mhf",  # Mamaa
        "evn",  # Evenki
        "nql",  # Ngendelengo
        "wep",  # Westphalien
        "orv",  # Old Russian
        "ynn",  # Yana
        "mue",  # Media Lengua
        "hmc",  # Central Huishui Hmong
        "pkn",  # Pakanha
        "wun",  # Bungu
        "mwo",  # Central Maewo
        "jnj",  # Yemsa
        "mjg",  # Tu
        "inh",  # Ingush
        "cdi",  # Chodri
        "sbp",  # Sangu (Tanzania)
        "ylr",  # Yalarnnga
        "adj",  # Adioukrou
        "yta",  # Talu
        "ppr",  # Piru
        "nja",  # Nzanyi
        "quj",  # Joyabaj Quiché
        "sqx",  # Kufr Qassem Sign Language (KQSL)
        "gbg",  # Gbanziri
        "krj",  # Kinaray-A
        "caf",  # Southern Carrier
        "piy",  # Piya-Kwonci
        "tpi",  # Tok Pisin
        "nhs",  # Southeastern Puebla Nahuatl
        "afz",  # Obokuitai
        "xpd",  # Oyster Bay Tasmanian
        "muw",  # Mundari
        "cpx",  # Pu-Xian Chinese
        "nxk",  # Koki Naga
        "peb",  # Eastern Pomo
        "swj",  # Sira
        "ukk",  # Muak Sa-aak
        "bam",  # Bambara
        "kzq",  # Kaike
        "bwn",  # Wunai Bunu
        "xsu",  # Sanumá
        "huw",  # Hukumina
        "duw",  # Dusun Witu
        "gyl",  # Gayil
        "gef",  # Gerai
        "era",  # Eravallan
        "mhs",  # Buru (Indonesia)
        "cpc",  # Ajyíninka Apurucayali
        "iml",  # Miluk
        "ntp",  # Northern Tepehuan
        "fip",  # Fipa
        "wka",  # Kw'adza
        "stt",  # Budeh Stieng
        "env",  # Enwan (Edo State)
        "mba",  # Higaonon
        "nbe",  # Konyak Naga
        "tqt",  # Western Totonac
        "tyv",  # Tuvinian
        "yes",  # Nyankpa
        "mkz",  # Makasae
        "rah",  # Rabha
        "kpg",  # Kapingamarangi
        "muh",  # Mündü
        "wlw",  # Walak
        "nxd",  # Ngando (Democratic Republic of Congo)
        "kuh",  # Kushi
        "lro",  # Laro
        "bxk",  # Bukusu
        "vku",  # Kurrama
        "cox",  # Nanti
        "tae",  # Tariana
        "nxn",  # Ngawun
        "pap",  # Papiamento
        "xkr",  # Xakriabá
        "tkv",  # Mur Pano
        "atr",  # Waimiri-Atroari
        "tux",  # Tuxináwa
        "cul",  # Culina
        "toq",  # Toposa
        "wap",  # Wapishana
        "bqq",  # Biritai
        "lgr",  # Lengo
        "avo",  # Agavotaguerra
        "ayo",  # Ayoreo
        "brt",  # Bitare
        "mgj",  # Abureni
        "bnv",  # Bonerif
        "ava",  # Avaric
        "nzy",  # Nzakambay
        "age",  # Angal
        "cat",  # Catalan
        "xch",  # Chemakum
        "ibl",  # Ibaloi
        "teo",  # Teso
        "kaa",  # Kara-Kalpak
        "tgq",  # Tring
        "zgh",  # Standard Moroccan Tamazight
        "xtm",  # Magdalena Peñasco Mixtec
        "nxa",  # Nauete
        "wib",  # Southern Toussian
        "scp",  # Hyolmo
        "kst",  # Winyé
        "tiz",  # Tai Hongjin
        "gcr",  # Guianese Creole French
        "enu",  # Enu
        "abh",  # Tajiki Arabic
        "aru",  # Aruá (Amazonas State)
        "nlg",  # Gela
        "sij",  # Numbami
        "smd",  # Sama
        "xme",  # Median
        "hld",  # Halang Doan
        "izm",  # Kizamani
        "qvi",  # Imbabura Highland Quichua
        "ogo",  # Khana
        "yay",  # Agwagwune
        "tla",  # Southwestern Tepehuan
        "hba",  # Hamba
        "dez",  # Dengese
        "lhl",  # Lahul Lohar
        "sgx",  # Sierra Leone Sign Language
        "peo",  # Old Persian (ca. 600-400 B.C.)
        "koi",  # Komi-Permyak
        "tzc",  # Chamula Tzotzil
        "ttp",  # Tombelala
        "isr",  # Israeli Sign Language
        "yob",  # Yoba
        "mpb",  # Malak Malak
        "ota",  # Ottoman Turkish (1500-1928)
        "hih",  # Pamosu
        "pbs",  # Central Pame
        "ctm",  # Chitimacha
        "tod",  # Toma
        "dri",  # C'Lela
        "kgo",  # Krongo
        "kav",  # Katukína
        "wau",  # Waurá
        "teb",  # Tetete
        "zhi",  # Zhire
        "mhd",  # Mbugu
        "ptw",  # Pentlatch
        "stp",  # Southeastern Tepehuan
        "zab",  # Western Tlacolula Valley Zapotec
        "xtq",  # Tumshuqese
        "xwd",  # Wadi Wadi
        "ilv",  # Ilue
        "xfa",  # Faliscan
        "teg",  # Teke-Tege
        "srr",  # Serer
        "moo",  # Monom
        "yab",  # Yuhup
        "ers",  # Ersu
        "doo",  # Dongo
        "xww",  # Wemba Wemba
        "awi",  # Aekyom
        "lha",  # Laha (Viet Nam)
        "plc",  # Central Palawano
        "cuo",  # Cumanagoto
        "bsu",  # Bahonsuai
        "bft",  # Balti
        "aig",  # Antigua and Barbuda Creole English
        "cof",  # Colorado
        "kzw",  # Karirí-Xocó
        "lcl",  # Lisela
        "hud",  # Huaulu
        "cuc",  # Usila Chinantec
        "bkk",  # Brokskat
        "kzp",  # Kaidipang
        "llp",  # North Efate
        "knh",  # Kayan River Kenyah
        "dmc",  # Gavak
        "xdc",  # Dacian
        "ano",  # Andoque
        "kwf",  # Kwara'ae
        "ssc",  # Suba-Simbiti
        "dot",  # Dass
        "aqz",  # Akuntsu
        "dam",  # Damakawa
        "miu",  # Cacaloxtepec Mixtec
        "dtt",  # Toro Tegu Dogon
        "cdm",  # Chepang
        "gil",  # Gilbertese
        "aps",  # Arop-Sissano
        "tzj",  # Tz'utujil
        "hmo",  # Hiri Motu
        "kri",  # Krio
        "xmz",  # Mori Bawah
        "ktv",  # Eastern Katu
        "pdc",  # Pennsylvania German
        "xkj",  # Kajali
        "rey",  # Reyesano
        "scq",  # Sa'och
        "krn",  # Sapo
        "awe",  # Awetí
        "jio",  # Jiamao
        "spp",  # Supyire Senoufo
        "ybk",  # Bokha
        "mvf",  # Peripheral Mongolian
        "lwo",  # Luwo
        "pmj",  # Southern Pumi
        "srn",  # Sranan Tongo
        "gnr",  # Gureng Gureng
        "kwu",  # Kwakum
        "huz",  # Hunzib
        "mbg",  # Northern Nambikuára
        "ruz",  # Ruma
        "ldo",  # Loo
        "jqr",  # Jaqaru
        "jkp",  # Paku Karen
        "kqm",  # Khisa
        "hks",  # Hong Kong Sign Language
        "sbr",  # Sembakung Murut
        "ymi",  # Moji
        "jmx",  # Western Juxtlahuaca Mixtec
        "xce",  # Celtiberian
        "lew",  # Ledo Kaili
        "cic",  # Chickasaw
        "tvt",  # Tutsa Naga
        "bqp",  # Busa
        "mgz",  # Mbugwe
        "aay",  # Aariya
        "whk",  # Wahau Kenyah
        "cce",  # Chopi
        "kiv",  # Kimbu
        "gbc",  # Garawa
        "ekr",  # Yace
        "kow",  # Kugama
        "nhr",  # Naro
        "yui",  # Yurutí
        "lnt",  # Lintang
        "hle",  # Hlersu
        "dbn",  # Duriankere
        "eus",  # Basque
        "cek",  # Eastern Khumi Chin
        "dnv",  # Danu
        "baa",  # Babatana
        "ztm",  # San Agustín Mixtepec Zapotec
        "ymo",  # Yangum Mon
        "lkb",  # Kabras
        "crx",  # Carrier
        "gwe",  # Gweno
        "hun",  # Hungarian
        "mof",  # Mohegan-Montauk-Narragansett
        "odu",  # Odual
        "lpa",  # Lelepa
        "seu",  # Serui-Laut
        "sng",  # Sanga (Democratic Republic of Congo)
        "lmh",  # Lambichhong
        "mkk",  # Byep
        "way",  # Wayana
        "had",  # Hatam
        "log",  # Logo
        "bxi",  # Pirlatapa
        "bry",  # Burui
        "bvs",  # Belgian Sign Language
        "mrl",  # Mortlockese
        "zsl",  # Zambian Sign Language
        "fll",  # North Fali
        "bmj",  # Bote-Majhi
        "mby",  # Memoni
        "kcu",  # Kami (Tanzania)
        "cao",  # Chácobo
        "bpn",  # Dzao Min
        "nss",  # Nali
        "xup",  # Upper Umpqua
        "lkd",  # Lakondê
        "qwa",  # Corongo Ancash Quechua
        "des",  # Desano
        "mmr",  # Western Xiangxi Miao
        "ade",  # Adele
        "wlx",  # Wali (Ghana)
        "npl",  # Southeastern Puebla Nahuatl
        "csv",  # Sumtu Chin
        "unx",  # Munda
        "lml",  # Hano
        "lsy",  # Mauritian Sign Language
        "zul",  # Zulu
        "llj",  # Ladji Ladji
        "bda",  # Bayot
        "vam",  # Vanimo
        "sja",  # Epena
        "cmo",  # Central Mnong
        "bms",  # Bilma Kanuri
        "rms",  # Romanian Sign Language
        "ukg",  # Ukuriguma
        "awo",  # Awak
        "spu",  # Sapuan
        "rge",  # Romano-Greek
        "kkd",  # Kinuku
        "qua",  # Quapaw
        "woc",  # Wogeo
        "bpv",  # Bian Marind
        "bfa",  # Bari
        "zmi",  # Negeri Sembilan Malay
        "sgt",  # Brokpake
        "dlm",  # Dalmatian
        "bjy",  # Bayali
        "esi",  # North Alaskan Inupiatun
        "dhx",  # Dhungaloo
        "bba",  # Baatonum
        "beu",  # Blagar
        "ngv",  # Nagumi
        "los",  # Loniu
        "kto",  # Kuot
        "pkp",  # Pukapuka
        "suc",  # Western Subanon
        "mtd",  # Mualang
        "ayx",  # Ayi (China)
        "ssi",  # Sansi
        "znk",  # Manangkari
        "llc",  # Lele (Guinea)
        "txh",  # Thracian
        "gaq",  # Gata'
        "mpk",  # Mbara (Chad)
        "xuo",  # Kuo
        "ddg",  # Fataluku
        "mrt",  # Marghi Central
        "rup",  # Macedo-Romanian
        "mei",  # Midob
        "tow",  # Jemez
        "mqn",  # Moronene
        "dkr",  # Kuijau
        "abo",  # Abon
        "wud",  # Wudu
        "kvp",  # Kompane
        "xul",  # Ngunawal
        "yak",  # Yakama
        "kap",  # Bezhta
        "mmi",  # Hember Avu
        "acn",  # Achang
        "gbl",  # Gamit
        "vmj",  # Ixtayutla Mixtec
        "agn",  # Agutaynen
        "dik",  # Southwestern Dinka
        "car",  # Galibi Carib
        "ili",  # Ili Turki
        "lum",  # Luimbi
        "cjh",  # Upper Chehalis
        "tnn",  # North Tanna
        "nio",  # Nganasan
        "teh",  # Tehuelche
        "mts",  # Yora
        "bmb",  # Bembe
        "aom",  # Ömie
        "lib",  # Likum
        "phk",  # Phake
        "gdk",  # Gadang
        "mcd",  # Sharanahua
        "skw",  # Skepi Creole Dutch
        "mur",  # Murle
        "tnl",  # Lenakel
        "bcx",  # Pamona
        "lln",  # Lele (Chad)
        "nmm",  # Manangba
        "rgk",  # Rangkas
        "cah",  # Cahuarano
        "ncl",  # Michoacán Nahuatl
        "chs",  # Chumash
        "cdo",  # Min Dong Chinese
        "yom",  # Yombe
        "guz",  # Gusii
        "ndt",  # Ndunga
        "aqr",  # Arhâ
        "gga",  # Gao
        "skn",  # Kolibugan Subanon
        "cpn",  # Cherepon
        "raa",  # Dungmali
        "kft",  # Kanjari
        "ztq",  # Quioquitani-Quierí Zapotec
        "kba",  # Kalarko
        "atn",  # Ashtiani
        "bgp",  # Eastern Balochi
        "fiz",  # Izere
        "btc",  # Bati (Cameroon)
        "doy",  # Dompo
        "fij",  # Fijian
        "nki",  # Thangal Naga
        "nza",  # Tigon Mbembe
        "man",  # Mandingo
        "nov",  # Novial
        "xcv",  # Chuvantsy
        "npy",  # Napu
        "bxl",  # Jalkunan
        "ghr",  # Ghera
        "enf",  # Forest Enets
        "csb",  # Kashubian
        "rmy",  # Vlax Romani
        "sbq",  # Sileibi
        "nlr",  # Ngarla
        "bcu",  # Awad Bing
        "zia",  # Zia
        "hmu",  # Hamap
        "xrg",  # Minang
        "mhy",  # Ma'anyan
        "toz",  # To
        "ngx",  # Nggwahyi
        "lws",  # Malawian Sign Language
        "ozm",  # Koonzime
        "wln",  # Walloon
        "bch",  # Bariai
        "kdn",  # Kunda
        "hmm",  # Central Mashan Hmong
        "bxq",  # Beele
        "ptt",  # Enrekang
        "tnm",  # Tabla
        "xmx",  # Salawati
        "njy",  # Njyem
        "bel",  # Belarusian
        "sbs",  # Subiya
        "tlv",  # Taliabu
        "luo",  # Luo (Kenya and Tanzania)
        "idc",  # Idon
        "bfg",  # Busang Kayan
        "ckz",  # Cakchiquel-Quiché Mixed Language
        "txr",  # Tartessian
        "xmp",  # Kuku-Mu'inh
        "sdm",  # Semandang
        "bnj",  # Eastern Tawbuid
        "kqw",  # Kandas
        "cak",  # Kaqchikel
        "apj",  # Jicarilla Apache
        "ekk",  # Standard Estonian
        "owl",  # Old Welsh
        "wno",  # Wano
        "pne",  # Western Penan
        "aen",  # Armenian Sign Language
        "frd",  # Fordata
        "knz",  # Kalamsé
        "zmc",  # Margany
        "tll",  # Tetela
        "mqa",  # Maba (Indonesia)
        "txm",  # Tomini
        "fuq",  # Central-Eastern Niger Fulfulde
        "alc",  # Qawasqar
        "mwp",  # Kala Lagaw Ya
        "bly",  # Notre
        "knv",  # Tabo
        "awc",  # Cicipu
        "xyt",  # Mayi-Thakurti
        "drl",  # Paakantyi
        "bmy",  # Bemba (Democratic Republic of Congo)
        "gdr",  # Wipi
        "buk",  # Bugawac
        "blc",  # Bella Coola
        "clh",  # Chilisso
        "pgi",  # Pagi
        "glg",  # Galician
        "sca",  # Sansu
        "mos",  # Mossi
        "zmy",  # Mariyedi
        "swp",  # Suau
        "oji",  # Ojibwa
        "lsg",  # Lyons Sign Language
        "yki",  # Yoke
        "nnm",  # Namia
        "wtf",  # Watiwa
        "duk",  # Uyajitaya
        "juu",  # Ju
        "gmh",  # Middle High German (ca. 1050-1500)
        "svc",  # Vincentian Creole English
        "pla",  # Miani
        "dbi",  # Doka
        "suy",  # Suyá
        "dds",  # Donno So Dogon
        "ttb",  # Gaa
        "rcf",  # Réunion Creole French
        "huh",  # Huilliche
        "bbk",  # Babanki
        "nog",  # Nogai
        "mfr",  # Marrithiyel
        "hto",  # Minica Huitoto
        "nkw",  # Nkutu
        "ckj",  # Santo Domingo Xenacoj Cakchiquel
        "guf",  # Gupapuyngu
        "tgb",  # Tobilung
        "yok",  # Yokuts
        "lby",  # Lamalama
        "jav",  # Javanese
        "hos",  # Ho Chi Minh City Sign Language
        "khf",  # Khuen
        "crm",  # Moose Cree
        "ppe",  # Papi
        "ivv",  # Ivatan
        "scx",  # Sicel
        "cnx",  # Middle Cornish
        "ngg",  # Ngbaka Manza
        "mtj",  # Moskona
        "fay",  # Southwestern Fars
        "tio",  # Teop
        "smg",  # Simbali
        "btj",  # Bacanese Malay
        "bza",  # Bandi
        "yir",  # North Awyu
        "mlw",  # Moloko
        "gbb",  # Kaytetye
        "sat",  # Santali
        "oos",  # Old Ossetic
        "thc",  # Tai Hang Tong
        "ati",  # Attié
        "dgk",  # Dagba
        "quu",  # Eastern Quiché
        "acr",  # Achi
        "cgc",  # Kagayanen
        "tnj",  # Tanjong
        "ggw",  # Gogodala
        "una",  # North Watut
        "iso",  # Isoko
        "ark",  # Arikapú
        "bpc",  # Mbuk
        "mym",  # Me'en
        "tpf",  # Tarpia
        "bon",  # Bine
        "bri",  # Mokpwe
        "mcp",  # Makaa
        "iws",  # Sepik Iwam
        "cos",  # Corsican
        "xtj",  # San Juan Teita Mixtec
        "lar",  # Larteh
        "nyu",  # Nyungwe
        "shl",  # Shendu
        "spq",  # Loreto-Ucayali Spanish
        "ssv",  # Shark Bay
        "auy",  # Awiyaana
        "okg",  # Koko Babangk
        "xtp",  # San Miguel Piedras Mixtec
        "tal",  # Tal
        "wac",  # Wasco-Wishram
        "yeu",  # Yerukula
        "liz",  # Libinza
        "kdl",  # Tsikimba
        "ecr",  # Eteocretan
        "snk",  # Soninke
        "jbe",  # Judeo-Berber
        "div",  # Dhivehi
        "mbo",  # Mbo (Cameroon)
        "mzv",  # Manza
        "byn",  # Bilin
        "awy",  # Edera Awyu
        "dug",  # Duruma
        "hnd",  # Southern Hindko
        "nzs",  # New Zealand Sign Language
        "skl",  # Selako
        "ltz",  # Luxembourgish
        "rai",  # Ramoaaina
        "iai",  # Iaai
        "kbj",  # Kari
        "wbq",  # Waddar
        "xom",  # Komo (Sudan)
        "mfe",  # Morisyen
        "mte",  # Mono (Solomon Islands)
        "pyy",  # Pyen
        "uur",  # Ura (Vanuatu)
        "bgd",  # Rathwi Bareli
        "ago",  # Tainae
        "huu",  # Murui Huitoto
        "mce",  # Itundujia Mixtec
        "ssb",  # Southern Sama
        "tmb",  # Katbol
        "ymd",  # Muda
        "tgk",  # Tajik
        "kbo",  # Keliko
        "awh",  # Awbono
        "mir",  # Isthmus Mixe
        "bhk",  # Albay Bicolano
        "wur",  # Wurrugu
        "bja",  # Budza
        "byi",  # Buyu
        "kfl",  # Kung
        "oaa",  # Orok
        "lou",  # Louisiana Creole
        "iko",  # Olulumo-Ikom
        "laf",  # Lafofa
        "xsd",  # Sidetic
        "lio",  # Liki
        "arp",  # Arapaho
        "pin",  # Piame
        "xtu",  # Cuyamecalco Mixtec
        "cux",  # Tepeuxila Cuicatec
        "sik",  # Sikiana
        "ctt",  # Wayanad Chetti
        "moh",  # Mohawk
        "elo",  # El Molo
        "prv",  # Provençal
        "bcd",  # North Babar
        "abl",  # Lampung Nyo
        "tgv",  # Tingui-Boto
        "gnn",  # Gumatj
        "ggo",  # Southern Gondi
        "yhl",  # Hlepho Phowa
        "bwg",  # Barwe
        "wii",  # Minidien
        "anb",  # Andoa
        "lhi",  # Lahu Shi
        "jrb",  # Judeo-Arabic
        "zoh",  # Chimalapa Zoque
        "bkb",  # Finallig
        "mlt",  # Maltese
        "ptr",  # Piamatsina
        "kij",  # Kilivila
        "gho",  # Ghomara
        "lmv",  # Lomaiviti
        "bsq",  # Bassa
        "ntg",  # Ngantangarra
        "qva",  # Ambo-Pasco Quechua
        "piv",  # Pileni
        "buq",  # Brem
        "zpc",  # Choapan Zapotec
        "cvg",  # Chug
        "xla",  # Kamula
        "xmw",  # Tsimihety Malagasy
        "poc",  # Poqomam
        "bnm",  # Batanga
        "nob",  # Norwegian Bokmål
        "azn",  # Western Durango Nahuatl
        "dje",  # Zarma
        "ugy",  # Uruguayan Sign Language
        "brq",  # Breri
        "sos",  # Seeku
        "ycp",  # Chepya
        "yiq",  # Miqie
        "ach",  # Acoli
        "gdb",  # Pottangi Ollar Gadaba
        "ake",  # Akawaio
        "kqf",  # Kakabai
        "mgr",  # Mambwe-Lungu
        "mhh",  # Maskoy Pidgin
        "dsk",  # Dokshi
        "pta",  # Pai Tavytera
        "etx",  # Eten
        "doa",  # Dom
        "pby",  # Pyu (Papua New Guinea)
        "xpp",  # Puyo-Paekche
        "mml",  # Man Met
        "tft",  # Ternate
        "bmf",  # Bom-Kim
        "ogc",  # Ogbah
        "rjb",  # Rajbanshi
        "mvl",  # Mbara (Australia)
        "bwt",  # Bafaw-Balong
        "aqd",  # Ampari Dogon
        "xms",  # Moroccan Sign Language
        "bhf",  # Odiai
        "ghl",  # Ghulfan
        "myj",  # Mangayat
        "bxg",  # Bangala
        "bhb",  # Bhili
        "kfr",  # Kachhi
        "tuj",  # Tugutil
        "zts",  # Tilquiapan Zapotec
        "nsp",  # Nepalese Sign Language
        "trb",  # Terebu
        "gcl",  # Grenadian Creole English
        "bbs",  # Bakpinka
        "wyb",  # Wangaaybuwan-Ngiyambaa
        "jni",  # Janji
        "lif",  # Limbu
        "bsv",  # Baga Sobané
        "kzc",  # Bondoukou Kulango
        "sqt",  # Soqotri
        "she",  # Sheko
        "dsq",  # Tadaksahak
        "luj",  # Luna
        "mio",  # Pinotepa Nacional Mixtec
        "mll",  # Malua Bay
        "ola",  # Walungge
        "syn",  # Senaya
        "dax",  # Dayi
        "zpt",  # San Vicente Coatlán Zapotec
        "xay",  # Kayan Mahakam
        "frt",  # Fortsenal
        "aul",  # Aulua
        "nid",  # Ngandi
        "lti",  # Leti (Indonesia)
        "niu",  # Niuean
        "tkt",  # Kathoriya Tharu
        "cim",  # Cimbrian
        "lsp",  # Panamanian Sign Language
        "slm",  # Pangutaran Sama
        "xaw",  # Kawaiisu
        "sha",  # Shall-Zwall
        "bfb",  # Pauri Bareli
        "met",  # Mato
        "tlu",  # Tulehu
        "diq",  # Dimli (individual language)
        "deu",  # German
        "lmq",  # Lamatuka
        "txo",  # Toto
        "sjd",  # Kildin Sami
        "apk",  # Kiowa Apache
        "miz",  # Coatzospan Mixtec
        "gjr",  # Gurindji Kriol
        "tmz",  # Tamanaku
        "aze",  # Azerbaijani
        "qwm",  # Kuman (Russia)
        "nea",  # Eastern Ngad'a
        "srf",  # Nafi
        "bro",  # Brokkat
        "kuc",  # Kwinsu
        "tid",  # Tidong
        "elh",  # El Hugeirat
        "atb",  # Zaiwa
        "moc",  # Mocoví
        "qvo",  # Napo Lowland Quechua
        "blp",  # Blablanga
        "ccc",  # Chamicuro
        "nly",  # Nyamal
        "izi",  # Izi-Ezaa-Ikwo-Mgbo
        "atx",  # Arutani
        "dni",  # Lower Grand Valley Dani
        "cap",  # Chipaya
        "slx",  # Salampasu
        "mfs",  # Mexican Sign Language
        "kbr",  # Kafa
        "iqw",  # Ikwo
        "bzt",  # Brithenig
        "hhi",  # Hoia Hoia
        "hoo",  # Holoholo
        "dyb",  # Dyaberdyaber
        "gib",  # Gibanawa
        "yha",  # Baha Buyang
        "udu",  # Uduk
        "mif",  # Mofu-Gudur
        "gmx",  # Magoma
        "slf",  # Swiss-Italian Sign Language
        "mmx",  # Madak
        "mko",  # Mingang Doso
        "swu",  # Suwawa
        "aal",  # Afade
        "bee",  # Byangsi
        "ilk",  # Ilongot
        "dgc",  # Casiguran Dumagat Agta
        "xak",  # Máku
        "gnz",  # Ganzi
        "xep",  # Epi-Olmec
        "teu",  # Soo
        "lfn",  # Lingua Franca Nova
        "gha",  # Ghadamès
        "gll",  # Garlali
        "sxb",  # Suba
        "bgm",  # Baga Mboteni
        "kre",  # Panará
        "udj",  # Ujir
        "yno",  # Yong
        "szp",  # Suabo
        "tfo",  # Tefaro
        "zho",  # Chinese
        "omr",  # Old Marathi
        "huf",  # Humene
        "puf",  # Punan Merah
        "msf",  # Mekwei
        "ppa",  # Pao
        "pcw",  # Pyapun
        "osp",  # Old Spanish
        "wig",  # Wik Ngathan
        "cbm",  # Yepocapa Southwestern Cakchiquel
        "ccm",  # Malaccan Creole Malay
        "orw",  # Oro Win
        "ayi",  # Leyigha
        "mud",  # Mednyj Aleut
        "tmh",  # Tamashek
        "gah",  # Alekano
        "qus",  # Santiago del Estero Quichua
        "dmm",  # Dama
        "jrt",  # Jakattoe
        "kao",  # Xaasongaxango
        "nnh",  # Ngiemboon
        "qul",  # North Bolivian Quechua
        "sev",  # Nyarafolo Senoufo
        "xkv",  # Kgalagadi
        "kkj",  # Kako
        "guk",  # Gumuz
        "apq",  # A-Pucikwar
        "kty",  # Kango (Bas-Uélé District)
        "roh",  # Romansh
        "bir",  # Bisorio
        "mrp",  # Morouas
        "pbh",  # E'ñapa Woromaipu
        "kpu",  # Kafoa
        "wmx",  # Womo
        "tmq",  # Tumleo
        "bki",  # Baki
        "blt",  # Tai Dam
        "aoh",  # Arma
        "bgi",  # Giangan
        "nsk",  # Naskapi
        "kda",  # Worimi
        "pgd",  # Gāndhārī
        "raq",  # Saam
        "cki",  # Santa María De Jesús Cakchiquel
        "rab",  # Camling
        "nmg",  # Kwasio
        "zps",  # Coatlán Zapotec
        "leo",  # Leti (Cameroon)
        "uuu",  # U
        "ncf",  # Notsi
        "kka",  # Kakanda
        "xqt",  # Qatabanian
        "avb",  # Avau
        "ity",  # Moyadan Itneg
        "hsn",  # Xiang Chinese
        "pbf",  # Coyotepec Popoloca
        "kpn",  # Kepkiriwát
        "svr",  # Savara
        "ved",  # Veddah
        "bpk",  # Orowe
        "jan",  # Jandai
        "xts",  # Sindihui Mixtec
        "mnr",  # Mono (USA)
        "dyr",  # Dyarim
        "ims",  # Marsian
        "ilw",  # Talur
        "qyp",  # Quiripi
        "aaw",  # Solong
        "spv",  # Sambalpuri
        "kfc",  # Konda-Dora
        "sty",  # Siberian Tatar
        "gnu",  # Gnau
        "dur",  # Dii
        "txe",  # Totoli
        "mkm",  # Moklen
        "lww",  # Lewo
        "unm",  # Unami
        "aiy",  # Ali
        "gpa",  # Gupa-Abawa
        "pai",  # Pe
        "ncr",  # Ncane
        "tcp",  # Tawr Chin
        "sao",  # Sause
        "gwf",  # Gowro
        "xud",  # Umiida
        "tqw",  # Tonkawa
        "apt",  # Apatani
        "nlx",  # Nahali
        "otr",  # Otoro
        "mip",  # Apasco-Apoala Mixtec
        "kyw",  # Kudmali
        "vun",  # Vunjo
        "pgg",  # Pangwali
        "byy",  # Buya
        "ybd",  # Yangbye
        "pnb",  # Western Panjabi
        "mdx",  # Dizin
        "xbc",  # Bactrian
        "bok",  # Bonjo
        "kpv",  # Komi-Zyrian
        "myf",  # Bambassi
        "csa",  # Chiltepec Chinantec
        "kbw",  # Kaiep
        "wed",  # Wedau
        "yyr",  # Yir Yoront
        "avm",  # Angkamuthi
        "klo",  # Kapya
        "tgh",  # Tobagonian Creole English
        "vap",  # Vaiphei
        "jcs",  # Jamaican Country Sign Language
        "kjo",  # Harijan Kinnauri
        "abz",  # Abui
        "smt",  # Simte
        "rkm",  # Marka
        "dui",  # Dumun
        "tke",  # Takwane
        "bxo",  # Barikanchi
        "ggh",  # Garreh-Ajuran
        "mgs",  # Manda (Tanzania)
        "nbl",  # South Ndebele
        "iby",  # Ibani
        "gak",  # Gamkonora
        "xgl",  # Galindan
        "srt",  # Sauri
        "mpn",  # Mindiri
        "daf",  # Dan
        "kez",  # Kukele
        "och",  # Old Chinese
        "sxn",  # Sangir
        "hoi",  # Holikachuk
        "geg",  # Gengle
        "adg",  # Andegerebinha
        "thq",  # Kochila Tharu
        "ifb",  # Batad Ifugao
        "uky",  # Kuuk-Yak
        "gwg",  # Moo
        "boj",  # Anjam
        "smp",  # Samaritan
        "tiy",  # Tiruray
        "fbl",  # West Albay Bikol
        "tyy",  # Tiyaa
        "ngs",  # Gvoko
        "nra",  # Ngom
        "klq",  # Rumu
        "yko",  # Yasa
        "tbj",  # Tiang
        "xph",  # North Midlands Tasmanian
        "kko",  # Karko
        "kxz",  # Kerewo
        "atj",  # Atikamekw
        "mln",  # Malango
        "tsu",  # Tsou
        "yue",  # Yue Chinese
        "bkp",  # Boko (Democratic Republic of Congo)
        "dgh",  # Dghwede
        "crg",  # Michif
        "doe",  # Doe
        "kbk",  # Grass Koiari
        "yog",  # Yogad
        "smh",  # Samei
        "gvr",  # Gurung
        "nka",  # Nkoya
        "urc",  # Urningangg
        "agp",  # Paranan
        "atf",  # Atuence
        "blx",  # Mag-Indi Ayta
        "kmv",  # Karipúna Creole French
        "gyf",  # Gungabula
        "mvt",  # Mpotovoro
        "ari",  # Arikara
        "anl",  # Anu-Hkongso Chin
        "fia",  # Nobiin
        "kvt",  # Lahta Karen
        "spl",  # Selepet
        "gqu",  # Qau
        "jma",  # Dima
        "stb",  # Northern Subanen
        "mis",  # Uncoded languages
        "omu",  # Omurano
        "jek",  # Jeri Kuo
        "ait",  # Arikem
        "goy",  # Goundo
        "ijs",  # Southeast Ijo
        "bis",  # Bislama
        "bdy",  # Bandjalang
        "bsy",  # Sabah Bisaya
        "cry",  # Cori
        "kht",  # Khamti
        "maq",  # Chiquihuitlán Mazatec
        "pmo",  # Pom
        "jos",  # Jordanian Sign Language
        "tmc",  # Tumak
        "gix",  # Gilima
        "leu",  # Kara (Papua New Guinea)
        "jpa",  # Jewish Palestinian Aramaic
        "fit",  # Tornedalen Finnish
        "wry",  # Merwari
        "wci",  # Waci Gbe
        "dbv",  # Dungu
        "ebc",  # Beginci
        "aoi",  # Anindilyakwa
        "pah",  # Tenharim
        "grh",  # Gbiri-Niragu
        "zyb",  # Yongbei Zhuang
        "tls",  # Tambotalo
        "mge",  # Mango
        "yal",  # Yalunka
        "yda",  # Yanda
        "aac",  # Ari
        "kga",  # Koyaga
        "srk",  # Serudung Murut
        "irh",  # Irarutu
        "mgk",  # Mawes
        "med",  # Melpa
        "qxi",  # San Andrés Quiché
        "lky",  # Lokoya
        "mnp",  # Min Bei Chinese
        "mnq",  # Minriq
        "ott",  # Temoaya Otomi
        "luq",  # Lucumi
        "adp",  # Adap
        "cin",  # Cinta Larga
        "lkj",  # Remun
        "amv",  # Ambelau
        "new",  # Newari
        "asr",  # Asuri
        "yoi",  # Yonaguni
        "lwl",  # Eastern Lawa
        "kpz",  # Kupsabiny
        "ssh",  # Shihhi Arabic
        "akc",  # Mpur
        "lki",  # Laki
        "jit",  # Jita
        "uis",  # Uisai
        "nww",  # Ndwewe
        "uni",  # Uni
        "kvo",  # Dobel
        "cnc",  # Côông
        "muy",  # Muyang
        "kan",  # Kannada
        "poq",  # Texistepec Popoluca
        "kwh",  # Kowiai
        "mrv",  # Mangareva
        "weg",  # Wergaia
        "mid",  # Mandaic
        "bwj",  # Láá Láá Bwamu
        "bbb",  # Barai
        "dge",  # Degenan
        "gor",  # Gorontalo
        "miy",  # Ayutla Mixtec
        "isd",  # Isnag
        "dop",  # Lukpa
        "eno",  # Enggano
        "bws",  # Bomboma
        "frk",  # Frankish
        "lmp",  # Limbum
        "swv",  # Shekhawati
        "rnr",  # Nari Nari
        "xxr",  # Koropó
        "sac",  # Meskwaki
        "ibh",  # Bih
        "woa",  # Kuwema
        "tik",  # Tikar
        "eka",  # Ekajuk
        "lbs",  # Libyan Sign Language
        "bpz",  # Bilba
        "byq",  # Basay
        "gwx",  # Gua
        "trt",  # Tunggare
        "kxb",  # Krobu
        "dpp",  # Papar
        "fuj",  # Ko
        "tnh",  # Maiani
        "gta",  # Guató
        "pog",  # Potiguára
        "mzf",  # Aiku
        "prp",  # Parsi
        "dee",  # Dewoin
        "bse",  # Wushi
        "anu",  # Anuak
        "bln",  # Southern Catanduanes Bikol
        "xop",  # Kopar
        "mqe",  # Matepi
        "acx",  # Omani Arabic
        "kwm",  # Kwambi
        "okm",  # Middle Korean (10th-16th cent.)
        "mvr",  # Marau
        "ywr",  # Yawuru
        "mzy",  # Mozambican Sign Language
        "nep",  # Nepali (macrolanguage)
        "bvb",  # Bube
        "xyb",  # Yandjibara
        "mco",  # Coatlán Mixe
        "dbm",  # Duguri
        "erw",  # Erokwanas
        "psc",  # Iranian Sign Language
        "pku",  # Paku
        "msy",  # Aruamu
        "sls",  # Singapore Sign Language
        "rbk",  # Northern Bontok
        "mej",  # Meyah
        "plr",  # Palaka Senoufo
        "mqc",  # Mangole
        "nll",  # Nihali
        "dgb",  # Bunoge Dogon
        "nyf",  # Giryama
        "mxm",  # Meramera
        "bsl",  # Basa-Gumna
        "tis",  # Masadiit Itneg
        "nnl",  # Northern Rengma Naga
        "jum",  # Jumjum
        "kic",  # Kickapoo
        "lsi",  # Lashi
        "yag",  # Yámana
        "hna",  # Mina (Cameroon)
        "mbc",  # Macushi
        "bwf",  # Boselewa
        "cpy",  # South Ucayali Ashéninka
        "lah",  # Lahnda
        "xgm",  # Dharumbal
        "erk",  # South Efate
        "ccx",  # Northern Zhuang
        "jal",  # Yalahatan
        "lok",  # Loko
        "ekl",  # Kol (Bangladesh)
        "gyz",  # Geji
        "cbk",  # Chavacano
        "aag",  # Ambrak
        "mxw",  # Namo
        "myr",  # Muniche
        "sas",  # Sasak
        "tta",  # Tutelo
        "wbw",  # Woi
        "pow",  # San Felipe Otlaltepec Popoloca
        "gbo",  # Northern Grebo
        "ywa",  # Kalou
        "zmm",  # Marimanindji
        "mbw",  # Maring
        "kzk",  # Kazukuru
        "sdg",  # Savi
        "pfe",  # Pere
        "hot",  # Hote
        "ksc",  # Southern Kalinga
        "ael",  # Ambele
        "igl",  # Igala
        "hac",  # Gurani
        "vnp",  # Vunapu
        "pgy",  # Pongyong
        "lor",  # Téén
        "czk",  # Knaanic
        "tpa",  # Taupota
        "soy",  # Miyobe
        "aau",  # Abau
        "rxd",  # Ngardi
        "tco",  # Taungyo
        "sdh",  # Southern Kurdish
        "ygu",  # Yugul
        "gdm",  # Laal
        "vah",  # Varhadi-Nagpuri
        "saq",  # Samburu
        "aza",  # Azha
        "tmg",  # Ternateño
        "xan",  # Xamtanga
        "lur",  # Laura
        "bfq",  # Badaga
        "oci",  # Occitan (post 1500)
        "ysc",  # Yassic
        "rwr",  # Marwari (India)
        "sor",  # Somrai
        "kpa",  # Kutto
        "yle",  # Yele
        "bxc",  # Molengue
        "tyn",  # Kombai
        "tzs",  # San Andrés Larrainzar Tzotzil
        "tuh",  # Taulil
        "olo",  # Livvi
        "tsy",  # Tebul Sign Language
        "njb",  # Nocte Naga
        "nli",  # Grangali
        "krr",  # Krung
        "biv",  # Southern Birifor
        "lut",  # Lushootseed
        "osi",  # Osing
        "xor",  # Korubo
        "jku",  # Labir
        "biq",  # Bipi
        "nie",  # Niellim
        "maf",  # Mafa
        "gip",  # Gimi (West New Britain)
        "dmr",  # East Damar
        "btl",  # Bhatola
        "gol",  # Gola
        "aao",  # Algerian Saharan Arabic
        "mka",  # Mbre
        "amh",  # Amharic
        "gwa",  # Mbato
        "miq",  # Mískito
        "ibb",  # Ibibio
        "fqs",  # Fas
        "jie",  # Jilbe
        "olu",  # Kuvale
        "nag",  # Naga Pidgin
        "usu",  # Uya
        "mtt",  # Mota
        "chm",  # Mari (Russia)
        "lkc",  # Kucong
        "hti",  # Hoti
        "tkn",  # Toku-No-Shima
        "guo",  # Guayabero
        "pes",  # Iranian Persian
        "meb",  # Ikobi
        "dmd",  # Madhi Madhi
        "tgd",  # Ciwogai
        "sly",  # Selayar
        "sqm",  # Suma
        "gos",  # Gronings
        "qxo",  # Southern Conchucos Ancash Quechua
        "sli",  # Lower Silesian
        "pca",  # Santa Inés Ahuatempan Popoloca
        "biz",  # Baloi
        "tsr",  # Akei
        "shy",  # Tachawit
        "ovd",  # Elfdalian
        "akd",  # Ukpet-Ehom
        "nna",  # Nyangumarta
        "kyb",  # Butbut Kalinga
        "fli",  # Fali
        "kui",  # Kuikúro-Kalapálo
        "djf",  # Djangun
        "azg",  # San Pedro Amuzgos Amuzgo
        "hbs",  # Serbo-Croatian
        "ike",  # Eastern Canadian Inuktitut
        "dol",  # Doso
        "nuh",  # Ndunda
        "bzh",  # Mapos Buang
        "now",  # Nyambo
        "mry",  # Mandaya
        "myu",  # Mundurukú
        "nuy",  # Nunggubuyu
        "dib",  # South Central Dinka
        "tka",  # Truká
        "rtw",  # Rathawi
        "xsv",  # Sudovian
        "slp",  # Lamaholot
        "gwi",  # Gwichʼin
        "agm",  # Angaataha
        "mer",  # Meru
        "shv",  # Shehri
        "vmo",  # Muko-Muko
        "igw",  # Igwe
        "sll",  # Salt-Yui
        "weu",  # Rawngtu Chin
        "cen",  # Cen
        "nyq",  # Nayini
        "lkr",  # Päri
        "klj",  # Khalaj
        "phl",  # Phalura
        "mlp",  # Bargam
        "rus",  # Russian
        "msg",  # Moraid
        "gbr",  # Gbagyi
        "jls",  # Jamaican Sign Language
        "frc",  # Cajun French
        "bpp",  # Kaure
        "bsk",  # Burushaski
        "kvj",  # Psikye
        "nuu",  # Ngbundu
        "ccp",  # Chakma
        "zpb",  # Yautepec Zapotec
        "mgy",  # Mbunga
        "abv",  # Baharna Arabic
        "lcp",  # Western Lawa
        "nbr",  # Numana
        "ahs",  # Ashe
        "dbq",  # Daba
        "kqq",  # Krenak
        "kng",  # Koongo
        "sip",  # Sikkimese
        "kce",  # Kaivi
        "nuq",  # Nukumanu
        "apl",  # Lipan Apache
        "ama",  # Amanayé
        "stm",  # Setaman
        "cfm",  # Falam Chin
        "mjq",  # Malaryan
        "mvg",  # Yucuañe Mixtec
        "frs",  # Eastern Frisian
        "mec",  # Marra
        "muj",  # Mabire
        "gsc",  # Gascon
        "llh",  # Lamu
        "tgo",  # Sudest
        "frm",  # Middle French (ca. 1400-1600)
        "alo",  # Larike-Wakasihu
        "emx",  # Erromintxela
        "ikv",  # Iku-Gora-Ankwa
        "xiy",  # Xipaya
        "kov",  # Kudu-Camo
        "pif",  # Pingelapese
        "pal",  # Pahlavi
        "pbe",  # Mezontla Popoloca
        "chu",  # Church Slavic
        "liw",  # Col
        "hoh",  # Hobyót
        "bnq",  # Bantik
        "xky",  # Uma' Lasan
        "but",  # Bungain
        "dcc",  # Deccan
        "ttv",  # Titan
        "bfl",  # Banda-Ndélé
        "mwj",  # Maligo
        "lbv",  # Lavatbura-Lamusong
        "rao",  # Rao
        "enb",  # Markweeta
        "msd",  # Yucatec Maya Sign Language
        "squ",  # Squamish
        "gzi",  # Gazi
        "ser",  # Serrano
        "nsg",  # Ngasa
        "qxw",  # Jauja Wanca Quechua
        "cjp",  # Cabécar
        "mxu",  # Mada (Cameroon)
        "mqy",  # Manggarai
        "hnh",  # ǁAni
        "bdj",  # Bai (South Sudan)
        "lox",  # Loun
        "zyp",  # Zyphe Chin
        "kxf",  # Manumanaw Karen
        "zae",  # Yareni Zapotec
        "kdi",  # Kumam
        "nks",  # North Asmat
        "por",  # Portuguese
        "spk",  # Sengo
        "wiy",  # Wiyot
        "gwd",  # Gawwada
        "plo",  # Oluta Popoluca
        "ndy",  # Lutos
        "mfx",  # Melo
        "xmy",  # Mayaguduna
        "mtz",  # Tacanec
        "xaq",  # Aquitanian
        "arh",  # Arhuaco
        "rmz",  # Marma
        "hil",  # Hiligaynon
        "scg",  # Sanggau
        "tyl",  # Thu Lao
        "stu",  # Samtao
        "yba",  # Yala
        "zdj",  # Ngazidja Comorian
        "dwr",  # Dawro
        "pci",  # Duruwa
        "bao",  # Waimaha
        "nhq",  # Huaxcaleca Nahuatl
        "xhm",  # Middle Khmer (1400 to 1850 CE)
        "lbf",  # Tinani
        "myv",  # Erzya
        "iwk",  # I-Wak
        "scu",  # Shumcho
        "awr",  # Awera
        "ekg",  # Ekari
        "tsq",  # Thai Sign Language
        "kjq",  # Western Keres
        "ist",  # Istriot
        "mfh",  # Matal
        "hmi",  # Northern Huishui Hmong
        "xli",  # Liburnian
        "fri",  # Western Frisian
        "tuf",  # Central Tunebo
        "arw",  # Arawak
        "mnb",  # Muna
        "ign",  # Ignaciano
        "xba",  # Kamba (Brazil)
        "bob",  # Aweer
        "knl",  # Keninjal
        "hup",  # Hupa
        "bbd",  # Bau
        "tly",  # Talysh
        "gvm",  # Gurmana
        "igo",  # Isebe
        "hrm",  # Horned Miao
        "xjb",  # Minjungbal
        "smn",  # Inari Sami
        "bap",  # Bantawa
        "kla",  # Klamath-Modoc
        "bvu",  # Bukit Malay
        "pia",  # Pima Bajo
        "auu",  # Auye
        "nmt",  # Namonuito
        "aud",  # Anuta
        "cae",  # Lehar
        "dih",  # Kumiai
        "gei",  # Gebe
        "org",  # Oring
        "ysn",  # Sani
        "kgc",  # Kasseng
        "ndz",  # Ndogo
        "fiw",  # Fiwaga
        "crw",  # Chrau
        "mbi",  # Ilianen Manobo
        "dym",  # Yanda Dom Dogon
        "nen",  # Nengone
        "etz",  # Semimi
        "kld",  # Gamilaraay
        "mij",  # Abar
        "afi",  # Akrukay
        "aty",  # Aneityum
        "sua",  # Sulka
        "zra",  # Kara (Korea)
        "tzz",  # Zinacantán Tzotzil
        "pna",  # Punan Bah-Biau
        "cch",  # Atsam
        "kuz",  # Kunza
        "kzs",  # Sugut Dusun
        "mvd",  # Mamboru
        "omk",  # Omok
        "app",  # Apma
        "muo",  # Nyong
        "nhv",  # Temascaltepec Nahuatl
        "zkb",  # Koibal
        "dyd",  # Dyugun
        "mgw",  # Matumbi
        "bfs",  # Southern Bai
        "nix",  # Hema
        "wlm",  # Middle Welsh
        "wab",  # Wab
        "tga",  # Sagalla
        "qwt",  # Kwalhioqua-Tlatskanai
        "rut",  # Rutul
        "mhl",  # Mauwake
        "ldk",  # Leelau
        "hro",  # Haroi
        "hoy",  # Holiya
        "tng",  # Tobanga
        "mpo",  # Miu
        "bdk",  # Budukh
        "mmj",  # Majhwar
        "kaf",  # Katso
        "knw",  # Kung-Ekoka
        "kcl",  # Kela (Papua New Guinea)
        "pld",  # Polari
        "yer",  # Tarok
        "krk",  # Kerek
        "amc",  # Amahuaca
        "hig",  # Kamwe
        "abj",  # Aka-Bea
        "gld",  # Nanai
        "mfw",  # Mulaha
        "agy",  # Southern Alta
        "sjs",  # Senhaja De Srair
        "uji",  # Tanjijili
        "tle",  # Southern Marakwet
        "kjs",  # East Kewa
        "num",  # Niuafo'ou
        "tbz",  # Ditammari
        "noj",  # Nonuya
        "quv",  # Sacapulteco
        "lof",  # Logol
        "dbp",  # Duwai
        "kse",  # Kuni
        "brv",  # Western Bru
        "rmk",  # Romkun
        "kal",  # Kalaallisut
        "tot",  # Patla-Chicontla Totonac
        "bje",  # Biao-Jiao Mien
        "gej",  # Gen
        "tey",  # Tulishi
        "kvm",  # Kendem
        "yun",  # Bena (Nigeria)
        "yat",  # Yambeta
        "okd",  # Okodia
        "tys",  # Tày Sa Pa
        "cgg",  # Chiga
        "kmb",  # Kimbundu
        "pnm",  # Punan Batu 1
        "seo",  # Suarmin
        "mqs",  # West Makian
        "noy",  # Noy
        "lmz",  # Lumbee
        "gnj",  # Ngen
        "pls",  # San Marcos Tlacoyalco Popoloca
        "vif",  # Vili
        "kou",  # Koke
        "sot",  # Southern Sotho
        "bps",  # Sarangani Blaan
        "pih",  # Pitcairn-Norfolk
        "knx",  # Kendayan
        "coh",  # Chonyi-Dzihana-Kauma
        "gba",  # Gbaya (Central African Republic)
        "pao",  # Northern Paiute
        "ldl",  # Kaan
        "sme",  # Northern Sami
        "tkz",  # Takua
        "trp",  # Kok Borok
        "mpg",  # Marba
        "mjm",  # Medebur
        "bbp",  # West Central Banda
        "gwn",  # Gwandara
        "taq",  # Tamasheq
        "ned",  # Nde-Gbite
        "gww",  # Kwini
        "roo",  # Rotokas
        "mad",  # Madurese
        "cjn",  # Chenapian
        "ayr",  # Central Aymara
        "pmm",  # Pomo
        "xsr",  # Sherpa
        "bxj",  # Bayungu
        "zmq",  # Mituku
        "agz",  # Mt. Iriga Agta
        "hlt",  # Matu Chin
        "bac",  # Badui
        "lmr",  # Lamalera
        "xlc",  # Lycian
        "gek",  # Ywom
        "bvg",  # Bonkeng
        "fnb",  # Fanbak
        "rmb",  # Rembarrnga
        "rwk",  # Rwa
        "bwh",  # Bishuo
        "rin",  # Nungu
        "agh",  # Ngelima
        "tvy",  # Timor Pidgin
        "xmt",  # Matbat
        "cll",  # Chala
        "ors",  # Orang Seletar
        "kyk",  # Kamayo
        "swh",  # Swahili (individual language)
        "dao",  # Daai Chin
        "gve",  # Duwet
        "ybh",  # Yakha
        "rmg",  # Traveller Norwegian
        "qui",  # Quileute
        "atw",  # Atsugewi
        "bby",  # Befang
        "ksh",  # Kölsch
        "ajs",  # Algerian Jewish Sign Language
        "wlc",  # Mwali Comorian
        "obu",  # Obulom
        "bdo",  # Morom
        "fuh",  # Western Niger Fulfulde
        "agj",  # Argobba
        "nzm",  # Zeme Naga
        "xkx",  # Karore
        "bfw",  # Bondo
        "lcd",  # Lola
        "keo",  # Kakwa
        "omt",  # Omotik
        "lre",  # Laurentian
        "bqo",  # Balo
        "ksx",  # Kedang
        "cog",  # Chong
        "sok",  # Sokoro
        "tpr",  # Tuparí
        "peh",  # Bonan
        "xmb",  # Mbonga
        "zga",  # Kinga
        "alh",  # Alawa
        "tra",  # Tirahi
        "uve",  # West Uvean
        "ttl",  # Totela
        "ifm",  # Teke-Fuumu
        "ycr",  # Yilan Creole
        "rka",  # Kraol
        "pox",  # Polabian
        "bvk",  # Bukat
        "ncq",  # Northern Katang
        "lev",  # Lamma
        "yra",  # Yerakai
        "anz",  # Anem
        "snx",  # Sam
        "krt",  # Tumari Kanuri
        "cut",  # Teutila Cuicatec
        "bie",  # Bepour
        "yne",  # Lang'e
        "bbv",  # Karnai
        "rir",  # Ribun
        "yif",  # Ache
        "osn",  # Old Sundanese
        "mtf",  # Murik (Papua New Guinea)
        "orr",  # Oruma
        "bmx",  # Baimak
        "wwo",  # Wetamut
        "lej",  # Lengola
        "bew",  # Betawi
        "xpl",  # Port Sorell Tasmanian
        "aqk",  # Aninka
        "wrn",  # Warnang
        "cdh",  # Chambeali
        "cja",  # Western Cham
        "kpi",  # Kofei
        "pof",  # Poke
        "bwu",  # Buli (Ghana)
        "mvb",  # Mattole
        "nwm",  # Nyamusa-Molo
        "pty",  # Pathiya
        "ans",  # Anserma
        "bbz",  # Babalia Creole Arabic
        "gop",  # Yeretuar
        "xpn",  # Kapinawá
        "kpm",  # Koho
        "mtw",  # Southern Binukidnon
        "mji",  # Kim Mun
        "kcc",  # Lubila
        "mey",  # Hassaniyya
        "bzg",  # Babuza
        "luk",  # Lunanakha
        "mic",  # Mi'kmaq
        "mfn",  # Cross River Mbembe
        "lrv",  # Larevat
        "lax",  # Tiwa
        "kzi",  # Kelabit
        "zor",  # Rayón Zoque
        "pep",  # Kunja
        "skm",  # Kutong
        "etc",  # Etchemin
        "kti",  # North Muyu
        "cna",  # Changthang
        "xgg",  # Goreng
        "bgs",  # Tagabawa
        "sju",  # Ume Sami
        "sqo",  # Sorkhei
        "kgd",  # Kataang
        "spg",  # Sian
        "nji",  # Gudanji
        "sbd",  # Southern Samo
        "mov",  # Mohave
        "lbz",  # Lardil
        "kog",  # Cogui
        "srx",  # Sirmauri
        "ckq",  # Kajakse
        "mnx",  # Manikion
        "uma",  # Umatilla
        "vgr",  # Vaghri
        "nmi",  # Nyam
        "quq",  # Quinqui
        "msz",  # Momare
        "obr",  # Old Burmese
        "mqw",  # Murupi
        "err",  # Erre
        "tmj",  # Samarokena
        "mak",  # Makasar
        "sti",  # Bulo Stieng
        "mbj",  # Nadëb
        "sjb",  # Sajau Basap
        "isa",  # Isabi
        "emm",  # Mamulique
        "mqm",  # South Marquesan
        "hvn",  # Sabu
        "ukq",  # Ukwa
        "puq",  # Puquina
        "wdt",  # Wendat
        "adb",  # Atauran
        "cet",  # Centúúm
        "ndv",  # Ndut
        "alx",  # Amol
        "tgi",  # Lawunuia
        "gun",  # Mbyá Guaraní
        "eve",  # Even
        "tpm",  # Tampulma
        "pua",  # Western Highland Purepecha
        "nci",  # Classical Nahuatl
        "grx",  # Guriaso
        "gbf",  # Gaikundi
        "jmd",  # Yamdena
        "biw",  # Kol (Cameroon)
        "ppk",  # Uma
        "jic",  # Tol
        "wla",  # Walio
        "uku",  # Ukue
        "tzu",  # Huixtán Tzotzil
        "bbi",  # Barombi
        "koz",  # Korak
        "hrw",  # Warwar Feni
        "trj",  # Toram
        "ccg",  # Samba Daka
        "hch",  # Huichol
        "gdc",  # Gugu Badhun
        "uiv",  # Iyive
        "bts",  # Batak Simalungun
        "tsi",  # Tsimshian
        "dap",  # Nisi (India)
        "ail",  # Aimele
        "mgn",  # Mbangi
        "hka",  # Kahe
        "mmv",  # Miriti
        "lan",  # Laru
        "jad",  # Jahanka
        "wli",  # Waioli
        "bgq",  # Bagri
        "bem",  # Bemba (Zambia)
        "awt",  # Araweté
        "dbo",  # Dulbu
        "der",  # Deori
        "ply",  # Bolyu
        "txt",  # Citak
        "jua",  # Júma
        "xgb",  # Gbin
        "tgf",  # Chalikha
        "oks",  # Oko-Eni-Osayen
        "ilo",  # Iloko
        "mpm",  # Yosondúa Mixtec
        "ltu",  # Latu
        "zir",  # Ziriya
        "cda",  # Choni
        "bxp",  # Bebil
        "gnb",  # Gangte
        "sfb",  # Langue des signes de Belgique Francophone
        "tbw",  # Tagbanwa
        "auh",  # Aushi
        "kfj",  # Kemiehua
        "bdr",  # West Coast Bajau
    ]
)
