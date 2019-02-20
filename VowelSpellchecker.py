class Solution:
    def spellchecker(self, wordlist: 'List[str]', queries: 'List[str]') -> 'List[str]':
        wordset = set(wordlist)
        nocase = {word.lower(): word for word in wordlist[::-1]}
        novowel = {re.sub(r'[aeiou]','#',word.lower()): word for word in wordlist[::-1]}
        answer = []
        
        for query in queries:
            if query in wordset:
                answer.append(query)
            elif query.lower() in nocase:
                answer.append(nocase[query.lower()])
            elif re.sub(r'[aeiou]','#',query.lower()) in novowel:
                answer.append(novowel[re.sub(r'[aeiou]','#',query.lower())])
            else:
                answer.append("")
        return answer
