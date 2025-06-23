import re
import stopwordsiso as stopwords
from mpstemmer import MPStemmer

# Inisialisasi stopwords dan stemmer
stopwords = stopwords.stopwords("id")
stemmer = MPStemmer()


def clean_regex(text):
    text = text.lower()

    # Hapus unicode escape seperti \xf, \x, \xb, \xe, dsb
    text = re.sub(r"(\\x[0-9a-fA-F]{2})+", " ", text)

    # Hapus karakter non-ASCII
    text = re.sub(r"[^\x00-\x7F]+", " ", text)

    # Hapus mentions, RT, URL, dan domain
    text = re.sub(r"\brt\b", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"@\w*", " ", text)
    text = re.sub(r"https?://\S+|www\.\S+", " ", text)
    text = re.sub(r"(?:\@|https?\://)\S+", " ", text)

    # Hapus HTML tag
    text = re.sub(r"<.*?>", " ", text)

    # Hapus emoji
    emoji_pattern = re.compile(
        "["
        "\U0001f600-\U0001f64f"  # emoticon
        "\U0001f300-\U0001f5ff"  # symbols & pictographs
        "\U0001f680-\U0001f6ff"  # transport & map symbols
        "\U0001f1e0-\U0001f1ff"  # flags (iOS)
        "\U00002702-\U000027b0"
        "\U000024c2-\U0001f251"
        "]+",
        flags=re.UNICODE,
    )
    text = emoji_pattern.sub(r"", text)

    # Hapus tanda baca & simbol non-alfabet lain
    text = re.sub(r"[^\w\s]", " ", text)

    # Ganti angka dengan token <NUM>
    text = re.sub(r"\b\d+\b", "<NUM>", text)

    # Bersihkan tagar, hapus '#' tapi simpan kata
    text = re.sub(r"#(\w+)", r"\1", text)

    # Hilangkan karakter khusus seperti 'user', 'usar'
    text = re.sub(r"\buser\b", " ", text)
    text = re.sub(r"\busar\b", " ", text)

    # Hilangkan underscore, backslash, slash, dsb
    text = re.sub(r"[\\\/\[\]\{\}\|\<\>\^~]", " ", text)

    # Hilangkan whitespace berlebih
    text = re.sub(r"\s+", " ", text).strip()

    text = " ".join([word for word in text.split() if len(word) > 1])

    return text


def remove_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in stopwords])


def stem_words(text):
    return " ".join([stemmer.stem(word) for word in text.split()])

def do_preprocess(raw_texts: list[str]):
    texts: list[str] = []
    for text in raw_texts:
        text = clean_regex(text)
        text = remove_stopwords(text)
        text = stem_words(text)
        texts.append(text)
    return texts
