from inspect_ai import Task, task
from inspect_ai.dataset import Sample, hf_dataset
from inspect_ai.scorer import choice
from inspect_ai.solver import multiple_choice


def record_to_sample(record):
    return Sample(
        input=record["question"],
        choices=record["choices"]["text"],
        target=record["answerKey"],
        metadata={
            "area": record["question_type"],
            "ano": record["exam_year"],
            "nullified": record["nullified"],
        },
    )


@task
def oab_r():
    return Task(
        dataset=hf_dataset(
            path="eduagarcia/oab_exams",
            split="train",
            sample_fields=record_to_sample,
        ).filter(
            lambda sample: not sample.metadata["nullified"]
        ),
        solver=multiple_choice(),
        scorer=choice(),
    )



def set_choice(record, posicao):
    lista = list(record["choices"]["text"])
    indice = ord(record["answerKey"]) - ord("A")
    memoria = lista.pop(indice)
    lista.insert(posicao, memoria)
    return Sample(
        input=record["question"],
        choices=lista,
        target=chr(ord("A") + posicao),
        metadata={
            "area": record["question_type"],
            "ano": record["exam_year"],
            "nullified": record["nullified"],
        },
    )


@task
def oab_fixedchoice(posicao: int = 0):
    return Task(
        dataset=hf_dataset(
            path="eduagarcia/oab_exams",
            split="train",
            sample_fields=lambda r: set_choice(r, posicao),
        ).filter(
            lambda sample: not sample.metadata["nullified"]
        ),
        solver=multiple_choice(),
        scorer=choice(),
    )