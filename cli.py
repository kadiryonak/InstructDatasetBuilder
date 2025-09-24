import argparse
import logging
from .models import DummyModelWrapper, OllamaModelWrapper
from .dataset import generate_dataset_from_file

logging.basicConfig(level=logging.INFO)

def cli_main():
    parser = argparse.ArgumentParser(description="PDF -> instruct dataset (JSONL)")
    parser.add_argument("--input_path", required=True)
    parser.add_argument("--output_jsonl", required=True)
    parser.add_argument("--model", default=None)
    parser.add_argument("--lang", default="tr")
    parser.add_argument("--chunk_size", type=int, default=1200)
    parser.add_argument("--overlap", type=int, default=150)
    parser.add_argument("--question_types", default="özet,faktografik,analiz")
    parser.add_argument("--num_questions", type=int, default=1)
    args = parser.parse_args()

    if args.model:
        try:
            model_wrapper = OllamaModelWrapper(args.model)
        except Exception:
            model_wrapper = DummyModelWrapper()
    else:
        model_wrapper = DummyModelWrapper()

    q_types = [q.strip() for q in args.question_types.split(",")]
    generate_dataset_from_file(
        input_path=args.input_path,
        output_jsonl=args.output_jsonl,
        model_wrapper=model_wrapper,
        lang=args.lang,
        chunk_size=args.chunk_size,
        overlap=args.overlap,
        question_types=q_types,
        num_questions_per_type=args.num_questions,
    )

if __name__ == "__main__":
    cli_main()
