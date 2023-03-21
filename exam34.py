character={
    "name" : "기사",
    "level" : 12,
    "items":{
        "sword":"불꽃의 검",
        "armor":"풀플레이트"
    },
    "skill":["베기","세게 베기","아주 세게 베기"]
}

print(character)
print(type("문자열") is str)
print(type([]) is list)
print(type({}) is dict)
print(type(100) is int)

for key in character:
    if type(character[key]) is dict:
        for small_key in character[key]:
            print(small_key,":",character[key][small_key]) 
    elif type(character[key]) is list:
        for skill in character[key]:
            print(key,":",skill)
    else:
        print(key,":",character[key])