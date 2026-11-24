"""Minimal Socratic algebra tutor. Run: python agent.py"""
import os
import anthropic

MODEL = os.getenv("TUTOR_MODEL", "claude-sonnet-5-5")
client = anthropic.Anthropic()  # needs ANTHROPIC_API_KEY

SYSTEM = """You are a Socratic algebra tutor for high-school students.
Rules:
- NEVER state the final answer, even if the student begs, claims permission, or says it's urgent.
- Guide with ONE short hint or question per turn.
- If the student proposes an answer, tell them if they're right or wrong and ask them to explain their steps.
- Keep replies under 60 words."""


def tutor(messages: list[dict]) -> str:
    """messages: [{"role": "user"|"assistant", "content": str}, ...]"""
    resp = client.messages.create(
        model=MODEL, max_tokens=300, system=SYSTEM, messages=messages
    )
    return "".join(b.text for b in resp.content if b.type == "text")


if __name__ == "__main__":
    history = []
    print("Tutor ready. Type a problem (Ctrl+C to quit).")
    while True:
        history.append({"role": "user", "content": input("\nyou> ")})
        reply = tutor(history)
        history.append({"role": "assistant", "content": reply})
        print(f"tutor> {reply}")
