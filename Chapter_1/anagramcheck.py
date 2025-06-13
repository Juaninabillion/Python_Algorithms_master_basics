import math
def main():
    print("we are main")

    s1 = "aabbc"
    s2 = "bbaac"
    print(f"{s1} and {s2} anagram results: {isAnagram(s1,s2)}")

def isAnagram(s1,s2):
    string_dict = {}
    concat_string = s1+s2
    for i in concat_string:
        if i in string_dict:
            string_dict[str(i)] += 1
        else:
            string_dict[str(i)] = 1


    for i in string_dict:
        if string_dict[i] % 2 !=0:return False 
    return True





if __name__ == "__main__":
    main()