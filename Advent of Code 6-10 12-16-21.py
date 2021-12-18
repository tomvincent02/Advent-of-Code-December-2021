#Day 6 LanternFish

import math

lanternfish = [3,5,2,5,4,3,2,2,3,5,2,3,2,2,2,2,3,5,3,5,5,2,2,3,4,2,3,5,5,3,3,5,2,4,
                        5,4,3,5,3,2,5,4,1,1,1,5,1,4,1,4,3,5,2,3,2,2,2,5,2,1,2,2,2,2,3,4,5,2,
                        5,4,1,3,1,5,5,5,3,5,3,1,5,4,2,5,3,3,5,5,5,3,2,2,1,1,3,2,1,2,2,4,3,4,1,
                        3,4,1,2,2,4,1,3,1,4,3,3,1,2,3,1,3,4,1,1,2,5,1,2,1,2,4,1,3,2,1,1,2,4,3,5,
                        1,3,2,1,3,2,3,4,5,5,4,1,3,4,1,2,3,5,2,3,5,2,1,1,5,5,4,4,4,5,3,3,2,5,4,4,1,
                        5,1,5,5,5,2,2,1,2,4,5,1,2,1,4,5,4,2,4,3,2,5,2,2,1,4,3,5,4,2,1,1,5,1,4,5,1,2,
                        5,5,1,4,1,1,4,5,2,5,3,1,4,5,2,1,3,1,3,3,5,5,1,4,1,3,2,2,3,5,4,3,2,5,1,1,1,2,2,5,
                        3,4,2,1,3,2,5,3,2,2,3,5,2,1,4,5,4,4,5,5,3,3,5,4,5,5,4,3,5,3,5,3,1,3,2,2,1,4,4,5,
                        2,2,4,2,1,4]
print(len(lanternfish))

def fish_count(input_days, number_of_lanternfish):
    days = 0
    first_gen_fish = []
    while days != input_days:
        for fish in number_of_lanternfish:
            if fish == 0:
                first_gen_fish.append(8)
                fish = 6
            else:
                fish -= 1
        if len(first_gen_fish) != 0:
            for babies in first_gen_fish:
                if babies == 0:
                    first_gen_fish.pop(babies)
                    number_of_lanternfish.append(6)
                    first_gen_fish(8)
                else:
                    babies -= 1
        days += 1
    return len(first_gen_fish) + len(number_of_lanternfish)

print(fish_count(80, lanternfish))

#day #7 The treachery of Whales

