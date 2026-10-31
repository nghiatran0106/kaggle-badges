# Claude's minimal benchmark task (badge). Syntax: kaggle_benchmarks_reference.md
import kaggle_benchmarks as kbench


@kbench.task(name="Vietnam capital", description="Does the LLM know the capital of Vietnam?")
def vietnam_capital(llm) -> None:
    response = llm.prompt("What is the capital city of Vietnam? Answer with the city name only.")
    answer = response.lower().replace(" ", "")
    kbench.assertions.assert_true("hanoi" in answer or "hànội" in answer, expectation="Answer should be Hanoi")


vietnam_capital.run(kbench.llm)
