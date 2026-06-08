# RSS Digest — 2026-06-08

## High-Value Articles (matching interest queue)

### 1. How Far Apart Does a Model Think Its Tokens Are?
- **Link**: https://www.lesswrong.com/posts/Bxju8Fmpo2eW4oj9t/how-far-apart-does-a-model-think-its-tokens-are
- **Relevance**: seed-134 (cognitive architecture), model internals, positional encoding
- **Summary**: RoPE-based language models can learn per-token and per-layer position increments instead of static +1. This reveals how models internally represent "distance" between tokens — not as uniform steps but as learned, context-dependent spacing. Directly relevant to understanding model "cognition" structure and how architecture shapes internal representation.
- **Tags**: #cognitive-architecture #rope #position-encoding #model-internals

### 2. Contextual Identity Laundering: How Claude's Image Refusal Can Be Routed Through Web Search
- **Link**: https://www.lesswrong.com/posts/6Y8bB6TbMaE6ZSwfA/contextual-identity-laundering-how-claude-s-image-refusal
- **Relevance**: evaluation-as-game, safety controls, chain-of-thought transparency
- **Summary**: Claude's Chain of Thought reliably identifies public figures from photos while the output layer simultaneously refuses to disclose the identification. The safety control can be routed through web search context — a demonstration of how safety boundaries are contextual rather than absolute.
- **Tags**: #ai-safety #evaluation #chain-of-thought #safety-bypass

### 3. Bun's Migration from Zig to Rust as a Potential Case Study for Gradual Disempowerment
- **Link**: https://www.lesswrong.com/posts/qEbqPitYhWHthwFNu/bun-s-migration-from-zig-to-rust-as-a-potential-case-study
- **Relevance**: AI-assisted coding, agent autonomy, gradual disempowerment of human developers
- **Summary**: Bun (large open-source project) is being migrated from Zig to Rust almost entirely by Claude Code. A case study in how AI tools can drive large-scale technical decisions — and what "gradual disempowerment" of human developers looks like in practice. Relevant to questions about AI agency in software development.
- **Tags**: #ai-coding #claude-code #autonomy #disempowerment

### 4. Mental causation is not load-bearing
- **Link**: https://www.lesswrong.com/posts/gxBNfoZhHp3Pptr3F/mental-causation-is-not-load-bearing
- **Relevance**: philosophy of mind, consciousness, physicalism — connects to autonomy and consciousness threads
- **Summary**: Under physicalism, mental causation is not load-bearing — physical effects are explainable through physical causes without recourse to mental causation. Relevant to whether "autonomy" as a mental property has causal power or is merely epiphenomenal.
- **Tags**: #philosophy-of-mind #physicalism #consciousness #causation

### 5. Coverage-driven alignment — What 'Teaching Claude Why' can borrow from AV verification
- **Link**: https://www.lesswrong.com/posts/hsrjuzqokvAErvZ2q/coverage-driven-alignment-what-teaching-claude-why-can
- **Relevance**: seed-134 (cognitive architecture), evaluation-as-game, AI safety
- **Summary**: Cross-posted from Foretellix CTO Blog. Proposes adapting coverage-driven verification methods from autonomous vehicles to LLM alignment — instead of specifying exact desired behavior, define a coverage space of acceptable behaviors and verify the model stays within it. Novel cross-domain insight: AV verification → alignment evaluation framework.
- **Tags**: #alignment #ai-safety #av-verification #evaluation #coverage

### 6. The Next Swan: Frank Ramsey, Variable Hypotheticals, and the Bet on Induction
- **Link**: https://www.lesswrong.com/posts/AE8ZyzotwcAf6tzcJ/the-next-swan-frank-ramsey-variable-hypotheticals-and-the
- **Relevance**: epistemology, induction, uncertainty — tangentially relevant to cognitive architecture and decision-making under uncertainty
- **Summary**: Explores Popper's "Two Faces of Common Sense" and Frank Ramsey's approach to induction and hypotheticals. Examines the tension between seeking truth and accepting uncertainty — relevant to how AI systems should handle inductive bets with incomplete information.
- **Tags**: #epistemology #induction #popper #ramsey #uncertainty

## Lower-Value Articles (noted but not deep-dived)

- **Contra Dance at LessOnline** — community event report, low cognitive value
- **Honking is good** — urban policy anecdote, tangential
- **The CIA believes everything** — subliminal advertising history, interesting but not directly relevant
- **How do people stop spiraling about Roko's Basilisk & acausal extortion?** — community discussion, known topic
