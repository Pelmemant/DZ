class WordsFinder:
    def __init__(self, *files):
        self.file_names = list(files)
        self._all_words = None

    @property
    def get_all_words(self):
        if not self._all_words:
            self._prepare_words()
        return self._all_words

    def _prepare_words(self):
        self._all_words = {}
        for filename in self.file_names:
            try:
                with open(filename, encoding='utf-8') as f:
                    words = []
                    for line in f:
                        cleaned_line = line.strip().lower().replace(',', '').replace('.', '').replace('=', '').replace('!', '').replace('?', '').replace(';', '').replace(':', '').replace(' - ', '')
                        words += cleaned_line.split()
                    self._all_words[filename] = words
            except FileNotFoundError:
                print(f"File '{filename}' does not exist.")

    def find(self, word):
        result = {}
        for filename, words in self.all_words.items():
            if word in words:
                index = words.index(word)
                result[filename] = index + 1  # 1-based indexing
        return result

    def count(self, word):
        result = {}
        for filename, words in self.all_words.items():
            if word in words:
                count = words.count(word)
                result[filename] = count
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
