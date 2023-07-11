function greedyThief(items, capacity) {
    const n = items.length;
    const dp = new Array(n + 1).fill(0).map(() => new Array(capacity + 1).fill(0));
  
    for (let i = 1; i <= n; i++) {
      const { weight, price } = items[i - 1];
      for (let j = 1; j <= capacity; j++) {
        if (weight <= j) {
          dp[i][j] = Math.max(price + dp[i - 1][j - weight], dp[i - 1][j]);
        } else {
          dp[i][j] = dp[i - 1][j];
        }
      }
    }
  
    const selectedItems = [];
    let i = n;
    let j = capacity;
    while (i > 0 && j > 0) {
      const { weight } = items[i - 1];
      if (dp[i][j] !== dp[i - 1][j]) {
        selectedItems.push(items[i - 1]);
        j -= weight;
      }
      i--;
    }
  
    return selectedItems.reverse();
  }
  