crab_position = '1101,1,29,67,1102,0,1,65,1008,65,35,66,1005,66,28,1,67,65,20,4,0,1001,65,1,65,1106,0,8,99,35,' \
                '67,101,99,105,32,110,39,101,115,116,32,112,97,115,32,117,110,101,32,105,110,116,99,111,100,101,32,112,' \
                '114,111,103,114,97,109,10,106,684,36,657,427,156,197,56,205,1104,170,307,291,88,330,12,24,1128,440,1099,' \
                '1523,936,198,266,1257,874,196,912,335,46,320,666,132,1035,145,877,1484,222,690,479,386,59,101,765,506,' \
                '27,250,478,609,807,1566,317,138,1390,245,1178,211,64,714,510,256,430,371,182,464,398,1749,57,1023,4,891,' \
                '1177,459,171,236,1,34,106,744,1766,51,8,256,571,290,462,852,56,372,612,2,688,33,452,1182,739,696,123,469,' \
                '583,77,40,191,416,1470,1153,459,848,228,677,1203,8,70,1302,207,21,913,9,855,47,81,188,354,700,1169,1199,' \
                '620,197,41,138,1825,466,387,1124,595,457,1231,3,61,292,120,98,846,893,97,142,673,429,797,139,193,83,586,' \
                '1726,201,365,415,63,525,277,335,1347,304,995,378,1884,185,331,69,351,134,972,262,208,21,108,1385,143,264,' \
                '287,625,657,90,345,578,569,280,604,335,453,773,39,79,13,431,245,760,433,167,608,409,655,796,611,45,1167,312,' \
                '439,1106,420,365,431,169,147,567,20,401,699,356,56,35,1233,975,105,29,787,618,404,179,469,284,304,140,50,' \
                '283,774,957,455,1651,1,308,936,502,313,218,62,51,1,255,224,64,299,546,4,23,100,868,641,331,1810,399,272,105,' \
                '156,1031,894,783,775,1823,211,209,1375,64,897,1083,367,14,516,311,86,50,716,1671,515,755,83,490,386,1015,' \
                '359,620,192,921,1257,606,853,1196,1304,92,1442,89,33,689,832,139,308,140,424,300,97,67,1102,138,1166,753,' \
                '53,274,236,245,567,205,368,1108,253,893,151,211,736,194,779,344,152,533,869,849,259,794,93,1092,301,51,' \
                '350,909,499,349,242,1014,55,813,613,75,211,1039,1310,626,1440,381,904,25,1625,491,54,584,465,79,1146,' \
                '60,476,476,111,1350,721,283,1102,276,41,1111,221,890,223,639,571,346,150,399,400,140,720,0,196,128,' \
                '1125,610,339,1034,490,979,1328,32,505,567,92,76,377,239,62,12,19,1265,857,182,781,834,682,802,201,313,' \
                '20,165,71,21,108,961,1190,1257,434,1223,208,488,93,19,96,29,205,264,1586,142,818,569,42,79,475,42,1079,303,' \
                '117,1569,4,422,750,142,454,116,3,1628,933,1408,274,200,393,544,717,382,65,53,522,71,842,971,1288,128,590,' \
                '46,882,1568,811,134,23,6,562,450,43,821,96,12,771,23,232,720,134,188,1394,4,1365,134,44,1896,1,194,83,474,' \
                '101,11,429,309,825,80,322,295,1009,142,198,58,13,647,334,382,334,1364,106,206,479,282,683,379,86,381,1407,' \
                '146,1470,93,465,588,110,750,1118,744,171,103,594,79,1075,0,501,63,792,293,18,1316,1510,143,406,344,453,28,' \
                '341,178,11,76,1366,1085,32,1536,1722,190,17,378,166,531,818,921,211,130,171,689,170,478,278,587,335,135,652,' \
                '41,155,715,109,144,867,847,1072,335,537,50,94,168,51,327,78,182,372,115,70,798,473,470,523,271,1028,1048,' \
                '607,469,40,91,1064,209,1759,38,994,781,602,80,31,387,356,494,373,44,10,379,62,174,96,1628,875,911,6,692,502,' \
                '161,329,595,368,1697,42,179,987,65,1091,343,657,84,184,98,926,208,728,698,269,165,99,856,410,167,339,884,258,' \
                '502,50,158,252,331,1653,107,32,382,1140,105,19,1433,32,827,5,826,1,1000,95,562,153,431,158,550,39,294,91,95,' \
                '165,8,51,243,1087,1290,597,688,839,332,61,41,321,11,217,150,1282,596,577,590,398,383,1875,88,111,1357,315,28,' \
                '1344,179,1072,161,613,393,222,421,492,445,1090,234,154,78,440,856,492,1517,351,1162,48,220,8,72,597,350,127,' \
                '562,1510,488,177,547,32,82,111,47,0,137,264,14,327,46,908,505,518,30,866,16,315,58,708,1776,233,604,1364,630,' \
                '215,1684,1949,628,118,626,33,150,4,1183,533,50,501,942,43,345,52,473,684,69,608,32,38,992,6,751,1106,523,93,' \
                '418,297,608,378,1846,32,597,1341,89,412,552,265,143,164,113,48,1181,1352,1066,1128,686,670,639,159,177,120,' \
                '761,632,129,7,1098,623,2,442,276,595,39,314,959,114,1990,235,1025,50,1547,196,23,476,822,365,430,31,759,2,' \
                '95,27,615,395,814,131,63,79,503,248,261,40,369,1673,53,130,910,573,28,237,1073,133,107,509,222,1517,441,528,' \
                '727,408,234,216,549,7,345,1557,1194,372,271,219,268,243,478,253,2,209,278,1200,1272,779,8,161,417,263,131,' \
                '798,791,58,566,464,1109,370,448,1166,452,1248,379,848,1212,280,444,139,145'
new_crab = list(crab_position.split(','))
print(new_crab)
final_crab = []
for each in new_crab:
    final_crab.append(int(each))
print(final_crab)
count = 0
for position in final_crab:
    count += position
