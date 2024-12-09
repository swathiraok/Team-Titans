from transformers import pipeline


class Summarization:
    """
    Text summarization using the provided pipeline model.
    """
    def __init__(self, model_name="dhivyeshrk/bart-large-cnn-samsum"):
        self.pipeline = pipeline("text2text-generation", model=model_name)

    def generate(self, text_input):
        tokens = text_input.split(" ")
        if len(tokens) > 500:
            text_input = " ".join(tokens[:500])
        return self.pipeline(text_input)


if __name__ == "__main__":
    summarizer = Summarization()
    sample_text = (
        "Arena BioWorks is promising big paydays to nearly 100 researchers "
        "from Harvard, M.I.T. and other prestigious institutions. "
        "In an unmarked laboratory stationed between Harvard and MIT, "
        "a splinter group of scientists is hunting for the next billion-dollar drug."
    )
    result = summarizer.generate(sample_text)
    print(result)