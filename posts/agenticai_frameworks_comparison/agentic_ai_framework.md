
---
author: Senthil Kumar
badges: true
branch: master
categories:
- AI/Agents
- AI/AgenticAI
- Tools/Langgraph
- Tools/Hermes
- Tools/Strands

description: What 40+ experiments taught us about when to use each framework — and what to steal from all three.
date: '2026-06-14'
draft: false
image: ./images/opening_image_2.png
toc: false
title: "4 Patterns × 3 Frameworks × 1 LLM: Building and Evaluating Agentic AI Patterns across LangGraph, Strands, and Hermes"
output-file: agentic_ai_frameworks.html

---


<div align="center">



### 4 Patterns × 3 Frameworks × 1 LLM:

#### Building and Evaluating Agentic AI Patterns across LangGraph, Strands, and Hermes




---



<img src="./images/opening_image_2.png" width="1200" alt="AI Agentic Frameworks">



<br>



###### **Author:** Senthil Kumar



</div>


<div align="center">

## Key Sections of this Talk

</div>

* I. The Entire Talk in 5 Min
* II. The Agentic AI Patterns in Focus
* III. Why LangGraph, Strands, and Hermes; Why Not Others?
* IV. What Does the Evaluation Say?
* V. Conclusion
* VI. Epilogue
* VII. GitHub Resource & Useful References

<div align="center"> 
    
## I. The Entire Talk in 5 Min

</div>

This post compares three agent frameworks across four progressively harder patterns. The goal is not to crown a single universal winner, but to show which design choice helps most when the workload changes.

### 5-Minute Executive Summary (1/3)

<img src="./images/5_min_version_simple.png" width="1300" alt="Pattern 1"/>

### 5-Minute Executive Summary (2/3)

| Pattern | Key Capability | Description |
|---|---|---|
| P1 | MCP tools | AI Agent with 2 Numeric Tools |
| P2 | +RAG tool | Same AI Agent with 2 Numeric Tools + 1 Semantic Retrieval Tool |
| P3 | +Skills | Same AI Agent with same tools + Skills |
| P4 | +Memory +chat | Same AI Agent with memory & terminal chat |

<div align="center">

<img src="./images/5_min_version_additive_patterns.png" width="1100" alt="Pattern 1"/>

</div>

### 5-Minute Executive Summary (3/3)

<img src="./images/5_min_version_detailed.png" width="1100" alt="Pattern 1"/>

<div align="center">
    
## II. The Agentic AI Patterns in Focus

</div>

<div align="center">
    
### Additive Architecture Lens

</div>

The four patterns below move from basic tool use to retrieval, skills, and multi-turn memory, so you can see how each framework behaves as the orchestration problem becomes more demanding.

| Pattern | Key Capability | Description |
|---|---|---|
| P1 | MCP tools | AI Agent with 2 Numeric Tools |
| P2 | +RAG tool | Same AI Agent with 2 Numeric Tools + 1 Semantic Retrieval Tool |
| P3 | +Skills | Same AI Agent with same tools + Skills |
| P4 | +Memory +chat | Same AI Agent with memory & terminal chat |



> Progressive Design :
> * *Layer one new behavior at a time and measure impact*


<img src="./images/pattern1.png" width="1100" alt="Pattern 1"/>

<img src="./images/pattern2.png" width="1200" alt="Pattern 2"/>

<img src="./images/pattern3.png" width="1300" alt="Pattern 3"/>

<img src="./images/pattern4.png" width="1300" alt="Pattern 4"/>

<img src="./images/the_4_patterns_summary.png" width="1500" alt="4 patterns summary"/>

<img src="./images/4_patterns_key_insights.png" width="1500" alt="4 patterns key insights"/>

<div align="center">
    
## III. Why LangGraph, Strands, and Hermes; Why Not Others?

</div>

<img src="./images/Why_L_S_H.png" width="1500" alt="Pattern 4"/>

<div align="center">
    
## IV. What Does the Evaluation Say?

</div>

<div align="center">

### Evaluation Guidelines

### [4 Patterns · 3 Frameworks · 40+ Experiments](https://github.com/senthilkumarm1901/agentic_frameworks_exploration/blob/main/eval/reports/Final_Evaluation_Report.md)

These tables summarize the 40+ experiments in this post. The benchmark keeps the model, tools, and prompts fixed so the framework design is the main variable.

> **Core Question**: *Which framework should you use — and when?* <br>
> **Alt Question**: *If you're building a custom framework, what's the best feature to borrow from each?*

| Common Factor        | Description                                                                  |
| ------------- | ---------------------------------------------------------------------- |
| Model         | `qwen3.5:35b-a3b-coding-nvfp4` (local Ollama — identical across all 3) |
| Tools | Same MCP (Model Context Protocol) server across 3 frameworks                                           |
| Prompts | Uniform across 3 frameworks                                       |


