import re


requiredKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optionalKeys = ['cid']
hgtRegexp = re.compile(r"^([0-9]+)(cm|in)$")
hclRegexp = re.compile(r"^#[0-9a-f]{6}$")
pidRegexp = re.compile(r"^[0-9]{9}$")
numberRegexp = re.compile(r"^[0-9]+$")
DEBUG = False

def validateID(id):
    isValid = True
    for key in requiredKeys:
        if key not in id:
            isValid = False
            break

    if isValid:
        for key in id.keys():
            if key not in requiredKeys and key not in optionalKeys:
                isValid = False

    return isValid

def validateFields(passport):
    isValid = True
    if not isValidBYR(passport['byr']):
        if DEBUG: print('byr invalid', passport)
        isValid = False
    if not isValidIYR(passport['iyr']):
        if DEBUG: print('iyr invalid', passport)
        isValid = False
    if not isValidEYR(passport['eyr']):
        if DEBUG: print('eyr invalid', passport)
        isValid = False
    if not isValidHGT(passport['hgt']):
        if DEBUG: print('hgt invalid', passport)
        isValid = False
    if not isValidHCL(passport['hcl']):
        if DEBUG: print('hcl invalid', passport)
        isValid = False
    if not isValidECL(passport['ecl']):
        if DEBUG: print('ecl invalid', passport)
        isValid = False
    if not isValidPID(passport['pid']):
        if DEBUG: print('pid invalid', passport)
        isValid = False
    return isValid

def isValidBYR(byr):
    if numberRegexp.search(byr):
        if int(byr)>=1920 and int(byr)<=2002:
            return True
        else:
            return False

def isValidIYR(iyr):
    if numberRegexp.search(iyr):
        if int(iyr)>=2010 and int(iyr)<=2020:
            return True
        else:
            return False

def isValidEYR(eyr):
    if numberRegexp.search(eyr):
        if int(eyr)>=2020 and int(eyr)<=2030:
            return True
        else:
            return False

def isValidHGT(hgt):
    isValid = False
    matches = hgtRegexp.search(hgt)
    if matches:
        if len(matches.groups()) == 2:
            height = int(matches.group(1))
            unit = matches.group(2)
            if unit == 'cm':
                if height >= 150 and height <= 193:
                    isValid = True
            elif unit == 'in':
                if height >= 59 and height <= 76:
                    isValid = True
    return isValid

def isValidHCL(hcl):
    matches = hclRegexp.search(hcl)
    if matches:
        return True
    else:
        return False

def isValidECL(ecl):
    isValid = False
    if len(ecl) == 3:
        if ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            isValid = True
    return isValid

def isValidPID(pid):
    matches = pidRegexp.search(pid)
    if matches:
        return True
    else:
        return False

def parseInput(text):
    passportsInput = text.split("\n\n")
    passports = []
    for line in passportsInput:
        passport = {}
        fields = line.split()
        for field in fields:
            key, val = field.split(':', 2)
            if key not in passport:
                passport[key] = val
            else:
                raise ValueError('Key already there')
        passports.append(passport)

    return passports


with open('day4input') as file:
    input = file.read()
    passports = parseInput(input)

    print("Part 1")
    validPassportsCpt = 0
    for passport in passports:
        check = validateID(passport)
        if(check):
            validPassportsCpt += 1
    print(validPassportsCpt)

    print("Part 2")
    validPassportsCpt = 0
    for passport in passports:
        check = validateID(passport)
        if(check):
            if(validateFields(passport)):
                validPassportsCpt += 1
    print(validPassportsCpt)
