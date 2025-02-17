from app import paraphraser


def test_if_llm_greets():
    answer = paraphraser("Paraphrase this : What a great game it was!!")
    assert "James" in answer
