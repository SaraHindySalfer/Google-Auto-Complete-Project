def filter_sentences(data, query, words):
    sentences = []
    for word in words:
        sentences += data.get_word_data()[word]
    auto_complete = []
    for sentence in sentences:
        if query in sentence.ignore_sentence:
            sentence.set_score(len(query) * 2)
            auto_complete += [sentence]
    return auto_complete


def get_completions(data, query):
    last_word = query.split()[-1]
    words = data.word_by_letter.get_possible_words(last_word)
    return filter_sentences(data, query, words)


def get_best_k_completions(data, query):
    best_k_completions = get_completions(data, query)
    n = len(best_k_completions)
    for _ in range(min(5, n)):
        best_sentence = max(best_k_completions)
        yield best_sentence
        best_k_completions.remove(best_sentence)


def ignore(sentence):
    source_sentence, ignore, sentence = sentence.lower(), 0, sentence.lower()
    for i in range(len(source_sentence)):
        if source_sentence[i] in ["'", ':', '!', '"', ';', '.', '@', '$', '%', '^', '&', '*', ',', '?', '(', ')'] or (
                source_sentence[i] == ' ' and source_sentence[max(0, i - 1)] == ' '):
            ignore += 1
            sentence = sentence.replace(source_sentence[i], '')
    return sentence
