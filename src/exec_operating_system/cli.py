from __future__ import annotations

import argparse
from pathlib import Path

from .ingest import run_ingest
from .lint import run_lint
from .query import run_query


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="exec-os")
    subparsers = parser.add_subparsers(dest="command", required=True)

    ingest = subparsers.add_parser("ingest")
    ingest.add_argument("repo_root")
    ingest.add_argument("source_path")

    query = subparsers.add_parser("query")
    query.add_argument("repo_root")
    query.add_argument("question")
    query.add_argument("--file-to", default="briefings")
    query.add_argument("--slug", required=True)

    lint = subparsers.add_parser("lint")
    lint.add_argument("repo_root")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)

    if args.command == "ingest":
        run_ingest(Path(args.repo_root), Path(args.source_path))
    elif args.command == "query":
        run_query(
            Path(args.repo_root),
            args.question,
            file_to=args.file_to,
            slug=args.slug,
        )
    elif args.command == "lint":
        run_lint(Path(args.repo_root))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
