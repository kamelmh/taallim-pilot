#!/usr/bin/env python3
import argparse
import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from exercise_generator import ExerciseGenerator, EXERCISE_TYPES, to_markdown, to_html
from topics import list_topics_formatted, find_topic_by_name, get_topics_by_level, get_topic_by_id


def cmd_generate(args):
    gen = ExerciseGenerator(api_key=args.api_key)
    if args.topic:
        topic = find_topic_by_name(args.topic)
        if not topic:
            print(f"Topic '{args.topic}' not found.", file=sys.stderr)
            sys.exit(1)
        topic_id = topic["id"]
    else:
        topic_id = None

    if args.level and not topic_id:
        results = gen.generate_for_level(args.level, args.type, args.count)
    elif topic_id:
        if args.type == "all":
            topic = get_topic_by_id(topic_id)
            results = []
            for etype in topic.get("exercise_types", []):
                r = gen.generate(topic_id, etype, args.count)
                if "error" not in r:
                    results.append(r)
        else:
            etype = args.type or "fill_in_blank"
            results = gen.generate(topic_id, etype, args.count)
            if "error" in results:
                print(results["error"], file=sys.stderr)
                sys.exit(1)
            results = [results]
    else:
        print("Specify --topic or --level.", file=sys.stderr)
        sys.exit(1)

    path = gen.save(results, args.output)
    print(f"Saved {len(results)} exercise set(s) to: {path}")
    print(f"Total exercises: {sum(r.get('count', 0) for r in results)}")
    return results


def cmd_topics(args):
    print(list_topics_formatted())


def cmd_export(args):
    with open(args.input, "r", encoding="utf-8") as f:
        data = json.load(f)
    if args.format == "markdown":
        content = to_markdown(data)
        out = args.output or args.input.replace(".json", ".md")
    elif args.format in ("html", "pdf"):
        content = to_html(data)
        out = args.output or args.input.replace(".json", ".html")
    else:
        print(f"Unknown format: {args.format}", file=sys.stderr)
        sys.exit(1)
    with open(out, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Exported to: {out}")


def main():
    parser = argparse.ArgumentParser(
        description="English Exercise Generator for Algerian Students",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python cli.py generate --topic "Present Simple" --level A1 --type fill_in_blank --count 10
  python cli.py generate --level A1 --type all --count 5
  python cli.py topics
  python cli.py export --input generated/exercises.json --format markdown
  python cli.py export --input generated/exercises.json --format pdf
        """
    )
    sub = parser.add_subparsers(dest="command")

    gen_p = sub.add_parser("generate", help="Generate exercises")
    gen_p.add_argument("--topic", "-t", help="Topic name (e.g., 'Present Simple')")
    gen_p.add_argument("--level", "-l", choices=["A1", "A2", "B1", "B2"], help="Level")
    gen_p.add_argument("--type", "-T", choices=EXERCISE_TYPES + ["all"], default="fill_in_blank", help="Exercise type")
    gen_p.add_argument("--count", "-c", type=int, default=10, help="Number of exercises")
    gen_p.add_argument("--output", "-o", help="Output filename")
    gen_p.add_argument("--api-key", help="Anthropic API key (or set ANTHROPIC_API_KEY env var)")

    sub.add_parser("topics", help="List all topics")

    exp_p = sub.add_parser("export", help="Export exercises to markdown or HTML")
    exp_p.add_argument("--input", "-i", required=True, help="Input JSON file")
    exp_p.add_argument("--format", "-f", choices=["markdown", "pdf"], default="markdown", help="Export format")
    exp_p.add_argument("--output", "-o", help="Output filename")

    args = parser.parse_args()
    if args.command == "generate":
        cmd_generate(args)
    elif args.command == "topics":
        cmd_topics(args)
    elif args.command == "export":
        cmd_export(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