number_of_crab = len(final_crab)
print(number_of_crab)
print(count)
print(count / number_of_crab)
def distance_from_input(lst):
    horizontal_distance = 0
    for crab in lst:
        median = 461
        if crab >= median:
            horizontal_distance += (crab - median)
            print(horizontal_distance)
        else:
            horizontal_distance += (median - crab)
    return horizontal_distance

marc = [400,501,400]
print(int(distance_from_input(marc)))

#final question
#def single_palindrome(possible):
#    for idx in range(0,len(possible)-1, 1):
#        if len(possible) > 1 or 2:
#            if possible[0] == possible[idx] and len(possible) < 5:
#                return single_palindrome(possible[1:idx])
#            else:
#                continue
#        else:
#            if len(possible) == 1:
#                return True
#            elif len(possible) == 2:
#                if possible[0] == possible[-1]:
#                    return True
#            else:
#                return False
#print(single_palindrome([1,2,1]))

#Day 8
#Seven Segment Search
input = 'bafdec cgefd gcebd ebcgd gdea bgefdc bea efdbg befda daefb egf gcdfa fbdac gd gdbcaf dgb abcdfeg febdg ae daebf gfea bfdea gbdef fcdebg ebfcdg gcade cfegdb dcg fadgcbe ecadg bgefad fag feba abdcge becagdf bagefdc bafec ebf afdce egadfc gcbaef cdfeg efgacb gaecb efbca cdgae daebcg geafdc gdfab ge gcbdfa badfg dbegc dfbeac cafgbe db gafec aebdcgf agdbfe cfega ab bacde ba decgaf dgb gbcefad dbg bdagef dgcba abegd bdacg begda agfbe ebcgd dagcbe egbda acfeb fag dcgae acfbgd fdgcae cfgdea edfcab cefad fgb fegdba fbaedc aefcdb bcfead fgbcea eb aefdb acdbge bfacde bgade cedabf dfeg daebf dcbfga gf abgcf aegbfdc bedacgf edgabc da fcgad gdbfc afgbce dfgebc cbd fcbad cdae ecbgaf bgafecd cbea gacbdf adfegbc gcafbe fcbgae adecb gc acg dcafe begad cgfa dbagcf fcag fagc abfdc ebfagc agbdf dcfegba deafgc fabce da gbcdef bfedca gdcbf daceb ebgdfa cgfb edbfa dbagf gbd gfead ba gbac egbdc abd bd gebcadf dafcg bc cb fgdabc bc cfgbe egdafc fbgdec cbfea begda bc decab defcga dgfecba cgeb bfdecg aedbfg bgfaedc afbcg efdgc cgfeb abgde bgdae daefg cfbagd cefb dafce dcebaf edgcafb fdbgec faegd eafgd gbf dcfbea debcf gdefc gdc cfdbg dbfgc fcdegb debcga gfbcd ebagdc dabfgc dfbgc gfbdac dbgca edacfb dfeagb dgcfabe aceb edgcaf afdgeb gfcbad feadc fcead gcafd fcaeb dgcefa facedg bdgf ecfadg cgdb bcdg gcfead cadbg dacbg cbadg bagcef gefa abcef dbfcga fbeca ecgdbf gedcfa gdcef gcdef  aegdc bcgad dcgfe fedacb ebdcfa ecbfa fcb cbagde gafec gfdeb fadbcge dcegbf fbgcda bgcad faceb eagdcf cegda bd cgeda bd abgcfd cfgbad cgeabfd dfcga ebacf ab gdafbc cgfeab agfdc gefcadb gdfba gfcdbea bagedcf gebca fcadg gbd efbcd fegcda bfdacge fgcbd abf fba bdgaf fagbdc cfd dc bdgcf gcebf agfdc bda dab dbacfe gfeda deacgf ecgfda deagb ceafbg adgcf gdecb bf degfa cdaf aed bacdeg dcfabg dacgeb debc dcfbga cdefg fcebag ebdfca fcbega fedcab fabge agbefd fcdbae adgfce cfbd cdfage fgacde cgaebf beagfd cbgae efagbd dcefa agdce ga abge gaecfbd adbc fdcgeb adcb aecgbd dgcfb gcbaef bdfgc agdebc bfegdc dcafe debfgca fbed bgd db dfcbge dfbage deg efbadg fagceb cfgdeba dgbcf cedfab cbf feabd fdegb dbafe bfead ceba afcdg ecfbagd efbgac eafgd cbgd fagde edafg abefc cbfadg bcdfe cdeg dgefbc bfd db dacb bgcfe fgaedc cd dfgaeb abgdc bde deb bcadgef fcgbde cegfdb fdecga degfc gecabf dcgf fbc cdgf acgebf bdfaec adb agecbd dcebf afebdg adcfbeg gbefdc cedgb gebdc cefgad aegcb fgadce daegfc de eagbf fbcga dgecaf fce cbea degcfab dfaecg gdafbc ecafdg bdcga dfgca dagcb cfabgd gdbcfe decgf efdgc gd fgdcbae dbgfae bgdaef edgaf adgfb dbgaf fcedab dba dbcfga badcf aedcf bagdfc degacf egdb ebadf dfbeagc dcfgbe egdabfc cfg fdega bcd fdcbeg gedcfab gcdabf dcbfge fadceb cdegf befacdg dabfg eafbcd bgcda aefcbd dfebc cfdbag ebcfd aebf bagce dac gbcfad adfbe dgcbe beg adbec bfadce fdca agfbc fadbeg gefbca ecbad fbgced bcfdg fde fdgeabc bedgca ebdgca bdegc fdcgb bcefdg gdbcf acf gfaecdb gbfca fgc gebfa cbedfg ecad cd cgaef bcdfg caed ad cbgfd fdcab fegcab bdeaf bc dea cbdfe bage ea dbgfcea cbead gbfcea geadcfb baecgd acfgb adebgc fbdcega cgebaf fegacb efcagb ebafcg bedcafg eacgf gfdace gbf caged dfaecb gbef ecgbfad adefcg fgcbde afgdb ac gdfac gcdab fd fagec dgbea bagde aefdb abedf cegd abgcde gdb afcbd acbdf cfabd cafde gfdeba ebgacfd becdg ebfgd edgabc gabfc adfge afbcgde fbgca cedbg gdcbaf gecbd cgdafb fbdea dbegcf abfgced acfdbg aebgc eafc acgbe bcfadg ecadb agebd bgdaec decg eg eagcb gfacbed cgeba cegad cdaeg ecgad gedac abfge abdg begafc ad gfdeb ebdgf fcbgea aedbgcf fcbegd gfaed fea fea ed gced cdeg ebfgda gaebdc geba cbgade ebag dafgebc eacdg gc cbeg bfcage bfeg fcdbgae gabec cgdaf gdcba feagcb fdg ebgaf edfcgb fbage fge egfda gafde gbfa bfe dcgbae da cagbfed daeg faeb bdefag cgeabd egcabd gecfbd cfbegd cbafdg cegfbd abf efcab bgaedf gcaf bg gcdae bgdcfa fbgd ce edfcg bcef dcgbef fgabecd bacefg agdf befcd gfaceb ed gcbad begfac aef dfbea fdgabc afe cabed bdeac dcfeg eadcb cagbe cebdgfa edacfg bg decab aebcd cafbed cadbe fdbcg faegdb fgbae egcfbda cegbf bedgf de fadbg egfdc abcdef fegcd cgefadb bcafe adbegc cbfae defcgba dgabecf dcgfe db gcfdb cfge afedb aebcg gdbcafe cd dbc aedfbgc cdegba daecb acfdbe cadeb dba bedcf dcefb bfcaed abdefcg gedcfb cadbf fbacg bcgefd fbdce gc bcefd gcedfb fedacg cdbgf ed efabdgc edbgcaf dbgeac gacbf beafgc de dgcbfe ed daeg fa fbadcg gadfebc cafbdg cebfadg debga abgfd abgfecd fgedbc gbdcef ebag gfbced dgbaef dfc bfeac bacfe bface bc bfdeca faecb cdeab fagec gd dcgafe baged fbceagd ecd edc fbced gbaf aegcdb acdgef efbdg gdefb eafd baefdgc eag beagd edfbg degbac geafdcb dgefab ecabd dcaeb aedg efgba dcagefb efdacb efcba cabged gfabc fbacde aedcfb efa afe fe ebafg feb agfbe bgde acbgef facbe cgbafe deabf fb cadebf gdabfc cfbdga fdge gbecd egfbca cfadb be gabe bed fbdac fbadge cfgda gfbace egcaf efd daecf cdaefg eacbf fbdgcea ebafd gdefacb fdcag ebafgd bfdgea ecdfa bfdcega bfg cdgeb fdebg cebdg'