### Frameworks

| Framework              | Language | Architecture                              | Key Characteristic                             |
| ---------------------- | -------- | ----------------------------------------- | ---------------------------------------------- |
| **LangGraph**          | Python   | Graph-based state machine                 | Nodes → edges → conditional routing            |
| **AWS Strands Agents** | Python   | AWS-native agent SDK                      | MCP subprocess isolation, event-driven         |
| **Hermes**             | Python   | Custom agent (evolved during experiments) | Fixed orchestration loop, `uv`-based packaging |

### Patterns (Progressive Complexity)

| Pattern                 | What It Tests                             | Key Challenge                                                 |
| ----------------------- | ----------------------------------------- | ------------------------------------------------------------- |
| [**P1** Simple MCP Tools](https://github.com/senthilkumarm1901/agentic_frameworks_exploration/blob/main/eval/reports/pattern_1_report.md) | Basic tool calling + answer synthesis     | Can the agent call tools and synthesize a coherent answer?    |
| [**P2** RAG + KB Search](https://github.com/senthilkumarm1901/agentic_frameworks_exploration/blob/main/eval/reports/pattern_2_report.md)  | Vector DB retrieval + knowledge grounding | Can the agent combine structured + unstructured knowledge?    |
| [**P3** Skills](https://github.com/senthilkumarm1901/agentic_frameworks_exploration/blob/main/eval/reports/pattern_3_report.md)           | Skill-guided multi-tool orchestration     | Can the agent choose the right skill and follow its workflow? |
| [**P4** Multi-Turn Chat](https://github.com/senthilkumarm1901/agentic_frameworks_exploration/blob/main/eval/reports/pattern_4_report.md)  | Cumulative conversation context           | How does cost scale with conversation depth?                  |

</div>


<div align="center">

### Executive Summary

**There is no universal winner in this benchmark.** The right framework is pattern-dependent:

| If you need...                | Use...        | Why                                                  |
| ----------------------------- | ------------- | ---------------------------------------------------- |
| Simple tool orchestration     | **Hermes**    | Fastest, lightest (9.5s, 49 MB, 267 deps)            |
| RAG-powered search            | **Strands**   | Lowest memory (44 MB), fastest RAG latency           |
| Complex multi-skill workflows | **LangGraph** | 100% accuracy, best multi-skill orchestration        |
| Multi-turn chatbot            | **Hermes**    | Flat O(1) LLM scaling — cost doesn't grow with depth |

| Framework     | Gold Medals (🥇) | Silver (🥈) |   Bronze (🥉)  |
| ------------- | :--------------: | :---------: | :------------: |
| **Hermes**    |  **2** (P1, P4)  |  2 (P2, P3) |        0       |

</div>

---

<div align="center">

### Pattern 1: Simple MCP Tools


> *Can the agent call tools and synthesize a coherent answer?*

| Metric         |    LangGraph   |   Strands   |    Hermes    |     🏆    |
| -------------- | :------------: | :---------: | :----------: | :-------: |
| Avg Latency    |    12.4 s   |  11.5 s  | **9.5 s** |   Hermes  |
| Avg Tokens     |      3,140     |    3,559    |   **3,092**  |   Hermes  |
| Peak Memory    |     58.6 MB    | **41.1 MB** |    51.1 MB   |  Strands  |
| Packaging      |     76.9 MB    |   72.8 MB   |  **49.3 MB** |   Hermes  |
| Dependencies   |       175      |     142     |    **101**   |   Hermes  |
| Answer Quality | **100%** (4/4) |  50% (2/4)  |   75% (3/4)  | LangGraph |

**🏆 Winner: Hermes** — in this setup, it was the fastest and lightest option with the fewest dependencies.

</div>

> * ⚠️ With same prompt, same tools and same LLM, across 3 frameworks, Strands returned raw tool output in 2/4 experiments.
> * LangGraph was the only framework with perfect answer quality (100%)
> * Improving answer quality in both Strands and Hermes was possible with explicit additional system prompt instructions like below

```python

_SYNTHESIS_SUFFIX = (
    "\n\nIMPORTANT: After using tools, you MUST always provide a final "
    "natural-language answer that synthesizes the results. "
    "Never end your response with just a tool call."
)
```

---


<div align="center">

### Pattern 2: RAG + Knowledge Base Search

> *Can the agent combine structured data with vector-retrieved knowledge?*

| Metric         | LangGraph |    Strands    |    Hermes    |     🏆    |
| -------------- | :-------: | :-----------: | :----------: | :-------: |
| Avg Latency    | 31,758 ms | **29,396 ms** |   32,849 ms  |  Strands  |
| Avg Tokens     | **2,627** |     3,688     |     2,898    | LangGraph |
| Peak Memory    |  133.6 MB |  **44.0 MB**  |    54.2 MB   |  Strands  |
| Packaging      |  984.8 MB |    996.8 MB   | **967.2 MB** |   Hermes  |
| Answer Quality |    100%   |      100%     |     100%     |    Tie    |

**🏆 Winner: Strands** — in this setup, it combined the fastest latency with the lowest memory (44 MB vs 134 MB LangGraph).

> * The RAG stack added \~900 MB to the packaging of all frameworks.
> * Strands' and Hermes' **MCP subprocess isolation** kept their memory lower by running embeddings in a separate process. LangGraph loaded everything **in-process** → 134 MB. 

</div>

---

<div align="center">

### Pattern 3: Agent with Skills

*Can the agent choose the right skill and follow its guided workflow?*

| Metric                |    LangGraph    |     Strands     |         Hermes        |      🏆      |
| --------------------- | :-------------: | :-------------: | :-------------------: | :----------: |
| Avg Latency           |    40,093 ms    |  **34,684 ms**  |       37,915 ms       |    Strands   |
| Avg Tokens            |      9,499      |      14,154     |       **8,031**       |    Hermes    |
| Peak Memory           |     134.6 MB    |   **45.6 MB**   |        54.4 MB        |    Strands   |
| **Factual Accuracy**  |  **100%** (4/4) |  **100%** (4/4) |     **75%** (3/4)     | LG / Strands |
| **Skill Utilization** | **5/5** correct | **5/5** correct | **4/5** (wrong skill) | LG / Strands |

**🏆 Winner: LangGraph** — 100% factual accuracy, correct multi-skill orchestration.

> Hermes chose the **wrong skill** for the European GDP question, causing it to **miss Russia** — factual error (14.98T instead of 17.05T). Strands self-corrected name lookup failures (`UK`→`United Kingdom`). 

</div>

---

<div align="center">

### Pattern 4: Multi-Turn Conversational Agent

> *How does cost scale as conversation history accumulates?*


| Metric                           |  LangGraph  |      Strands       |            Hermes            |    🏆     |
| -------------------------------- | :---------: | :----------------: | :--------------------------: | :-------: |
| LLM Call Growth (T1→T4)          | 4→14 (3.5×) |    6→33 (5.5×)     |       **4→3 (0.75×)**        |  Hermes   |
| Token Growth (T1→T3)             |    4.6×     |        8.4×        |           **2.6×**           |  Hermes   |
| T2-T4 Avg Latency                |    62.8s    |     **24.5s**      |            34.8s             |  Strands  |
| Context Test ("Same for Brazil") |   ✅ Pass    | ⚠️ Partial (3-way) | ❌ **Fail** (did Brazil vs Japan; should have been Brazil vs India) | LangGraph |
| Error Recovery (T4)              |      Correct from beginning      |         Correct from beginning            |    ✅ Russia→Russian Fed.     |  All 3   |

**🏆 Winner: Hermes** — in this setup, it showed the flattest O(1) LLM scaling and the most token-efficient growth (2.6× vs Strands 8.4×).
</div>



|            | Good at                                                    | Bad at                                                         |
| ---------- | ---------------------------------------------------------- | -------------------------------------------------------------- |
| **Hermes** | Not **wasting tokens** re-processing history (2.6× growth) | **Understanding** what history implies ("Same for Brazil" → ❌) |
| **LangGraph** | **Deep context reasoning**  | **Linear growth** in (4→14) LLM calls |


**Key Insight**: 

* The fix for both frameworks is the same - one preprocessing LLM call before the main loop.
* For Hermes, it resolves ambiguous references ("Same for Brazil" → "Compare India and Brazil").
* For LangGraph, it compresses history into a bounded summary. Neither requires a rewrite — just a single added stage in the existing pipeline.



<img src="./images/Cross-pattern-winner-summary.png" width="1500" alt="Pattern 4"/>

<div align="center">
    
## V. Key Learnings

</div>

### 1. There are no bad frameworks — only untested ones

* Identify the failed areas in that framework and rectify it

| Framework | Best                     | Worst                         |
| --------- | ------------------------------- | ------------------------------------ |
| LangGraph | 100% accuracy across P1+P3      | 134 MB memory, slowest latency       |
| Strands   | 44 MB memory, 18s warm turns    | 33 LLM calls by Turn 4, very high - 124K tokens - consumption|
| Hermes    | O(1) scaling, 2.6× token growth | ❌ Failed context test, missed Russia |

### 2. Know what you're getting into — Architecture reveals weaknesses before your users do

Knowing the architectural choices baked into a framework's philosophy helps unearth weaknesses **before production**, not after.

| Framework     | Architecture Philosophy                               | Weakness It Causes                                                                |
| ------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------- |
| **LangGraph** | Graph-based state machine — re-evaluate at every node | LLM calls grow linearly (4→14); memory loaded in-process (134 MB)                 |
| **Strands**   | Full context replay — every LLM call sees everything  | Tokens explode (9.9K→124K); Too high token consumption as turns increase                           |
| **Hermes**    | Fixed orchestration loop — plan once, execute, answer | Shallow reasoning over history; fails implicit references ("Same for Brazil" → ❌) |

> None of these showed up in Pattern 1. All of them showed up by Pattern 4. **The architecture didn't change — the workload revealed it.**


### 3. Treat evaluation as a product feature, not an afterthought

Standard metrics (latency, tokens, memory) tell you **how fast**. Designed tests tell you **how wrong**.

| What We Measured                 | What We Discovered                                 | How              |
| -------------------------------- | -------------------------------------------------- | ---------------- |
| Latency, tokens, memory          | Hermes is fastest, cheapest                        | Standard metrics |
| "Same for Brazil"                | Hermes **drops context entirely**                  | Designed test    |
| "Most populous European country" | Same model, different framework → different answer | Designed test    |
| European GDP total               | Hermes picked wrong skill → missed a country       | Designed test    |

> Every ❌ in this evaluation was caught by a **designed test**, not a dashboard metric. If we'd only measured speed and cost, Hermes would look flawless.


<div align="center">

## VI. Epilogue

</div>

### Bonus Pattern 5: (-)RAG -> (+)Wiki

> *Remove RAG; include Karpathy's LLM Wiki pattern.*

<img src="./images/pattern_5_vs_patter2_final_2.png" width="1200" alt="Pattern 5"/>

<img src="./images/the_5_patterns_summary_2.png" width="1500" alt="Pattern 5"/>

<img src="./images/patterns_key_insights_2.png" width="1500" alt="Pattern 5"/>

For the next iteration:

- Try Workflow Patterns
    - Routing-Workflow
    - Parallel-Workflow
    - Sequential-Workflow

<img src="./images/workflow_patterns.png" width="1000" alt="Pattern 4"/>

- Try comparing with other agentic AI frameworks
    - There are still other good ones like: `temporal` (python/typescript), `pydantic ai` (python), `rig` (rust)

Reproducibility note: These results reflect one local Ollama-based benchmark run with the same model, the same MCP tools, and the same prompts across all three frameworks. If you rerun them with a different model or different tool behavior, the rankings may change.

---

## VII. Github Resource

- The codebase, evaluation reports conducted are logged in github here: [senthilkumarm1901/agentic_frameworks_exploration](https://github.com/senthilkumarm1901/agentic_frameworks_exploration)


### Useful Reading References


Follow below links  for reading material on Agentic AI, each expanding on the link above that.  

1.  Simple article first: [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents "https://www.anthropic.com/engineering/building-effective-agents")
2. Inspired by the above article and based on my day-to-day experience, I wrote an article on similar lines long ago: [https://medium.com/@senthilkumar.m1901/single-llm-to-agentic-ai-genais-evolution-explained-c0670d83…](https://medium.com/@senthilkumar.m1901/single-llm-to-agentic-ai-genais-evolution-explained-c0670d8325f3?source=friends_link&sk=d040821d89a7ce8c5e506fde3184c948 "https://medium.com/@senthilkumar.m1901/single-llm-to-agentic-ai-genais-evolution-explained-c0670d8325f3?source=friends_link&sk=d040821d89a7ce8c5e506fde3184c948")
3. None of the above have skills explained well: [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills "https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills") 
4. Same Stuff as 1 but elaborated further with **Skills** and More Agentic Patterns; Anthropic gave version 2: [https://resources.anthropic.com/hubfs/Building%20Effective%20AI%20Agents-%20Architecture%20Patterns…](https://resources.anthropic.com/hubfs/Building%20Effective%20AI%20Agents-%20Architecture%20Patterns%20and%20Implementation%20Frameworks.pdf "https://resources.anthropic.com/hubfs/building%20effective%20ai%20agents-%20architecture%20patterns%20and%20implementation%20frameworks.pdf")
5. [Hermes Agent Masterclass](https://www.dailydoseofds.com/p/hermes-agent-masterclass/ "https://www.dailydoseofds.com/p/hermes-agent-masterclass/") (the pics here are 👌)
6. The Context Engineering 101 (in pic):<br>
<img src="./images/context_engineering_101.png" width="1500" alt="CE 101"/>
