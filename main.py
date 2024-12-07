def wordcounter(frankenstein):
    word_count = len(frankenstein.split())
    return(word_count)

def charcounter(bookstring):
    charcount = {}
    b=bookstring.lower()
    for char in b:
        if char not in charcount:
            charcount[char] = 1
        else:
            charcount[char] += 1
    return(charcount)

def sort_it_out(dict):
    holding = {}
    sorted_dict = []
    for k, v in dict.items():
        if k.isalpha():
            holding = {"char": k, "count": v}
            sorted_dict.append(holding)
    
    sorted_dict.sort(reverse=True, key=lambda dict: dict["count"])
    return (sorted_dict)
def print_report(word_count, sorted_chars):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    for char in sorted_chars:
        print(f"The '{char['char']}' character was found {char['count']} times")
    print("--- End report ---")


def main():
    frankenstein = None
    with open("books/frankenstein.txt") as f:
        frankenstein = f.read()
    word_count=wordcounter(frankenstein)
    dict_list = charcounter(frankenstein)
    print_report(word_count,sort_it_out(dict_list))
main()

