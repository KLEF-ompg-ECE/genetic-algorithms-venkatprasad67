# Assignment 2 — Genetic Algorithm: Knapsack Problem
## Observation Report

**Student Name  :** ________________K. Venkat Prasad___________  
**Student ID    :** ________________2310040076___________  
**Date Submitted:** ______________09/03/2026_____________  

---

## How to Submit

1. Run each experiment following the instructions below
2. Fill in every answer box — do not leave placeholders
3. Make sure the `plots/` folder contains all required images
4. Commit this README and the `plots/` folder to your GitHub repo

---

## Before You Begin — Read the Code

Open `ga_knapsack.py` and read through it. Then answer these questions.

**Q1. What does the `fitness()` function return? Why does an overweight solution score 0?**

```
 The fitness() function return the total value of the selected items if their total weight is within the knapsack capacity. 
```

**Q2. What does `tournament_select()` do? Why are higher-fitness individuals more likely to be chosen?**

```
[ tournament_select() randomly selects a small group of individuals from the population and chooses the one with the highest fitness among them. ]
```

**Q3. Look at the `run_ga()` loop. Find this line:**
```python
next_gen = [best_chromosome[:]]
```
**What is this doing? Why is it important to always keep the best solution?**

```
[ This line copies the best chromosome from the current generation into the next generation without any changes (elitism). ]
```

---

## Experiment 1 — Baseline Run

**Instructions:** Run the program without changing anything.
```bash
python ga_knapsack.py
```

**Fill in this table:**

| Metric | Your result |
|--------|-------------|
| Number of generations | 50|
| Best value at generation 1 |60 |
| Final best value |77 |
| Total weight of best solution (kg) | 14.4kg|
| Is solution valid (Yes / No) | Yes|

**Copy the printed packing list here:**
```
[ Best Packing List
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
Valid  : Yes ]
```

**Look at `plots/experiment_1.png` and describe what you see (2–3 sentences).**  
*Where does the biggest improvement happen? Does the curve flatten at some point?*
```
[ The plot shows a rapid increase in fitness during the early generations, indicating quick improvement in solutions. The biggest improvement occurs in the first few generations as the algorithm identifies strong combinations. After that, the curve gradually flattens, showing convergence as fewer improvements are found.]
```

---

## Experiment 2 — Effect of Mutation Rate

**Instructions:** In `ga_knapsack.py`, find the `# EXPERIMENT 2` block in `__main__`.  
Copy it three times and run with `mutation_rate` = **0.01**, **0.05**, and **0.30**.  
Save plots as `experiment_2a.png`, `experiment_2b.png`, `experiment_2c.png`.

**Results table:**

| mutation_rate | Final best value | Weight (kg) | Valid? | Shape of curve |
|--------------|-----------------|-------------|--------|----------------|
| 0.01         |        75         |    14.9         |    Yes    |        Smooth, early flat        |
| 0.05         |        77         |      14.4       |    Yes    |      Steady improvement          |
| 0.30         |        78         |      14.1       |    Yes    |        Noisy/unstable        |

**Compare the three plots. What happens when mutation is too low? Too high? (3–4 sentences)**  
*Hint: Too low = no diversity, may get stuck. Too high = random search. What is the sweet spot?*
```
[ When the mutation rate is too low (0.01), the algorithm quickly converges but may get stuck in local optima due to low diversity. When the mutation rate is too high (0.30), the search becomes unstable and behaves more like random search, causing irregular improvement. A moderate mutation rate (0.05) gives steady and reliable progress. Overall, the plots show that balanced mutation helps maintain both exploration and stability. ]
```

**Which mutation_rate gave the best result? Why do you think that is?**
```
[ The mutation rate of 0.30 gave the best result because it achieved the highest final value (78). The higher mutation introduced more diversity, which helped the algorithm discover a better solution in this case.]
```

---

## Summary

**Complete this table with your best result from each experiment:**

| Experiment | Key setting | Final value | Main finding in one sentence |
|------------|-------------|-------------|------------------------------|
| 1 — Baseline | mutation_rate = 0.05 |77 |GA improves quickly and then converges. |
| 2 — Mutation rate | mutation_rate = ___ |78 |Higher mutation found slightly better solution. |

**In your own words — what is the most important thing you learned about Genetic Algorithms from these experiments? (3–5 sentences)**
```
[ From these experiments, I learned that mutation rate strongly affects the performance of Genetic Algorithms. A low mutation rate reduces diversity and may cause the algorithm to get stuck, while a high mutation rate increases exploration. In this experiment, a higher mutation rate produced the best result, but it also made the search less stable. Overall, I understood how GA gradually evolves better solutions across generations. ]
```

---

## Submission Checklist

- [✔ ] Student name and ID filled in
- [ ✔] Q1, Q2, Q3 answered
- [✔ ] Experiment 1: table filled, packing list pasted, plot observation written
- [✔ ] Experiment 2: results table filled (3 rows), observation and answer written
- [✔ ] Summary table completed and reflection written
- [✔ ] `plots/` contains: `experiment_1.png`, `experiment_2a.png`, `experiment_2b.png`, `experiment_2c.png`