new_input = input.split(' ')
print(new_input)
lst = {1:2,4:4,7:3,8:7}

def number_times(segment, router):
    count = 0
    for string in segment:
        for value in router.values():
            if len(string) == value:
                count += 1
    return count
print(number_times(new_input, lst))
print(len(input))

num_lists = int(4828)
lists = []
for p in range(num_lists):
    lists.append([])
print(lists)

def format(segment,long):
    for idx in range(len(segment)-1):
        for letter in segment[idx]:
            long[idx].append(letter)
    return long
new = format(new_input, lists)
print(new)
print('THIS') 
#value_cost = {['c','a','g','e','d','b']: 0,['a','b']: 1 ,['g','c','d','f','a']: 2,['f','b','c','a','d']: 3,['e','a','f','b']: 4,['c','d','f','b','e']: 5,['c','d','f','g','e','b']: 6,['d','a','b']: 7,['a','c','e','d','g','f','b']: 8,['c','e','f','a','b','d']: 9}
#
#def final(segment, router):
#    num_list = []
#    for each in segment:
#        for key in router.keys():
#            if sorted(each) == sorted(key):
#                num_list.append(router[key])
#    return num_list
#print(final(new, value_cost))
#string = ['h','e','y']
#print(sorted(string) == sorted(['e','h','y']))

