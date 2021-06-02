"""

--- Day 4: Passport Processing ---
You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. 
While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't 
actually valid documentation for travel in most of the world.

It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport 
scanners, and the delay could upset your travel itinerary.

Due to some questionable network security, you realize you might be able to solve both of these problems at the same 
time.

The automatic passport scanners are slow because they're having trouble detecting which passports have all required 
fields. The expected fields are as follows:

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of key:value 
pairs separated by spaces or newlines. Passports are separated by blank lines.

Here is an example batch file containing four passports:

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt 
(the Height field).

The third passport is interesting; the only missing field is cid, so it looks like data from North Pole Credentials, 
not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing cid fields. 
Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is not, 
so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, 
how many passports are valid?

"""
## TODO: gotta try and get all of the passport onto one line and then get into key, value pairs in a list
# After this is figured out should just check each length for 8 to get valid ones and then check all keys of length 7 to 
# see if they are without "CID" for another valid passport. -- PARSING this ended up being quite confusing but got it

with open("passports.txt") as file:
    
    split1 = file.read().split("\n\n")
    split2 = [string.replace("\n", " ") for string in split1]
    entries = [string.split() for string in split2]

## PART 1 ##
valid = 0
for entry in entries:
    pDict = {}
    for e in entry:
        pDict.update({e[0:3]:e[4:]})
    if len(pDict) == 8:
        valid += 1
        #print(pDict["hgt"][:-2])
        #print(pDict)
    if len(pDict) == 7 and "cid" not in pDict:
        valid += 1
        #print(pDict["hgt"][:-2])
        #print(pDict)
print(f"Part 1: {valid}")

def passportCheck(pDict):
    BYR = IYR = EYR = HGT = HCL = ECL = PID = False
    if int(pDict["byr"]) <= 2002 and int(pDict["byr"]) >= 1920:
        BYR = True
    if int(pDict["iyr"]) <= 2020 and int(pDict["iyr"]) >= 2010:
        IYR = True
    if int(pDict["eyr"]) <= 2030 and int(pDict["eyr"]) >= 2020:
        EYR = True
    #height = int(pDict["hgt"][:-2])
    if pDict["hgt"].endswith('in'):
        if int(pDict["hgt"][:-2]) <= 76 and int(pDict["hgt"][:-2]) >= 59:
            HGT = True
    if pDict["hgt"].endswith('cm'):
        if int(pDict["hgt"][:-2]) <= 193 and int(pDict["hgt"][:-2]) >= 150:
            HGT = True
    if pDict["hcl"].startswith("#") and len(pDict["hcl"]) == 7:
        HCL = True
    if pDict["ecl"] in {"amb", "blu", "brn", "grn", "gry", "hzl", "oth"}:
        ECL = True
    if len(pDict["pid"]) == 9:
        PID = True
    return BYR and IYR and EYR and HGT and HCL and ECL and PID 

part2 = 0
for entry in entries:
    pDict = {}
    for e in entry:
        pDict.update({e[0:3]:e[4:]})
    if len(pDict) == 8:
        if passportCheck(pDict):
            part2 += 1
    if len(pDict) == 7 and "cid" not in pDict:
        if passportCheck(pDict):
            part2 += 1
print(f"Part 2: {part2}")

