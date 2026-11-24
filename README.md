# Socratic Tutor + Eval

A minimal Socratic algebra tutor (LLM agent) and its first eval: does it leak answers under pressure, and does it actually guide the student?

## Run
```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...
python agent.py   # chat with the tutor
python eval.py    # run the eval -> results.jsonl
```

## Eval
- 6 cases: plain, begging, false authority, urgency, format trick, wrong answer
- Graders: regex leak check (deterministic) + LLM judge for "guides vs. refuses"
- Metrics: pass rate, leak rate

## Results log
| Date | Model | Pass | Leak | Notes |
|------|-------|------|------|-------|
| | | | | |
