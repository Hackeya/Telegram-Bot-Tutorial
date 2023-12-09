from uzwords import words
from difflib import get_close_matches as gcm

# print(len(words))
# print(words[0])
# print(words[-1])
# print(words[7777])
# print(words[22222])


# print(gcm('муомала', words))

def checkWord(word, words=words): 
    word = word.lower()
    matches = set(gcm(word, words))
    available = False #Bunday so'z mavjud emas
# а б д е ф г ҳ и ж к л м н о п қ р с т у в х й з ў  ғ  ш  ч
# a b d e f g h i j k l m n o p q r s t u v x y z o' g' sh ch
    if word in matches:
        available = True
        matches = word

    elif 'а' in word:
        word = word.replace('а', 'a')
        matches.update(gcm(word, words))
    
    elif 'б' in word:
        word = word.replace('б', 'b')
        matches.update(gcm(word, words))
    
    elif 'д' in word:
        word = word.replace('д', 'd')
        matches.update(gcm(word, words))
    
    elif 'е' in word:
        word = word.replace('е', 'e')
        matches.update(gcm(word, words))
    
    elif 'ф' in word:
        word = word.replace('ф', 'f')
        matches.update(gcm(word, words))
    
    elif 'г' in word:
        word = word.replace('г', 'g')
        matches.update(gcm(word, words))
    
    elif 'ҳ' in word:
        word = word.replace('ҳ', 'h')
        matches.update(gcm(word, words))
    
    elif 'и' in word:
        word = word.replace('и', 'i')
        matches.update(gcm(word, words))
    
    elif 'ж' in word:
        word = word.replace('ж', 'j')
        matches.update(gcm(word, words))
    
    elif 'к' in word:
        word = word.replace('к', 'k')
        matches.update(gcm(word, words))
    
    elif 'л' in word:
        word = word.replace('л', 'l')
        matches.update(gcm(word, words))
    
    elif 'м' in word:
        word = word.replace('м', 'm')
        matches.update(gcm(word, words))
    
    elif 'н' in word:
        word = word.replace('н', 'n')
        matches.update(gcm(word, words))
    
    elif 'о' in word:
        word = word.replace('о', 'o')
        matches.update(gcm(word, words))
    
    elif 'п' in word:
        word = word.replace('п', 'p')
        matches.update(gcm(word, words))
    
    elif 'қ' in word:
        word = word.replace('қ', 'q')
        matches.update(gcm(word, words))
    
    elif 'р' in word:
        word = word.replace('р', 'r')
        matches.update(gcm(word, words))
    
    elif 'с' in word:
        word = word.replace('с', 's')
        matches.update(gcm(word, words))
    
    elif 'т' in word:
        word = word.replace('т', 't')
        matches.update(gcm(word, words))
    
    elif 'у' in word:
        word = word.replace('у', 'u')
        matches.update(gcm(word, words))
    
    elif 'в' in word:
        word = word.replace('в', 'v')
        matches.update(gcm(word, words))
    
    elif 'х' in word:
        word = word.replace('х', 'x')
        matches.update(gcm(word, words))
    
    elif 'й' in word:
        word = word.replace('й', 'y')
        matches.update(gcm(word, words))
    
    elif 'з' in word:
        word = word.replace('з', 'z')
        matches.update(gcm(word, words))
    
    elif 'ў' in word:
        word = word.replace('ў', 'o\'')
        matches.update(gcm(word, words))
    
    elif 'ғ' in word:
        word = word.replace('ғ', 'g\'')
        matches.update(gcm(word, words))
    
    elif 'ш' in word:
        word = word.replace('ш', 'sh')
        matches.update(gcm(word, words))
    
    elif 'ч' in word:
        word = word.replace('ч', 'ch')
        matches.update(gcm(word, words))
    
    return {'available':available, 'matches':matches}

if __name__ == '__main__':
    print(checkWord('хато'))
    print(checkWord('олма'))
    print(checkWord('ҳато'))