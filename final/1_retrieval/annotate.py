
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#Classifying keywords/hashtags into categories
hillaryPositive = ["hillary2016","imwithher","clinton2016", "hilaryclinton","hilary2016","billclinton"]
hillaryNegative = ["fuckhilary","notwithher","whichhillary","releasethetranscripts"]
berniePositive = ["feelthebern", "stillsanders", "berniesanders2016", "berniesanders", "berniesandersforpresident", "voteforbernie","canadiansforbernie", "bernie2016"]
bernieNegative = []
trumpPositive = ["donaldtrump","trump2016","trumptrain","trumprally","mrtrump","letsmakeamericagreatagain","presidenttrump","makeamericagreatagain","trumpforpresident","alwaystrump"]
trumpNegative = ["makeamericahateagain","drumpf","makedonalddrumpfagain","dumptrump","fucktrump","trumpisachump"]
cruzPositive = ["tedcruz", "cruz2016","cruztovictory","cruzcrew"]
cruzNegative = []
gopNeutral = ["republicans","conservatives""republican","gop","republicanparty", "cruz", "trump"]
demNeutral = ["democrats", "bernie","hillary"]
neutral = ["presidentialelection","demdebate","gopdebate","aipac2016","2016presidentialelection","presidentialelection2016"]

file_names = ["rawdata.csv"]
out_file_name = "../2_learn_classify/annotated.csv"

#Getting sentiment for tags
def getValue(tag, positiveTags, negativeTags):
    if tag in positiveTags:
        return "1"
    elif tag in negativeTags:
        return "-1"
    return "0"

#Getting name for tags
def getName(tag):
    if tag in hillaryPositive:
        return "hillaryPositive"
    elif tag in hillaryNegative:
        return "hillaryNegative"
    elif tag in berniePositive:
        return "berniePositive"
    elif tag in bernieNegative:
        return "bernieNegative"
    elif tag in trumpPositive:
        return "trumpPositive"
    elif tag in trumpNegative:
        return "trumpNegative"
    elif tag in cruzPositive:
        return "cruzPositive"
    elif tag in cruzNegative:
        return "cruzNegative"
    elif tag in gopNeutral:
        return "gopNeutral"
    elif tag in demNeutral:
        return "demNeutral"
    
    return "neutral"

#Read file
fh = open(out_file_name, 'w')
fileKey = []

for file_name in file_names:
    with open(file_name) as f:
        content = f.readlines()

    for line in content:
        parts = line.split(",")
        key = parts[4] + "-" + getName(parts[1])
        if key not in fileKey:
            fh.write(parts[0] + "," + parts[1] + "," + parts[2] + "," + parts[3] + "," + parts[4] + "," + parts[5] + "," + getValue(parts[1], hillaryPositive, hillaryNegative) + "," + getValue(parts[1], berniePositive, bernieNegative) + "," + getValue(parts[1], trumpPositive, trumpNegative) + "," + getValue(parts[1], cruzPositive, cruzNegative) + "," + getValue(parts[1], gopNeutral, []) + "," + getValue(parts[1], demNeutral, []) + "," + (str(("#" + parts[1]) in ' '.join(parts[12:]).lower())) + "," + getName(parts[1]) + "," + ' '.join(parts[12:]))
            #fileKey.append(parts[4] + "-" + getName(parts[1]))
        else:
            fh.write(parts[0] + "," + parts[1] + "," + parts[2] + "," + parts[3] + "," + parts[4] + "," + parts[5] + "," + getValue(parts[1], hillaryPositive, hillaryNegative) + "," + getValue(parts[1], berniePositive, bernieNegative) + "," + getValue(parts[1], trumpPositive, trumpNegative) + "," + getValue(parts[1], cruzPositive, cruzNegative) + "," + getValue(parts[1], gopNeutral, []) + "," + getValue(parts[1], demNeutral, []) + "," + (str(("#" + parts[1]) in ' '.join(parts[12:]).lower())) + "," + getName(parts[1]) + "," + ' '.join(parts[12:]))

fh.close
