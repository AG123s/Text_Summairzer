import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string

# Download necessary resources from nltk
nltk.download("punkt")
nltk.download("stopwords")

def summarize_text(text, summary_length=3):
    """
    Summarize the given text into a smaller set of sentences.

    Parameters:
        text (str): The paragraph to be summarized.
        summary_length (int): Number of sentences in the summary.

    Returns:
        str: The summarized text.
    """
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Tokenize words and remove stopwords/punctuation
    stop_words = set(stopwords.words("english"))
    word_scores = {}
    for sentence in sentences:
        words = word_tokenize(sentence.lower())
        for word in words:
            if word not in stop_words and word not in string.punctuation:
                word_scores[word] = word_scores.get(word, 0) + 1

    # Score each sentence based on word frequency
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_scores:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_scores[word]

    # Sort sentences by their scores
    ranked_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)

    # Return the top-ranked sentences as the summary
    summary = " ".join(ranked_sentences[:summary_length])
    return summary


if __name__ == "__main__":
    # Example input
    text = """Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed 
              to think like humans and mimic their actions. The term may also be applied to any machine that exhibits traits 
              associated with a human mind such as learning and problem-solving. AI has become an essential part of the technology 
              industry, with numerous applications ranging from healthcare to robotics."""

    print("Original Text:")
    print(text)
    print("\nSummarized Text:")
    print(summarize_text(text))
