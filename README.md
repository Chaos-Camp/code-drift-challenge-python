
# Code Drift Challenge

Welcome to the Code Drift Challenge! This challenge simulates the common real-world problem of code drift, where different versions of code diverge in functionality, leading to potential conflicts, bugs, and misunderstandings.

Your task is to recognize areas of code drift, reconcile the differences across branches, and produce a unified, functional version of the application.

## Objective:

1. Identify areas where code has drifted across branches.
2. Merge features and changes from all branches (`dev`, `staging`, and `production`) into a new unified branch.
3. Resolve any conflicts that arise.
4. Ensure the final code runs without errors and has all intended features.
5. Update documentation to reflect the reconciled code's actual behavior.

## Instructions:

### Step 1: Setup

Clone this repository:

```bash
git clone [repository_url] code_drift_challenge
cd code_drift_challenge
```

### Step 2: Investigate

Navigate through the branches to understand the unique features or changes each branch introduces:

```bash
git checkout dev
# Review changes

git checkout staging
# Review changes

git checkout production
# Review changes
```

### Step 3: Reconcile Drift

Create a new branch for your unified code:

```bash
git checkout -b unified_code
```

Merge features from `dev`, `staging`, and `production` into `unified_code`. You'll likely encounter merge conflicts, which you'll need to resolve manually.

### Step 4: Test

Run the application to ensure that it's working as intended. All features from the separate branches should be present in your unified code without any errors.

### Step 5: Update Documentation

Based on the final version of your code, update the `README.md` to accurately describe the application's behavior and features.

## Hints:

1. Review the commit history of each branch to understand the evolution of the code.
2. Make sure to test the application after merging each branch to catch and rectify any issues early on.
3. While resolving merge conflicts, understand the intent behind each change instead of choosing one change over another arbitrarily.

## Evaluation Criteria:

1. Successful identification and reconciliation of all areas of drift.
2. Merged code runs without errors.
3. Documentation accurately describes the application's behavior and features.

## Conclusion:

Once completed, you'll have a better understanding of code drift, its implications, and how to tackle it in a real-world scenario. Good luck, and happy coding!
