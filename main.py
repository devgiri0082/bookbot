def main():
  with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    words_len = len(file_contents.split())
    charDict = countChar(file_contents)
    charArr = dictToArr(charDict)
    charArr.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_len} words found in the document")
    for dict in charArr:
      print(f"The {dict["letter"]} character was found {dict["count"]} times")
      
def sort_on(dict):
  return dict["count"]
  

def dictToArr(dict):
  arr = []
  for key in dict:
    arr.append({"letter": key, "count": dict[key]})
  return arr

def countChar(content):
  charDict = {}
  for char in content:
    char_lower = char.lower()
    if not char_lower.isalpha(): continue
    if char_lower in charDict:
      charDict[char_lower] += 1
    else:
      charDict[char_lower] = 1 
  return charDict


main()