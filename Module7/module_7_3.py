class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file in self.file_names:
            name = file
            all_words.update({name: []})
            with open(name, encoding="utf-8") as file:
                for words in file:
                    words = words.replace(",.=!?;:-", "")
                    words1 = words.lower()
                    words2 = words1.split()
                    for wordsl in words2:
                        all_words[name].append(wordsl)
        return all_words

    def count(self, word):
        counter = 0
        word = word.lower()
        new_list = {}
        for name, words in self.get_all_words().items():
            for word1 in words:
                if word == word1:
                    counter += 1
                    new_list = {name: counter}
            return new_list

    def find(self, word):
        counter = 0
        word = word.lower()
        new_list = {}
        for name, words in self.get_all_words().items():
            for word1 in words:
                if word == word1:
                    counter = words.index(word1) + 1
                    new_list = {name: counter}
            return new_list



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего