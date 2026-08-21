"""验证第 6–12 章归档结构并编译所有 Python 源文件。"""

from __future__ import annotations

import py_compile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PROJECTS = (
    "L6/L6-2/AutoGen", "L6/L6-3/AgentScope", "L6/L6-4/CAMEL", "L6/L6-5/LangGraph",
    "L7/L7-2/LLM-Extension", "L7/L7-4/Agent-Patterns", "L7/L7-5/Tool-System",
    "L8/L8-2/Memory", "L8/L8-3/RAG", "L8/L8-4/Document-QA",
    "L9/L9-3/ContextBuilder", "L9/L9-4/NoteTool", "L9/L9-5/TerminalTool", "L9/L9-6/Codebase-Maintainer",
    "L10/L10-1/Quick-Start", "L10/L10-2/MCP", "L10/L10-3/A2A", "L10/L10-4/ANP", "L10/L10-5/Custom-MCP-Server",
    "L11/L11-1/Quick-Start", "L11/L11-2/Data-and-Rewards", "L11/L11-3/SFT", "L11/L11-4/GRPO",
    "L11/L11-5/Evaluation", "L11/L11-6/Training-Pipeline",
    "L12/L12-1/Basic-Agent", "L12/L12-2/BFCL", "L12/L12-3/GAIA", "L12/L12-4/Data-Generation-Evaluation",
)
DEEPSEEK_ENV = {
    "LLM_MODEL_ID": "deepseek-v4-flash",
    "LLM_BASE_URL": "https://api.deepseek.com",
}
REQUIRED_DIAGRAM_COUNT = 7
CHAPTERS = tuple(range(6, 13))
CHAPTER_DIAGRAM_COUNT = 3


def main() -> None:
    errors: list[str] = []
    for relative in REQUIRED_PROJECTS:
        project = ROOT / relative
        if not project.is_dir():
            errors.append(f"缺少目录：{relative}")
        if not (project / "requirements.txt").is_file():
            errors.append(f"缺少依赖清单：{relative}/requirements.txt")
        env_example = project / ".env.example"
        if not env_example.is_file():
            errors.append(f"缺少环境模板：{relative}/.env.example")
        else:
            env_values = {}
            for line in env_example.read_text(encoding="utf-8").splitlines():
                if "=" in line and not line.lstrip().startswith("#"):
                    key, value = line.split("=", 1)
                    env_values[key.strip()] = value.strip()
            for key, expected in DEEPSEEK_ENV.items():
                if env_values.get(key) != expected:
                    errors.append(
                        f"DeepSeek 配置不一致：{relative}/.env.example "
                        f"中的 {key} 应为 {expected}",
                    )
            if env_values.get("LLM_API_KEY") != "your-deepseek-api-key":
                errors.append(
                    f"DeepSeek 配置不一致：{relative}/.env.example "
                    "中的 LLM_API_KEY 应使用占位值",
                )

        learning_diagrams = project / "LEARNING_DIAGRAMS.md"
        diagram_dir = project / "diagrams"
        if not learning_diagrams.is_file():
            errors.append(f"缺少图文讲解：{relative}/LEARNING_DIAGRAMS.md")
        if not (diagram_dir / "README.md").is_file():
            errors.append(f"缺少图表索引：{relative}/diagrams/README.md")
        diagram_files = sorted(diagram_dir.glob("*.mmd"))
        if len(diagram_files) != REQUIRED_DIAGRAM_COUNT:
            errors.append(
                f"图表数量不正确：{relative} 应有 {REQUIRED_DIAGRAM_COUNT} 张，"
                f"实际 {len(diagram_files)} 张",
            )
        for diagram in diagram_files:
            content = diagram.read_text(encoding="utf-8")
            if "中文注释" not in content:
                errors.append(
                    f"图表缺少中文注释：{diagram.relative_to(ROOT)}",
                )
            svg = diagram.with_suffix(".svg")
            if not svg.is_file() or svg.stat().st_size == 0:
                errors.append(
                    f"缺少 SVG 成品图：{svg.relative_to(ROOT)}",
                )

    for number in CHAPTERS:
        chapter = f"L{number}"
        chapter_home = ROOT / chapter / "README.md"
        chapter_diagram_dir = ROOT / chapter / "diagrams"
        if not chapter_home.is_file():
            errors.append(f"缺少章节首页：{chapter}/README.md")
        if not (chapter_diagram_dir / "README.md").is_file():
            errors.append(f"缺少章节图表索引：{chapter}/diagrams/README.md")
        chapter_diagrams = sorted(chapter_diagram_dir.glob("*.mmd"))
        if len(chapter_diagrams) != CHAPTER_DIAGRAM_COUNT:
            errors.append(
                f"章节图表数量不正确：{chapter} 应有 {CHAPTER_DIAGRAM_COUNT} 张，"
                f"实际 {len(chapter_diagrams)} 张",
            )
        for diagram in chapter_diagrams:
            if "中文注释" not in diagram.read_text(encoding="utf-8"):
                errors.append(f"章节图表缺少中文注释：{diagram.relative_to(ROOT)}")
            svg = diagram.with_suffix(".svg")
            if not svg.is_file() or svg.stat().st_size == 0:
                errors.append(f"缺少章节 SVG 成品图：{svg.relative_to(ROOT)}")

    sources = [
        path for path in ROOT.glob("L*/**/*.py")
        if ".venv" not in path.parts and "__pycache__" not in path.parts
    ]
    for source in sources:
        try:
            py_compile.compile(str(source), doraise=True)
        except py_compile.PyCompileError as exc:
            errors.append(f"编译失败：{source.relative_to(ROOT)}\n{exc}")

    if errors:
        raise SystemExit("\n".join(errors))
    print(f"归档结构完整：{len(REQUIRED_PROJECTS)} 个实践目录")
    print(f"DeepSeek 配置通过：{len(REQUIRED_PROJECTS)} 个环境模板")
    print(
        f"中文设计图通过：{len(REQUIRED_PROJECTS)} 个实践，"
        f"共 {len(REQUIRED_PROJECTS) * REQUIRED_DIAGRAM_COUNT} 张",
    )
    print(
        f"章节聚合通过：L6–L12 共 {len(CHAPTERS)} 章，"
        f"{len(CHAPTERS) * CHAPTER_DIAGRAM_COUNT} 张章节图",
    )
    print(f"Python 编译通过：{len(sources)} 个源文件")


if __name__ == "__main__":
    main()
