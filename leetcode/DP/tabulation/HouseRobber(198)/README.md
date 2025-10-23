### 🔒 **Problem Statement Recap:**

You are a professional robber planning to rob houses along a street. Each house has some amount of money stashed. However, adjacent houses have security systems connected — **robbing two adjacent houses will alert the police**.

### 🎯 Goal:

Return the **maximum amount of money** you can rob **without robbing two adjacent houses**.

---

### ✅ **Example:**

```java
nums = [2, 7, 9, 3, 1]
```

You cannot rob both house `1` and house `2` (index 0 and 1), or house `2` and `3`, etc.
The optimal plan is to rob house 0 (2), house 2 (9), and house 4 (1) → total = 2 + 9 + 1 = 12.

---

### 🔧 **Code Breakdown and Explanation:**

```java
class Solution {
    public int rob(int[] nums) {
```

* `nums[]` is the array of money at each house.
* We want to calculate the **maximum amount** we can rob under the constraint.

---

#### 🧪 Step 1: Handle Base Cases

```java
        if (nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];
```

* If there are no houses, return 0.
* If only one house, rob it (since there’s no adjacent house to worry about).

---

#### 📦 Step 2: Initialize DP Array

```java
        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);
```

* `dp[i]` = Maximum amount that can be robbed from **house 0 to i**.
* `dp[0]` = Just rob the first house.
* `dp[1]` = Choose the better of the first two houses (you can’t rob both).

---

#### 🔁 Step 3: Fill DP Array

```java
        for (int i = 2; i < nums.length; i++) {
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + nums[i]);
        }
```

This is the core logic. For each house `i`:

* You have **2 choices**:

  1. **Skip** current house → take `dp[i-1]`.
  2. **Rob** current house → add its money to `dp[i-2]`.

So:

```java
dp[i] = max(
    dp[i - 1],         // don’t rob current house
    dp[i - 2] + nums[i]  // rob current house
)
```

👉 This ensures no adjacent house is robbed.

---

#### 🏁 Step 4: Return Final Answer

```java
        return dp[nums.length - 1];
    }
}
```

* Return the **last element of `dp[]`**, which contains the optimal result for the entire array.

---

### 💡 Dry Run Example:

```java
nums = [2, 7, 9, 3, 1]
```

Step by step:

* `dp[0] = 2`
* `dp[1] = max(2, 7) = 7`
* `dp[2] = max(7, 2 + 9) = 11`
* `dp[3] = max(11, 7 + 3) = 11`
* `dp[4] = max(11, 11 + 1) = 12`

➡️ Return `dp[4] = 12`

---

### 🧠 Time & Space Complexity

| Type  | Complexity |
| ----- | ---------- |
| Time  | `O(n)`     |
| Space | `O(n)`     |

