def character_count(text:str):
    # return len(text)
    character_count_map = {}
    for i in text:
        if i in character_count_map.keys():
            character_count_map[i]+=1
        else:
            character_count_map[i]=1
        

    return character_count_map

if __name__ == "__main__":
    str = "google.com"
    character_count_map = character_count(str)
    print(character_count_map)