#Day 9 Smoke Basin
# check where the low points are, up down left right
#add one to all low points and add them all together to find risk check

inputs = '2199943210398789492198567898928767896789989996567899999999999999999999999999999999999999999999999999'
vale = []
for val in inputs:
    vale.append(int(val))
print(vale)
print(len(vale))

#def low_points(numbers, column_length):
#    min = []
#    for idx in range(0,len(numbers)-1,1):
#        if idx in range(1,10):
#            if numbers[idx] < numbers[idx - 1] and numbers[idx] < numbers[idx + 1] and numbers[idx] < numbers[idx + column_length]:
#                min.append(int(numbers[idx]))
#                break
#        if idx in range(11,len(numbers)/column_length),10):
#            if numbers[idx] < numbers[idx - column_length] and numbers[idx] < numbers[idx + 1] and numbers[idx] < numbers[idx + column_length]:
#                min.append(int(numbers[idx]))
#                break
#        if idx in range(10, len(numbers)/ column_length,10):
#            if numbers[idx] < numbers[idx - 1] and numbers[idx] < numbers[idx - column_length] and numbers[idx] < numbers[idx + column_length]:
#                    min.append(int(numbers[idx]))
#                    break
#        if idx in range(61,column_length * column_length, 1):
#            if numbers[idx] < numbers[idx - 1] and numbers[idx] < numbers[idx - column_length] and numbers[idx] <numbers[idx + 1]:
#                min.append(numbers[idx])
#                break
#        if idx == 0:
#            if numbers[idx] < numbers[idx + column_length] and numbers[idx] <numbers[idx + 1]:
#                min.append(numbers[idx])
#                break
#        if idx == column_length:
#            if numbers[idx] < numbers[idx + column_length] and numbers[idx] <numbers[idx - 1]:
#                min.append(numbers[idx])
#                break
#        if idx == (column_length * column_length - column_length + 1):
#            if numbers[idx] < numbers[idx - column_length] and numbers[idx] <numbers[idx + 1]:
#                min.append(numbers[idx])
#                break
#        if idx == (column_length * column_length - column_length + 1):
#            if numbers[idx] < numbers[idx - column_length] and numbers[idx] <numbers[idx - 1]:
#                min.append(numbers[idx])
#                break
#        else:
#            if numbers[idx] < numbers[idx - 1] and numbers[idx] < numbers[idx - column_length] and numbers[idx] < numbers[idx + 1] and numbers[idx] < numbers[idx + column_length]:
#                min.append(numbers[idx])
#                break
#    return min
#
#print(low_points(inputs,10))

