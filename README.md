# Assignment 2 — Genetic Algorithm: Knapsack Problem
## Observation Report

**Student Name  :** K. Venkat Prasad  
**Student ID    :** 2310040076  
**Date Submitted:** 09/03/2026  

---

## Before You Begin — Read the Code

**Q1. What does the `fitness()` function return? Why does an overweight solution score 0?**

The fitness() function returns the total value of selected items if their total weight is within the limit. If the weight exceeds the maximum capacity, it returns 0. This prevents invalid solutions from being selected during evolution.

---

**Q2. What does `tournament_select()` do? Why are higher-fitness individuals more likely to be chosen?**

tournament_select() randomly selects a small group of individuals and chooses the one with highest fitness. Higher-fitness individuals are more likely to win tournaments. This helps good solutions survive and reproduce.

---

**Q3. Look at the `run_ga()` loop. Find this line:**

```python
next_gen = [best_chromosome[:]]
```

**What is this doing? Why is it important to always keep the best solution?**

This line copies the best chromosome into the next generation unchanged. This is called elitism. It ensures the best solution is never lost during crossover or mutation.

---

## Experiment 1 — Baseline Run

| Metric | Your result |
|--------|-------------|
| Number of generations | 50 |
| Best value at generation 1 | 60 |
| Final best value | 77 |
| Total weight of best solution (kg) | 14.4 |
| Is solution valid (Yes / No) | Yes |

**Copy the printed packing list here:**

```
Best Packing List
--------------------------------------
+ Water bottle
+ First aid kit
+ Sleeping bag
+ Torch
+ Energy bars (x6)
+ Rain jacket
+ Map & compass
+ Cooking stove
+ Rope (10 m)
+ Sunscreen
+ Power bank
--------------------------------------
Weight : 14.4 / 15.0 kg
Value  : 77
Valid  : Yes
```

**Look at `plots/experiment_1.png` and describe what you see (2–3 sentences).**

The plot shows a rapid increase in fitness during the early generations. The biggest improvement occurs in the first few generations. After that, the curve gradually flattens, showing convergence.

---

## Experiment 2 — Effect of Mutation Rate

| mutation_rate | Final best value | Weight (kg) | Valid? | Shape of curve |
|--------------|------------------|-------------|--------|----------------|
| 0.01 | 75 | 14.9 | Yes | Smooth, early flat |
| 0.05 | 77 | 14.4 | Yes | Steady improvement |
| 0.30 | 78 | 14.1 | Yes | Noisy/unstable |

**Compare the three plots. What happens when mutation is too low? Too high? (3–4 sentences)**

When the mutation rate is too low (0.01), the algorithm converges early and gets stuck due to low diversity. When the mutation rate is too high (0.30), the search becomes unstable but finds a better solution. A moderate mutation rate (0.05) gives steady improvement.

---

**Which mutation_rate gave the best result? Why do you think that is?**

The mutation rate of 0.30 gave the best result because it achieved the highest final value (78). The higher mutation introduced more diversity, which helped the algorithm discover a better solution in this case.

---

## Summary

| Experiment | Key setting | Final value | Main finding in one sentence |
|------------|-------------|-------------|------------------------------|
| 1 — Baseline | mutation_rate = 0.05 | 77 | GA improves quickly and then converges. |
| 2 — Mutation rate | mutation_rate = 0.30 | 78 | Higher mutation found slightly better solution. |

**In your own words — what is the most important thing you learned about Genetic Algorithms from these experiments? (3–5 sentences)**

From these experiments, I learned that mutation rate strongly affects Genetic Algorithm performance. A low mutation rate reduces diversity and may cause premature convergence. A high mutation rate improves exploration but reduces stability. Balanced tuning helps GA find better solutions.


---

## Submission Checklist

- [✔ ] Student name and ID filled in
- [ ✔] Q1, Q2, Q3 answered
- [✔ ] Experiment 1: table filled, packing list pasted, plot observation written
- [✔ ] Experiment 2: results table filled (3 rows), observation and answer written
- [✔ ] Summary table completed and reflection written
- [✔ ] `plots/` contains: `experiment_1.png`, `experiment_2a.png`, `experiment_2b.png`, `experiment_2c.png`
